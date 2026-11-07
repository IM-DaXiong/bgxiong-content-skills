# 旧文件处置

`packs/` 下的 CONTENT_SKILL 与 AUTHORING 文档、`examples/content-plan/`、`examples/generation-policy/`、`examples/optimize/`、`contracts/v1/` 里的旧能力与 pipeline 合同，以及 `scripts/validate-example.py`，保留在原地作为历史。

它们要求 `skill.manifest.json` 和 `local.*`。当前作者入口改为 `SKILL.md` 与 `scripts/validate_skill.py`。历史目录不再写入发行 catalog。

不删除这些文件，也不把它们重写成第二条可执行路径。逐文件哈希见 `ASSET-INVENTORY.json`。
