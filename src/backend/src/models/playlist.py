# ./src/schemas/playlist.py
from pydantic import BaseModel
from src.schemas.song import SongResponse


class PlaylistCreate(BaseModel):
    name: str


class PlaylistResponse(BaseModel):
    id: int
    name: str
    user_id: int
    songs: list[SongResponse] = []

    model_config = {"from_attributes": True}
