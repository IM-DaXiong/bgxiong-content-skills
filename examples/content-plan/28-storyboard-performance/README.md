# 案例28 · 表演分镜

SOURCES: 机制提炼自 martial-arts-director-cy / fight-video-create-skill / facial-expression-prompting（通用机制，非原文照抄）。

## 用途

`content.plan` + `optimize.storyboard_shot`。表演调度分镜：因果链与可见动作优先，禁空泛抒情。

## 控制返回格式

- 固定 **6** 镜；必填 `performanceBeat`
- `shotSize` ∈ MS/CU/ECU；`cameraMove` ∈ static/pan/dolly_in；`angleId` ∈ medium/closeup/low/high/pov
- 优化合同：`outputSchema.optimizedPrompt`；`emptyPolicy.forbidHostFabrication=true`

## 字段表

| 字段 | 约束 |
|---|---|
| performanceBeat | 调度/视线/节拍功能/潜台词可见动作 |
| action | 可见动作，服务因果链 trigger→…→residue |
| shotSize / cameraMove / angleId | 见上枚举 |

## 可改 / 不可改

- 可改：具体戏的 trigger/障碍/泄漏与用词粒度
- 不可改：能力声明、6 镜、performanceBeat 必填、景别/运镜枚举、forbidHostFabrication

## 怎么用

1. 导入本包 → 选用为编排 Skill（content.plan）
2. 需要「AI 优化提示词」时绑定同包的 optimize.storyboard_shot
3. 检查返回含 6 条 shots 且每条有 performanceBeat

## 不合格示例

- 只有「很悲伤」无可见动作
- 全脸肌肉一次性拉满
- 编造对白填空上下文
- 使用 MS/CU/ECU 以外景别

## 拷给其它 LLM（3 步）

1. 粘贴本 README + `skill.manifest.json` + `pipeline.json` + `optimize-storyboard-shot.json`
2. 要求：遵守因果链与 performanceBeat；勿发明新能力字符串
3. 产出可导入的 content-skill-v1 @ 1.1.0 包
