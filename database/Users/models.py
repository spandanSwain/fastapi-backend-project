from pydantic import BaseModel
from datetime import datetime

class Users(BaseModel):
    employee_id: int
    employee_name: str
    employee_email: str
    employee_domain: str
    employee_password: str
    employee_status: bool = False
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))