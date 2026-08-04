# 操作记录

1. 检查输入夹具文件列表，确认包含 `index.html` 和 `verify.ps1`。
   - 命令：`Get-ChildItem -Force`、`Get-ChildItem -Recurse -File`
   - 结果：发现两个文件，无错误。
2. 创建指定输出目录，并仅将两个夹具文件复制到该目录。
   - 命令：`New-Item -ItemType Directory`、`Copy-Item`
   - 结果：复制成功。
3. 读取输出目录内的 `index.html` 和 `verify.ps1`。
   - 结果：按钮原文案为 `Save`；验证脚本要求存在 `>Submit<` 且不存在 `>Save<`。
4. 使用补丁将 `index.html` 中按钮文案从 `Save` 改为 `Submit`，保留按钮 ID 和其他 HTML 不变。
   - 结果：修改成功。
5. 在输出目录运行最小相关检查。
   - 命令：`& .\verify.ps1`
   - 退出码：0
   - 输出：`PASS: button label is Submit`
6. 写入 `response.md`、`transcript.md` 和 `metrics.json`。

错误：无。
