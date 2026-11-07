# 修改已有技能

1. 从导出的副本或本仓库副本开始，保留原包。
2. 改正文、描述或 `references/`。
3. 自有包修改内容后提高 `metadata.version`。
4. 用 `python scripts/validate_skill.py <包目录> --profile author-current` 检查。
5. 在应用里预览并确认替换。用户导入的包是用户来源，不会伪装成随应用更新的官方包。

不要直接改应用安装目录里的文件。恢复时重新导入原来的版本即可。
