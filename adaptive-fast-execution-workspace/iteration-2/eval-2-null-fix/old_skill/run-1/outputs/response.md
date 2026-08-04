我已检查项目上下文：当前 `parse_user` 直接访问 `payload["name"]`，因此传入 `None` 时会崩溃；现有测试期望这种情况返回 `None`。

在进入方案设计前，我需要先确认一个问题：除了整个 `payload` 为 `None` 之外，这次修复是否也需要处理 `{"name": None}`？
