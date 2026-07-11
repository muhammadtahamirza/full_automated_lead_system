from sqlmodel import Field, SQLModel


class Lead(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    website : str
    email : str
    company_name: str | None = None



class MailAccount(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    password : str
    smtp_server : str
    port : int


class template(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)
	subject: str
	body: str


class Campaign(SQLModel, table=True):
	id: int | None = Field(default=None, primary_key=True)




