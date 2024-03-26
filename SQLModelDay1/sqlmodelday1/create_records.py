from models import Customer
from datetime import date
from engines import engine
from sqlmodel import Session
def create_customers():
    customer1: Customer = Customer(
        first_name='Muhammad',
        last_name='Hashim',
        email='hashiimtahir@gmail.com',
        phone='0734672273',
        age=24,
        birth_date=date(1999, 10, 30)
    )

    customer2: Customer = Customer(
        first_name="John",
        last_name="Doe",
        email="johndoe@example.com",
        phone="123-456-7890",
        age=35,
        # Assuming you have imported 'date' from 'datetime'
        birth_date=date(1987, 10, 25)
    )
    with Session(engine) as session:
        session.add(customer1)
        session.add(customer2)
        session.commit()

