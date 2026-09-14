# 比格熊内容创作Skills / bgxiong-content-skills

**独立开源案例与规范仓**（slug: `bgxiong-content-skills`）。  
与产品仓 `bgxiong-ai-story` **完全独立**：本仓不绑定产品构建/门禁，**禁止回写产品**。

## 30 秒理解

- 本仓提供可导入的 **Content Skill 包**（`examples/`）+ 契约只读 pin（`contracts/`）+ 作者文档（`packs/`）。
- 包需导入 **比格熊数字导演**（或兼容 Host）才能执行；本仓**不内嵌** Host / UI / Rust 运行时。
- 能力闭集：`content.plan` / `generation.policy` / `optimize.storyboard_shot` / `optimize.segment`。

## 导入路径（产品）

设置 → 创作 Skills → 导入文件夹 → 选择 `examples/.../<pack>/`。

## 目录

```text
docs/          CASE-MATRIX / INSPIRATIONS / GENRE-* / USAGE
packs/         AUTHORING / CONTENT_SKILL（人+智能体）
contracts/     只读 pin 自产品 app-contracts（勿改语义）
examples/      content-plan / generation-policy / optimize
scripts/       validate-example.*
community/     贡献 stub
```

## 贡献规则（ABS / NOTICE）

1. **ABS-01** 只抽机制，不整文件搬迁他人 SKILL.md  
2. **ABS-02** 优先 MIT / Apache-2.0；不明许可只写「启发」  
3. **ABS-03** IP 脱敏：禁角色名/作品专名照抄  
4. **ABS-04** 外来概念必须映射本仓闭集  
5. **ABS-05** 每案例 README 含 SOURCES  
6. 校验：`python scripts/validate-example.py examples/.../<pack>`  

详见 `docs/INSPIRATIONS.md` 与仓根 `NOTICES.md`。

## Remote

**暂无公开 Git remote**。本机仓就绪即可；勿推送机密/产品私货。

## 与产品关系

| 资产 | 真源 | 本仓 |
|---|---|---|
| Host Rust / UI / SQLite | 产品 | **无**（产品独有） |
| app-contracts JSON | 产品 | `contracts/` 只读拷贝 |
| 教学案例 | 产品 fixtures 先建 | 单向拷贝到 `examples/` |

抽取时间见 `contracts/VERSION`。
