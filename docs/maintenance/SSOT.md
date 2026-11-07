# 内容源边界

创作技能的可编辑正文以本仓库为准。开发技能在同级 `bgxiong-dev-skills`，不属于本仓库。第三方适配器仓库不存放这些技能。

主仓继续拥有安装、权限、用途闭集、执行 schema，以及 `video-prompt-packages.json` 这种运行时清单。本仓库的 `contracts/snapshots/` 是只读副本。内部提示词资源 `internal-prompt-skills` 不迁移到这里。

主仓通过固定提交和文件摘要消费本仓库，用户运行已安装的应用时不需要这台开发机上的目录。
