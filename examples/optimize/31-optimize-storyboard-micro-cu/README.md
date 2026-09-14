# 案例31 · 微表情特写优化提示词

SOURCES: 机制提炼自 martial-arts-director-cy / fight-video-create-skill / facial-expression-prompting（通用机制，非原文照抄）。

## 用途

capabilities 仅 `optimize.storyboard_shot`。微表情特写「AI 优化提示词」教学包；pipeline 为安装占位。

## 控制返回格式

- `optimizedPrompt`；CU/ECU + static；可见解剖词；禁 AU 码进最终提示词
- `forbidHostFabrication=true`；空字段省略；禁编造对白

## 字段表

优化合同字段见 `optimize-storyboard-shot.json` 的 outputSchema / emptyPolicy。

## 可改 / 不可改

- 可改：具体解剖词选择
- 不可改：仅 optimize.storyboard_shot；禁 AU 入最终提示；forbidHostFabrication

## 怎么用

1. 导入并绑定为分镜优化 Skill
2. 对微表情特写镜点「AI 优化提示词」
3. 检查无 AU 编码、无编造对白

## 不合格示例

- 最终提示含 AU12 等编码
- 全脸夸张无局部解剖
- 编造对白

## 拷给其它 LLM（3 步）

1. 粘贴 README + manifest + optimize-storyboard-shot.json
2. 要求：CU/ECU、可见解剖词、禁 AU
3. 产出 content-skill-v1 @ 1.1.0
