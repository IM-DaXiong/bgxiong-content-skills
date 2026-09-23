# 比格熊内容创作Skills / bgxiong-content-skills

开源、可导入的 **Content Skills 案例与规范包**。  
本仓库为 [**比格熊数字导演工作站**](https://www.bgxiong.com)（产品仓 `bgxiong-ai-story`）提供**可安装的 Skills 素材**——分镜规划、镜头/片段提示词优化、生图策略等；**不包含**产品 Host / UI / Rust 运行时。

> 与产品仓 **完全独立**：可自由贡献与二次分发；**禁止**把本仓改动回写进产品私有实现。契约以产品 `app-contracts` 为准，本仓 `contracts/` 仅为只读 pin。

---

## 这是做什么的？

比格熊 Host 关闭能力（closed capabilities）包括：

| 能力 | 作用 |
|------|------|
| `content.plan` | 故事 → 章节 / 角色 / 场次 / 分镜结构 |
| `optimize.storyboard_shot` | 单镜提示词优化（武打、微表情、表演等） |
| `optimize.segment` | 片段级提示词 / 连续性优化 |
| `generation.policy` | 生图策略（多视角、定妆、九宫格等） |

本仓提供可导入示例（`examples/`）、作者规范（`packs/`）、矩阵与戏种卡（`docs/`），让作者与智能体按统一契约写出**可被工作站直接导入执行**的 Skills。

---

## 怎么使用（导入到比格熊）

1. 安装并打开 **比格熊数字导演工作站**（官网下载：[https://www.bgxiong.com](https://www.bgxiong.com)）。
2. 打开 **设置 → 创作 Skills**（以客户端实际菜单为准）。
3. **导入**本仓中的某一个示例文件夹，例如：
   - `examples/content-plan/28-storyboard-performance`
   - `examples/optimize/30-optimize-storyboard-fight`
   - `examples/optimize/31-optimize-storyboard-micro-cu`
   - `examples/optimize/32-optimize-segment-continuity`
   - `examples/content-plan/34-short-video-creative`
   - `examples/content-plan/33-viral-song-mv`
   - `examples/generation-policy/23-generation-policy-multi-angle-character-sheet`
   - `examples/generation-policy/15-generation-policy-expression-9grid
   - examples/generation-policy/22-generation-policy-imax-65mm-authentic-photochemical`
4. 导入后在对应工作流里选用该 Skill（分镜规划 / AI 优化提示词 / 生图策略）。
5. 可选本地校验：

```bash
python scripts/validate-example.py examples/optimize/30-optimize-storyboard-fight
```

PowerShell：

```powershell
.\scripts\validate-example.ps1 examples\optimize\30-optimize-storyboard-fight
```

更细的目录与贡献约定见 `docs/USAGE.zh-CN.md`、`AGENT.md`、`NOTICES.md`。

---

## 仓库结构

```text
docs/          CASE-MATRIX / INSPIRATIONS / GENRE-* / USAGE
packs/         CONTENT_SKILL / AUTHORING 作者规范（中/英）
contracts/     只读 pin（对齐产品 app-contracts 版本）
examples/      content-plan / generation-policy / optimize
scripts/       validate-example.*
community/     贡献入口 stub
```

## 贡献红线（ABS / NOTICE）

1. **ABS-01** 只提炼规则，不整段搬迁第三方 SKILL.md  
2. **ABS-02** 外部灵感优先 MIT / Apache-2.0 来源；专有许可只写灵感层（本仓自身为自定义许可，见 LICENSE）  
3. **ABS-03** IP 安全：禁角色名 / 产品专有口诀硬抄  
4. **ABS-04** 每条规则映射本仓能力字段  
5. **ABS-05** 每个包 README 含 SOURCES  
6. 校验：`python scripts/validate-example.py examples/.../<pack>`

详见 `docs/INSPIRATIONS.md` 与 `NOTICES.md`。

## 与产品的边界

| 资产 | 来源 | 本仓 |
|------|------|------|
| Host Rust / UI / SQLite | 产品 | **不**收录 |
| app-contracts JSON | 产品 SSOT | `contracts/` 只读镜像 |
| 教学案例 | 产品 fixtures 先建 | 拷贝至 `examples/`（产品 fixtures 仍保留） |

---

## About BGXiong / 关于比格熊

**比格熊数字导演工作站**是装在你电脑上的 AI 导演工具：从一句话创意到故事展开、场次与分镜、批量生图/生视频、配音与导出，尽量在同一桌面客户端走完——数据在本地，模型由你自选，不为网页白板式「一句话出一张图」止步。

- 官网 / 下载：[https://www.bgxiong.com](https://www.bgxiong.com)
- 客户端版本说明：[https://www.bgxiong.com/client/version.html](https://www.bgxiong.com/client/version.html)
- 本开源仓：提供可导入的 Content Skills，**服务**于工作站，但仓库本身独立维护。

口号参考：从故事到片段。一个人，也能开拍。

---

## 联系我们 / Contact

公众号搜索 **天途影像**，可在后台私信联系。

WeChat Official Account: search **天途影像** and message us in the backend.

## License

本仓库使用**自定义许可**（不是 MIT）：**个人与商用均可使用**；**禁止将本仓库内容原样或改造后作为独立商品出售**。全文见 [LICENSE](./LICENSE)。

第三方灵感来源仍遵循各自许可，见 NOTICES.md。
