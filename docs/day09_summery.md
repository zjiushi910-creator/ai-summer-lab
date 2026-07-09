# Day9 Summary: Requests, Exception and Logging

## 1. 今日学习内容

今天学习了 Python 企业开发中常用的三个模块：

- requests
- exception
- logging

---

## 2. Requests

### 学到了什么

- `requests.get()`
- `response.status_code`
- `response.text`
- `response.json()`
- `timeout`

### 我的理解

`requests` 用来向服务器发送 HTTP 请求，并获取服务器返回的数据。

如果服务器返回的是 JSON 数据，可以使用：

```python
data = response.json()