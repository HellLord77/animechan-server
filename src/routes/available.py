from fastapi import APIRouter

from controller import get_all_anime_names
from controller import get_all_character_names

router = APIRouter()

router.get("/anime", response_model=list[str])(get_all_anime_names)
router.get("/character", response_model=list[str])(get_all_character_names)
