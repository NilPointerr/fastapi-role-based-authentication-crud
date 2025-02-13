from fastapi import Form 
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    profilepic: str = None
    cellnumber: str
    email: str
    password: str
    roleId: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    cellnumber: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    roleId: str

    class Config:
        orm_mode = True


# class Scopes:
#     read_data = "read_data"
#     write_data = "write_data"

# You can define the Token response model to include scope information
class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    # scopes: list[str]  # List of granted scopes#


class TokenData(BaseModel):
    role_id: str 
    cellnumber: str | None = None



class EmailPasswordForm(BaseModel):
    cellnumber: str
    password: str

    @classmethod
    async def as_form(
        cls,
        cellnumber: str = Form(...),
        password: str = Form(...),
    ) -> "EmailPasswordForm":
        return cls(cellnumber=cellnumber, password=password)