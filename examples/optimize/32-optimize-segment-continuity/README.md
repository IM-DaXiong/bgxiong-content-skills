# 案例32 · 片段连续优化提示词

SOURCES: 机制提炼自 martial-arts-director-cy / fight-video-create-skill / facial-expression-prompting（通用机制，非原文照抄）。

## 用途

capabilities 仅 `optimize.segment`。文件名必须为 `optimize-segment.json`。

用于片段「AI 优化提示词」。与设置「提示词规范」分层：规范=项目写法；本 Skill=当次合同。

## 控制返回格式

- `outputSchema.finalPrompt`
- 连续性：上一镜/段 end-state → 下一段 start
- 空对白省略；`forbidHostFabrication=true`

## 字段表

见 `optimize-segment.json`。

## 可改 / 不可改

- 可改：连续性叙述粒度
- 不可改：文件名 optimize-segment.json；capability optimize.segment；finalPrompt；forbidHostFabrication

## 怎么用

1. 导入并绑定为片段优化 Skill
2. 点「AI 优化提示词」
3. 检查 finalPrompt 含 end→start 连续且无空对白编造

## 不合格示例

- 输出字段不是 finalPrompt
- 段间跳跃无 end-state
- 编造对白

## 拷给其它 LLM（3 步）

1. 粘贴 README + manifest + optimize-segment.json
2. 要求：连续性 + 与提示词规范分层
3. 产出 content-skill-v1 @ 1.1.0
