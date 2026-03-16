# ./src/repositories/playlist_repository.py
from sqlalchemy.orm import Session
from src.db.tables import PlaylistTable


class PlaylistRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, user_id: int) -> PlaylistTable:
        playlist = PlaylistTable(name=name, user_id=user_id)
        self.db.add(playlist)
        self.db.commit()
        self.db.refresh(playlist)
        return playlist

    def get_all_by_user(self, user_id: int) -> list[PlaylistTable]:
        return self.db.query(PlaylistTable).filter(PlaylistTable.user_id == user_id).all()

    def get_by_id_and_user(self, playlist_id: int, user_id: int) -> PlaylistTable | None:
        return self.db.query(PlaylistTable).filter(
            PlaylistTable.id == playlist_id,
            PlaylistTable.user_id == user_id,
        ).first()

    def delete(self, playlist: PlaylistTable) -> None:
        self.db.delete(playlist)
        self.db.commit()
