---
name: generation-policy-imax-65mm-large-scene
description: "强调环境尺度、空间层次与大气透视，适用于环境图片及环境为主的视频表达。"
metadata:
  bgx-workflow: clips-v1
  version: "1.0.1"
  bgx-categories: "visual-style"
  bgx-display-name: "巨幕胶片环境风格"
  bgx-hosts: "video-photography-style optimize-image-prompt clip-environment-prompt clip-video-draft"
---

# 巨幕胶片环境风格

以 `references/layout.json` 的 `visualStyleOverlay` 作为摄影质感参考。视频摄影用途读取这段资源；图片提示词、环境提示词和片段草稿用途结合当前正文按需采用，不另定义字段或输出格式。

大画幅胶片环境质感，建筑与地貌细节自然，前中远景层次、大气透视和空间尺度可信，颗粒细腻，色彩克制，高光柔和。相机运动时视差、几何、光照与纹理连贯。保留用户取景与主体，不为展示尺度擅自改成远景。

摄影是创作建议，不能覆盖用户的媒介、剧情、对白、否定要求或手写取景。图片不添加运动时序；视频不强制帧率、时长或镜数。仅选择技能不触发生成，实际媒体提交由用户确认并受当前能力合同约束。

不声称生成结果由真实摄影机、胶片或特定商业制式实拍。评审偏差给出改进建议并保留成果，不按关键词或评分拒收，不自动重写。
