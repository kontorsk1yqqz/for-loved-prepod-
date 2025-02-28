from typing import List
from fastapi import APIRouter, Depends
from src.models.users import User, get_user_service, UserService

router = APIRouter()

@router.get("/users", response_model=List[User])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()
