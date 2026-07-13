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

class CampaignLeads(SQLModel, table=True):
	pass


"""connecting templates to campaigns"""
class CampaignTemplates(SQLModel, table =True):
	pass
