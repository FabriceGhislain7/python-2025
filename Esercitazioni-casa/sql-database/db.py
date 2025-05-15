from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

# Moteur SQLAlchemy
engine = create_engine("sqlite:///school.db", echo=True)

# Creazione della base per le classi ORM
Base = declarative_base()
metadata = MetaData()

# Sessione per interagire con il database
SessionLocal = sessionmaker(bind=engine)
