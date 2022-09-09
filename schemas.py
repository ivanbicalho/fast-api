from typing import Set
from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import date


class Address(BaseModel):
    country: str = Field(title="Country", description="Country address")
    city: str = Field(title="City", description="City address")

    # This is a way to give an example
    # The other way is by using Field method = Field(example="Ivan")
    class Config:
        schema_extra = {
            "example": {
                "country": "Brasil",
                "city": "Belo Horizonte",
            }
        }


# FastAPI relies on pydantic to data validation and uses the info here in docs like Swagger
class UserRequest(BaseModel):
    name: str = Field(title="Name", description="User first name", example="Ivan")
    age: int = Field(title="Age", description="User age", example="22", gt=0)
    email: EmailStr = Field(title="Email", description="User email", example="ivan.bicalho@carta.com")
    birth_date: date = Field(title="Birth Date", description="User birth date", example="1990-01-25")
    profile_url: HttpUrl = Field(title="Profile URL", description="User profile URL", example="https://ivanbicalho.com")
    tags: Set[str] = Field(
        default=[], example=["engineer", "dev", "python"]
    )  # setting a default makes the field optional
    address: Address = None  # optional field


# Suppose we want to return just these fields in the response
class UserResponse(BaseModel):
    id: int
    name: str
