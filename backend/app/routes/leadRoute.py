from sqlmodel import Session, select
from fastapi import APIRouter, Depends
from schemas import UserCreate
from models import Lead, MailAccount
from backend.app.core.database import engine, get_session
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



@router.post("/add-email")
def add_email(email: MailAccount):
	with Session(engine)as session:
		session.add(email)
		response =session.commit()
		print(response)
		session.close()


	return {
		"status" : "email added"
	}

@router.get("/all-emails")
def get_all_email(session : Session =  Depends(get_session)):
	statemet =select(MailAccount)
	output = session.exec(statemet)

	# print(type(output._allrows()))
	data = output.all()

	# print(output)
	print(data)

	return {"emails" : data}

@router.get("/lead")
def get_all_leads(session : Session =  Depends(get_session)):

	statement = select(Lead)

	results = session.exec(statement)
	data = results.all()

	return{
		"leads" : data
	}