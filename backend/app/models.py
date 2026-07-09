from sqlmodel import Field, SQLModel


class Lead(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    website : str
    email : str
    company_name: str | None = None

