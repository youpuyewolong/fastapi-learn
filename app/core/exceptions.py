from fastapi.exceptions import (
    HTTPException,
    RequestValidationError,
    ResponseValidationError,
)
from fastapi.requests import Request
from fastapi.responses import JSONResponse




class CustomException(Exception):
    def __init__(self, status_code: int = 401, detail: dict = None):
        self.status_code = status_code
        self.detail = detail or {"code": 1, "msg": "未知错误"}


async def custom_exception_handler(_: Request, exc: CustomException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

