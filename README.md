# 钉钉服务端 API

## 特点

- 兼容新旧 SDK
- 采用与官方文档相同的组织结构
- 丰富的注释和类型标注
- Pydantic 集成

## 安装

```shell
pip install dingtalk-api
```

## 使用

```python
from dingtalk_api import ApiClient

client = ApiClient(
    CLIENT_ID,
    CLIENT_SECRET,
)

# 查询用户详情 旧版SDK
resp = client.contact.user.queryDetails(userid)
print(resp.model_dump())

# 下载机器人接收消息的文件内容 新版SDK
resp = client.im.robot.downloadMessageFiles(downloadCode, ROBOT_CODE)
print(resp.model_dump())
```
