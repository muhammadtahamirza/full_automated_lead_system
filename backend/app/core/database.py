from sqlmodel import create_engine, Session
from fastapi import Depends
from typing import Annotated
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


engine = create_engine(sqlite_url)




def get_session():
	with Session(engine) as session:
		yield session


db_dependency = Annotated[Session, Depends(get_session)]


