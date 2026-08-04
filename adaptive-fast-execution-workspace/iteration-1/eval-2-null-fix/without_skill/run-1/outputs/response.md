已修复 `parse_user` 在接收 `None` 时崩溃的问题：现在会直接返回 `None`，正常字典输入的解析行为保持不变。

验证已完成：`python -m unittest -v`，2 个测试全部通过。
