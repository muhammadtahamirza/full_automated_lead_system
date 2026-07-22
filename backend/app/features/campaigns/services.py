# from celery_tasks import redis_client
from datetime import date
from sqlmodel import select, Session
from fastapi import HTTPException
from ..campaigns.models import CampaignLeads, CampaignTemplates, Campaign
from ..mailboxes.models import MailAccount
from ..leads.models import Lead
from ..templates.models import Template
from .tasks import send_single_email
import random




def trigger_campaign(campaign_id: int , db : Session): #ignore

	cmpn, leads, templates, mailboxes =  get_cmpn_leads_tepmlates_mailboxes(campaign_id, db)

	# scheduling all email sendig tasks in celery

	cumulative_delay = 0
	mailbox_index = 0
	queued = 0
	info = []
	for index, lead in enumerate(leads):

		# get avaialbe next mailbox
		assigned_mailbox, mailbox_index = get_mailbox(mailbox_index, mailboxes)
		if not assigned_mailbox:
			print("All mailboxes hit 0 capacity. Exiting loop.")
			return{
				"status" : "all mailbox limit finished",

			}
		#TODO do it in the celery task based on weatehr mail send or not
		assigned_mailbox.daily_limit -= 1  # to check


		# get template
		shift = index // len(mailboxes)
		template_index = (index + shift) % len(templates)
		assigned_template = templates[template_index]

		cumulative_delay += random.randint(60, 100)

		info.append({
			"lead" : lead,
			"template" : assigned_template,
			"mailbox" : assigned_mailbox
		})

			# Queue the task in Redis for Celery to handle later
		send_single_email.apply_async(
			args=(assigned_mailbox.id, lead.id, assigned_template.id),
			countdown=cumulative_delay
		)
		queued+=1


	return {
		"status" : f"{queued} tasks cretaed in celery",
		"data" : info
	}



def get_cmpn_leads_tepmlates_mailboxes(campaign_id: int, db : Session):
	cmpn = db.get(Campaign, campaign_id)
	campaign_limit = cmpn.daily_sending_limit

	# get leads from db
	statement = select(CampaignLeads, Lead).join(Lead).where(CampaignLeads.campaign_id == campaign_id,
																			CampaignLeads.stage == None).limit(campaign_limit)
	rows = db.exec(statement).all()
	only_leads_rows = [lead for camp_templ, lead in  rows]

	# get templates from db
	statement = select(CampaignTemplates, Template).join(Template).where(CampaignTemplates.campaign_id == campaign_id,
																			CampaignTemplates.followup_no == None) ##showing starting message
	rows = db.exec(statement).all()
	only_template_rows = [temp for camp_templ, temp in  rows]

	# get mailboxes from db
	statement = select(MailAccount).where(MailAccount.status =="active")
	mailbox_rows = db.exec(statement).all()

	return cmpn, only_leads_rows, only_template_rows, mailbox_rows





def get_mailbox(curr_ind : int, mailboxes : list[MailAccount]):
	size = len(mailboxes)

	for _ in range(size):
		current_mb = mailboxes[curr_ind % size]
		curr_ind += 1

		# check limit
		if current_mb.daily_limit > 0:
			return current_mb, curr_ind
	return None



