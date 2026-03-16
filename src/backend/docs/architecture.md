# Backend Architecture

The MOSA backend follows a three-layer architecture that enforces a clear separation of concerns. Each layer has a single, well-defined responsibility, and communication between them flows in one direction only — from the outermost layer inward.

```
Router  →  Service  →  Repository  →  PostgreSQL
```

This structure makes the codebase easier to maintain, test, and extend over time. Adding a new feature means adding a router, a service, and a repository — each in its own place, without touching unrelated code.

## Directory Structure

### `main.py`

The entry point of the application. Its only responsibilities are to initialize the FastAPI instance, register the routers, and configure global middleware such as CORS. It contains no business logic.

### `src/core/`

Contains the foundational configuration that the rest of the application depends on.

`config.py` loads all environment variables from the `.env` file using `pydantic-settings`. Every configurable value in the application — the database URL, the JWT secret key, the downloads directory — is defined here as a typed setting. This means that if a required variable is missing at startup, the application fails immediately with a clear error instead of breaking later in an unexpected place.

`security.py` centralizes all authentication logic: generating the 16-digit account code, hashing it with bcrypt, verifying it on sign-in, and issuing and validating JWT tokens. Any part of the application that needs to deal with authentication imports from here.

### `src/db/`

Contains everything related to the database connection and table definitions.

`session.py` creates the SQLAlchemy engine, the session factory, and the `get_db` dependency that FastAPI injects into routers to provide a database session per request.

`tables.py` defines the three ORM table classes — `UserTable`, `PlaylistTable`, and `SongTable` — that map directly to the PostgreSQL tables. These are purely structural definitions with no logic attached to them.

### `src/models/`

Contains pure Python domain classes that represent the core concepts of the application: `User`, `Song`, and `Playlist`. These classes have no dependency on SQLAlchemy or any other library — they are plain Python dataclasses.

The models are where domain logic lives. For example, the `Song` model is responsible for generating the kebab-case filename from the artist and title. This keeps that logic in one place, independent of the database or the API layer.

### `src/schemas/`

Contains Pydantic models used exclusively for validating incoming requests and serializing outgoing responses. Schemas are the contract between the frontend and the API — they define exactly what data each endpoint accepts and what it returns.

Keeping schemas separate from models is intentional. A model represents a domain concept; a schema represents a data shape for the API. They often look similar but serve different purposes and evolve independently.

### `src/repositories/`

The only layer that communicates directly with the database. Each repository class corresponds to one domain entity — `UserRepository`, `SongRepository`, and `PlaylistRepository` — and contains only SQLAlchemy queries. No business logic lives here.

This separation means that if the database or the ORM were ever replaced, only the repositories would need to change. The rest of the application would remain untouched.

### `src/services/`

The layer where all business logic lives. Services orchestrate the work: they call repositories to read or write data, invoke external tools like yt-dlp to download audio or mutagen to write MP3 metadata, and return the result to the router.

Each service corresponds to a domain — `AuthService`, `SongService`, and `PlaylistService`. Routers never contain logic; they instantiate the appropriate service and delegate to it entirely.

### `src/routers/`

The outermost layer of the application. Routers define the HTTP endpoints — the method, the path, the expected input, and the expected output. Their only job is to receive a request, call the corresponding service method, and return the response. A well-written router function is typically three to five lines long.

### `alembic/`

Contains the database migration configuration and all migration scripts. Alembic tracks the history of changes made to the database schema, allowing the database to be upgraded or rolled back to any previous state. The `versions/` subdirectory holds one migration file per schema change, generated automatically from the table definitions in `src/db/tables.py`.

### `tests/`

Contains the test suite for the backend. Tests use SQLite in memory as a substitute for PostgreSQL, so they run without requiring a database connection. The `conftest.py` file sets up and tears down the test database automatically between each test function.

### `docs/`

Contains the technical documentation for the backend, including this file, the component diagram, and the sequence diagrams organized by user story.
