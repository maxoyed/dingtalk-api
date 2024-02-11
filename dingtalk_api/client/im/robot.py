from pydantic import BaseModel

from dingtalk_api.client import API_SESSION


class downloadMessageFilesResp(BaseModel):
    downloadUrl: str
    """文件的临时下载链接

    访问临时下载链接，获取下载文件，在文件被下载到本地后，需开发者替换本地下载的文件扩展名。

    例如替换视频文件：
    - 替换前：iAEI******IVAiYgXNCKMGzSsRB85j_Z7zCM0CYA.file
    - 替换后：iAEI******IVAiYgXNCKMGzSsRB85j_Z7zCM0CYA.mp4
    """


class Robot:
    def downloadMessageFiles(
        self, downloadCode: str, robotCode: str
    ) -> downloadMessageFilesResp:
        """[下载机器人接收消息的文件内容](https://open.dingtalk.com/document/orgapp/download-the-file-content-of-the-robot-receiving-message) 新版SDK

        Args:
            downloadCode (str): 用户向机器人发送文件消息后，机器人回调给开发者消息中的下载码
            robotCode (str): 机器人的编码

        Returns:
            downloadMessageFilesResp: 返回参数
        """
        endpoint = "/v1.0/robot/messageFiles/download"
        data = {
            "downloadCode": downloadCode,
            "robotCode": robotCode,
        }
        resp = API_SESSION.request("POST", endpoint, json=data)
        return downloadMessageFilesResp(**resp.json())
