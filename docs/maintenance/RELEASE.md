# 发布流程

1. 编辑技能副本并运行 `python scripts/validate_skill.py skills --all --profile author-current`。
2. 核对 `docs/maintenance/SOURCES-AND-RIGHTS.md`。被阻止的包不进入 `catalog/packages.json`。
3. 自有包有内容变化时提高版本号。
4. `python scripts/build_packages.py --check --output dist` 生成 ZIP。`dist/` 不作为源码提交。
5. 本地提交源码后，再用该提交构建最终 ZIP。不要把未提交的工作区说成已发布版本。
6. 公开推送和 Release 需要单独授权。认证或许可问题就停止。

本文件描述流程。它本身不是发布已经完成的记录。
