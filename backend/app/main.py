from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import init_db
from app.api.endpoints import router

# Create an instance of the FastAPI class
app = FastAPI()

# Define the list of allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

# Add the CORSMiddleware to the FastAPI app instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from the specified origins
    allow_credentials=True,  # Allow credentials (cookies, headers) to be sent with requests
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the router in the FastAPI app instance
app.include_router(router)

@app.on_event("startup")
def on_startup():
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)