# 案例13 · 分镜风格 overlay

## 能做什么

- `styleDomain` 仍是现有 12 档之一（本例 `cinematic`），**不新增** domain id。
- `visualStyleOverlay` 整段替换该域官方 medium_lock / compile 头。

## 不能做什么

- 不解冻 `plan_image`；Comfy 仍不走 L2 产品 compile。
- 工作台里改画面风格只改本次会话，不回写本 zip。

## 点哪个按钮

分镜单镜工作台或批量静帧工作台 → 生图策略选本包 → 风格仍选电影感档 → 开始生成。

## 跑完应看到什么

任务最终提示词 CONSTRAINTS 出现「用户策略替换句」，不再是未绑时的官方电影感 lock 全文。
