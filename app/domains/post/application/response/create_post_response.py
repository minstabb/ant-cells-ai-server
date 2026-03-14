from datetime import datetime

from pydantic import BaseModel


class CreatePostResponse(BaseModel):
    id: int
    created_at: datetime