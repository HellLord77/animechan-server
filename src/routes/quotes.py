from fastapi import APIRouter

import description
from controller import get_quotes_by_anime
from controller import get_quotes_by_character
from controller import get_random_quotes
from schemas import Quote

router = APIRouter()

router.get("", response_model=list[Quote], description=description.ROUTE_QUOTES)(
    get_random_quotes
)
router.get(
    "/anime", response_model=list[Quote], description=description.ROUTE_QUOTES_ANIME
)(get_quotes_by_anime)
router.get(
    "/character",
    response_model=list[Quote],
    description=description.ROUTE_QUOTES_CHARACTER,
)(get_quotes_by_character)
