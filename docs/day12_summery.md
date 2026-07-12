# Day12 学习总结 —— dataclass 与数据模型

## 今日目标

学习 Python 的 dataclass，并将 GitHub API 返回的数据封装成自己的数据对象（Model）。

---

## 今日知识点

### 1. 什么是 dataclass

dataclass 是 Python 提供的一个用于定义数据对象的装饰器。

例如：

```python
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    color: str
```

相比传统写法，不需要自己编写：

- __init__()
- __repr__()
- __eq__()

Python 会自动生成。

---

### 2. dataclass 自动生成的方法

创建对象：

```python
dog = Dog("旺财", 1, "red")
```

打印对象：

```python
print(dog)
```

输出：

```text
Dog(name='旺财', age=1, color='red')
```

说明 dataclass 自动生成了：

```python
__repr__()
```

比较对象：

```python
dog1 == dog2
```

说明 dataclass 自动生成了：

```python
__eq__()
```

---

### 3. 为什么需要 Model

GitHub API 返回的是：

```python
dict
```

例如：

```python
{
    "login": "torvalds",
    "followers": 311000,
    "public_repos": 12,
    ...
}
```

但是整个 JSON 太大。

真正需要的只有几个字段。

于是创建：

```python
@dataclass
class GitHubUser:
    login: str
    followers: int
    public_repos: int
```

以后整个项目都使用：

```python
GitHubUser
```

而不是直接操作 dict。

---

### 4. JSON -> Model

学习了两种写法。

方法一：

```python
user = GitHubUser(
    login=data["login"],
    followers=data["followers"],
    public_repos=data["public_repos"]
)
```

优点：

- 简单
- 容易理解

---

方法二：

先清洗数据：

```python
clean_data = {
    "login": data["login"],
    "followers": data["followers"],
    "public_repos": data["public_repos"]
}
```

然后：

```python
user = GitHubUser(**clean_data)
```

这里：

```python
**
```

表示：

把字典展开成关键字参数。

等价于：

```python
GitHubUser(
    login=...,
    followers=...,
    public_repos=...
)
```

这种方式更适合大型项目，因为：

- 可以先统一处理数据
- 更容易扩展
- 更容易复用

---

### 5. build_user 思想

今天开始学习：

不要把所有逻辑写在 main()。

而是封装：

```python
build_user()
```

负责：

```
Response

↓

JSON

↓

清洗数据

↓

GitHubUser
```

这样：

main()

不需要知道 JSON 是怎么解析的。

---

### 6. run()

进一步封装流程：

```python
run()

↓

get_data()

↓

build_user()

↓

返回 GitHubUser
```

于是主程序变成：

```python
user = analyzer.run()
```

而不用：

```python
get_data()

↓

json()

↓

clean_data()

↓

GitHubUser(...)
```

所有细节全部隐藏。

---

## 今日收获

今天真正开始接触：

"数据模型（Model）"

以前：

```
Response

↓

dict

↓

自己取值
```

现在：

```
Response

↓

dict

↓

GitHubUser
```

以后整个项目都会围绕：

Model

进行开发。

---

## 今日关键词

- dataclass
- Model
- __init__
- __repr__
- __eq__
- JSON
- dict
- **
- build_user
- run
- 封装
- 数据模型

---

## 明日预告（Day13）

开始学习项目分层。

把项目拆分成：

- Client（负责请求）
- Service（负责业务）
- Model（负责数据）

真正开始搭建企业级 Python 项目结构。