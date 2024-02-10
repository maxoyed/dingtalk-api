from typing import Optional
from pydantic import BaseModel


class OApiRespBase(BaseModel):
    request_id: Optional[str] = None
    "请求ID"
    errcode: int
    "返回码"
    errmsg: str
    "返回码描述"
