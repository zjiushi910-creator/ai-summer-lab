# Day15 - 企业级数据建模（Data Modeling）

## 今日知识

### 1. Type Hint 的真正作用
- Type Hint 主要服务于开发者、IDE 和静态检查工具。
- 默认不会影响 Python 运行。

---

### 2. 现代类型写法

学习了：

- str | None
- list[T]
- dict[K, V]

例如：

```python
company: str | None
repos: list[GitHubRepository]
```

---

### 3. Any

```python
dict[str, Any]
```

表示 value 可以是任意类型。

优点：

- 灵活。

缺点：

- IDE 无法推导具体类型。
- 类型检查基本失效。

---

### 4. TypedDict

作用：

给 dict 增加类型信息。

例如：

```python
class RepositoryResponse(TypedDict):
    name: str
    language: str | None
```

特点：

- 本质仍然是 dict。
- 使用 repo["name"] 访问。
- 不会运行时检查。

---

### 5. DTO 与 Domain Model

RepositoryResponse

↓

GitHubRepository

RepositoryResponse：

- 描述外部 API 返回的数据。

GitHubRepository：

- 描述程序内部的数据。

二者之间需要 Mapper 负责转换。

---

### 6. Mapper

build_repo()

负责：

list[dict]

↓

list[GitHubRepository]

Mapper 不关心数据来自：

- GitHub
- 数据库
- CSV
- AI 模型

只负责模型转换。

---

## 工程思维

今天最大的收获不是 Type Hint。

而是理解了：

"外部数据" 与 "内部数据" 应该解耦。

Service 的职责不是保存数据，而是完成模型转换。

---

## 企业设计原则

✓ SRP（单一职责）

✓ DTO（数据传输对象）

✓ Domain Model（领域模型）

✓ Mapper（模型转换）

---

## 为 Day16 做准备

今天发现：

- dict
- TypedDict
- dataclass

都不会做运行时数据校验。

因此需要学习：

Pydantic（BaseModel）

它将在运行时验证数据，并成为 FastAPI、OpenAI SDK、LangChain 等框架的重要基础。