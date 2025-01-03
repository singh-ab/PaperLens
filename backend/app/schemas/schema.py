from pydantic import BaseModel

# Define the UploadResponse model
class UploadResponse(BaseModel):
    id: int  # ID of the uploaded PDF text
    filename: str  # Filename of the uploaded PDF
    message: str  # Success message for the upload

# Define the QuestionRequest model
class QuestionRequest(BaseModel):
    text_id: int  # ID of the PDF text to ask a question about
    question: str  # The question to be answered

# Define the AnswerResponse model
class AnswerResponse(BaseModel):
    answer: str  # The generated answer to the question