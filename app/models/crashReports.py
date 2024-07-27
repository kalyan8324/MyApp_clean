from pydantic import BaseModel
from typing import List
from datetime import datetime
from pymongo import MongoClient


class CrashReportSchema(BaseModel):
    TIMESTAMP: str
    ERROR: str
    FILE: str
    LINE: int
    COLUMN: int
    STACK: List[str]
    SERVICE: str
    EMBEDDING: List[float]
    CREATED_DATE: datetime

    # example 
    class Config:
        schema_extra = {
            "example": {
                "TIMESTAMP": "2024-07-23T10:20:30.400Z",
                "ERROR": "Example error message",
                "FILE": "example_file.py",
                "LINE": 42,
                "COLUMN": 10,
                "STACK": ["Error at line 42", "Error at line 43"],
                "SERVICE": "phub",
                "EMBEDDING": [0.1, 0.2, 0.3, 0.4],
                "CREATED_DATE": "2024-07-23T10:20:30.400Z"
            }
        }
        
#  resp
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
