from sqlmodel import Session, select
from fastapi import APIRouter, Depends
from schemas import UserCreate
from models import Lead
from db import engine, get_session
router = APIRouter()




@router.post("/lead")
def create_lead(user: Lead):
	with Session(engine) as session:
		session.add(user)
		session.commit()
		session.close()
	return {
		"status" : "success"
	}

@router.get("/lead")
def get_all_leads(session : Session =  Depends(get_session)):

	statement = select(Lead)

	results = session.exec(statement)

	return{
		"leads" : results.all()
	}