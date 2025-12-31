
from fastapi import FastAPI
from app.routers import api_router
from app.core.exceptions import CustomException, custom_exception_handler



def register_exceptions(app: FastAPI):
    """注册全局异常处理器
    
    参数:
        app (FastAPI): FastAPI应用实例
    """
    # 注册各种异常处理器
    app.add_exception_handler(CustomException, custom_exception_handler)    # 处理自定义异常


def register_routers(app: FastAPI, prefix: str = "/api"):
    """注册应用路由
    
    参数:
        app (FastAPI): FastAPI应用实例
        prefix (str): 路由前缀，默认为"/api"
    """
    # 包含API路由到应用中
    app.include_router(api_router, prefix=prefix)


