from fastapi import FastAPI, status
from schemas import CreateDocument, DocumentResponse
from routes.documents import router as documents_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi from Document upload api"}

app.include_router(documents_router)
