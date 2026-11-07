---
name: generation-policy-imax-65mm-portrait-closeup
description: "强调皮肤、眼神、面部立体感与自然光学，适用于人物图片及表演视频。"
metadata:
  bgx-workflow: clips-v1
  version: "1.0.1"
  bgx-categories: "visual-style"
  bgx-display-name: "巨幕胶片人像风格"
  bgx-hosts: "video-photography-style optimize-image-prompt clip-environment-prompt clip-video-draft"
---

# 巨幕胶片人像风格

以 `references/layout.json` 的 `visualStyleOverlay` 作为摄影质感参考。视频摄影用途读取这段资源；图片提示词、环境提示词和片段草稿用途结合当前正文按需采用，不另定义字段或输出格式。

大画幅胶片人像质感，皮肤纹理与眼神清楚自然，柔和高光，肤色真实，细颗粒与可信焦点过渡。保留人物身份、表情和用户取景，不用磨皮、夸张虚化或额外动作代替真实质感；视频中肤理、曝光和焦点连贯。

摄影是创作建议，不能覆盖用户的媒介、剧情、对白、否定要求或手写取景。图片不添加运动时序；视频不强制帧率、时长或镜数。仅选择技能不触发生成，实际媒体提交由用户确认并受当前能力合同约束。

不声称生成结果由真实摄影机、胶片或特定商业制式实拍。评审偏差给出改进建议并保留成果，不按关键词或评分拒收，不自动重写。
