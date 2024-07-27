from motor.motor_asyncio import AsyncIOMotorClient
import os
from fastapi import HTTPException

class DataBase:
    client: AsyncIOMotorClient = None
    appDB = None

db = DataBase()

async def connect_db():
    mongodb_url = os.getenv('MONGODB_URL')
    if not mongodb_url:
        raise ValueError("MONGODB_URL environment variable not set")
    db.client = AsyncIOMotorClient(mongodb_url)
    db.appDB = db.client.get_database("test") 
    try:
        # Test the connection
        await db.appDB.command("ping")
        print("MongoDB connected")
    except Exception as e:
        raise Exception(f"Error connecting to MongoDB: {e}")

def close_db():
    if db.client:
        db.client.close()
        print("Database connection closed")
