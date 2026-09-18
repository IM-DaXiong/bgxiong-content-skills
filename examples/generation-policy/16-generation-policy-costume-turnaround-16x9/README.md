# 案例16 · 角色 / 演员服装转面（横版 16:9）

面向**角色定妆**与**演员定妆**（`hostFamily: character`）。九槽为**服装与身份资产参考**：左半两张全身正/背，右上脸特写，右下六张局部。给后续视频锁脸、服装、鞋、腰、发饰、材质用。

## 能做什么

- `view9` 九槽（slotId）：`full_body_front` / `full_body_back` / `face_closeup` / `wrist_hand` / `shoes` / `waist_belt` / `shoulder_sleeve` / `hair_back` / `fabric_hem`
- **单图合成**：`sheet.view9` 为横版 16:9；左 50% 两竖格全身正/背，右上脸特写，右下 2×3 局部（自写 qualityTail，不会吃官方「only the camera angle differs」）
- **分张批量**：同一九槽各出一张；槽位 suffix **不含**整张 16:9 九宫格 layout，避免每张都画成整表
- `view3`：正面全身 + 背面全身 + 面部特写
- `view4`：再加腰部/腰封
- 第 0 槽 `full_body_front` 为身份锚（`identityAnchor: true`）

## 不能做什么

- 不解冻 `plan_image`；不会自己点生成
- 不改官方 JSON；工作台换风格只影响本次会话
- `view3` / `view4` **没有** sheet 段：选三/四视角 + 单图合成会明确失败（请改 9 视角，或改分张批量 / 换回官方默认）
- 右下只有 6 格：衣服纹理/胸前装饰与裙摆/下摆合并在 `fabric_hem`，不会拆成第 10 张

## 点哪个按钮

1. 设置 → 创作智能体 → Skills 库 → 导入本文件夹（或安装目录 `user-examples\content-skills\16-generation-policy-costume-turnaround-16x9` 的**副本**）
2. **角色定妆**或**演员定妆** → 选 **9 视角** → 方式选 **单图合成** → 生图策略选本包 → 开始生成
3. 若要九张分角：同样 9 视角，方式改 **分张批量**

## 跑完应看到什么

- 单图合成：成功 **1 张** `{versionId}-sheet` 横版 16:9 服装参考表；最终提示词含 Left half / facial close-up / 2 rows × 3 columns；**不得**出现官方 worm's-eye 或「only the camera angle differs」
- 分张批量：共 9 张，身份（脸/发型/服装/配色）一致；画廊标签显示下表中文名或 slotId

## 视图对照

| # | slotId | 中文 | 在 16:9 单图中的位置 |
|---|---|---|---|
| 1 | full_body_front | 正面全身 | 左半 · 左竖格 |
| 2 | full_body_back | 背面全身 | 左半 · 右竖格 |
| 3 | face_closeup | 面部大特写 | 右半 · 上方 |
| 4 | wrist_hand | 手腕 / 手部 | 右下 2×3 · 行1列1 |
| 5 | shoes | 鞋子 | 右下 2×3 · 行1列2 |
| 6 | waist_belt | 腰部 / 腰封 | 右下 2×3 · 行1列3 |
| 7 | shoulder_sleeve | 肩部 / 袖口 | 右下 2×3 · 行2列1 |
| 8 | hair_back | 发型 / 后脑勺 | 右下 2×3 · 行2列2 |
| 9 | fabric_hem | 衣料胸饰 / 下摆 | 右下 2×3 · 行2列3 |
