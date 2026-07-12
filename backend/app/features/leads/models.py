from sqlmodel import Field, SQLModel


class CreateLead(SQLModel):
    website : str
    email : str
    company_name: str | None = None


class UpdateLead(SQLModel):
    website : str | None = None
    email : str | None = None
    company_name: str | None = None


# for databse model
class Lead(CreateLead, table=True):
    id: int | None = Field(default=None, primary_key=True)


