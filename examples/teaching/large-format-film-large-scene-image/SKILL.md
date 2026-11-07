---
name: large-format-film-large-scene-image
description: "为大场景图片提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。"
license: Proprietary
metadata:
  bgx-workflow: clips-v1
  version: "2.0.2"
  publisher: bgxiong
  bgx-categories: "visual-style"
  bgx-display-name: "IMAX大画幅胶片·大场景·图片"
  bgx-hosts: "image-photography-style"
---

# IMAX大画幅胶片·大场景·图片

图片包用于图片摄影风格，独立于图片提示词优化助手；选择后在本次生图提交时应用风格正文。选择本身不调用 AI；最终是否出图/视频由用户提交决定。

风格正文唯一来源为 `references/layout.json` 的 `visualStyleOverlay`：

大画幅胶片环境质感，前中远景与大气透视自然，肤理及建筑地貌纹理真实，材质反光克制，高光柔和，局部对比适度，色彩克制、颗粒细腻。保留原景别、机位、构图与画幅。

保留用户原文、对白、景别、机位、构图与画幅；摄影质感不添加人物、动作或器材。

只处理摄影质感，不承诺设备实拍或特定商业制式效果；不改模型、时长、帧率或用户意图，不截断或重写用户提示词。图片包不添加运动及时序指令。

适用于独立图片和环境图片提示词；不要求场次、故事板或静帧实体，也不要求用户先写严格模板。不添加运动、时序或视频镜数。摄影术语只是表达建议，不作为拒存或自动重写条件；输出字段遵守宿主当次合同，不输出私有格式。

本包为比格熊自有摄影提示词的精简编排。许可见 `LICENSE.txt`。
