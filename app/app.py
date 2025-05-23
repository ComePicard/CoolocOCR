from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="CoolocOCR")

app.include_router(router, prefix="")
