#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product
from dotenv import load_dotenv
import os

# load enviroment variables from .env file
load_dotenv('.env')

# get the database URI from enviroment variables
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

# create an engine to connect to data base

engine = create_engine(SQLALCHEMY_DATABASE_URI)

# create a sessionmaker bound to the engine
session = sessionmaker(bind=engine)

# create a session
session = Session()

#Define a product data
# lipstick department
lipsticks_data = [
    {'name': 'Matte lipstick', 'price':12.99, 'description': 'Long lasting matte lipstick in various shades'},
    {'name': 'Liquid lipstick', 'price':14.99, 'description': 'Highly pigmented liquid lipstick with a glossy finish'},
    {'name': 'Satin lipstick', 'price':11.99, 'description': 'Satin-finish lipstick providing rich colour and hydration'},
    {'name': 'Sheer lipstick', 'price':10.99, 'description': 'Sheer lipstick offering a hind of colour for a natural look'}
]

# foundation department
foundation_data = [
    {'name': 'Liquid foundation', 'price':24.99, 'description': 'Full-coverage liquid foundation suitable for all skin types'},
    {'name': 'Powder foundation', 'price':19.99, 'description': 'Lightweight powder foundation providing a natural finish'},
    {'name': 'Stick foundation', 'price':22.99, 'description': 'Creamy stick foundation for easy application and buildable coverage'},
    {'name': 'BB cream', 'price':18.99, 'description' : 'multi-functional BB cream offering hydration, coverage and sun protection'}
]

# eye shadow
eyeshadow_palettes_data = [
    {'name': 'Neutral Eyeshadow Palette', 'price': 29.99, 'description': 'Palette featuring a range of neutral eyeshadow shades for everyday looks'},
    {'name': 'Colorful Eyeshadow Palette', 'price': 34.99, 'description': 'Palette containing vibrant eyeshadow shades for bold and creative looks'},
    {'name': 'Smoky Eyeshadow Palette', 'price': 32.99, 'description': 'Palette with deep, sultry shades for creating smoky eye makeup looks'},
    {'name': 'Shimmer Eyeshadow Palette', 'price': 31.99, 'description': 'Palette featuring shimmering eyeshadow shades for adding sparkle to your eyes'}
]

# add lipstick products to the database
for product_info in lipsticks_data:
    product = Product(**product_info, category="Lipsticks")
    session.add(product)
    
# add foundation products to the database
for product_info in foundation_data:
    product = Product(**product_info, category="Foundations")
    session.add(product)
    
#add eyeshadow palette prpducts to the data base
for product_info in eyeshadow_palettes_data:
    product = Product(**product_info, category="Eyeshadow Palettes")
    session.add(product)
    
# commmit the changes to persist them to data base
session.commit()

# close the session
session.close()

print("Products categorized and added successfully!")
