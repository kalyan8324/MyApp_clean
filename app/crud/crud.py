from fastapi import HTTPException
from ..database.dbconnection import db

# helpers
def crash_rep_helper(crash_report) -> dict:
    return {
        "id": str(crash_report["_id"]),
        "TIMESTAMP": crash_report["TIMESTAMP"],
        "ERROR": crash_report["ERROR"],
        "FILE": crash_report["FILE"],
        "LINE": crash_report["LINE"],
        "COLUMN": crash_report["COLUMN"],
        "STACK": crash_report["STACK"],
        "SERVICE": crash_report["SERVICE"],
        "EMBEDDING": crash_report["EMBEDDING"],
        "CREATED_DATE": crash_report["CREATED_DATE"],
    }

# Add a new crash report into the database
async def SaveCrashReports(crashData: dict) -> dict:
    try:
        # # 
        # if db.appDB is None:
        #     raise HTTPException(status_code=500, detail="Database not initialized")
        # To get Collection name
        collection = db.appDB["CrashReports"]
        result = await collection.insert_one(crashData) 
        # checking inserted or not  
        if result.inserted_id:
            inserted_doc = await collection.find_one({"_id": result.inserted_id})
            return crash_rep_helper(inserted_doc)
        else:
            raise HTTPException(status_code=400, detail="Insertion failed")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
