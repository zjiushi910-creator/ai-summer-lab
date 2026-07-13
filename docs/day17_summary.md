# Day17 - AI Project Kickoff & GitHub Client Design

## 今日目标

开始真正的 AI 工程项目，不再编写独立 Demo。

建立 GitHub AI Analyst 项目的整体架构，并完成第一层（Client Layer）的设计。

---

# 今日知识

## 1. AI Project 启动

新建独立项目：

GitHub AI Analyst

与 AI Summer Lab 分离。

Summer Lab：

负责学习知识与实验。

GitHub AI Analyst：

负责企业级 AI 项目开发。

---

## 2. 项目架构

继续采用三层架构：

Main

↓

Service

↓

Client

↓

GitHub API

职责：

Main：

程序入口。

负责获取用户输入并组织程序流程。

Service：

负责业务逻辑。

负责：

Response

↓

dict

↓

Pydantic Model

Client：

负责 HTTP 请求。

返回 Response。

Model：

负责数据结构。

使用 Pydantic BaseModel。

---

## 3. Client 的职责

GitHubClient 只负责：

发送 HTTP 请求。

返回：

Response

不负责：

- json()
- model_validate()
- 业务逻辑

保持单一职责（SRP）。

---

## 4. Main 的职责

Main 是程序入口。

负责：

- 获取 GitHub 用户名
- 创建 Service
- 调用 Service
- 输出结果

用户输入应放在：

main.py

而不是：

Client

或：

Service

这样以后切换为 FastAPI 或 MCP 时，只需要替换入口。

---

## 5. GitHubClient 设计

第一版设计：

GitHubClient

↓

get_user(username)

↓

get_repositories(username)

Client 内部负责：

拼接 URL

↓

requests.get()

↓

Response

---

## 6. base_url

将：

path

升级为：

base_url

例如：

https://api.github.com

固定部分放入 Client。

变化部分由各个方法负责拼接。

提高代码可扩展性。

---

## 7. _request()

了解了为什么企业会抽取：

_request()

统一处理：

requests.get()

不过遵循：

Don't Abstract Too Early

当前项目暂不实现复杂抽象。

保持代码简单。

---

## 8. Service 返回什么？

再次明确：

Client：

返回 Response。

Service：

返回 Model。

例如：

GitHubUser

而不是：

dict

这样 Main 不需要关心：

- JSON
- dict
- model_validate()

只负责使用业务对象。

---

# 工程思维

今天开始真正进入企业开发模式。

项目开发遵循：

需求

↓

架构

↓

编码

↓

Code Review

↓

Refactor

而不是：

直接开始写代码。

---

Client 越简单越好。

Service 负责业务。

Main 负责组织流程。

每一层只负责自己的职责。

---

# 今日项目进度

GitHub AI Analyst：

完成：

✓ 项目初始化

✓ 企业目录结构

✓ main.py

✓ settings.py

✓ GitHubClient 初版设计

开始设计：

GitHubService

项目进入：

Sprint 2 - GitHub Data Layer

---

# 今日收获

今天最大的收获不是 GitHub API。

而是理解：

如何按照企业方式设计 AI 项目。

开始从：

"会写 Python"

逐步转变为：

"会设计软件架构。"

---

# 下一步

Sprint 2 - Part 2

完成：

Main

↓

GitHubService

↓

GitHubClient

↓

GitHub API

↓

Response

↓

Pydantic Model

↓

Main 输出

正式打通 GitHub AI Analyst 的第一条完整数据流。