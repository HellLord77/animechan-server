import os
from typing import Final

LOGGING_LEVEL: Final[str] = os.getenv("LOGGING_LEVEL", "INFO").upper()

DEBUG_FASTAPI: Final[bool] = os.getenv("DEBUG_FASTAPI", "false").lower() == "true"

DATA_PATH: Final[str] = os.getenv("DATA_PATH", "data.json")
DATABASE_URL: Final[str] = os.getenv("DATABASE_URL", "sqlite:///./database.db")

CORS_ALLOW_ORIGIN: Final[str] = os.getenv("CORS_ALLOW_ORIGIN", "*")
QUOTES_PER_PAGE: Final[int] = int(os.getenv("PAGE_SIZE", 10))
