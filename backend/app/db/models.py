from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base

# Define the PDFText model
class PDFText(Base):
    # Set the table name for the model
    __tablename__ = "pdf_texts"

    # Define the columns for the table
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    filename = Column(String, unique=True, index=True)  # Unique filename column, indexed
    text = Column(Text, nullable=False)  # Text column, cannot be null
