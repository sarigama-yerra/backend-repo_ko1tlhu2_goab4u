from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Contact(BaseModel):
    """
    Contact messages collection schema
    Collection name: "contact" (lowercase)
    """
    name: str = Field(..., min_length=1, max_length=120)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=5000)
