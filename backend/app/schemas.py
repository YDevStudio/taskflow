from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timedelta

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str  # ← EXPECTS username, but you're sending email
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# Auth Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    username: str

class TokenData(BaseModel):
    id: Optional[str] = None

# Task Schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None  # 🔴 Ensure this is Optional

    class Config:
        orm_mode = True

class TaskOut(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True