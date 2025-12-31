from typing import Optional

from fastapi import Depends, Header, HTTPException
from app.core.exceptions import CustomException

class AuthControl:
    @classmethod
    async def is_authed(cls, token: str = Header(..., description="token验证")) -> dict:
        print("进入依赖注入")
        try:
            if token == "dev":
                return {"user_id": 1, "token": token}  # 认证成功时返回用户信息
            else:
                # token 错误时抛出认证异常
                raise CustomException(status_code=401, detail={"code": 1, "msg": "token错误"})
        except CustomException:
            # 如果是自定义异常，直接重新抛出
            raise
        except Exception as e:
            # 只有在发生其他意外异常时才执行这里
            raise HTTPException(status_code=500, detail=str(e))


DependAuth = Depends(AuthControl.is_authed)