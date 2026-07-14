from core.routers import build_crud_router
from sqlmodel import Session, insert
from core.database import get_session, Session
from fastapi import File, UploadFile, Depends
from .models import Lead, CreateLead, UpdateLead
from .services import upload_leads_csv

prefix = "/leads"
leadRotuer = build_crud_router(
	model=Lead,
    create_schema=CreateLead,
    update_schema=UpdateLead,
    prefix=prefix,
    tag="Leads",

)

## TODO to be decided weather i should allow direct upload or not
@leadRotuer.post("/upload-leads-csv")
def upload_csv(file : UploadFile = File(...) , db: Session = Depends(get_session)):
	valid_ids = upload_leads_csv(file,db)
	return{
		"status" : f"{len(valid_ids)} rows inserted"
	}







"""specifc cruds"""
# @router.post("/lead", response_model= Lead)
# def create_lead(lead : CreateLead,  session:db_session ):
# 	ld = repository(session, Lead)
# 	db_lead = lead.model_dump()
# 	user = Lead(**db_lead)
# 	row = ld.create_row(user)
# 	return row


# @router.get("/lead", response_model=list[Lead])
# def read_all_leads(session: db_session):
#     ld = repository(session, Lead)
#     rows = ld.get_all_rows()
#     return rows

# @router.get("/lead/{id}", response_model=Lead)
# def read_lead_by_id(id: int, session: db_session):
# 	ld = repository(session, Lead)
# 	row = ld.get_row_from_id(id)
# 	return row


# @router.put("/lead/{id}", response_model=Lead)
# def update_lead(id :int, ld: UpdateLead, session: db_session):
# 	db = repository(session, Lead)
# 	return db.update_row(id, ld)


# @router.delete("/lead/{id}")
# def delete_lead(id:int, session: db_session):
# 	db = repository(session, Lead)
# 	status = db.delete_row(id)
# 	return status


