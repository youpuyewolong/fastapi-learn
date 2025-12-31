from fastapi import APIRouter
from .default import router as default_router
from .sql import router as sql_router
from app.core.dependency import DependAuth
api_router = APIRouter()
# api_router.include_router(default_router, tags=["default"],prefix="/default",dependencies=[DependAuth])
api_router.include_router(default_router, tags=["default"],prefix="/default")
api_router.include_router(sql_router, tags=["sql"],prefix="/sql")


# __all__ 定义了当使用 "from module import *" 时，哪些符号应该被导入
# 这行代码的作用是限制外部模块只能导入 api_router，而不会导入其他内部变量
# 这是一种良好的编程实践，用于控制模块的公共接口
__all__ = ["api_router"]