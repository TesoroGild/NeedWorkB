from typing import List
from fastapi import APIRouter, Depends
from controllers import auth, users_Controller
from repositories.database import SessionLocal
from sqlalchemy.orm import Session

import schemas.user_schema as user_schema

router = APIRouter(prefix = "/users", tags = ["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model = List[user_schema.User])
async def get_users(db: Session = Depends(get_db)):
    return users_Controller.get_users(db)

@router.post("/login", response_model = user_schema.UserResponse)
async def login(user_credentials: user_schema.UserCredentials, db: Session = Depends(get_db)):
    return auth.login(user_credentials, db)