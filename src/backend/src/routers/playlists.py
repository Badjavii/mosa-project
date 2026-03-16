# ./src/routers/playlists.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.core.security import get_current_user_id
from src.schemas.song import SongCreate, SongUpdate, SongResponse
from src.schemas.playlist import PlaylistCreate, PlaylistResponse
from src.services.playlist_service import PlaylistService

router = APIRouter(prefix="/playlists", tags=["Playlists"])


# ── Playlist CRUD ─────────────────────────────────────────────────────────────

@router.get("/", response_model=list[PlaylistResponse])
def get_all_playlists(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).get_all(user_id)


@router.post("/", response_model=PlaylistResponse, status_code=status.HTTP_201_CREATED)
def create_playlist(
    body: PlaylistCreate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).create(body, user_id)


@router.get("/{playlist_id}", response_model=PlaylistResponse)
def get_playlist(
    playlist_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).get(playlist_id, user_id)


@router.delete("/{playlist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_playlist(
    playlist_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    PlaylistService(db).delete(playlist_id, user_id)


# ── Songs dentro de Playlist ──────────────────────────────────────────────────

@router.post("/{playlist_id}/songs", response_model=SongResponse, status_code=status.HTTP_201_CREATED)
def add_song(
    playlist_id: int,
    body: SongCreate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).add_song(playlist_id, user_id, body)


@router.get("/{playlist_id}/songs/{song_id}", response_model=SongResponse)
def get_song(
    playlist_id: int,
    song_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).get_song(playlist_id, song_id, user_id)


@router.put("/{playlist_id}/songs/{song_id}", response_model=SongResponse)
def update_song(
    playlist_id: int,
    song_id: int,
    body: SongUpdate,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).update_song(playlist_id, song_id, user_id, body)


@router.delete("/{playlist_id}/songs/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_song(
    playlist_id: int,
    song_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    PlaylistService(db).remove_song(playlist_id, song_id, user_id)


# ── Descarga completa ─────────────────────────────────────────────────────────

@router.get("/{playlist_id}/download")
def download_playlist(
    playlist_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return PlaylistService(db).download(playlist_id, user_id)
