from sqlmodel import SQLModel, Field


#TODO : adding rest of data in campgasins for AI agent understanding like system prompts etc

class CreateCampaign(SQLModel):
	name: str

class UpdateCampaign(SQLModel):
	name : str | None = None

class Campaign(CreateCampaign, table= True):
	id: int | None = Field(default=None, primary_key=True)



## tables for many-to-many relatoins
"""connecting leads to campaigns"""
## non-primary keys tells which mailbox and tmeplate was used for that lead under a campaign would be assigned by the cold email system
##1. user would add lead to capmain only
##2. system would automatically assign tempalte and mail and stage
class CampaignLeads(SQLModel, table=True):
	campaign_id : int | None = Field(default=None, foreign_key="campaign.id", primary_key=True)
	lead_id : int | None = Field(default=None, foreign_key="lead.id", primary_key=True)
	mail_id : int | None = Field(default=None, foreign_key="mailaccount.id")
	template_id : int | None = Field(default=None,foreign_key="template.id")
	stage : str | None  = Field(default=None)


"""connecting templates to campaigns"""
class CampaignTemplates(SQLModel, table =True):
	template_id : int | None = Field(default=None, foreign_key="template.id", primary_key=True)
	campaign_id : int | None = Field(default=None, foreign_key="campaign.id", primary_key=True)
	description : str | None
	followup_no : int | None