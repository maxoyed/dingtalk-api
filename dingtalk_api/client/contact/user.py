from typing import Literal, Optional

from pydantic import BaseModel
from dingtalk_api.common.exception import OApiError
from dingtalk_api.common.response import OApiRespBase
from dingtalk_api.client import OAPI_SESSION


class queryDetailsResult(BaseModel):
    userid: str
    "员工的userId"

    unionid: str
    "员工在当前开发者企业账号范围内的唯一标识"

    name: str
    "员工姓名"

    avatar: Optional[str] = None
    """头像
    
    员工使用默认头像，不返回该字段，手动设置头像会返回
    """

    state_code: Optional[str] = None
    """国际电话区号

    第三方企业应用不返回该字段；如需获取state_code，可以使用 [钉钉统一授权套件](https://open.dingtalk.com/document/orgapp/overview-2?spm=ding_open_doc.document.0.0.35c53ca7NMhyAA) 方式获取。
    """

    manager_userid: Optional[str] = None
    """员工的直属主管
    
    员工在企业管理后台个人信息面板中，直属主管内有值，才会返回该字段。
    """

    mobile: Optional[str] = None
    """手机号码

    - 企业内部应用，只有应用开通通讯录邮箱等个人信息权限，才会返回该字段。
    - 第三方企业应用不返回该字段，如需获取mobile，可以使用 [钉钉统一授权套件](https://open.dingtalk.com/document/orgapp/overview-2?spm=ding_open_doc.document.0.0.35c53ca7NMhyAA) 方式获取。
    """

    hide_mobile: bool
    """是否号码隐藏

    隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话
    """

    telephone: Optional[str] = None
    """分机号

    第三方企业应用不返回该参数
    """

    job_number: Optional[str] = None
    "员工工号"

    title: str
    "职位"

    email: Optional[str] = None
    """邮箱

    - 企业内部应用，只有应用开通通讯录邮箱等个人信息权限，才会返回该字段。
    - 第三方企业应用不返回该字段，如需获取email，可以使用 [钉钉统一授权套件](https://open.dingtalk.com/document/orgapp/overview-2?spm=ding_open_doc.document.0.0.35c53ca7NMhyAA) 方式获取。
    """


class queryDetailsResp(OApiRespBase):
    result: queryDetailsResult
    "返回结果"


class User:
    def queryDetails(
        self, userid: str, language: Literal["zh_CN", "en_US"] = "zh_CN"
    ) -> queryDetailsResult:
        """[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details) 旧版SDK

        Args:
            userid (str): 用户的userId
            language (Literal[&quot;zh_CN&quot;, &quot;en_US&quot;], optional): 通讯录语言. Defaults to "zh_CN".

        Returns:
            queryDetailsResp: 用户详情
        """
        endpoint = "/topapi/v2/user/get"
        data = {"userid": userid, "language": language}
        response = OAPI_SESSION.request("POST", endpoint, json=data)
        response = queryDetailsResp(**response.json())
        if response.errcode != 0:
            raise OApiError(response.errmsg)
        return response.result
