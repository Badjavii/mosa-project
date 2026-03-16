# ./src/routers/songs.py
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.core.security import get_current_user_id
from src.schemas.song import SongCreate, SongUpdate, SongResponse, YouTubeSearchResult
from src.services.song_service import SongService

router = APIRouter(prefix="/songs", tags=["Songs"])


@router.get("/search", response_model=list[YouTubeSearchResult])
def search_songs(
    q: str = Query(..., description="Nombre de la canción a buscar"),
    limit: int = Query(10, ge=1, le=25),
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return SongService(db).search(q, limit)


@router.post("/download", status_code=status.HTTP_200_OK)
def download_single_song(
    body: SongCreate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return SongService(db).download_single(body)


@router.put("/{song_id}", response_model=SongResponse)
def update_song_metadata(
    song_id: int,
    body: SongUpdate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return SongService(db).update_metadata(song_id, body)
