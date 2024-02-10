from pydantic import BaseModel
from requests import get, post
from dingtalk_api.common.response import OApiRespBase
from dingtalk_api.core.constant import OAPI_GATEWAY, API_GATEWAY, API_VERSION


class ApiGetAccessTokenResp(BaseModel):
    accessToken: str
    "生成的accessToken"
    expireIn: int
    "过期时间/秒"


class OApiGetAccessTokenResp(OApiRespBase):
    access_token: str
    "生成的accessToken"
    expires_in: int
    "过期时间/秒"


def ApiGetAccessToken(appKey: str, appSecret: str) -> ApiGetAccessTokenResp:
    """[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app) 新版SDK

    Args:
        appKey (str): 已创建的企业内部应用的AppKey
        appSecret (str): 已创建的企业内部应用的AppSecret

    Returns:
        ApiGetAccessTokenResp: 返回参数
    """
    url = f"{API_GATEWAY}/{API_VERSION}/oauth2/accessToken"
    headers = {"Content-Type": "application/json"}
    response = post(
        url, headers=headers, json={"appKey": appKey, "appSecret": appSecret}
    )
    response.raise_for_status()
    return ApiGetAccessTokenResp(**response.json())


def OApiGetAccessToken(appKey: str, appSecret: str) -> OApiGetAccessTokenResp:
    """[获取企业内部应用的access_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token) 旧版SDK

    Args:
        appKey (str): 应用的唯一标识key
        appSecret (str): 应用的密钥。AppKey和AppSecret可在 [钉钉开发者后台](https://open-dev.dingtalk.com/?spm=ding_open_doc.document.0.0.66d876e003FRRD) 的应用详情页面获取。

    Returns:
        OApiGetAccessTokenResp: 返回参数
    """
    url = f"{OAPI_GATEWAY}/gettoken"
    response = get(url, params={"appkey": appKey, "appsecret": appSecret})
    response.raise_for_status()
    return OApiGetAccessTokenResp(**response.json())
