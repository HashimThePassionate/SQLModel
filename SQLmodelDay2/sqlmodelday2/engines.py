from sqlmodel import create_engine
import os

DATABASE_STRING = os.getenv('DATABASE_STRING')
engine = create_engine(DATABASE_STRING, echo=True)
