# 案例33 · 音乐影像导演

> 流程仍抄 `03-staged-to-shots`。v2.0 把核心从「爆款手法清单」换成导演链：创意命题 → 人物视觉语法 → 情绪曲线 → 场内视觉段落 → 镜头功能与信息增量。时长/场次/镜数不写死。

## 这个 Skill 控制 LLM 返回什么格式

一键直出选用本包：圣经 → 角色 → 剧集 → 场次 → 分镜。  
分镜信封 `count.min=1`～`max=48`（上限，不是目标）。每镜必填 `content`、机位三件套、`lyricAnchor`、`visualFunction`、`informationGain`。

## 导演链（五步各管一层）

| 步 | 回答什么 |
|----|----------|
| 圣经 | 这支片子要让观众记住什么？唯一视觉母题是什么？ |
| 角色 | 谁承担这个表达？视觉身份、动作习惯、情绪部位、镜头待遇 |
| 剧集 | 观众此刻该感觉什么？能量如何变化？ |
| 场次 | 物理地点不变时，视觉事件如何发展？ |
| 分镜 | 这镜为什么存在？新增了什么？用什么摄影语言实现？ |

卡点、对嘴、POV、舞蹈只是工具，不是本包卖点。用户原文里的镜序、运镜、负面优先于本 Skill。

## 字段表（只列本包用到的）

| 字段 | 含义 |
|------|------|
| content | 可拍画面（40–220 字） |
| angleId / shotSize / cameraMove | 角度 / 景别 / 运镜（闭集不含 truck；慢动作等写进 content） |
| lyricAnchor | 本镜歌词摘录 |
| visualFunction | 本镜任务：establish / reveal / intensify / contrast / misdirect / payoff / breathe / transform / callback |
| informationGain | 相对上一镜的新事实（8–80 字） |

## 你可以改什么 / 不要改什么

- **可以改**：各步 `authorText`、`visualFunction` 枚举词、字数与机位枚举（schema 与 budget 对齐）。
- **不要改**：不要加 `structure.*` / `count.const` 写死；不要删 `outputSchema.shots`；会跳步时不要手写 coverage。不要把 `shotMode` 加回去。

## 用户怎么用

导入本文件夹 → 源文贴完整歌词 → 一键直出选本 Skill。已导入的 1.2.0 不会自动换文案，需要重新导入 2.0.0。

## 不合格时你会看到什么

缺 `lyricAnchor` / `visualFunction` / `informationGain` 或 content 过短会验收失败；未绑走官方默认。

## 拷给其它 LLM（3 步）

1. 复制目录，改 `local.` id 与 displayName。  
2. 只改允许改的指令/枚举。  
3. 导入后选用。
