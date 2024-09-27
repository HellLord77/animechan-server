from typing import Optional
from typing import TypeVar

import fastapi
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import func

from models import Quote

T = TypeVar("T", bound=Quote | list[Quote])

RANDOM = func.random()


def check_empty_quote(
    quote: Optional[T],
) -> T:
    if not quote:
        raise HTTPException(fastapi.status.HTTP_404_NOT_FOUND)
    return quote
