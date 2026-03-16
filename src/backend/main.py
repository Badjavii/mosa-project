# ./main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import auth, songs, playlists

app = FastAPI(
    title="Music Manager API",
    description="Download and manage your music from YouTube Music",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(songs.router)
app.include_router(playlists.router)


@app.get("/")
def root():
    return {"status": "Music Manager API is running"}
