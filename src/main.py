from contextlib import asynccontextmanager

import fastapi
import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

import config
import description
from common import JSONResponse
from common import logger
from init import load_database
from routes import available
from routes import quotes
from routes import random


@asynccontextmanager
async def lifespan(_: FastAPI):
    load_database()
    yield


app = FastAPI(
    debug=config.DEBUG_FASTAPI,
    title="Animechan",
    description=description.APP,
    lifespan=lifespan,
)
# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=(config.CORS_ALLOW_ORIGIN,),
    allow_methods=("*",),
    allow_headers=("*",),
)
# noinspection PyTypeChecker
app.add_middleware(GZipMiddleware)


@app.get("/status")
async def get_status():
    return {"status": 200, "active": True}


app.include_router(random.router, prefix="/random")
app.include_router(quotes.router, prefix="/quotes")
app.include_router(available.router, prefix="/available")


@app.exception_handler(Exception)
async def exception_handler(_: Request, exc: Exception) -> JSONResponse:
    logger.error("Database Error: %s", exc, exc_info=exc)
    return JSONResponse(
        {"error": description.ERROR_500},
        fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(
    _: Request, __: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        {"error": description.ERROR_400},
        fastapi.status.HTTP_400_BAD_REQUEST,
    )


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()
