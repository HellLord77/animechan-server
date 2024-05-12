from typing import Optional

import fastapi
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import func

RANDOM = func.random()


def check_empty_quote(
    quote: Optional[list[str] | list[list[str]]],
) -> list[str] | list[list[str]]:
    if not quote:
        raise HTTPException(fastapi.status.HTTP_404_NOT_FOUND)
    return quote
