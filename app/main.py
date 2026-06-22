from fastapi import FastAPI

app = FastAPI(title="Career Agent")

@app.get("/")
def health():
    return {"status": "healthy"}