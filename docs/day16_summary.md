# Day16 - Pydantic 入门与企业级数据验证

## 今日目标

理解为什么现代 Python AI 工程几乎都会使用 Pydantic，而不是仅使用 dataclass。

将 Pydantic 第一次应用到 GitHub 项目中。

---

# 今日知识

## 1. BaseModel

学习：

```python
from pydantic import BaseModel
```

定义：

```python
class User(BaseModel):
    name: str
    age: int
```

BaseModel 可以看作：

> dataclass + Validation + Serialization

---

## 2. model_validate()

学习：

```python
repo = GitHubRepository.model_validate(data)
```

作用：

dict

↓

验证（Validation）

↓

类型转换（Type Coercion）

↓

创建 BaseModel 对象

返回：

GitHubRepository

---

## 3. Type Coercion

例如：

```python
age="18"
```

自动转换：

```python
18
```

而：

```python
name=123
```

默认会触发 ValidationError。

Pydantic 不仅验证，还会进行安全的类型转换。

---

## 4. Validation

Pydantic 在对象创建时会：

- 检查字段是否存在
- 检查字段类型
- 自动转换可以转换的数据
- 无法转换时抛出 ValidationError

相比 dataclass：

错误会更早暴露。

---

## 5. Mapper 与 Pydantic

今天最大的收获：

Mapper：

负责：

外部数据

↓

内部数据

例如：

GitHub

↓

GitHubRepository

Pydantic：

负责：

验证

↓

创建对象

两者职责不同。

---

## 6. model_validate() 在项目中的应用

将：

```python
GitHubRepository(**clean_repo)
```

升级为：

```python
GitHubRepository.model_validate(clean_repo)
```

项目仍然保持：

list[GitHubRepository]

不影响上层代码。

---

# 工程思维

今天真正理解了：

Pydantic 并不是为了少写代码。

而是：

让数据在进入系统时就完成：

✓ 验证

✓ 转换

✓ 创建对象

---

Mapper 不应该消失。

Mapper 与 Pydantic 的职责分别是：

Mapper：

负责字段转换。

Pydantic：

负责数据验证。

---

不要让外部 API 决定内部 Model。

外部协议发生变化：

↓

修改 Mapper。

业务代码保持稳定。

---

# 今日项目演进

GitHub 项目第一次引入 Pydantic。

完成：

✓ BaseModel

✓ model_validate()

✓ GitHubRepository Pydantic Demo

✓ Service 使用 model_validate()

保持原有项目可以继续运行。

---

# 今日收获

今天开始理解：

Pydantic 不只是一个库。

它代表的是：

"企业级数据入口"

所有进入系统的数据：

↓

Validation

↓

Business Model

这是 FastAPI、OpenAI SDK、LangChain 等框架共同采用的设计思想。

---

# 下一步（Day17）

学习：

- Field()
- model_dump()
- 将 GitHubRepository 完整升级为 BaseModel
- GitHubUser 升级为 BaseModel
- 开始真正重构 GitHub 项目

目标：

让项目继续演进，而不是重新写 Demo。