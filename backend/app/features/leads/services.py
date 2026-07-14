import csv
import codecs
from features.leads.models import CreateLead, Lead
from sqlmodel import insert, Session
from fastapi import UploadFile



def upload_leads_csv(file : UploadFile  , db: Session) -> list[int]:
	csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))

	valid_dicts = []
	# errors = [] TODO handling bad rows
	for row in (csvReader):
		Lead.model_validate(row)
		valid_dicts.append(row)

	statement = insert(Lead).returning(Lead.id) #return ids

	##updaed rows with ids from database
	updated_db_dicts = db.scalars(statement, valid_dicts).all()
	db.commit()
	return updated_db_dicts