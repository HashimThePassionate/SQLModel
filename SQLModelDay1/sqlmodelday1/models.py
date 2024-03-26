from sqlmodel import Field, SQLModel, create_engine
from datetime import date


class Customer(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    first_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    email: str = Field(max_length=255)
    phone: str = Field(max_length=100)
    age: int | None = None
    birth_date: date | None = Field(default=None, nullable=True)
