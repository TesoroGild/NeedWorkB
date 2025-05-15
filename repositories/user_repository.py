from sqlalchemy.orm import Session
from models.user_model import User

def get_db_users(db: Session):
    #return db.query(User).all()
    return usersTest

#TEST
usersTest = [
    User(
        username = "admin",
        first_name = "admin",
        last_name ="admin",
        email = "admin@admin.ca",
        password = "admin",
        role = "admin"
    ),
    User(
        username = "The Godfather",
        first_name = "Vito",
        last_name ="Corleone",
        email = "corleone@vito.ca",
        password = "vito",
        role = "employer"
    ),
    User(
        username = "Sanji",
        first_name = "Sanji",
        last_name ="Vinsmok",
        email = "vinsmok@sanji.ca",
        password = "sanji",
        role = "jobseeker"
    )
]