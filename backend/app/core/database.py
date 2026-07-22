from sqlmodel import create_engine, Session
from fastapi import Depends
from typing import Annotated


#TODO put username pass in .env
DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)




def get_session():
	with Session(engine) as session:
		yield session


db_dependency = Annotated[Session, Depends(get_session)]


