from fastapi import APIRouter

import description
from controller import get_random_quote
from controller import get_random_quote_by_anime
from controller import get_random_quote_by_character
from schemas import Quote

router = APIRouter()

router.get("", response_model=Quote, description=description.ROUTE_RANDOM)(
    get_random_quote
)
router.get("/anime", response_model=Quote, description=description.ROUTE_RANDOM_ANIME)(
    get_random_quote_by_anime
)
router.get(
    "/character", response_model=Quote, description=description.ROUTE_RANDOM_CHARACTER
)(get_random_quote_by_character)
