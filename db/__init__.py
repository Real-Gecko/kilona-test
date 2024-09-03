# Utilize sqlalchemy to connect to DB
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from db import settings

url = URL.create(
    drivername="postgresql",
    username=settings.POSTGRES_USER,
    host=settings.POSTGRES_HOST,
    database=settings.POSTGRES_DB,
    password=settings.POSTGRES_PASSWORD,
)

engine = create_engine(url)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
