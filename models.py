from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    orders = relationship('Order', backref='customer')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    description = Column(String(500))
    reviews = relationship('Review', backref='product')
    order_items = relationship('OrderItem', backref='product')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(String(100))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_items = relationship('OrderItem', backref='order')

class OrderItem(Base):

    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

class CartItem(Base):

    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('shoppingCarts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    cart_items = relationship('CartItem', backref='cart')

class Review(Base):
    __tablename__  = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    comment = Column(String(500))
