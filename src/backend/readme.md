# Backend

The MOSA backend is the component responsible for managing all server-side logic. It acts as the bridge between the frontend and external services such as YouTube and the database. Without the backend, MOSA cannot search for music, manage playlists, or download files.

## Technologies

| Name | Type | Version |
|------|------|---------|
| Python | Programming language | 3.12+ |
| FastAPI | Web framework | 0.111+ |
| SQLAlchemy | PostgreSQL ORM | 2.0+ |
| Alembic | Database migrations | 1.13+ |
| PostgreSQL | Relational database | 16+ |
| yt-dlp | YouTube audio downloader | latest |
| mutagen | MP3 metadata writer | 1.47+ |
| bcrypt | Account code hashing | 4.1+ |
| python-jose | JWT generation and validation | 3.3+ |
| Uvicorn | ASGI server | 0.30+ |

## Endpoints

### Authentication — `/auth`

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/auth/sign_up` | Creates a new account and returns a 16-digit access code |
| `POST` | `/auth/sign_in` | Authenticates with the access code and returns a JWT |
| `DELETE` | `/auth/delete_account` | Permanently deletes the user account |

### Songs — `/songs`

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/songs/search?q=...` | Searches for songs on YouTube and returns the results |
| `POST` | `/songs/download` | Downloads a single song as an MP3 file |
| `PUT` | `/songs/{song_id}` | Updates the metadata of a song |

### Playlists — `/playlists`

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/playlists/` | Lists all playlists belonging to the authenticated user |
| `POST` | `/playlists/` | Creates a new playlist |
| `GET` | `/playlists/{id}` | Retrieves a playlist with all its songs |
| `DELETE` | `/playlists/{id}` | Deletes a playlist |
| `POST` | `/playlists/{id}/songs` | Adds a song to the playlist |
| `GET` | `/playlists/{id}/songs/{song_id}` | Retrieves a specific song from the playlist |
| `PUT` | `/playlists/{id}/songs/{song_id}` | Updates the metadata of a song within the playlist |
| `DELETE` | `/playlists/{id}/songs/{song_id}` | Removes a song from the playlist |
| `GET` | `/playlists/{id}/download` | Downloads the full playlist as a `.zip` file |

> Interactive documentation for all endpoints is available at `http://localhost:8000/docs` when the server is running.

## Running the Backend

```bash
# 1. Navigate to the directory
cd src/backend

# 2. Clean up any existing virtual environment.
rm -rf .venv

# 3. Create a new virtual environment\
python3 -m venv .venv

# 4. Activate the virtual environment
source .venv/bin/activate

# 5. Install the dependencies inside the venv
pip install -r requirements.txt

# 6. Run migrations (only the first time or after database changes)
alembic upgrade head

# 7. Start the server
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`.

## Technical Documentation

To understand how the backend is built in depth, refer to the following documents:

- [Architecture](./docs/architecture.md) — layered structure, design decisions and data flow.
- [Component diagram](./docs/component-diagram.png) — relationships between models, schemas, repositories and services.
- [Sequence diagrams](./docs/sequences/) — user stories illustrating the complete flow of each main operation.
