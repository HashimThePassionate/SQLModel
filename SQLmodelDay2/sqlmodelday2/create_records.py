from models import Product_table
from engines import engine
from sqlmodel import Session


def create_products():
    pro1: Product_table = Product_table(
        title="Product 1",
        description="Description of Product 1",
        price=10.99,
        inventory=100
    )
    pro2: Product_table = Product_table(
        title="Product 2",
        description="Description of Product 2",
        price=19.99,
        inventory=50
    )
    pro3: Product_table = Product_table(
        title="Product 3",
        description="Description of Product 3",
        price=5.99,
        inventory=200
    )
    print(f'Product 1 {pro1}')
    print(f'Product 2 {pro2}')
    print(f'Product 3 {pro3}')

    with Session(engine) as session:
        session.add(pro1)
        session.add(pro2)
        session.add(pro3)
        # session.commit()
