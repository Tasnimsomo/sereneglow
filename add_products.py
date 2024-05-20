#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv('.env')

# get the database URI from environment variables
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

# create an engine to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# create a session
session = Session()

# Define product data
# lipstick department
lipsticks_data = [
    {'name': 'Matte lipstick', 'price': 12.99, 'description': 'Long lasting matte lipstick in various shades'},
    {'name': 'Liquid lipstick', 'price': 14.99, 'description': 'Highly pigmented liquid lipstick with a glossy finish'},
    {'name': 'Satin lipstick', 'price': 11.99, 'description': 'Satin-finish lipstick providing rich color and hydration'},
    {'name': 'Sheer lipstick', 'price': 10.99, 'description': 'Sheer lipstick offering a hint of color for a natural look'}
]

# foundation department
foundation_data = [
    {'name': 'Liquid foundation', 'price': 24.99, 'description': 'Full-coverage liquid foundation suitable for all skin types'},
    {'name': 'Powder foundation', 'price': 19.99, 'description': 'Lightweight powder foundation providing a natural finish'},
    {'name': 'Stick foundation', 'price': 22.99, 'description': 'Creamy stick foundation for easy application and buildable coverage'},
    {'name': 'BB cream', 'price': 18.99, 'description': 'multi-functional BB cream offering hydration, coverage and sun protection'}
]

# eyeshadow
eyeshadow_palettes_data = [
    {'name': 'Neutral Eyeshadow Palette', 'price': 29.99, 'description': 'Palette featuring a range of neutral eyeshadow shades for everyday looks'},
    {'name': 'Colorful Eyeshadow Palette', 'price': 34.99, 'description': 'Palette containing vibrant eyeshadow shades for bold and creative looks'},
    {'name': 'Smoky Eyeshadow Palette', 'price': 32.99, 'description': 'Palette with deep, sultry shades for creating smoky eye makeup looks'},
    {'name': 'Shimmer Eyeshadow Palette', 'price': 31.99, 'description': 'Palette featuring shimmering eyeshadow shades for adding sparkle to your eyes'}
]

# Define skin care products data
skin_care_data = [
    {'name': 'Moisturizing Cream', 'price': 19.99, 'description': 'Hydrating moisturizer for all skin types'},
    {'name': 'Cleansing Gel', 'price': 14.99, 'description': 'Gentle cleansing gel to remove impurities and makeup'},
    {'name': 'Serum', 'price': 29.99, 'description': 'Anti-aging serum with collagen-boosting properties'},
    {'name': 'Sunscreen', 'price': 12.99, 'description': 'Broad-spectrum sunscreen with SPF 30 protection'}
]

# Define body care products data
body_care_data = [
    {'name': 'Body Lotion', 'price': 16.99, 'description': 'Hydrating body lotion for soft and smooth skin'},
    {'name': 'Body Wash', 'price': 12.99, 'description': 'Refreshing body wash with moisturizing properties'},
    {'name': 'Body Scrub', 'price': 18.99, 'description': 'Exfoliating body scrub to remove dead skin cells'},
    {'name': 'Body Oil', 'price': 21.99, 'description': 'Nourishing body oil for deep hydration and glow'}
]

# Define hair care products data
hair_care_data = [
    {'name': 'Shampoo', 'price': 14.99, 'description': 'Gentle shampoo for clean and healthy hair'},
    {'name': 'Conditioner', 'price': 16.99, 'description': 'Moisturizing conditioner for soft and silky hair'},
    {'name': 'Hair Mask', 'price': 19.99, 'description': 'Deep conditioning hair mask for repairing damaged hair'},
    {'name': 'Hair Oil', 'price': 22.99, 'description': 'Nourishing hair oil for strength and shine'}
]

# add lipstick products to the database
for product_info in lipsticks_data:
    product = Product(**product_info, category="Lipsticks")
    session.add(product)

# add foundation products to the database
for product_info in foundation_data:
    product = Product(**product_info, category="Foundations")
    session.add(product)

# add eyeshadow palette products to the database
for product_info in eyeshadow_palettes_data:
    product = Product(**product_info, category="Eyeshadow Palettes")
    session.add(product)

# Add skin care products to the database
for product_info in skin_care_data:
    product = Product(**product_info, category="Skin Care")
    session.add(product)

# Add body care products to the database
for product_info in body_care_data:
    product = Product(**product_info, category="Body Care")
    session.add(product)

# Add hair care products to the database
for product_info in hair_care_data:
    product = Product(**product_info, category="Hair Care")
    session.add(product)

# commit the changes to persist them to the database
session.commit()

# close the session
session.close()

print("Products categorized and added successfully!")

