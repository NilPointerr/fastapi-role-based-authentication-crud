# routers/auth_routes.py
import datetime
from database import get_db
from datetime import timedelta
from models.user import User
from schemas.schemas import Token,UserResponse  
from sqlalchemy.orm import Session
from models.access_token import AccessToken
from schemas.schemas import EmailPasswordForm
from fastapi import  Depends, HTTPException, status, APIRouter
from auth import (authenticate_user, create_access_token, create_refresh_token,ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user)

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: EmailPasswordForm = Depends(EmailPasswordForm.as_form),
    db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.cellnumber, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect cell number or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.cellnumber,"roleId": user.roleId}, expires_delta=access_token_expires
    )

    refresh_token_expires = timedelta(days=7)
    refresh_token = create_refresh_token(
        data={"sub": user.cellnumber}, expires_delta=refresh_token_expires
    )

    db_token = AccessToken(
        token=access_token,
        ttl=ACCESS_TOKEN_EXPIRE_MINUTES * 60 * 1000,
        userId=user.id,
        created=datetime.datetime.now(),
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)

    return Token(access_token=access_token, token_type="bearer", refresh_token=refresh_token)



@router.get("/users/{id}", response_model=UserResponse)
async def get_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    if current_user.roleId == "Admin":
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    # Normal users can only access their own data
    if current_user.roleId == "Normal User" and current_user.id != id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: You can only view your own data"
        )

    # Fetch the user for normal users viewing their own data
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.patch("/users/{id}")
async def update_user(id: int, name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.roleId != "Admin":
        raise HTTPException(status_code=403, detail="Access denied")
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = name
    db.commit()
    return {"message": "User updated successfully"}

@router.delete("/users/{id}")
async def delete_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.roleId != "Admin":
        raise HTTPException(status_code=403, detail="Access denied")
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@router.get("/users")
async def list_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.roleId != "Admin":
        raise HTTPException(status_code=403, detail="Access denied")
    users = db.query(User).all()
    return users