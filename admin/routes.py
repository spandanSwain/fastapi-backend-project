from fastapi import APIRouter, HTTPException, status, Depends
from configurations import db
from database.Users.models import Users

admin_router = APIRouter()
users_collection = db["users"]

@admin_router.get("/report")
def get_all_user_report_json():
    try:
        users = []
        cursor = users_collection.find(
             {},
             {
                "_id": 1,
                "employee_id": 1,
                "employee_name": 1,
                "employee_email": 1,
                "employee_domain": 1,
                "employee_status": 1
            }
        )

        for user in cursor:
            user["_id"] = str(user["_id"])
            users.append(user)
        
        return {"users": users}
    except HTTPException as hex:
        raise hex
    except Exception as ex:
        return HTTPException(
            status_code=500,
            detail=f"Some exception occured in routes.py/report() /admin/report :: {ex}"
        )


@admin_router.get("/kpi")
def get_dashboard_data_json():
    try:
        pass
    except HTTPException as hex:
        raise hex
    except Exception as ex:
        return HTTPException(
            status_code=500,
            detail=f"Some exception occured in routes.py/kpi() /admin/kpi :: {ex}"
        )