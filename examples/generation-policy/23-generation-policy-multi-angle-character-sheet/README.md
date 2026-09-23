# 案例23 · 角色 / 演员多角度正交参考板

> **定妆入口（INV-MV-CUSTOM-ENTRY）**：在角色/演员定妆视角条选择 **「自定义」**，再绑定本策略；不要只点「9视角」——按钮文案仍是官方九角语义，槽数与含义以本包 `view9[]` 为准（当前为 15 槽）。


面向**角色定妆**与**演员定妆**（`hostFamily: character`）。

主视角六槽：**同一身份、同一站姿**，只转观察角度（正交）。  
另加 **9 个细节切片**（眼/唇/发/领/袖/腰/面料/鞋/配饰），对应参考图里主图旁的小图资产锁，不是新造型。

## 能做什么

### 主角度（正交）

| # | slotId | 中文 |
|---|---|---|
| 1 | full_body_front | 正面全身 0°（身份锚） |
| 2 | full_body_side | 左侧全身严格 90° |
| 3 | full_body_back | 背面全身 180° |
| 4 | face_front | 正面面部特写 |
| 5 | face_three_quarter | 面部约 45° |
| 6 | face_profile | 正侧面部 90° |

### 细节切片（同一人资产特写）

| # | slotId | 中文 |
|---|---|---|
| 7 | eye_detail | 眼部特写 |
| 8 | lip_detail | 唇部特写 |
| 9 | hair_detail | 发型 / 发饰 |
| 10 | collar_detail | 领口细节 |
| 11 | sleeve_detail | 袖口细节 |
| 12 | waist_detail | 腰带 / 腰饰 |
| 13 | fabric_detail | 面料纹理 |
| 14 | shoe_detail | 鞋子细节 |
| 15 | accessory_detail | 配饰细节 |

- `view3`：全身三向；`view4`：全身三向 + 正脸；`view9`：**15 槽**（6 主角度 + 9 细节；Host 每 mode 最多 16）
- **单图合成**：`sheet.view9` 描述「左全身三向 + 右上三脸 + 细节小图网格」，自写 qualityTail
- **分张批量**：15 张分角/切片；细节槽 suffix 不含整表 layout

## 硬约束

- 主视角：orthographic；NOT different poses / NOT different moments；camera rotates；do not redesign the face  
- 细节：同一角色资产特写；禁止另起炉灶的刺绣/配饰/脸型

## 不能做什么

- 不解冻 `plan_image`  
- 不是纯表情九宫格（15）、不是案例 16 那种「左正背+右上脸+右下六服装格」的固定 16:9 九槽表（本包主角度 + 面料/五官切片更全）

## 点哪个按钮

导入本文件夹 → 角色/演员定妆 → **9 视角**（本包 15 槽）→ 单图合成或分张批量 → 生图策略选本包。

## 跑完应看到什么

- 单图：一张参考板，含全身三向、三脸、以及眼唇发领袖等小图，身份与服装一致  
- 分张：最多 15 张；细节图不得变成另一个人/另一套衣服
