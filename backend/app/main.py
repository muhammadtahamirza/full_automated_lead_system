from sqlmodel import SQLModel
from fastapi import FastAPI
import models
from backend.app.core.database import engine

from routes import leadRoute
app = FastAPI()


SQLModel.metadata.create_all(engine)


app.include_router(leadRoute.router)

@app.get("/")
def health():
	return{
		"message" : "working fine"
	}


