# Day13 学习总结 —— 项目分层（Client / Service / Model）

## 今日目标

学习如何将一个功能完整但耦合较高的程序拆分为多个模块，让代码更符合真实项目开发方式。

---

## 今日知识点

### 1. 单一职责原则（Single Responsibility Principle）

一个类只负责一件事情。

例如：

GitHubClient

负责：

- 请求 GitHub API
- 返回 Response

不负责：

- 解析 JSON
- 创建 User
- 业务逻辑

---

GitHubService

负责：

- 调用 Client
- 解析 Response
- 提取需要的数据
- 构建 GitHubUser

不负责：

- 请求网络
- 读取配置

---

GitHubUser

负责：

- 保存 GitHub 用户信息

例如：

- login
- followers
- public_repos

它只是一个数据对象（Model）。

---

### 2. Client

作用：

与外部系统通信。

例如：

```python
client = GitHubClient(username, base_url)
response = client.get_user()
```