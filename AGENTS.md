# 仓库协作约定

## MCP 使用

- 分析、定位或修改代码前，先使用 Codegraph MCP 获取相关符号、调用关系和影响范围；只有索引未覆盖所需内容时，才使用 `rg` 或直接读取文件补充确认。
- 查询 GitHub 远端仓库、分支、提交、议题或拉取请求时，优先使用已授权的 GitHub MCP；本地工作区状态、提交和推送仍使用 `git`。
- 本仓库的 GitHub 远端为 `jhonatancitogaru789-art/-`，默认分支为 `main`。
- GitHub MCP 的授权属于用户账户配置。不得把访问令牌、密钥或其他凭据写入仓库。

## Codegraph 索引

- `Py_Code` 下的中文文件名必须被完整索引；索引完成后应能识别全部 8 个 Python 文件。
- 合并、重命名或批量修改 Python 文件后，运行 `codegraph index --force`，再用 `codegraph status` 和 `codegraph files` 检查覆盖范围。
- `.codegraph/` 仅保存本机索引缓存，不应提交到 Git。
