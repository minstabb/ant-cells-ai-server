from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Post:
    title: str
    content: str
    id: int | None = field(default=None)
    created_at: datetime | None = field(default=None)