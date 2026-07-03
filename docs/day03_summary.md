# Day 3/56 Summary

## Today I learned 

- How to create a JSON config file 
- How to read a JSON file with python
- How to use `json.loads()`
- How to convert a dictionary into a dataclass object
- How to access config values with dot syntax

## Important concepts

### 1. Config file 

A config file stores project parameters outside the Python code.

Example:
```json
{
  "project_name": "AI summer Lab",
  "chunk_size": 500,
  "top_k": 3
}
```

### 2. dataclass

A dataclass is useful for storing structured data.

```python
@dataclass
class AppConfig:
    project_name: str
    data_dir: str
    log_level: str
    chunk_size: int
    top_k: int
```

### 3. JSON to Python object

The process is:

```text
JSON file -> text -> dict -> AppConfig object
```

## Code completed

- `configs/app_config.json`
- `src/day03_config.py`
- `docs/day03_summary.md`

## Run result

```text
Project name: AI Summer Lab
Data directory: data
Log level: INFO
Chunk size: 500
Top K: 3
```