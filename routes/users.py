from typing import Dict, List
from fastapi import status, HTTPException
from data.models import User
from schemas import UserRequest, UserResponse
from fastapi import APIRouter, Depends
from data.user_repository import UserRepository
from utils.auth import get_logged_username

# prefix will add the prefix in all requests in this router
# tags will group requests in Swagger docs
router = APIRouter(prefix="/users", tags=["Users"])
user_repository = UserRepository.factory()


# ORDERING OF ROUTES IS IMPORTANT:
# /users/{username} = if this route comes first, the next route will never be reached
# /users/admin


# Optional query parameter ?name=Ivan
@router.get("/", summary="List all users (can filter by name)", response_model=List[UserResponse])
def get_all(name: str = None, username: str = Depends(get_logged_username)):
    users = user_repository.list()
    if name:
        return list(filter(lambda x: name.lower() in x.name.lower(), users))
    return users


# The response_model can set the fields you want to return to the caller
@router.get("/{id}", summary="Get a specific user", response_model=UserResponse)
def get(id: int, username: str = Depends(get_logged_username)):
    user = user_repository.get(id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")
    return user


# status_code set the default status code result
@router.post("/", summary="Add a new user", status_code=status.HTTP_201_CREATED)
def post(request: UserRequest, username: str = Depends(get_logged_username)) -> Dict[str, str]:
    user = User(**request.dict())
    user_repository.add(user)
    return {"message": "Created"}


@router.put("/{id}", summary="Update a user", response_model=UserResponse)
def put(id: int, request: UserRequest, username: str = Depends(get_logged_username)):
    user = user_repository.get(id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")

    user.name = request.name
    # ...
    user_repository.update(user)
    return user
