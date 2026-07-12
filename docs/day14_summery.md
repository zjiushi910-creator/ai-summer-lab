# Day14 学习总结 —— 处理列表数据（List[Model]）

## 今日目标

学习处理 GitHub Repository API 返回的列表数据，并将多个 dict 转换成 Python 对象列表。

---

## 今日知识点

### 1. 一个接口可以返回多个对象

昨天：

```
Response
    ↓
dict
    ↓
GitHubUser
```

今天：

```
Response
    ↓
list
    ↓
for
    ↓
dict
    ↓
GitHubRepository
```

最大的区别：

**今天返回的是 list，而不是 dict。**

---

### 2. list 与 dict 的区别

昨天：

```python
raw_data["login"]
```

今天：

```python
for repo in raw_data:
    print(repo["name"])
```

因为 list 中的每一个元素才是 dict。

---

### 3. dict 转 Model

遍历每个 Repository：

```
dict
    ↓
GitHubRepository
```

最终得到：

```
list[GitHubRepository]
```

以后可以直接：

```python
repo.name
repo.language
repo.stargazers_count
repo.forks_count
```

---

### 4. Service 的职责

```
Response
    ↓
json()
    ↓
list
    ↓
遍历
    ↓
GitHubRepository
    ↓
list[GitHubRepository]
```

所有数据转换都放在 Service 中完成。

---

## 今日总结

今天学会了处理**多个对象**。

```
Response
    ↓
list
    ↓
for
    ↓
dict
    ↓
Model
    ↓
list[Model]
```

进一步理解了项目分层：

```
Main
    ↓
Service
    ↓
Client
    ↓
GitHub API
```

各层职责清晰，代码更容易维护和扩展。

---

## Git Commit

```bash
git add .
git commit -m "Day14: support GitHub repository list and model conversion"
```