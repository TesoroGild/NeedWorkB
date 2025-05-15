from sqlalchemy.orm import Session
from models.user_model import User
from schemas import user_schema

def get_db_users(db: Session):
    #return db.query(User).all()
    return usersTest

def get_db_user(user_credentials : user_schema.UserCredentials, db: Session):
    #
    return userResponseTest

#TEST
usersTest = [
    user_schema.User(
        username = "admin",
        first_name = "admin",
        last_name ="admin",
        email = "admin@admin.ca",
        password = "admin",
        role = "admin"
    ),
    user_schema.User(
        username = "The Godfather",
        first_name = "Vito",
        last_name ="Corleone",
        email = "corleone@vito.ca",
        password = "vito",
        role = "employer"
    ),
    user_schema.User(
        username = "Sanji",
        first_name = "Sanji",
        last_name ="Vinsmok",
        email = "vinsmok@sanji.ca",
        password = "sanji",
        role = "jobseeker"
    )
]

userResponseTest = user_schema.UserResponse(
    username = "admin",
    first_name = "admin",
    last_name ="admin",
    email = "admin@admin.ca",
    role = "admin"
)