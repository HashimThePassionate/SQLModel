from sqlmodel import Field, SQLModel, create_engine


class Product_table(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    title: str = Field(max_length=255)
    description: str = Field(max_length=255)
    price: float = Field()
    inventory: int = Field()
