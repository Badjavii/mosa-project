# ./main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# == Users

@app.get("/users/sign_up")
def sign_up():
    code: int = user_sevice.sign_up()
    return {"account_code": code}

@app.get("/users/sign_in/{account_code}")
def sign_in(account_code: int):
    permission: bool = user_service.sign_in(account_code)
    return {"status": permission}

@app.get("/users/delete/{account_code}")
def delete_account(account_code: int):
    status_code: int = user_service.delete_account(account_code)
    return {"status": status_code}

# == Playlists

@app.get("/playlist/get_all/{account_code}")
def get_playlists(account_code: int):
    playlist_collection = playlist_service.get_all()
    return {"playlist_collection": playlist_collection}

@app.post("/playlist/create/{account_code}")
def create_playlist(account_code: int):
    status_code: int = playlist_service.create_playlist(account_code)
    return {"status": status_code}

@app.delete("/playlist/delete/{account_code}/{playlist_id}")
def delete_playlist(account_code: int, playlist_id: int):
    status_code: int = playlist_service.delete_playlist(account_code, playlist_id)
    return {"status": status_code}

@app.post("/playlist/add_song/{account_code}/{playlist_id}/{song_url}")
def add_song_to_playlist(account_code: int, playlist_id: int, song_url: str):
    status_code: int = playlist_service.add_song_to_playlist(account_code, playlist_id, song_url)
    return {"status": status_code}

@app.delete("/playlist/delete_song/{account_code}/{playlist_id}/{song_id}")
def delete_song_on_playlist(account_code: int, playlist_id: int, song_id: int):
    status_code: int = playlist_service.delete_song_on_playlist(account_code, playlist_id, song_id)
    return {"status": status_code}

# this will return the all playlist with all songs with all id of each song
# so frontend will storage the ids of the songs. this will complement the search_song_on_playlist
@app.get("/playlist/search/{playlist_id}")
def search_playlist(playlist_id: int):
    playlist = playlist_service.search(playlist_id)
    return {"playlist": playlist}

# This will let the user to get the song and the user will be able to change the metadata and the place in the song 
@app.get("/playlist/search_song/{account_code}/{playlist_id}/{song_id}")
def search_song_on_playlist(account_code: int, playlist_id: int, song_id: int):
    target_song: Song, status_code: int = playlist_service.search_song_on_playlist(account_code, playlist_id, song_id)
    return {"status": status_code, "song": target_song}
# Song is an object that will have data like name of song, artists, album name and file name (that will be the name of the song but in kebak-case) and the id of the song (this id will make the order of the playlist) and youtube url of song 

#This will update the song object properties. Will help us to modify the metadata
@app.put("/playlist/update_song/{account_code}/{playlist_id}/{song_id}")
def update_song_on_playlist(account_code: int, playlist_id: int, song_id: int, updated_song: Song):
    status_code: int = playlist_service.update_song_on_playlist(account_code, playlist_id, song_id, update_song)
    return {"status": status_code}

@app.get("/playlist/download/{playlist_id}")
def download_playlist(playlist_id: int):
    downloaded_playlist = playlist_service.download(playlist_id)
    return {"download_playlist": download_playlist}
