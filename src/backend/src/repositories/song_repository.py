# ./src/repositories/song_repository.py
from sqlalchemy.orm import Session
from src.db.tables import SongTable


class SongRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        title: str,
        artist: str,
        youtube_url: str,
        file_name: str,
        album: str | None = None,
        playlist_id: int | None = None,
        order: int | None = None,
    ) -> SongTable:
        song = SongTable(
            title=title,
            artist=artist,
            youtube_url=youtube_url,
            file_name=file_name,
            album=album,
            playlist_id=playlist_id,
            order=order,
        )
        self.db.add(song)
        self.db.commit()
        self.db.refresh(song)
        return song

    def get_by_id(self, song_id: int) -> SongTable | None:
        return self.db.query(SongTable).filter(SongTable.id == song_id).first()

    def get_by_id_and_playlist(self, song_id: int, playlist_id: int) -> SongTable | None:
        return self.db.query(SongTable).filter(
            SongTable.id == song_id,
            SongTable.playlist_id == playlist_id,
        ).first()

    def get_by_playlist(self, playlist_id: int) -> list[SongTable]:
        return (
            self.db.query(SongTable)
            .filter(SongTable.playlist_id == playlist_id)
            .order_by(SongTable.order)
            .all()
        )

    def count_in_playlist(self, playlist_id: int) -> int:
        return self.db.query(SongTable).filter(SongTable.playlist_id == playlist_id).count()

    def update(self, song: SongTable, **fields) -> SongTable:
        for key, value in fields.items():
            if value is not None:
                setattr(song, key, value)
        self.db.commit()
        self.db.refresh(song)
        return song

    def delete(self, song: SongTable) -> None:
        self.db.delete(song)
        self.db.commit()
