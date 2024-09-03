# Describe our single table and ensure it's created

from sqlalchemy import Column, Float, Integer
from sqlalchemy.orm import declarative_base

from db import engine

Base = declarative_base()


class GeneratedNumbers(Base):
    __tablename__ = "generated_numbers"

    id = Column(Integer(), primary_key=True)
    number = Column(Float(), nullable=False)


Base.metadata.create_all(engine)
