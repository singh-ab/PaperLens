import uvicorn
from app.main import app

# Run the app with Uvicorn on host 0.0.0.0 and port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
