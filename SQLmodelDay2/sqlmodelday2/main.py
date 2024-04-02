from sqlmodel import Field, SQLModel, create_engine
from engines import engine
from create_records import create_products
from select_products import select_product
from dotenv import load_dotenv
from sqlalchemy import MetaData


def recreate_table():
    metadata = MetaData()
    SQLModel.metadata.create_all(engine)
    print('Table Created Again')


def main():
    load_dotenv()
    # recreate_table()
    # create_products()
    select_product()


if __name__ == '__main__':
    main()
