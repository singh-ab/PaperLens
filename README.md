# Chat with your PDFs using AI

## Tech Stack

### Frontend

- React
- TypeScript
- Tailwind CSS
- Vite

### Backend

- FastAPI
- Langchain
- PostgreSQL (NeonDB)
- Gemini
- AWS S3

## Installation Steps

### Step 1: Clone the Project

Start by cloning the repository to your local machine.

```bash
git clone https://github.com/singh-ab/PaperLens.git
```

### Step-2: Backend Setup

1. Navigate to backend directory:

```bash
cd ../backend
```

2. Create `.env` file using the [.env.example](./backend/.env.example) file.

3. Setup Python environment:

```bash
py -m venv someenv
.\someenv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start backend server (default port 8000):

```bash
py run.py
```

### Step 3: Frontend Setup

1. Navigate to frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start development server (default port 5173):

```bash
npm run dev
```
