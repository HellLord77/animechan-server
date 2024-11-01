from fastapi import APIRouter

from crud import get_all_anime_names
from crud import get_all_character_names

router = APIRouter(tags=["available"])

router.get("/anime", response_model=list[str], tags=["anime"])(get_all_anime_names)
router.get("/character", response_model=list[str], tags=["character"])(
    get_all_character_names
)
