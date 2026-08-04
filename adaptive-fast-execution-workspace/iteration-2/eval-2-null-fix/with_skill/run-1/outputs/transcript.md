# Execution transcript

1. 完整读取 `adaptive-fast-execution/SKILL.md` 和 `brainstorming/SKILL.md`。
2. 路由判断：任务单一、局部、可逆、低风险且预计一小时内完成，符合 adaptive fast execution；未触发 brainstorming 设计门。
3. 将 fixture 内容复制到指定隔离输出目录，后续仅在该目录操作。
4. 检查文件清单以及 `parse_user` 和 `None` 相关位置；未发现 `AGENTS.md`。
5. 阅读 `user_parser.py` 与 `test_user_parser.py`，确认 `None` 输入因执行 `payload["name"]` 而崩溃，测试期望返回 `None`。
6. 在 `parse_user` 开头加入最小空值守卫：`payload is None` 时返回 `None`。
7. 执行 `python -m unittest -v`。

## Verification output

```text
test_normal_name (test_user_parser.ParseUserTests.test_normal_name) ... ok
test_null_payload_returns_none (test_user_parser.ParseUserTests.test_null_payload_returns_none) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
