import fastapi
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

import description
from common import JSONResponse
from common import logger
from schemas import Error

_ERROR_400 = Error(error=description.ERROR_400).dict()
_ERROR_404 = Error(error=description.ERROR_404).dict()
_ERROR_500 = Error(error=description.ERROR_500).dict()


async def validation_error_handler(
    _: Request, __: RequestValidationError
) -> JSONResponse:
    return JSONResponse(_ERROR_400, fastapi.status.HTTP_400_BAD_REQUEST)


async def not_found_error_handler(_: Request, __: HTTPException) -> JSONResponse:
    return JSONResponse(_ERROR_404, fastapi.status.HTTP_404_NOT_FOUND)


async def exception_handler(_: Request, exc: Exception) -> JSONResponse:
    logger.error("Database Error: %s", exc, exc_info=exc)
    return JSONResponse(_ERROR_500, fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR)
