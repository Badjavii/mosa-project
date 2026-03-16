# ./src/models/song.py
import re
from dataclasses import dataclass, field


def to_kebab_case(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text


@dataclass
class Song:
    id: int
    title: str
    artist: str
    youtube_url: str
    file_name: str
    album: str | None = None
    playlist_id: int | None = None
    order: int | None = None

    @staticmethod
    def build_file_name(artist: str, title: str) -> str:
        return f"{to_kebab_case(artist)}-{to_kebab_case(title)}.mp3"
