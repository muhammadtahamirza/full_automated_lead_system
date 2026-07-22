from sqlmodel import SQLModel, Field



class CreateMail(SQLModel):
    email: str
    password : str
    smtp_server : str
    port : int
    daily_limit : int
    status: str

class UpdateMail(SQLModel):
    email: str | None = None
    password : str | None = None
    smtp_server : str | None = None
    port : int | None = None
    daily_limit : int | None = None
    status: str| None = None



## for the sql model to put data in database
class MailAccount(CreateMail, table=True):
    id: int | None = Field(default=None, primary_key=True)
