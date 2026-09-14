# 案例30 · 武打分镜优化提示词

SOURCES: 机制提炼自 martial-arts-director-cy / fight-video-create-skill / facial-expression-prompting（通用机制，非原文照抄）。

## 用途

**纯优化教学包**：capabilities 仅 `optimize.storyboard_shot`。用于「AI 优化提示词」绑定。

`pipeline.json` 仅为 Host 安装布局占位，**勿当编排主 Skill**。

## 控制返回格式

- 优化输出：`optimizedPrompt`
- `emptyPolicy.forbidHostFabrication=true`；空上下文省略；禁编造对白

## 字段表

优化侧不强制 shots 表；若上下文含 fightBeat，按一行：purpose→path→opponent response→contact result→next condition。

## 可改 / 不可改

- 可改：具体招式与地理细节用词
- 不可改：仅 optimize.storyboard_shot；软暴力边界；forbidHostFabrication；六拍可读性要求

## 怎么用

1. 导入 → 在设置/分镜优化中绑定本 Skill
2. 对武打分镜点「AI 优化提示词」
3. 检查提示词含谁/中否/结果与地理，无对白编造

## 不合格示例

- 血腥/致死距离/枪械/未成年年龄
- 对手与结果不可读
- 编造对白填空

## 拷给其它 LLM（3 步）

1. 粘贴本 README + manifest + optimize-storyboard-shot.json（pipeline 可附但注明占位）
2. 要求：清晰优先 + 六拍可压缩 + 软暴力
3. 产出 content-skill-v1 @ 1.1.0，capabilities 仅 optimize.storyboard_shot
