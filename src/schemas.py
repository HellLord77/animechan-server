from pydantic import BaseModel

import config


class Quote(BaseModel):
    if config.INCLUDE_QUOTE_ID:
        id: int
    anime: str
    character: str
    quote: str
