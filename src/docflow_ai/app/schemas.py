from pydantic import BaseModel, Field, HttpUrl
from typing import Literal
from enum import Enum

class DocumentCategory(str, Enum):
    programming = "Programming"
    business = "Business"
    finance = "Finance"
    research = "Research"
    
class DocumentBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str  | None = None
    category: DocumentCategory | None = None
    
class DocumentSource(BaseModel):
    name: str
    url: HttpUrl | None = None
    

class CreateDocument(DocumentBase):
    priority: int = Field(default=3, ge=1, le=5)
    source: DocumentSource | None = None
    
    
class DocumentResponse(DocumentBase):
    id: int
