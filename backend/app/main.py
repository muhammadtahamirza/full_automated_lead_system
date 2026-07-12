from sqlmodel import SQLModel
from fastapi import FastAPI, Depends
from core.database import engine

from features.leads.routers import leadRotuer
from features.mailboxes.routers import mailRouter
from features.outreach.routers import outreachRouter


app = FastAPI()


SQLModel.metadata.create_all(engine)

app.include_router(leadRotuer)
app.include_router(mailRouter)
app.include_router(outreachRouter)



@app.get("/")
def health():
	return{
		"message" : "working fine"
	}
