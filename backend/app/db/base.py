from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.db.base_class import Base  # Updated import
from app.db.models import PDFText  # Ensure the model is imported

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

# Define a dependency function for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()