# Day 19 - Build GitHub AI Analyst Pipeline

## 今日目标

完成 GitHub AI Analyst 项目的核心分析流程：

GitHub Repository
        ↓
README 获取
        ↓
Markdown 清洗
        ↓
Prompt 构造
        ↓
Local LLM (Ollama + Qwen)
        ↓
项目分析结果输出


---

# 1. 今日学习内容

## 1.1 README 数据获取与处理

### GitHub API Response

GitHub README API 返回的是 JSON：

```json
{
    "name": "README.md",
    "encoding": "base64",
    "content": "xxxx"
}