from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def get_superuser_token_headers(client: TestClient, user, password) -> Dict[str, str]:
    login_data = {
        "username": user.email,
        "password": password,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
