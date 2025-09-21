from fastapi import APIRouter
from model import mysql_test

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404:{"description":"Not found"}}
)



@router.get("/list",summary="admin 조회")
def get_user():
    results = mysql_test.list_admin()
    return results