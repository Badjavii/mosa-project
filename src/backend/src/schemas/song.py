from pydantic import BaseModel

class YouTubeSearchResult(BaseModel):
    title: str
    channel: str
    duration: str
    youtube_url: str
    thumbnail: str

class SongCreate(BaseModel):
    title: str
    artist: str
    youtube_url: str
    album: str | None = None

class SongUpdate(BaseModel):
    title: str | None = None
    artist: str | None = None
    album: str | None = None
    order: int | None = None

class SongResponse(BaseModel):
    id: int
    title: str
    artist: str
    album: str | None
    youtube_url: str
    file_name: str
    playlist_id: int | None
    order: int | None
    model_config = {"from_attributes": True}
