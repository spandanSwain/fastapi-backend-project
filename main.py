from fastapi import FastAPI
from auth.routes import auth_router
from admin.routes import admin_router

# uv run uvicorn main:app --reload
# to run the app run the following command

app = FastAPI() # init app

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
# merge all routes from router into the main app