from pydantic import BaseModel


class Quote(BaseModel):
    anime: str
    character: str
    quote: str
