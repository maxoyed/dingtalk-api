from dingtalk_api.core.session import ApiSession as ApiSession, OApiSession


API_SESSION = None
OAPI_SESSION = None
APP_KEY = None


class ApiClient:
    def __init__(self, appKey: str, appSecret: str):
        """API 客户端

        Args:
            appKey (str): 应用的唯一标识key
            appSecret (str): 应用的密钥。AppKey和AppSecret可在[钉钉开发者后台](https://open-dev.dingtalk.com/?spm=ding_open_doc.document.0.0.66d876e003FRRD)的应用详情页面获取
        """
        global API_SESSION
        global OAPI_SESSION
        global APP_KEY

        if not API_SESSION:
            API_SESSION = ApiSession(appKey, appSecret)
        if not OAPI_SESSION:
            OAPI_SESSION = OApiSession(appKey, appSecret)
        if not APP_KEY:
            APP_KEY = appKey

    @property
    def appKey(self):
        return APP_KEY

    @property
    def contact(self):
        "通讯录管理"
        from dingtalk_api.client.contact import Contact

        return Contact()

    @property
    def im(self):
        "即时通讯IM"
        from dingtalk_api.client.im import IM

        return IM()
