from typing import Dict
from fastapi import APIRouter, Depends
from utils.auth import get_logged_username

router = APIRouter(prefix="/greetings", tags=["Greetings"])


@router.get("/hello", summary="Hello to anyone")
def hello() -> Dict[str, str]:
    return {"message": "Hello!"}


@router.get("/hi", summary="Hi to the logged user only")
def hello(username: str = Depends(get_logged_username)) -> Dict[str, str]:
    return {"message": f"Hi {username}"}
