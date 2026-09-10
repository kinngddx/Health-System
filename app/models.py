from app.database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer , String



# class Base(declarative_base):
#     pass


class Product(Base):
    __tablename__="products"
    id = mapped_column(Integer, primary_key=True)   #primarey key true mtlb ki unique hoga 
    name = mapped_column(String(50), nullable=False)
    price = mapped_column(Integer)
    stock = mapped_column(Integer)



