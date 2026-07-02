# Day 2 / 56 Summary
## Today I learned

- How to define Python functions
- How to use function parameters //如何使用函数参数
- How to return values
- How to use type hints
- How to read a text file with `Path.read_text()`
- How to split text into words with `split()`
- How to split text into lines with `splitlines()`\
- How to use a dictionary to store analysis results

## Important concepts

### 1. Function
A function is a reusable block of code.

Example:

```commandline
def count_words(text: str) -> int:
    words = text.split()
    return len(words)
```
```commandline
def load_text_file(file_path: Path) -> str:

输入一个路径返回文件中的字符串
```
```commandline
{
    "word_count": 16,
    "line_count": 3,
    "character_count": 89,
}
字典的形式
```
