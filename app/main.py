from fastapi import FastAPI
from app.routers import api_router
from app.core.init_app import register_exceptions

app = FastAPI()

# 注册异常处理器

register_exceptions(app)

app.include_router(api_router,prefix="/api" )