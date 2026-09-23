# 案例34 · 短视频创意策划增强

在现有圣经 → 角色 → 剧集 → 场次 → 分镜上，让正文更像短视频策划。

这不是独立的创意状态机：没有单独的 Diagnosis / Hero 资产表 / Visual Beat 实体。场次仍按地点、昼夜、内外落库。观看推进写在镜头的 `beatId` 上。`heroVisualLabel` 是一句标签，不是外键。

## 分镜扩展

必填：`visualFunction`、`informationGain`。

可空：`audioAnchorType`、`audioAnchorRef`（没有可判断的声音结构就留空，不要编造节拍）、`beatId`、`heroVisualLabel`、`executionNote`。

核心机位 `angleId` / `shotSize` / `cameraMove` 仍要填，并继续投影。

用户已经写明的镜序、运镜、负面优先于本包。本包不弹窗问创作方向；模型在圣经里写明默认方向后继续。
