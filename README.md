<div align="center">

```
███╗   ███╗ ██████╗ ███████╗ █████╗ 
████╗ ████║██╔═══██╗██╔════╝██╔══██╗
██╔████╔██║██║   ██║███████╗███████║
██║╚██╔╝██║██║   ██║╚════██║██╔══██║
██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
```

**Music Open Source Application**

*Search, manage and download your music freely*

![License](https://img.shields.io/badge/license-GPL--3.0-green)
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Angular](https://img.shields.io/badge/Angular-21-red)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-teal)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)

</div>

## About this project

MOSA is an open source web application that lets you search music, build playlists, edit song metadata and download your music as high-quality MP3 files.

No email. No password. No data collection. Just music, privacy and freedom.

## Features

- **Anonymous accounts:** Sign up with a generated 16-digit code, no personal data required. Inspired by [Mullvad VPN](https://mullvad.net).
- **Music search:** Search songs directly from the UI.
- **Playlist management:** Create playlists, add songs, and reorder them with drag & drop.
- **Metadata editing:** Edit title, artist and album before downloading.
- **MP3 download:** Download single songs or full playlists as a `.zip`, with filenames exported in kebab-case.

## Technologies

| Name | Used in | Type | Version |
|------|---------|------|---------|
| Python | Backend | High-level programming language | 3.12+ |
| FastAPI | Backend | Python web framework | 0.111+ |
| yt-dlp | Backend | Python library for downloading audio | latest |
| PostgreSQL | Backend | Relational database | 16+ |
| Docker | Backend | Containerization platform | 24+ |
| Swagger UI | Backend | API documentation tool (integrated in FastAPI) | — |
| Angular | Frontend | TypeScript web framework | 21+ |
| TailwindCSS | Frontend | Utility-first CSS library | 3+ |
| Node.js | Frontend | JavaScript runtime environment | 22+ |

## Architecture

MOSA is based on a simple general architecture.

```
mosa-project/
└─ src/
   ├── backend/
   └── frontend/
```

Additionally, the frontend and backend architectures are tied to the functionality of the frameworks used for each one. For more information, please read the following files:

- Backend [architecture](./src/backend/docs/architecture.md) file.
- Frontend [architecture](./src/frontend/docs/architecture.md) file.

## Installation

MOSA is free to install on your own computer. See the [installation](./documents/installation.md) file for more details on how to install the repository and the technologies required to run it.

## Contributing

MOSA is open source and contributions are welcome. See the [contribution](./documents/contributions.md) file for more details on how to get involved in improving free and open source software.

> Make sure you're signed up on GitHub before contributing.

## License

MOSA is licensed under the GPL-3.0 License. See the [LICENSE](./documents/LICENSE) file for more details about how you can use this project.

## Sustainability

The MOSA project is a non-profit project. The founder and developer do not receive any return or profit from this project. Furthermore, the developer only uses openly available libraries, dependencies, and tools integrated into standard software development packages, and makes no warranty against claims of copyright infringement.

The MOSA project is currently active and is financially supported solely by the founder and developer. Donations, investments, and external funding are not accepted. The project also does not accept offers to display advertisements of any kind.

Finally, the MOSA project is committed to not collecting user data of any kind. This clarification is made to avoid false accusations of unauthorized tracking or improper commercialization of user data.

## Project philosophy

The MOSA project is based on the philosophy of free software, open-source software, and software as a solution to real-world problems. To better understand the philosophy behind this project, please review the [Philosophy and Motivation](./documents/philosophy.md) file.

By reading it, you will likely understand the significance this can have for people — and you will probably reflect on how you build software.

## Credits

This project is proudly designed and developed by **Badjavii**, junior developer.
