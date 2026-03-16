# ./src/services/song_service.py
import os
from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import yt_dlp
from mutagen.id3 import ID3, TIT2, TPE1, TALB, ID3NoHeaderError
from mutagen.mp3 import MP3

from src.core.config import settings
from src.models.song import Song, to_kebab_case
from src.repositories.song_repository import SongRepository
from src.schemas.song import SongCreate, SongUpdate, SongResponse, YouTubeSearchResult

os.makedirs(settings.DOWNLOADS_DIR, exist_ok=True)


class SongService:

    def __init__(self, db: Session):
        self.repo = SongRepository(db)

    # ── YouTube Search ────────────────────────────────────────────────────────

    def search(self, query: str, limit: int = 10) -> list[YouTubeSearchResult]:
        ydl_opts = {
            "quiet": True,
            "extract_flat": True,   # no descarga, solo metadata
            "skip_download": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            raw = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)

        entries = raw.get("entries", [])
        if not entries:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sin resultados")

        results = []
        for item in entries:
            duration_secs = item.get("duration") or 0
            minutes, seconds = divmod(int(duration_secs), 60)
            results.append(YouTubeSearchResult(
                title=item.get("title", ""),
                channel=item.get("channel") or item.get("uploader", ""),
                duration=f"{minutes}:{seconds:02d}",
                youtube_url=f"https://www.youtube.com/watch?v={item['id']}",
                thumbnail=item.get("thumbnail") or "",
            ))
        return results

    # ── Download ──────────────────────────────────────────────────────────────

    def download_single(self, data: SongCreate) -> FileResponse:
        file_name = Song.build_file_name(data.artist, data.title)
        file_path = self._download_audio(data.youtube_url, file_name)
        self._write_metadata(file_path, title=data.title, artist=data.artist, album=data.album)

        self.repo.create(
            title=data.title,
            artist=data.artist,
            youtube_url=data.youtube_url,
            file_name=file_name,
            album=data.album,
        )
        return FileResponse(path=file_path, filename=file_name, media_type="audio/mpeg")

    # ── Metadata update ───────────────────────────────────────────────────────

    def update_metadata(self, song_id: int, data: SongUpdate) -> SongResponse:
        song = self.repo.get_by_id(song_id)
        if not song:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Canción no encontrada")

        updated_title  = data.title  or song.title
        updated_artist = data.artist or song.artist
        new_file_name  = Song.build_file_name(updated_artist, updated_title)

        updated = self.repo.update(
            song,
            title=data.title,
            artist=data.artist,
            album=data.album,
            order=data.order,
            file_name=new_file_name,
        )

        # Actualiza metadatos en el archivo si existe
        file_path = os.path.join(settings.DOWNLOADS_DIR, new_file_name)
        if os.path.exists(file_path):
            self._write_metadata(file_path, title=updated.title, artist=updated.artist, album=updated.album)

        return SongResponse.model_validate(updated)

    # ── Helpers privados ──────────────────────────────────────────────────────

    def _download_audio(self, youtube_url: str, file_name: str) -> str:
        output_path = os.path.join(settings.DOWNLOADS_DIR, file_name.replace(".mp3", ""))
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_path,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }],
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        return f"{output_path}.mp3"

    def _write_metadata(
        self,
        file_path: str,
        title: str,
        artist: str,
        album: str | None = None,
    ) -> None:
        try:
            tags = ID3(file_path)
        except ID3NoHeaderError:
            tags = ID3()

        tags[" TIT2"] = TIT2(encoding=3, text=title)
        tags["TPE1"] = TPE1(encoding=3, text=artist)
        if album:
            tags["TALB"] = TALB(encoding=3, text=album)

        tags.save(file_path)
