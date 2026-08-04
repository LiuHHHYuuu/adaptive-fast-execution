# Transcript

1. 完整读取旧版 `mandatory-brainstorming` 基线。
2. 只读检查输入目录及全部项目文件。
3. 确认故障位置：`parse_user` 对 `None` 执行 `payload["name"]`。
4. 确认已有测试契约：`parse_user(None)` 应返回 `None`。
5. 根据强制门控，在第一个澄清问题处暂停；未提出方案、未编写设计、未修改输入、未运行实现后测试。

## Assistant response

我已检查项目上下文：当前 `parse_user` 直接访问 `payload["name"]`，因此传入 `None` 时会崩溃；现有测试期望这种情况返回 `None`。

在进入方案设计前，我需要先确认一个问题：除了整个 `payload` 为 `None` 之外，这次修复是否也需要处理 `{"name": None}`？
