# 案例15 · 角色 / 演员表情九宫格

面向**角色定妆**与**演员定妆**（`hostFamily: character`）。九槽全部为**正面半身 bust**，同一身份锁 + 九种表情。

## 能做什么

- `view9` 九槽表情（slotId）：`calm_neutral` / `joyful_smile` / `angry` / `wronged_tearful` / `surprised` / `confused` / `coquettish` / `disdain` / `smug_smile`
- 对应：平静、开心、生气、委屈、惊讶、疑惑、撒娇、鄙视、得意
- **单图合成**：`sheet.view9.layout` 用整段 9-panel 九宫格提示词（自写 qualityTail，不会吃官方转面尾「only the camera angle differs」）
- **分张批量**：同一九槽各出一张 bust；槽位 suffix **不含** `9-panel expression sheet style`，避免每张图都画成九宫格
- `view3` / `view4` 为前 3 / 前 4 表情子集
- 第 0 槽 `calm_neutral` 为身份锚（`identityAnchor: true`）

## 不能做什么

- 不解冻 `plan_image`；不会自己点生成
- 不改官方 JSON；工作台换风格只影响本次会话
- `view3` / `view4` **没有** sheet 段：选三/四视角 + 单图合成会明确失败（请改 9 视角，或改分张批量 / 换回官方默认）

## 点哪个按钮

1. 设置 → 创作 Skills → 导入本文件夹（或安装目录 `user-examples\content-skills\15-generation-policy-expression-9grid` 的**副本**）
2. **角色定妆**或**演员定妆** → 选 **9 视角** → 方式选 **单图合成** → 生图策略选本包 → 开始生成
3. 若只要九张分角：同样 9 视角，方式改 **分张批量**

## 跑完应看到什么

- 单图合成：成功 **1 张** `{versionId}-sheet` 表情九宫格；最终提示词含本包 layout 关键句，**不得**出现官方 worm's-eye / hero shot 或「only the camera angle differs」
- 分张批量：共 9 张正面半身，表情明显区分，身份（脸/发型/服装）保持一致；画廊标签显示上列中文名或 slotId

## 表情对照

| # | slotId | 中文 |
|---|---|---|
| 1 | calm_neutral | 平静 / 面无表情 |
| 2 | joyful_smile | 开心 / 灿烂笑容 |
| 3 | angry | 生气 / 愤怒 |
| 4 | wronged_tearful | 委屈 / 想哭 |
| 5 | surprised | 惊讶 / 震惊 |
| 6 | confused | 疑惑 / 不理解 |
| 7 | coquettish | 撒娇 / 可爱 |
| 8 | disdain | 鄙视 / 无语 |
| 9 | smug_smile | 得意 / 坏笑 |
