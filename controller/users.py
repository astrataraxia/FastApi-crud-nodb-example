from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404:{"description":"Not found"}}
)


class User(BaseModel):
    user_id: int

temp_db = {
    1: User(user_id=1),
    2: User(user_id=2),
    3: User(user_id=3),
} 

@router.get("/{user_id}",summary="유저조회")
def get_user(user_id:int) -> User:
    return temp_db[user_id]