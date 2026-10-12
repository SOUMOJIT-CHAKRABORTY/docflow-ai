from fastapi import APIRouter, status, Query, Depends
from schemas import CreateDocument, DocumentResponse
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)
@router.get("")
async def list_documents(
    search: str | None = None,
    skip: int = 0,
    limit: int = Query(default=10, le=100)
):
    return {
        "search": search,
            "skip": skip,
            "limit": limit
            }

@router.get("/{document_id}")
async def get_document(document_id: int):
    return {
        "id": document_id,
    }

@router.post("", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def create_document(
    document: CreateDocument,
    db: Session = Depends(get_db)
    ):
    return {
        "id": 1,
        "title": document.title,
        "description": document.description,
        "category": document.category,
    }