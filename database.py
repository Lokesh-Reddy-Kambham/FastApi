from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:5711@localhost:5432/fastapidb"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

