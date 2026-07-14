# Day18 - GitHub Repository API & README Processing

## 今日目标

将 GitHub AI Reviewer 从“分析用户”升级为“分析仓库”。

学习 GitHub Repository API，并成功获取和解析 GitHub 项目的 README，为后续 AI 阅读项目打下基础。

---

# 今日知识

## 1. GitHub Repository API

学习了 GitHub Repository 相关接口：

获取仓库信息：

GET /repos/{owner}/{repo}

获取 README：

GET /repos/{owner}/{repo}/readme

获取目录：

GET /repos/{owner}/{repo}/contents/{path}

理解了：

GitHub User API

与

GitHub Repository API

属于不同的数据接口。

---

## 2. GitHubProject Model

新增：

GitHubProject

用于表示单个 GitHub Repository。

第一版包含：

- name
- full_name
- description
- language
- stargazers_count
- forks_count
- default_branch

理解：

Model 只保存当前项目真正需要的数据。

遵循：

YAGNI（You Aren't Gonna Need It）

避免一次加入过多字段。

---

## 3. RepositoryReadme Model

新增：

RepositoryReadme

用于保存 README API 返回的数据。

包含：

- name
- encoding
- content

其中：

content

仍然是：

Base64

编码。

---

## 4. Base64 解码

第一次真正处理：

Base64

↓

bytes

↓

UTF-8

↓

Markdown

学习：

base64.b64decode()

以及：

.decode("utf-8")

最终成功获取：

真正的 README.md 文本。

---

## 5. GitHubService 扩展

新增：

get_repository()

负责：

Response

↓

dict

↓

GitHubProject

新增：

build_readme()

负责：

Response

↓

dict

↓

RepositoryReadme

↓

Base64 Decode

↓

Markdown String

---

## 6. GitHubClient 扩展

新增：

- get_repository()
- get_readme()
- get_contents()

进一步完善 GitHub API Client。

Client 仍然保持：

只负责 HTTP 请求。

不负责：

- JSON 转换
- Base64 解码
- 业务逻辑

---

# 工程思维

再次强化：

Client

↓

Response

↓

Service

↓

Business Object

↓

Main

Client：

负责访问外部 API。

Service：

负责将外部数据转换为项目内部数据。

Main：

负责组织程序流程。

保持各层职责单一。

---

# 项目方向调整

项目重新定位为：

GitHub AI Repository Reviewer

目标：

输入一个 GitHub Repository。

自动：

- 获取 Repository 信息
- 获取 README
- 理解项目内容
- 使用 LLM 生成技术分析报告

而不是简单统计：

Star

Fork

Language

真正发挥 AI 的能力：

理解代码与文档。

---

# 今日项目进度

完成：

✓ GitHub Repository API

✓ GitHubProject Model

✓ RepositoryReadme Model

✓ GitHubService.get_repository()

✓ GitHubService.build_readme()

✓ README Base64 解码

✓ 成功读取 GitHub README.md

项目进入：

Repository Understanding

阶段。

---

# 今日收获

今天最大的收获不是新增 API。

而是成功让程序真正读取 GitHub 项目文档。

项目已经具备：

"AI 阅读 GitHub Repository"

所需的数据基础。

---

# 下一步

Day19

开始真正接入 AI：

README

↓

Clean Markdown

↓

Ollama

↓

Project Summary

实现第一版：

AI Repository Review。