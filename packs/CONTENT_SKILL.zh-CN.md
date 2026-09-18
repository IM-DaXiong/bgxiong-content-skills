# Content Skill 包契约（content-skill-v1）

> **本仓对外作者标准（中文）**  
> 给要编写 / 导入「创作 Skills」的人读。  
> English: [`CONTENT_SKILL.en.md`](CONTENT_SKILL.en.md)

## 这是什么

Content Skill 是一份**可导入的创作编排包**。**1.1.0 起 Skill = LLM 返回格式 SSOT**：`bind` + `directives` + `outputSchema`。禁止 `steps[].input`。分镜包必须声明 `outputSchema.shots`，否则拒装。

场次故事板可按 `sceneNodeId` 绑定 Skill（冻 planHash）以覆盖官方格式。未绑走官方 `native.content.plan`，仍可拆镜；不会用入口编排顶上。

另有一种**生图策略 Skill**：不代替你点「生成」，只替换多视角槽位文案、可选单图合成 `sheet` 布局，或分镜静帧风格句。

## 权威入口

| 材料 | 位置 |
|------|------|
| 本文（中文） | 安装目录 `user-examples/content-skills/CONTENT_SKILL.zh-CN.md`（开发仓同路径在 `fixtures/content-skills/local-samples/`） |
| 英文版 | `CONTENT_SKILL.en.md` |
| 可导入案例 | 同目录 `01-…`～`14-…`（见 `README.md`） |
| 机器闭集 | `packages/app-contracts/v1/content-skill-*.json` |
| 打包工具 | 仓库 `tools/content-skill/` |

## 开箱怎么用（用户）

1. 设置 → **创作智能体** → **Skills 库** → **导入包**（文件夹或 zip）。安装版可先打开随包案例，把 `user-examples/content-skills/` 下某案例拷到可写目录再导入。
2. 导入成功只表示包在本机（**L1**），还不算出内容。
3. 打开「生成剧集」或「一键直出」，编排方式选该 Skill，确认计划（**L2**）后再跑（**L3**）。
4. 用户包 `id` 必须以 `local.` 开头。`official.*` 仅仓库夹具，导入会被拒绝。

## 包里要有什么

```
<skill-dir>/
  skill.manifest.json     # 必需
  pipeline.json           # 必需
  pack-pin.json           # 安装后必需（可用工具生成）
  produce-plan.component.wasm  # 可选
  generation-policy.json  # 生图策略能力时必需
  README.md               # 可选
```

### `skill.manifest.json` 主要字段

| 字段 | 必需 | 含义 |
|------|------|------|
| `id` | 是 | 用户包必须 `local.` 前缀 |
| `version` | 是 | semver；同 id 再装 = 覆盖 |
| `protocol` | 是 | 必须 `content-skill-v1` |
| `displayName` / `description` | 否 | 管理页展示 |
| `capabilities` | 否 | Host 闭集：`content.plan` / `generation.policy` / `optimize.storyboard_shot` / `optimize.segment`。空数组且无生图政策文件 = 视为 `content.plan`。**禁止**自造 `category` / `tags` 当分类 |
| `entry` | 否 | 默认 `pipeline.json` |

### `pipeline.json` 主要字段

| 字段 | 必需 | 含义 |
|------|------|------|
| `steps` | 是 | 非空步骤列表 |
| `steps[].id` | 是 | 包内唯一 |
| `steps[].op` | 是 | 只能是公开操作（见下） |
| `steps[].dependsOn` | 否 | 前置步骤 id；禁环 |
| `steps[].when` | 否 | 条件；成立才保留该步 |
| `coverage` | 否 | 制品层；缺省由步骤推导。有 `when` 跳步时不要手写冲突的 coverage |

### 公开操作（可写进用户包）

| op | 做什么 |
|----|--------|
| `plan_bible` | 故事圣经 |
| `plan_chapters` | 剧集 |
| `plan_roles` | 角色 |
| `plan_scenes` | 场次（通常依赖剧集） |
| `plan_shots` | 分镜（通常依赖场次） |
| `plan_package` | 成片包装层 |

不要写 `materialize_*`、`assemble_package`、`plan_appearance`、`plan_continuity` 等内部/非公开 op。`plan_image` 在合同里可能出现，但当前发行不可用——不要当能出图。

### `when` 常用谓词

`exists` / `notEmpty` / `equals` / `count`。v1 准备期上下文主要是 `$ctx.storyId`、`$ctx.sourceText`。

### `pack-pin.json`

钉住 `pipeline.json`（及可选 wasm）原始字节哈希。被改过的编排与 pin 不一致 → 导入/加载硬拒，不会静默放过。

## 生图策略 Skill（可选）

包内 `generation-policy.json`，能力声明含 `generation.policy`。  
作用：整份替换多视角槽（四臂文案等）、可选 `sheet` 单图布局，或分镜静帧风格句；**不**创建生图任务。  
案例：`10-generation-policy-*`～`13-…`；`14-…` 是故意无效的负例；`15-generation-policy-expression-9grid` 是表情九宫格（9 视角可单图合成一张）；`16-generation-policy-costume-turnaround-16x9` 是横版 16:9 服装转面（左全身正/背、右上脸特写、右下六局部）；`17-generation-policy-imax-65mm-generic` 是 IMAX胶片摄影通用风格 overlay；`18-generation-policy-imax-65mm-large-scene` 是 IMAX 胶片摄影大场景 overlay；`19-generation-policy-imax-65mm-portrait-closeup` 是 IMAX 胶片摄影人像特写 overlay。

## 铁律

1. 选了 Skill 却失败时，软件**不会**偷偷改走内置编排假装成功。
2. L1 导入 ≠ L2 计划通过 ≠ L3 已出内容。
3. 案例目录是标本；字段标准以本文 + 合同 JSON 为准。

## 推荐起步

复制 `01-chapters-only`，改 `id`（仍 `local.`）、`displayName`、`pipeline.json`，导入后在「生成剧集」选用。更复杂再看 `02`、`03`。
