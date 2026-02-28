from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from configurations import db
from database.Users.models import Users
from auth.hashing import hash_password, verify_password
from auth.jwt_handler import create_access_token
from auth.dependencies import get_current_user

auth_router = APIRouter()
users_collection = db["users"]

@auth_router.post("/register")
def register(user: Users):
    user_dict = user.model_dump()
    try:
        existing = users_collection.find_one({"employee_id": int(user.employee_id)})
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee ID already exists"
            )

        user_dict["employee_password"] = hash_password(str(user.employee_password))
        resp = users_collection.insert_one(user_dict)
        return {"message": f"User created successfully with id = {resp.inserted_id}"}
    except HTTPException as hex:
        raise hex
    except Exception as ex:
        return HTTPException(
            status_code=500,
            detail=f"Some exception occured in routes.py/register() /auth/register :: {ex}"
        )


@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        employee_id = int(form_data.username)
        employee_password = form_data.password
        user = users_collection.find_one({"employee_id": employee_id})

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid employee_id"
            )

        if not verify_password(employee_password, user["employee_password"]):
            raise HTTPException(
                status_code=401,
                detail="Invalid password"
            )

        token = create_access_token(employee_id)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except HTTPException as hex:
        raise hex
    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=f"Some exception occured in routes.py/login() /auth/login :: {ex}"
        )


@auth_router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "employee_id": current_user["employee_id"],
        "employee_name": current_user["employee_name"],
        "employee_email": current_user["employee_email"]
    }