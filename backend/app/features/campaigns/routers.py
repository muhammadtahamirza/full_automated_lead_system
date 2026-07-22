from core.routers import build_crud_router
from core.database import get_session, Session
from fastapi import Depends, File, UploadFile
from sqlmodel import select, insert
from features.templates.models import Template
from features.campaigns.models import Campaign, CampaignTemplates, CampaignLeads
from features.leads.models import Lead
from .models import Campaign, CreateCampaign, UpdateCampaign
from features.leads.services import upload_leads_csv

from .services import trigger_campaign
# campaignRouter = build_crud_router(
# 	model=Campaign,
#     create_schema=CreateCampaign,
#     update_schema=UpdateCampaign,
#     prefix="/campaign",
#     tag="Camgaigns",
# )
from fastapi import APIRouter

campaignRouter = APIRouter()

@campaignRouter.post("/trigger_campgain")
def do_test(db : Session = Depends(get_session)):

	return trigger_campaign(1, db)



@campaignRouter.post("/add-templates-campaign")
def add_template_to_campaign(templ : CampaignTemplates,  db : Session = Depends(get_session)):

	template = db.get(Template, templ.template_id)
	campaign = db.get(Campaign, templ.campaign_id)
	if template and campaign:
		db.add(templ)
		db.commit()
		return{
			"status" : "success"
		}
	return{
		"status" : "not found eighter templ or campasing"
	}


@campaignRouter.get("/get-all-templates")
def get_all_tmeplate_of_campaing(camp_id : int ,  db : Session = Depends(get_session)):
	statement = select(CampaignTemplates, Template).join(Template).where(CampaignTemplates.campaign_id == camp_id)
	rows = db.exec(statement).all()
	only_template_rows = [t for ct, t in  rows]

	return {
		"rows" : only_template_rows
	}





@campaignRouter.post("/add-leads-campaign")
def add_leads_csv_campagin(camp_id: int, file : UploadFile = File(...),  db : Session = Depends(get_session)):
	valid_ids = upload_leads_csv(file, db)

	lead_campaign_dict: list[dict] = []

	###campainns

	for lead_id in valid_ids:
		## validating each row and saving the list of dicts instead of list of objs in database
		row = {
			"campaign_id" : camp_id,
			"lead_id" : lead_id
		}
		cmpn_lead_obj = CampaignLeads.model_validate(row)
		lead_campaign_dict.append(cmpn_lead_obj.model_dump())

		## saving bulk dictionries
	statement = insert(CampaignLeads).values(lead_campaign_dict)
	db.exec(statement)
	db.commit()
	return {
		"status" : f"{len(lead_campaign_dict)} rows inserted in campain {camp_id}"
	}


@campaignRouter.get("/get-all-leads")
def get_all_tmeplate_of_campaing(camp_id : int ,  db : Session = Depends(get_session)):
	statement = select(CampaignLeads, Lead).join(Lead).where(CampaignLeads.campaign_id == camp_id)
	rows = db.exec(statement).all()
	only_leads_rows = [lead for camp_templ, lead in  rows]  ## seperate all lead rows to return

	return {
		"rows" : only_leads_rows
	}




@campaignRouter.post("/start-campaign")
def start_email_campaigns(campgain_id : int, db : Session = Depends(get_session)):
	return trigger_campaign(campaign_id=campgain_id, db=db)
