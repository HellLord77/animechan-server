import config

TITLE = "Animechan"
APP = "A free restful API serving quality anime quotes"

ROUTE_RANDOM = "Get a random quote"
ROUTE_RANDOM_ANIME = "Get a random quote by anime title"
ROUTE_RANDOM_CHARACTER = "Get a random quote by anime character"

ROUTE_QUOTES = f"Get {config.QUOTES_PER_PAGE} random quotes"
ROUTE_QUOTES_ANIME = f"Get {config.QUOTES_PER_PAGE} quotes by anime title"
ROUTE_QUOTES_CHARACTER = f"Get {config.QUOTES_PER_PAGE} quotes by anime character"

ERROR_400 = "Bad Request"
ERROR_404 = "No related quotes found!"
ERROR_500 = "Internal Server Error"
