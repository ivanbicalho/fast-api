from typing import Dict
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utils.auth import generate_access_token

router = APIRouter(tags=["Login"])


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Dict[str, str]:
    if form_data.username == "admin" and form_data.password == "admin":
        return {
            "access_token": generate_access_token(form_data.username),
            "token_type": "bearer",
        }

    raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid username or password")
