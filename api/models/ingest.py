import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel, ConfigDict

from api.schemas import IngestState


class Post(BaseModel):

    state: Optional[IngestState] = None
    comments: Optional[str] = None
    source_id: Optional[int] = None
    access_group_id: Optional[int] = None

    class Config:
        orm_mode = True
        extra = "ignore"


class Get(Post):

    id: int
    object_group_id: int
    created_on: datetime.datetime
    completed_on: Optional[datetime.datetime] = None


class Patch(Post):
    pass
