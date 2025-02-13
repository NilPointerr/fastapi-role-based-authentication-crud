#models/user.py
from sqlalchemy import Enum
from models.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime

class User(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True, index=True)
    profilepic = Column(String(255), nullable=True)
    name = Column(String(100), nullable=False)
    cellnumber = Column(String(15), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    deletedAt = Column(DateTime, nullable=True)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    roleId = Column(Enum("Admin", "Normal User"), nullable=False)

    tokens = relationship("AccessToken", back_populates="user", cascade="all, delete-orphan")
