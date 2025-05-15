from repositories.user_repository import get_db_users
from sqlalchemy.orm import Session


def get_users(db : Session):
    return get_db_users(db)