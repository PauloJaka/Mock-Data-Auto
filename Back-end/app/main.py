from app.controllers.generator_controller import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
