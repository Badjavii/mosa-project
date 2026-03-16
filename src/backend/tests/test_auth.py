# ./tests/test_auth.py


def test_sign_up_returns_account_code(client):
    response = client.post("/auth/sign_up")
    assert response.status_code == 201
    data = response.json()
    assert "account_code" in data
    assert len(data["account_code"]) == 16
    assert data["account_code"].isdigit()


def test_sign_in_with_valid_code(client):
    # Create account
    sign_up = client.post("/auth/sign_up")
    account_code = sign_up.json()["account_code"]

    # Log in
    response = client.post("/auth/sign_in", json={"account_code": account_code})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_sign_in_with_invalid_code(client):
    response = client.post("/auth/sign_in", json={"account_code": "0000000000000000"})
    assert response.status_code == 401


def test_delete_account(client):
    sign_up = client.post("/auth/sign_up")
    account_code = sign_up.json()["account_code"]

    response = client.request(
        "DELETE",
        "/auth/delete_account",
        json={"account_code": account_code},
    )
    assert response.status_code == 204

    # You can no longer log in.
    sign_in = client.post("/auth/sign_in", json={"account_code": account_code})
    assert sign_in.status_code == 401
