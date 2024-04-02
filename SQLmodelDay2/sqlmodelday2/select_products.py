from models import Product_table
from engines import engine
from sqlmodel import Session, select


def select_product():
    with Session(engine) as session:
        statement = select(Product_table)
        results = session.exec(statement)
        record = results.all()
        # print(record)
        for r in results:
            print(f'''
Read using Select: {r.id}  {r.title}  {r.description}  {r.price}  {r.inventory}
            ''')
