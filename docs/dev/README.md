# 开发者文档

在课程平台、项目管理平台、文档平台等项目可能需要。

在课程平台服务端需要：
- 接收Service Hook推送的事件。可能需要结合框架才可以封装，最多可以封装WSGI协议的实现。
- 获取项目信息、代码仓库信息的API。可以直接封装，在框架SDK中二次封装即可。