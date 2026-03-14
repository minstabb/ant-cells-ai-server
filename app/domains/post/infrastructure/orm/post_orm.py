from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.infrastructure.database.session import Base


class PostORM(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)