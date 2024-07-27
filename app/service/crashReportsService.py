from typing import Dict
import re
from datetime import datetime
import json
from app.models.crashReports import CrashReportSchema


async def init(date: str, err_data: Dict[str, str]):
    from ..crud.crud import SaveCrashReports
    res_data = await format_crash_reports(date,err_data)
    result = await SaveCrashReports(res_data)
    return result

    

async def format_crash_reports(date: str, err_data: Dict[str, str]) -> CrashReportSchema:
    try:
        if isinstance(err_data.get('err_resp'), str):
            err_resp = json.loads(err_data['err_resp'])
        else:
            err_resp = err_data.get('err_resp')
        # Extract fields
        message = err_resp.get("message")
        stack = [line.strip() for line in err_resp.get("stack", "").split('\n')]
        first_stack_line = stack[1] if stack else ''
        pattern = r"\((.*):(\d+):(\d+)\)$"
        stack_line_parts = re.search(pattern, first_stack_line)
        # stack_line_parts = re.match(r'/\((.*):(\d+):(\d+)\)$/', first_stack_line)
        file_name, line_number, column_number = '', '', ''
        if stack_line_parts:
            file_name = stack_line_parts.group(1)
            line_number = stack_line_parts.group(2)
            column_number = stack_line_parts.group(3)
        service_name = file_name.split('/')[5]
        # Create and return the formatted crash report
        return {
            "TIMESTAMP": datetime.now().isoformat(),
            "ERROR": message,
            "FILE": file_name,
            "LINE": int(line_number) if line_number.isdigit() else None,
            "COLUMN": int(column_number) if column_number.isdigit() else None,
            "STACK": stack,
            "SERVICE": service_name,
            "EMBEDDING": [1.0, 0.0],
            "CREATED_DATE": datetime.now().isoformat()
        }
    except Exception as err:
        print("Error formatting crash reports:", err)
        raise err

