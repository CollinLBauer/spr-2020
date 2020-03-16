## 1. Broken code

The code has the following problems.
- some indexing through q in dequeue erroneously uses `_` instead of `->`
- enqueue uses `exit(1)` in an error handle statement, despite the function not having a return value.