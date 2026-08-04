1. 完整读取 `adaptive-fast-execution/SKILL.md` 与 `brainstorming/SKILL.md`。
2. 判定任务符合快速执行条件，不进入设计流程。
3. 首次复制命令因 `-LiteralPath` 不展开通配符而失败；确认输出目录为空后，改用枚举源目录并成功复制夹具。
4. 检查输出中的 `index.html` 和 `verify.ps1`，定位唯一目标文案及直接验证脚本。
5. 将 `<button id="save-button">Save</button>` 改为 `<button id="save-button">Submit</button>`。
6. 在输出目录运行 `verify.ps1`，结果为 `PASS: button label is Submit`。
7. 首次写评测产物的补丁格式无效，未创建文件；修正补丁格式后写入三个要求的产物。
