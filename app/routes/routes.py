from typing import Any, Dict
from ..service import crashReportsService
from fastapi import APIRouter,HTTPException


router = APIRouter()

@router.post("/saveCrashReports")
async def read_root(reports:  Dict[Any, Any]):
    try:
        reports_dict = reports
        # extracting date and error
        date = reports_dict['headers']['date']
        error = reports_dict['headers']['error']
        result = await crashReportsService.init(str(date),error)
        return result
    except Exception as e:
        print("Error processing reports:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/getCrash")
async def get_root():
    return "Hello my application"
    


