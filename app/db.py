from typing import Any, Generator

from sqlalchemy import URL
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from app.config import configuration

conn_url: URL = URL.create(
    drivername="postgresql+psycopg",
    host=configuration.get('database', 'host'),
    port=configuration.getint('database', 'port'),
    username=configuration.get('database', 'username'),
    password=configuration.get('database', 'password'),
    database=configuration.get('database', 'name')    
)
engine: Engine = create_engine(conn_url)

session: Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base: Any = declarative_base()
metadata: Any = base.metadata

def get_session() -> Generator:
    db: Session = session()
    try:
        yield db
    finally:
        db.close()
