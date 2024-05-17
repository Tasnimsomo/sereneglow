#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os

load_dotenv('.env')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
