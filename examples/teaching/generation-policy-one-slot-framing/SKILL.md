---
name: generation-policy-one-slot-framing
description: "只改一个槽位取景的 4 视角变体：其余槽位保持官方，仅 4 视角里右侧转身那一张改成右侧半身。在需要官方 4 视角、但右侧一张要半身而不是全身时使用。"
metadata:
  bgx-workflow: clips-v1
  version: "1.0.1"
  bgx-categories: "visual-style character-design"
  bgx-hosts: multi-view
  bgx-display-name: "四视角局部半身定妆"
---

# 四视角局部半身定妆

## 内容

`references/layout.json` 的槽位顺序与官方完全一致；唯一差别写在 `slotOverrides.view4.right.framing`：4 视角里的右侧转身一张改为右侧半身。3 视角和 9 视角里的 `right` 沿用官方全身取景。

## 使用方式

1. 角色定妆或演员定妆选 4 视角，生图技能选本技能。
2. 开始生成：右侧那一张是半身，其余三张与官方一致。
3. 出网提示词里应出现本包的取景原文，不能被应用内置角度表覆盖。

## 边界

- 因为取景已被改，本技能不适用单图合成（sheet）。
- 本技能不修改官方默认合同本身。

## 当前创作边界

槽位、子模式与引用按实际多视角执行合同处理，图像布局数量不是视频镜数限制。人物一致性、摄影与表演质量是创作建议；出现偏差时说明具体问题并保留成果，不因评分硬拒或自动重写。尊重用户媒介风格，不添加固定摄影控件要求或启动未发布工具。
