已修复 `parse_user(None)` 崩溃：当输入为 `None` 时现在直接返回 `None`，正常字典输入的名字去空格行为保持不变。

验证：`python -m unittest -v` 通过，2/2 测试成功。
