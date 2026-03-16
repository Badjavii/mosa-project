# ./src/db/tables.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.session import Base


class UserTable(Base):
    __tablename__ = "users"

    id                = Column(Integer, primary_key=True, index=True)
    account_code_hash = Column(String, nullable=False, unique=True)

    playlists = relationship("PlaylistTable", back_populates="user", cascade="all, delete")


class PlaylistTable(Base):
    __tablename__ = "playlists"

    id      = Column(Integer, primary_key=True, index=True)
    name    = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user  = relationship("UserTable", back_populates="playlists")
    songs = relationship(
        "SongTable",
        back_populates="playlist",
        cascade="all, delete",
        order_by="SongTable.order",
    )


class SongTable(Base):
    __tablename__ = "songs"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    artist      = Column(String, nullable=False)
    album       = Column(String, nullable=True)
    youtube_url = Column(String, nullable=False)
    file_name   = Column(String, nullable=False)   # kebab-case, generado automáticamente
    playlist_id = Column(Integer, ForeignKey("playlists.id"), nullable=True)
    order       = Column(Integer, nullable=True)   # posición dentro de la playlist

    playlist = relationship("PlaylistTable", back_populates="songs")
