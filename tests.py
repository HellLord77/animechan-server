import sys

import anime_api.apis.animechan
import fastapi
from anime_api.apis.animechan import AnimechanAPI
from fastapi.testclient import TestClient

sys.path.append("src")
from src.main import app  # NOQA E402

client = TestClient(app)
api = AnimechanAPI()

anime_api.apis.animechan.requests.get = lambda url, *args, **kwargs: client.get(
    url.removeprefix(api.endpoint), *args, **kwargs
)


def test_status():
    assert fastapi.status.HTTP_200_OK == client.get("/status").json()["status"]


def test_random():
    assert api.get_random_quote()

    assert api.get_random_quote(anime_title="naruto")
    assert api.get_random_quote(character_name="saitama")


def test_quotes():
    assert api.get_many_random_quotes()

    assert api.search_by_anime_title("naruto")
    assert api.search_by_character_name("saitama")

    assert api.search_by_anime_title("naruto", page=2)


def test_available():
    assert client.get("/available/anime").json()
    assert client.get("/available/character").json()
