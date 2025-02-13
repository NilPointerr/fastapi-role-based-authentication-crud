from sqlalchemy import Enum
from models.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, BIGINT
from models.user import User


class AccessToken(Base):
    __tablename__ = "accesstoken"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(255), nullable=False)
    ttl = Column(BIGINT, nullable=False)
    userId = Column(Integer, ForeignKey("user_profile.id"), nullable=False)  # Ensure the table name is correct
    created = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="tokens")
