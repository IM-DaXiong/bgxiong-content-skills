# 修改已有技能

1. 项目维护者和开发智能体先在本仓库定位包的唯一源码（skills/ 或 examples/teaching/），保留有效修改；不直接改主仓随包副本。用户个人可从导出副本开始修改自己的包。
2. 改正文、描述或 `references/`。
3. 自有包修改内容后提高 `metadata.version`。
4. 用 `python scripts/validate_skill.py <包目录> --profile author-current` 检查。
5. 在应用里预览并确认替换。用户导入的包是用户来源，不会伪装成随应用更新的官方包。

不要直接改应用安装目录里的文件。恢复时重新导入原来的版本即可。

项目开发目录与主仓同步按[三仓唯一治理规范](../../bgxiong-ai-story/docs/dev/guides/20261107-GUIDE-三仓平级与创作Skill唯一治理目录.md)执行。
