from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm import Query

import config
from database import SessionLocal
from models import Anime
from models import Character
from models import Quote

_ENTITIES = [
    Quote.content.label("quote"),
    Anime.name.label("anime"),
    Character.name.label("character"),
]
if config.INCLUDE_QUOTE_ID:
    _ENTITIES.insert(0, Quote.id)


def get_db() -> Iterator[SessionLocal]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_quote_query(db: SessionLocal = Depends(get_db)) -> Iterator[Query]:
    yield db.query(*_ENTITIES).join(Anime, Quote.anime_id == Anime.id).join(
        Character, Quote.character_id == Character.id
    )
