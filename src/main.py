import uvicorn

from fastapi import FastAPI
from src.users.views import router as user_router
from src.trains.views import router as trains_router
from src.food.views import router as food_router


app = FastAPI()
app.include_router(user_router)
app.include_router(trains_router)
app.include_router(food_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
