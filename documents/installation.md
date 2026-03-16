# Installation

The MOSA frontend and backend can both be installed on your own computer or server. MOSA has the advantage of being self-hosted. The following steps outline how to install and run the project locally.

## Requirements

Make sure you have the following tools installed on your system before proceeding.

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12+ | Backend runtime |
| pip | latest | Python package manager |
| PostgreSQL | 16+ | Database |
| ffmpeg | any recent | Audio conversion (required by yt-dlp) |
| Node.js | 22+ | Frontend runtime |
| npm | 10+ | Node package manager |
| Angular CLI | 21+ | Frontend tooling |
| Git | any | Version control |

### Installing requirements on Fedora
```bash
sudo dnf install python3 python3-pip postgresql postgresql-server ffmpeg nodejs git
npm install -g @angular/cli
```

### Installing requirements on Ubuntu/Debian
```bash
sudo apt install python3 python3-pip postgresql ffmpeg nodejs git
npm install -g @angular/cli
```

### Installing requirements on macOS
```bash
brew install python postgresql ffmpeg node git
npm install -g @angular/cli
```

## Clone repository on your machine
```bash
git clone https://github.com/Badjavii/mosa-project.git
cd mosa-project
```

## Backend

### Installation

**1. Navigate to the backend directory:**
```bash
cd mosa/src/backend
```

**2. Create and activate a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate
```
> On Windows use: `.venv\Scripts\activate`

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set up PostgreSQL:**

Start the PostgreSQL service:
```bash
# Fedora
sudo systemctl enable --now postgresql

# Ubuntu
sudo systemctl start postgresql
```

Create the database and user:
```bash
sudo -u postgres psql
```
```sql
CREATE USER music_user WITH PASSWORD 'music_pass';
CREATE DATABASE music_manager OWNER music_user;
\q
```

**5. Configure environment variables:**
```bash
cp .env.example .env
```

Edit `.env` with your values:
```
DATABASE_URL=postgresql://music_user:music_pass@localhost:5432/music_manager
SECRET_KEY=your-random-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
DOWNLOADS_DIR=/tmp/music_manager/downloads
```

**6. Run database migrations:**
```bash
alembic upgrade head
```

### Testing

Make sure the virtual environment is active, then run:
```bash
pytest tests/ -v
```

### Running the Backend

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.  
The interactive API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

## Frontend

### Installation

**1. Navigate to the frontend directory:**
```bash
cd mosa/src/frontend
```

**2. Install dependencies:**
```bash
npm install
```

**3. Configure the environment:**

Open `src/environments/environment.ts` and make sure the API URL points to your running backend:
```ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000',
};
```

### Testing

```bash
ng build
```

If the build completes without errors, the project is correctly set up.

### Running the Frontend

```bash
ng serve
```

The application will be available at `http://localhost:4200`.

> Make sure the backend is running before using the frontend, as all features depend on the API.
