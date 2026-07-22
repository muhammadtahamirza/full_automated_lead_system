# from celery_tasks import redis_client
from datetime import date
from sqlmodel import select, Session
from ..campaigns.models import CampaignLeads, CampaignTemplates, Campaign
from ..mailboxes.models import MailAccount
from ..leads.models import Lead
from ..templates.models import Template
from .celery_tasks import send_single_email
import random


def trigger_campaign(campaign_id: int , db : Session): #ignore

	# get cmpain from db
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
	only_template_row = [temp for camp_templ, temp in  rows]

	# get mailboxes from db
	statement = select(MailAccount).where(MailAccount.status =="active")
	mailbox_rows = db.exec(statement).all()


	## scheduling all email sendig tasks in celery

	cumulative_delay = 0
	mailbox_index = 0

	queued = 0

	for index, lead in enumerate(only_leads_rows):

		# get avaialbe next mailbox
		assigned_mailbox = get_mailbox(mailbox_index, mailbox_rows)
		if not assigned_mailbox:
			print("All mailboxes hit 0 capacity. Exiting loop.")
			return{
				"status" : "mailbox limit finished",

			}
		assigned_mailbox.daily_limit -= 1  # to check

		# get template
		shift = index // len(mailbox_rows)
		template_index = (index + shift) % len(only_template_row)
		assigned_template = only_template_row[template_index]

		cumulative_delay += random.randint(60, 100)

		# Queue the task in Redis for Celery to handle later
		send_single_email.apply_async(
			args=[ assigned_mailbox.id, lead.id, assigned_template.id],
			countdown=cumulative_delay
		)
		queued+=1

		return {
			"status" : f"{queued} tasks cretaed in celery"
		}



def get_mailbox(curr_ind : int, mailboxes : list[MailAccount]):
	for _ in range(len(mailboxes)):
		current_mb = mailboxes[mailbox_index % len(mailboxes)]
		mailbox_index += 1

		# check limit
		if current_mb['daily_limit'] > 0:
			return current_mb
	return None


