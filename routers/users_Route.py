from typing import List
from fastapi import APIRouter, Depends
from controllers import users_Controller
from schemas.user_schema import User
from repositories.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix = "/users", tags = ["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model = List[User])
async def get_users(db: Session = Depends(get_db)):
    return users_Controller.get_users(db)

