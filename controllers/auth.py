from repositories.user_repository import get_db_user
from schemas import user_schema
from sqlalchemy.orm import Session

def login(user_credentials : user_schema.UserCredentials, db : Session):
    return get_db_user(user_credentials, db)