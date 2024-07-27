import uvicorn
from app import app
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT', '8001') 
HOST = os.getenv('HOST', '0.0.0.0') 


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=HOST, port=int(PORT), reload=True)