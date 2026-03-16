# ./src/services/playlist_service.py
import os
import zipfile
from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from src.core.config import settings
from src.models.song import Song, to_kebab_case
from src.repositories.playlist_repository import PlaylistRepository
from src.repositories.song_repository import SongRepository
from src.schemas.song import SongCreate, SongUpdate, SongResponse
from src.schemas.playlist import PlaylistCreate, PlaylistResponse
from src.services.song_service import SongService

os.makedirs(settings.DOWNLOADS_DIR, exist_ok=True)


class PlaylistService:

    def __init__(self, db: Session):
        self.playlist_repo = PlaylistRepository(db)
        self.song_repo     = SongRepository(db)
        self.song_service  = SongService(db)

    # ── Playlist CRUD ─────────────────────────────────────────────────────────

    def get_all(self, user_id: int) -> list[PlaylistResponse]:
        playlists = self.playlist_repo.get_all_by_user(user_id)
        return [PlaylistResponse.model_validate(p) for p in playlists]

    def create(self, data: PlaylistCreate, user_id: int) -> PlaylistResponse:
        playlist = self.playlist_repo.create(name=data.name, user_id=user_id)
        return PlaylistResponse.model_validate(playlist)

    def get(self, playlist_id: int, user_id: int) -> PlaylistResponse:
        playlist = self._get_or_404(playlist_id, user_id)
        return PlaylistResponse.model_validate(playlist)

    def delete(self, playlist_id: int, user_id: int) -> None:
        playlist = self._get_or_404(playlist_id, user_id)
        self.playlist_repo.delete(playlist)

    # ── Songs dentro de Playlist ──────────────────────────────────────────────

    def add_song(self, playlist_id: int, user_id: int, data: SongCreate) -> SongResponse:
        self._get_or_404(playlist_id, user_id)
        order = self.song_repo.count_in_playlist(playlist_id) + 1
        file_name = Song.build_file_name(data.artist, data.title)
        song = self.song_repo.create(
            title=data.title,
            artist=data.artist,
            youtube_url=data.youtube_url,
            file_name=file_name,
            album=data.album,
            playlist_id=playlist_id,
            order=order,
        )
        return SongResponse.model_validate(song)

    def get_song(self, playlist_id: int, song_id: int, user_id: int) -> SongResponse:
        self._get_or_404(playlist_id, user_id)
        song = self.song_repo.get_by_id_and_playlist(song_id, playlist_id)
        if not song:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Canción no encontrada")
        return SongResponse.model_validate(song)

    def update_song(self, playlist_id: int, song_id: int, user_id: int, data: SongUpdate) -> SongResponse:
        self._get_or_404(playlist_id, user_id)
        song = self.song_repo.get_by_id_and_playlist(song_id, playlist_id)
        if not song:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Canción no encontrada")
        return self.song_service.update_metadata(song_id, data)

    def remove_song(self, playlist_id: int, song_id: int, user_id: int) -> None:
        self._get_or_404(playlist_id, user_id)
        song = self.song_repo.get_by_id_and_playlist(song_id, playlist_id)
        if not song:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Canción no encontrada")
        self.song_repo.delete(song)

    # ── Descarga completa ─────────────────────────────────────────────────────

    def download(self, playlist_id: int, user_id: int) -> FileResponse:
        playlist = self._get_or_404(playlist_id, user_id)
        songs = self.song_repo.get_by_playlist(playlist_id)
        if not songs:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La playlist está vacía")

        zip_name = f"{to_kebab_case(playlist.name)}.zip"
        zip_path = os.path.join(settings.DOWNLOADS_DIR, zip_name)

        with zipfile.ZipFile(zip_path, "w") as zf:
            for song in songs:
                file_path = self.song_service._download_audio(song.youtube_url, song.file_name)
                self.song_service._write_metadata(
                    file_path,
                    title=song.title,
                    artist=song.artist,
                    album=song.album,
                )
                archive_name = f"{str(song.order).zfill(2)}-{song.file_name}"
                zf.write(file_path, archive_name)

        return FileResponse(path=zip_path, filename=zip_name, media_type="application/zip")

    # ── Helper privado ────────────────────────────────────────────────────────

    def _get_or_404(self, playlist_id: int, user_id: int):
        playlist = self.playlist_repo.get_by_id_and_user(playlist_id, user_id)
        if not playlist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist no encontrada")
        return playlist
