from sqlmodel import create_engine
from connection_string import DATABASE_STRING


engine = create_engine(DATABASE_STRING, echo=True)
