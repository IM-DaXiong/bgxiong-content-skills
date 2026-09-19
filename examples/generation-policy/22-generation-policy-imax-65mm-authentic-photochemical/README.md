# IMAX 胶片摄影·正统光化

## 能做什么

- Skills 库显示名：**IMAX 胶片摄影·正统光化**。
- `styleDomain` 仍是 `cinematic`，**不新增** domain id。
- `visualStyleOverlay` 整段替换该域官方 medium_lock / compile 头为 AUTHENTIC IMAX 15-perf 65mm **正统光化** lock（含 24fps 运动 / AVOID，含禁摄制设备入画）。
- 槽位四臂与案例 13/17/18 相同；本包不改构图。大场景 / 人像专用另包。

## 不能做什么

- 不解冻 `plan_image`；Comfy 仍不走 L2 产品 compile。
- 工作台里改画面风格只改本次会话，不回写本 zip。
- 定妆/多视角本轮不一定吃 overlay。

## 点哪个按钮

分镜单镜工作台或批量静帧工作台 → 生图策略选本包 → 风格仍选电影感档 → 开始生成。

## 跑完应看到什么

任务最终提示词 CONSTRAINTS 出现 `AUTHENTIC IMAX` / `15-PERF` / `65mm` / `AVOID`，不再是未绑时的官方电影感 lock 全文。
