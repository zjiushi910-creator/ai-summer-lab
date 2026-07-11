# Day11 Summary

## Today's Topic

Configuration Driven Development

把代码(Code)和配置(Configuration)分离。

---

## New Knowledge

### 1. config.json

项目参数不再写死在 Python 中。

例如：

- username
- base_url

都放到：

configs/github_config.json

修改配置即可切换分析对象。

---

### 2. OOP + Config

对象负责读取自己的配置。

例如：

GitHubDataAnalyzer

在 __init__() 中：

- load_config()
- 保存 self.config
- 初始化 self.username
- 初始化 self.base_url

对象负责管理自己的状态(State)。

---

### 3. Pathlib

继续使用：

Path(__file__).resolve().parents[1]

定位项目根目录。

不使用硬编码路径。

---

### 4. Configuration Driven

以前：

修改 Python 源码

↓

运行

现在：

修改 github_config.json

↓

运行

代码完全不用修改。

---

### 5. 企业为什么这样写？

实现：

Code 与 Configuration 分离。

优点：

- 易维护
- 易扩展
- 易部署
- 不同环境只修改配置即可

---

## Project

完成：

GitHubDataAnalyzer V2

新增：

- github_config.json
- load_config()
- 自动读取配置
- logging
- requests
- exception

项目已经不再写死 GitHub 用户。

---

## What I Learned

我理解了：

配置也是对象的一部分状态。

对象负责管理自己的配置，而不是依赖全局变量。

---

## Interview Notes

为什么使用配置文件？

答：

为了实现 Code 和 Configuration 分离，提高项目的可维护性和可扩展性。

以后修改：

- 用户名
- API
- 环境

都无需修改源码，只修改配置即可。

---

## Git Commit

feat: add configuration-driven GitHub analyzer