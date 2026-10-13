from enum import Enum

class Users(Enum):
    Admin = "Admin"
    User = "User"

class NonAdminException(Exception):
    def __init__(self):
        super().__init__("Invalid : Only Admin Allowed")

def get_user():
    CURRENT_USER: Users = Users.User
    return CURRENT_USER

def admin(func):
    def wrapper(*args, **kwargs):
        current_user = get_user()
        if current_user != Users.Admin:
            raise NonAdminException
    return wrapper

@admin
def database_operation():
    print("DataBase Operation Done")

try:
    database_operation()
except NonAdminException as e:
    print(e)