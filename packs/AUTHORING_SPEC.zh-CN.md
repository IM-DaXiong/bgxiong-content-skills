# AUTHORING_SPEC.zh-CN — Content Skill 1.1.0 总规范

给作者与其它 LLM。机器合同：`packages/app-contracts/v1/content-skill-*.json`。协议固定 `protocolId=content-skill-v1`、`protocolVersion=1.1.0`（window min=max=1.1.0）。

每一节含：含义 / 类型 / 是否必需 / 可改范围 / 非法示例 / 合法示例。

## 1. 包清单与 skill.manifest.json

| 字段 | 含义 | 类型 | 必需 | 可改范围 | 非法 | 合法 |
|------|------|------|------|----------|------|------|
| id | 安装身份 | string | 是 | 必须以 `local.` 开头 | `official.foo` | `local.wuxia.fight` |
| version | 版本 | semver | 是 | 自增 | 空 | `1.1.0` |
| protocol | 协议族 | string | 是 | 只能 `content-skill-v1` | `content-skill-v2` | `content-skill-v1` |
| protocolVersion | 协议版本 | string | 建议 | 只能 `1.1.0` | `1.0.0` 当能双栈 | `1.1.0` |
| capabilities | 能力 | string[] | 编排包写 `content.plan` | 勿把 `generation.policy` 当故事板 | `["generation.policy"]` 绑分镜 | `["content.plan"]` |

## 2. pipeline.json 步骤图

| 字段 | 含义 | 类型 | 必需 | 可改范围 | 非法 | 合法 |
|------|------|------|------|----------|------|------|
| id | 步骤名 | string | 是 | 包内唯一 | 重复 id | `"shots"` |
| op | 公开操作 | string | 是 | 仅 plan_bible/chapters/roles/scenes/shots/package | `plan_image` 当真能出图 | `plan_shots` |
| dependsOn | 前置 | string[] | 否 | 禁环 | 分镜不依赖场次又声明 coverage 冲突 | `["scenes"]` |
| when | 条件 | object | 否 | exists/notEmpty/equals/count | 幻想未注入路径 | `{ "notEmpty": "$ctx.sourceText" }` |

禁止 `steps[].input`（1.1 已删）。

## 3. bind

可引用 `$ctx.storyId` / `$ctx.sourceText` / `$ctx.sceneNodeId` / `$ctx.chapterNodeId` / `$ctx.writeMode` / `$ctx.anchor`。不要幻想 `$ctx.weather`。

| 字段 | 含义 | 类型 | 必需 | 可改范围 | 非法 | 合法 |
|------|------|------|------|----------|------|------|
| storyId | 当前故事 | template | 建议 | 只写 `$ctx.storyId` | `"s1"` 写死 | `"$ctx.storyId"` |
| sceneNodeId | 当前场次 | template | 场次故事板建议 | 只写 `$ctx.sceneNodeId` | 入口 storyId 顶未绑场 | `"$ctx.sceneNodeId"` |

## 4. directives

| 字段 | 含义 | 类型 | 必需 | 可改范围 | 非法 | 合法 |
|------|------|------|------|----------|------|------|
| prose.style.text | 文案风格 | string | 否 | 自然语言 | 把 literaryMode 当风格 | `"武打白话"` |
| prose.budget.perShot | 每镜字数 | {min,max} | 否 | 必须与 schema minLength/maxLength 一致 | 预算 40-160 但 schema maxLength=2000 | min=40 max=160 且 schema 对齐 |
| structure.maxChapters | 最多集数 | number | 否 | 正整数 | 负数 | `8` |

literaryMode 是 Host 书签，不是 prose.style。

## 5. outputSchema（主合同）

分镜包无 `outputSchema.shots` **拒装**。

| 字段 | 含义 | 类型 | 必需 | 可改范围 | 非法 | 合法 |
|------|------|------|------|----------|------|------|
| shots.count.const | 固定镜数 | integer | 一场 6 镜用 const=6 | 与 minItems=maxItems 一致 | const=6 又 maxItems=8 | `{ "const": 6 }` |
| item.required | 每镜必填 | string[] | 建议含 content/angleId/shotSize/cameraMove | 不得靠 Host 暗加必填 | 空 required 指望官方列 | 见案例 21 |
| item.properties.content | 画面要点 | string | 常用 | minLength/maxLength | 外网 $ref | `{ "type":"string","minLength":40,"maxLength":160 }` |
| angleId / shotSize / cameraMove | 机位字段 | enum 或 string | 建议 enum | 词表自定 | 任意 HTML | `"enum":["CU","ECU"]` |

核心字段投影到正式分镜；自定义字段只进有界 `skillExtension`。

## 6. 场次绑定

故事入口编排 ≠ 场次故事板。场次工作台可 `sceneNodeId → skillId+planHash` 覆盖官方格式。未绑走官方 `native.content.plan`，禁止用入口 Skill 顶包。generation.policy 包装此槽会拒绑。

## 7. 不合格修复与用户裁决

Host 按同一 schema 自动修 **恰好一轮**。仍失败：`ai_task` 终态失败，run=`awaiting_user_decision`，内容进 decision draft。用户选保存草稿自改或放弃。作者不能指望 Host 放宽 schema。

## 8. 与 generation.policy 的边界

生图策略只改多视角槽/风格 overlay，不解冻 `plan_image`，不能当故事板 Skill。

## 9. 优化能力（可选文件）

`optimize-storyboard-shot.json` / `optimize-segment.json`：capability + outputSchema + emptyPolicy。`forbidHostFabrication` 必须 true。空对白按 emptyPolicy 省略，禁止 Host 捏造。
