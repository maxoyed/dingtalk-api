import time
from requests import Session
from dingtalk_api.common.exception import AuthError
from dingtalk_api.core.auth import ApiGetAccessToken, OApiGetAccessToken
from dingtalk_api.core.constant import API_GATEWAY, API_VERSION, OAPI_GATEWAY


class ApiSession(Session):
    def __init__(self, appKey, appSecret):
        super(ApiSession, self).__init__()
        if not appKey or not appSecret:
            raise AuthError("appKey 或 appSecret 不能为空")
        self.appKey = appKey
        self.appSecret = appSecret
        self.__accessToken = None
        self.__expireIn = 0
        self.__base_url = f"{API_GATEWAY}/{API_VERSION}"
        self.__updateAccessToken()

    def __updateAccessToken(self):
        if time.time() > self.__expireIn or not self.__accessToken:
            getAccessTokenResp = ApiGetAccessToken(self.appKey, self.appSecret)
            self.__accessToken = getAccessTokenResp.accessToken
            self.__expireIn = time.time() + getAccessTokenResp.expireIn - 60
            self.headers.update(
                {
                    "Content-Type": "application/json",
                    "x-acs-dingtalk-access-token": self.__accessToken,
                }
            )

    @property
    def base_url(self):
        return self.__base_url

    @property
    def accessToken(self):
        self.__updateAccessToken()
        return self.__accessToken

    def request(self, method: str, endpoint: str, **kwargs):
        self.__updateAccessToken()
        if not endpoint.startswith("http"):
            endpoint = self.__base_url + endpoint
        return super(ApiSession, self).request(method, endpoint, **kwargs)


class OApiSession(Session):
    def __init__(self, appKey, appSecret):
        super(OApiSession, self).__init__()
        if not appKey or not appSecret:
            raise AuthError("appKey 或 appSecret 不能为空")
        self.appKey = appKey
        self.appSecret = appSecret
        self.__accessToken = None
        self.__expireIn = 0
        self.__base_url = f"{OAPI_GATEWAY}"
        self.headers.update(
            {
                "Content-Type": "application/json",
            }
        )
        self.__updateAccessToken()

    def __updateAccessToken(self):
        if time.time() > self.__expireIn or not self.__accessToken:
            getAccessTokenResp = OApiGetAccessToken(self.appKey, self.appSecret)
            if getAccessTokenResp.errcode != 0:
                raise AuthError(getAccessTokenResp.errmsg)
            self.__accessToken = getAccessTokenResp.access_token
            self.__expireIn = time.time() + getAccessTokenResp.expires_in - 60

    @property
    def base_url(self):
        return self.__base_url

    @property
    def accessToken(self):
        self.__updateAccessToken()
        return self.__accessToken

    def request(self, method: str, endpoint: str, **kwargs):
        self.__updateAccessToken()
        if not endpoint.startswith("http"):
            endpoint = self.__base_url + endpoint
        if "params" in kwargs:
            kwargs["params"].update({"access_token": self.__accessToken})
        else:
            kwargs["params"] = {"access_token": self.__accessToken}
        return super(OApiSession, self).request(method, endpoint, **kwargs)
