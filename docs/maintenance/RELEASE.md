> **BAS-3 修订 / 用户 t372–t374 / 2026-11-23**：唯一交付根 `L:\00Dev\bgxiong-00-release` 下必须直接平级 `dev-项目名`、`release-项目名`、`cdn-项目名`、`deploy-项目名`，不再有编号分类/主机名/client/ai-story导航外壳。进入项目目录就选/拖成品；包内模块/平台结构照旧，CDN实际对象键不变。按本仓 RELEASE_OUTPUTS.md；同项目/用途/类型/平台/渠道只保留有版本/构建证据的最新完整成品，核验后删旧版，不按复制mtime判断；运行安装目录、源码、配置、缓存不迁移。

# 发布流程

1. 编辑技能副本并运行 `python scripts/validate_skill.py skills --all --profile author-current`。
2. 核对 `docs/maintenance/SOURCES-AND-RIGHTS.md`。被阻止的包不进入 `catalog/packages.json`。
3. 自有包有内容变化时提高版本号。
4. `python scripts/build_packages.py --check --output "L:/00Dev/bgxiong-00-release/release-bgxiong-content-skills/<batch>"` 生成 ZIP；`<batch>`替换为本批真实版本/构建身份，不是字面目录。原dist仅内部临时组装，不作为交付或源码提交。
5. 本地提交源码后，再用该提交构建最终 ZIP。不要把未提交的工作区说成已发布版本。
6. 公开推送和 Release 需要单独授权。认证或许可问题就停止。

本文件描述流程。它本身不是发布已经完成的记录。

## 唯一交付与CDN根（2026-11-23）

必读根`RELEASE_OUTPUTS.md`。Skills生产在线批次用`publish_online_index.py --output`指定`L:/00Dev/bgxiong-00-release/cdn-bgxiong-content-skills/`，整套ZIP、生产签名latest.json和既有公开验签材料保持同批；签名/资格前置不变。本轮不执行签名或发布，测试签名不可上传生产。远端打开相同前缀，拖本地该目录**内容**，不多套文件夹。只报旧dist路径不算交付。
