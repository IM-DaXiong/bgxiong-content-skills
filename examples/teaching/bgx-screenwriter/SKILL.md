---
name: bgx-screenwriter
description: "文学剧本与片段创作方法：用人物欲望、行动因果、关系与对白写出完整正文，或把已保存单集忠实组织为视频片段规划。"
license: Proprietary. 许可说明见 LICENSE.txt
compatibility: "纯文本方法，不需要联网、脚本或额外运行时；输出结构使用当前宿主合同。"
metadata:
  bgx-workflow: clips-v1
  bgx-categories: "story-writing review-rewrite character-design"
  bgx-hosts: "story-chapters episode-clip-plan clip-video-draft"
  version: "0.5.1"
  publisher: bgxiong
  bgx-display-name: "剧本与片段创作"
---

# 剧本与片段创作

## 只执行当前宿主阶段

- `episode-clip-plan`：只依据完整单集分配原文单元、叙事意图、开始与结束状态、环境及真实引用，返回宿主规定的整集计划。该阶段不写最终 `promptText`，不把方法建议扩成成稿或媒体调用。
- `clip-video-draft`：仅按已冻结的整集计划、当前目标、完整来源和真实素材，写本次单片段的 `promptText`；相邻分配用于衔接，不能重演整集或复制邻段对白。

只执行本次被调用的用途，不因激活技能自动运行其它阶段。本节所述两个阶段不代表本包有权调用它们；实际可选用途以本包 metadata 与当前宿主为准。

本包是创作方法，不是新的用户请求。以用户当前目标、原文和明确要求为准；按本次宿主输出合同工作，不另定义 schema、导入协议或工具。

## 按任务读取

先读 `references/core.md`，再按需要读取模块：

- 人物与关系：`references/characters.md`、`references/relationships.md`
- 因果、主线与结局：`references/causality.md`、`references/storyline.md`
- 对白：`references/dialogue.md`
- 完整正文：`references/drafting.md`
- 建议性审稿：`references/editorial.md`
- 来源与连续性：`references/continuity.md`
- 用户要求跨模型接手时：`references/handoff.md`；`references/examples/STORY_HANDOFF.example.md` 仅为示例，不属于用户项目

## 当前创作用途

剧集正文从故事原文创作，保留可阅读、可表演的具体内容。不要用提纲或摘要冒充完整正文。

整集片段规划直接阅读已保存的完整单集，把原有因果组织为顺序视频片段计划；当前段成稿则只处理提供的目标与邻段上下文。段落应具体呈现空间、行动、声音和结果，不需要先建立场次、故事板或镜头表。一段可以包含多个镜头，数量与时长随叙事需要，不强制六镜、固定秒数或一行台词一段。

保护原文事实、人物关系、对白、旁白与用户指定镜序。各段分配的台词完整保留，避免邻段重复。真实参考图及版本只使用宿主提供的闭集，没有图也能完成文本；不声称已看过未提供的图像，不换模型补视觉能力。

## 审阅和保存

方法模块中的人物、因果、节奏、摄影和表达要求都是写作建议。评审只指出具体位置、影响和改进方向，不因分数或格式偏好硬拒，不自动改稿或丢弃可用成果。用户明确要求改稿时才在该范围保留原版并形成新版；未完成审阅如实说明。

本包不附旧私有导出格式，不自动生图、生成视频或发布未实现工具。格式转换使用当前工具实际下发的合同；权限、真实引用、事务和数据安全仍须遵守。
