from models.user import Role, User


def get_users():
    return usersTest

#TEST
usersTest = {
    0: User(
        username = "admin",
        first_name = "admin",
        last_name ="admin",
        email = "admin@admin.ca",
        password = "admin",
        role = Role.admin
    ),
    1: User(
        username = "The Godfather",
        first_name = "Vito",
        last_name ="Corleone",
        email = "corleone@vito.ca",
        password = "vito",
        role = Role.employer
    ),
    2: User(
        username = "Sanji",
        first_name = "Sanji",
        last_name ="Vinsmok",
        email = "vinsmok@sanji.ca",
        password = "sanji",
        role = Role.job_seeker
    )
}