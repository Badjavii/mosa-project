# ./tests/test_playlists.py


def _auth_header(client) -> dict:
    """Helper: crea una cuenta y retorna el header Authorization."""
    sign_up = client.post("/auth/sign_up")
    code = sign_up.json()["account_code"]
    sign_in = client.post("/auth/sign_in", json={"account_code": code})
    token = sign_in.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_playlist(client):
    headers = _auth_header(client)
    response = client.post("/playlists/", json={"name": "Mi Playlist"}, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Mi Playlist"
    assert "id" in data


def test_get_all_playlists(client):
    headers = _auth_header(client)
    client.post("/playlists/", json={"name": "Playlist 1"}, headers=headers)
    client.post("/playlists/", json={"name": "Playlist 2"}, headers=headers)

    response = client.get("/playlists/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_delete_playlist(client):
    headers = _auth_header(client)
    created = client.post("/playlists/", json={"name": "Borrar"}, headers=headers)
    playlist_id = created.json()["id"]

    response = client.delete(f"/playlists/{playlist_id}", headers=headers)
    assert response.status_code == 204

    # Ya no debe existir
    get = client.get(f"/playlists/{playlist_id}", headers=headers)
    assert get.status_code == 404


def test_add_song_to_playlist(client):
    headers = _auth_header(client)
    playlist = client.post("/playlists/", json={"name": "Rock"}, headers=headers).json()

    song_data = {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "youtube_url": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
    }
    response = client.post(f"/playlists/{playlist['id']}/songs", json=song_data, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["file_name"] == "queen-bohemian-rhapsody.mp3"
    assert data["order"] == 1


def test_song_order_increments(client):
    headers = _auth_header(client)
    playlist = client.post("/playlists/", json={"name": "Pop"}, headers=headers).json()

    for i, title in enumerate(["Song A", "Song B", "Song C"], start=1):
        res = client.post(
            f"/playlists/{playlist['id']}/songs",
            json={"title": title, "artist": "Artist", "youtube_url": "https://youtube.com/watch?v=test"},
            headers=headers,
        )
        assert res.json()["order"] == i
