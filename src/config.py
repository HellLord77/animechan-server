import os
from typing import Final

LOGGING_LEVEL: Final[str] = os.getenv("LOGGING_LEVEL", "INFO").upper()

DEBUG_SQLALCHEMY: Final[bool] = os.getenv("DEBUG_SQLALCHEMY", "false").lower() == "true"
DEBUG_FASTAPI: Final[bool] = os.getenv("DEBUG_FASTAPI", "false").lower() == "true"

DATA_PATH: Final[str] = os.getenv("DATA_PATH", "data.json")
DATABASE_URL: Final[str] = os.getenv("DATABASE_URL", "sqlite:///./database.sqlite")

INCLUDE_QUOTE_ID: Final[bool] = os.getenv("INCLUDE_QUOTE_ID", "false").lower() == "true"
QUOTES_PER_PAGE: Final[int] = int(os.getenv("PAGE_SIZE", 10))
