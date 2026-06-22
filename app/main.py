from fastapi import FastAPI
from app.api.jobs import router

app = FastAPI(title="Career Agent")

app.include_router(router)


@app.get("/")
def health():
    return {"status": "healthy"}