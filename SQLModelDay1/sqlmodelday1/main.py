from sqlmodel import Field, SQLModel, create_engine
from models import Customer
from engines import engine
from create_records import create_customers


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    create_customers()


if __name__ == '__main__':
    main()
