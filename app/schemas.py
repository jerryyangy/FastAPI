from pydantic import BaseModel, EmailStr
from datetime import datetime



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass 
    owner_id: int

# this is the user response model
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
       # orm_mode = True
        from_attribute = True

# Below is the schema for the response of the post
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    # owner: UserOut

    class Config:
       # orm_mode = True
        from_attribute = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str