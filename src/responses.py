import fastapi

import description
from schemas import Error

BASE = {
    fastapi.status.HTTP_404_NOT_FOUND: {
        "model": Error,
        "description": description.ERROR_404,
    },
    fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "model": Error,
        "description": description.ERROR_500,
    },
}

QUERY = {
    fastapi.status.HTTP_400_BAD_REQUEST: {
        "model": Error,
        "description": description.ERROR_400,
    }
}
