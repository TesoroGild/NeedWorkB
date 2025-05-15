from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    admin = 'admin'
    employer = 'employer'
    job_seeker = 'jobseeker'

class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    role: Role
    
    class Config:
        orm_mode = True

class UserCredentials(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    role: Role
    
    class Config:
        orm_mode = True