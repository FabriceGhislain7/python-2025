from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, declarative_base

# Moteur SQLAlchemy
engine = create_engine("sqlite:///school.db", echo=True)

# Double système (comme en cours)
Base = declarative_base()
metadata = MetaData()

# Session pour l'ORM
SessionLocal = sessionmaker(bind=engine)