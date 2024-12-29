from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

engine = create_engine("postgresql+psycopg://postgres:password@localhost:5432/postgres")

def get_session():
    return Session(engine)
