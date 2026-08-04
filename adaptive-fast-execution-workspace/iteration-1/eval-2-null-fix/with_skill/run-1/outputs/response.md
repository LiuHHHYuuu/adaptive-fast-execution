已修复 `parse_user` 在输入为 `None` 时崩溃的问题：现在会直接返回 `None`，正常用户数据的原有解析行为保持不变。

验证通过：`python -m unittest -v` 共运行 2 个测试，全部通过。
