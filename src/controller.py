import itertools
from typing import Iterator
from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Query
from sqlalchemy.sql.expression import func

import config
import description
from common import JSONResponse
from database import SessionLocal
from models import Anime
from models import Character
from models import Quote


def _get_db() -> Iterator[SessionLocal]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _get_quote_query() -> Iterator[Query]:
    yield (
        next(_get_db())
        .query(
            Quote.content.label("quote"),
            Anime.name.label("anime"),
            Character.name.label("character"),
        )
        .join(Anime, Quote.anime_id == Anime.id)
        .join(Character, Quote.character_id == Character.id)
    )


def _check_empty_quote(
    quote: Optional[dict[str, str] | list[dict[str, str]]], page: Optional[int] = None
):
    if quote is None or not quote:
        quote = JSONResponse(
            {"error": description.ERROR_404_PAGE if page else description.ERROR_404},
            404,
        )
    return quote


def get_random_quote(query: Query = Depends(_get_quote_query)):
    return _check_empty_quote(query.order_by(func.random()).limit(1).first())


def get_random_quotes(query: Query = Depends(_get_quote_query)):
    return _check_empty_quote(
        query.order_by(func.random()).limit(config.QUOTES_PER_PAGE).all()
    )


def get_random_quote_by_anime(title: str, query: Query = Depends(_get_quote_query)):
    return _check_empty_quote(
        query.filter(func.lower(Anime.name).like(func.lower(title)))
        .order_by(func.random())
        .limit(1)
        .first()
    )


def get_random_quote_by_character(name: str, query: Query = Depends(_get_quote_query)):
    return _check_empty_quote(
        query.filter(func.lower(Character.name).like(func.lower(name)))
        .order_by(func.random())
        .limit(1)
        .first()
    )


def get_quotes_by_anime(
    title: str, page: int = 0, query: Query = Depends(_get_quote_query)
):
    return _check_empty_quote(
        query.filter(func.lower(Anime.name).like(func.lower(title)))
        .offset(page * config.QUOTES_PER_PAGE)
        .limit(config.QUOTES_PER_PAGE)
        .all(),
        page,
    )


def get_quotes_by_character(
    name: str, page: int = 0, query: Query = Depends(_get_quote_query)
):
    return _check_empty_quote(
        query.filter(func.lower(Character.name).like(func.lower(name)))
        .offset(page * config.QUOTES_PER_PAGE)
        .limit(config.QUOTES_PER_PAGE)
        .all(),
        page,
    )


def get_all_anime_names(db: SessionLocal = Depends(_get_db)):
    # noinspection PyTypeChecker
    return itertools.chain.from_iterable(db.query(Anime.name).all())


def get_all_character_names(db: SessionLocal = Depends(_get_db)):
    # noinspection PyTypeChecker
    return itertools.chain.from_iterable(db.query(Character.name).all())
