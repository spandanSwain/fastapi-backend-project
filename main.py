from fastapi import FastAPI
from auth.routes import auth_router
from admin.routes import admin_router
from fastapi.middleware.cors import CORSMiddleware

# uv run uvicorn main:app --reload
# to run the app run the following command

app = FastAPI() # init app
# ... after app = FastAPI() ...

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Allow your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
# merge all routes from router into the main app