from sqlalchemy import Column, BigInteger, CHAR, REAL

from app.db import base

class Product(base):
    __tablename__ = 'products'

    id: Column[int] = Column(name="product_id", type_=BigInteger, primary_key=True)
    name: Column[str] = Column(name="name", type_=CHAR(255), unique=True, nullable=False)
    category: Column[str] = Column(name="category", type_=CHAR(255), nullable=False)
    price: Column[float] = Column(name="price", type_=REAL, nullable=False)

    def to_dict(self):
        return dict(product_id=self.id, name=self.name, category=self.category, price=self.price)