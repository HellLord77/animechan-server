from contextlib import asynccontextmanager

import fastapi
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.gzip import GZipMiddleware

import config
import description
import exceptions
import init
import responses
from routers import available
from routers import quotes
from routers import random


@asynccontextmanager
async def lifespan(_: FastAPI):
    init.load_database()
    yield
    init.close_database()


app = FastAPI(
    debug=config.DEBUG_FASTAPI,
    title=description.TITLE,
    description=description.APP,
    exception_handlers={
        RequestValidationError: exceptions.validation_error_handler,
        fastapi.status.HTTP_404_NOT_FOUND: exceptions.not_found_error_handler,
        Exception: exceptions.exception_handler,
    },
    lifespan=lifespan,
    responses=responses.BASE,
)
# noinspection PyTypeChecker
app.add_middleware(GZipMiddleware)


@app.get("/status")
async def get_status():
    return {"status": 200, "active": True}


app.include_router(random.router, prefix="/random")
app.include_router(quotes.router, prefix="/quotes")
app.include_router(available.router, prefix="/available")


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()
