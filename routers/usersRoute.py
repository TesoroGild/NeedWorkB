from fastapi import APIRouter
from controllers import usersController

router = APIRouter(prefix = "/user", tags = ["users"])

@router.get("/")
async def get_users():
    return usersController.get_users()

