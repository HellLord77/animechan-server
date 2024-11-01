from fastapi import APIRouter

import description
import responses
from crud import get_random_quote
from crud import get_random_quote_by_anime
from crud import get_random_quote_by_character
from schemas import Quote

router = APIRouter(tags=["random"])

router.get("", response_model=Quote, description=description.ROUTE_RANDOM)(
    get_random_quote
)
router.get(
    "/anime",
    response_model=Quote,
    tags=["anime"],
    description=description.ROUTE_RANDOM_ANIME,
    responses=responses.QUERY,
)(get_random_quote_by_anime)
router.get(
    "/character",
    tags=["character"],
    response_model=Quote,
    description=description.ROUTE_RANDOM_CHARACTER,
    responses=responses.QUERY,
)(get_random_quote_by_character)
