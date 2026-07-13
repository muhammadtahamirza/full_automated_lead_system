from sqlmodel import SQLModel, Field


class CreateTemplate(SQLModel):
	subject: str
	body: str

class UpdateTemplate(SQLModel):
	subject: str | None = None
	body: str | None = None


class Template(CreateTemplate, table=True):
	id: int | None = Field(default=None, primary_key=True)


