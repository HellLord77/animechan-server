import itertools
from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm import Query
from sqlalchemy.sql.expression import func

import config
import controller.utils
from database import SessionLocal
from dependencies import get_db
from dependencies import get_quote_query
from models import Anime
from models import Character


def get_random_quote(query: Query = Depends(get_quote_query)) -> list[str]:
    return controller.utils.check_empty_quote(
        query.order_by(controller.utils.RANDOM).limit(1).first()
    )


def get_random_quotes(query: Query = Depends(get_quote_query)) -> list[list[str]]:
    return controller.utils.check_empty_quote(
        query.order_by(controller.utils.RANDOM).limit(config.QUOTES_PER_PAGE).all()
    )


def get_random_quote_by_anime(
    title: str, query: Query = Depends(get_quote_query)
) -> list[str]:
    return controller.utils.check_empty_quote(
        query.filter(func.lower(Anime.name).like(func.lower(title)))
        .order_by(controller.utils.RANDOM)
        .limit(1)
        .first()
    )


def get_random_quote_by_character(
    name: str, query: Query = Depends(get_quote_query)
) -> list[str]:
    return controller.utils.check_empty_quote(
        query.filter(func.lower(Character.name).like(func.lower(name)))
        .order_by(controller.utils.RANDOM)
        .limit(1)
        .first()
    )


def get_quotes_by_anime(
    title: str, page: int = 1, query: Query = Depends(get_quote_query)
) -> list[list[str]]:
    return controller.utils.check_empty_quote(
        query.filter(func.lower(Anime.name).like(func.lower(title)))
        .offset((page - 1) * config.QUOTES_PER_PAGE)
        .limit(config.QUOTES_PER_PAGE)
        .all(),
    )


def get_quotes_by_character(
    name: str, page: int = 1, query: Query = Depends(get_quote_query)
) -> list[list[str]]:
    return controller.utils.check_empty_quote(
        query.filter(func.lower(Character.name).like(func.lower(name)))
        .offset((page - 1) * config.QUOTES_PER_PAGE)
        .limit(config.QUOTES_PER_PAGE)
        .all(),
    )


def get_all_anime_names(
    db: SessionLocal = Depends(get_db),
) -> Iterator[str]:
    return itertools.chain.from_iterable(db.query(Anime.name).all())


def get_all_character_names(
    db: SessionLocal = Depends(get_db),
) -> Iterator[str]:
    return itertools.chain.from_iterable(db.query(Character.name).all())
