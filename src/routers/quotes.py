from fastapi import APIRouter

import description
import responses
from controller import get_quotes_by_anime
from controller import get_quotes_by_character
from controller import get_random_quotes
from schemas import Quote

router = APIRouter(tags=["quotes"])

router.get("", response_model=list[Quote], description=description.ROUTE_QUOTES)(
    get_random_quotes
)
router.get(
    "/anime",
    response_model=list[Quote],
    tags=["anime"],
    description=description.ROUTE_QUOTES_ANIME,
    responses=responses.QUERY,
)(get_quotes_by_anime)
router.get(
    "/character",
    tags=["character"],
    response_model=list[Quote],
    description=description.ROUTE_QUOTES_CHARACTER,
    responses=responses.QUERY,
)(get_quotes_by_character)
