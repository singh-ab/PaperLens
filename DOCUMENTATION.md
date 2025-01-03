# Project Documentation

## Architecture Overview

### 1. Project Structure

The project follows a client-server architecture with distinct frontend and backend components.

```
project/
├── frontend/          # React application
│   ├── src/
│   │   ├── components/
│   │   └── services/
└── backend/           # FastAPI server
    ├── api/
    ├── services/
    └── models/
```

### 2. Key Components

#### Backend Components

##### API Layer (endpoints.py)

- Handles HTTP requests
- Manages two primary endpoints:
  - `/upload/`: PDF document processing
  - `/chat/`: Conversation handling
- Validates incoming requests

##### Database Layer

- Uses PostgreSQL via SQLAlchemy ORM
- Key files:
  - `base.py`: Database connection management
  - `models.py`: PDFText model definition

##### Services Layer

- `pdf_processor.py`: Handles PDF text extraction
- `nlp_processor.py`: Integrates Gemini for Q&A processing
- Storage services:
  - AWS S3 for PDF document storage
  - PostgreSQL for processed text storage

#### Frontend Components

##### UI Components

- PDF upload interface
- Chat interface with message history
- Response display with formatting

##### API Integration

- Manages backend communication
- Handles file uploads and chat requests
- Error state management

### 3. Data Flow

1. User uploads PDF → Frontend → S3 Storage
2. Text extraction → Database storage
3. User query → LLM processing → Response
4. Response display → User interface

### 4. API Endpoints

```
POST /api/upload
- Accepts PDF files
- Returns document ID

POST /api/chat
- Accepts user queries
- Returns AI-generated responses
```

### 5. Error Handling

- File validation for PDFs
- Database connection monitoring
- S3 storage error management
- LLM processing error handling

### 6. Technologies

- Backend: FastAPI, Langchain, PostgreSQL
- Frontend: React, TypeScript, Tailwind
- AI: Google Gemini
- Storage: NeonDB, AWS S3
