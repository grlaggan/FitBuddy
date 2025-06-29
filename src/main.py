from fastapi import FastAPI
from src.users.views import router as user_router


app = FastAPI()
app.include_router(user_router)
