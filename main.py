import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.constants import VALIDATION_ERROR_CODE
from app.core.config import settings
from app.exceptions import BaseHttpException
from app.utils.format import format_validation_errors

if settings.ENVIRONMENT != "development":
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=0.6,
    )

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = format_validation_errors(errors=exc.errors())
    content = {"errors": errors, "error_code": VALIDATION_ERROR_CODE}
    return JSONResponse(
        status_code=400,
        content=content,
    )


@app.exception_handler(BaseHttpException)
async def http_exception_handler(request: Request, exc: BaseHttpException):
    content = {"errors": exc.detail, "error_code": exc.error_code}
    return JSONResponse(
        status_code=exc.status_code,
        content=content,
    )


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0  # noqa
