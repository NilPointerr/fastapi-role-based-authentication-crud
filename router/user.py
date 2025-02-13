from database import get_db
from models.user import User
from auth import get_password_hash
from sqlalchemy.orm import Session
from schemas.schemas import UserCreate, UserResponse
from fastapi import APIRouter, Depends, HTTPException



router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the cellnumber or email already exists
    db_user = db.query(User).filter(User.cellnumber == user.cellnumber).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Cell number already registered")
    db_user_email = db.query(User).filter(User.email == user.email).first()
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Create a new user
    db_user = User(**user.dict(exclude={"password"}), password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
