# 案例26 · 文戏微表情

## 这个 Skill 控制 LLM 返回什么格式
6 镜，shotSize 只能 CU/ECU，cameraMove 只能 static，必填 faceBeat。

## 字段表（只列本包用到的）
| 字段 | 含义 |
| faceBeat | 微表情要点 |
| shotSize | CU 或 ECU |

## 你可以改什么 / 不要改什么
可以改 faceBeat 说明。不要放开全景枚举，那会变成武打包。

## 用户怎么用（导入 → 绑定到哪 → 点哪个按钮）
导入后把文戏场绑本 Skill。与案例 25 分绑同一故事的两场。

## 不合格时你会看到什么（人话）
返回 WS 或 handheld 会验收失败。

## 拷给其它 LLM 时如何改成自己的包（3 步）
1. 复制本目录，改 skill.manifest.json 的 id（必须 local. 开头）和 displayName。
2. 只改 pipeline.json 里本 README 允许改的字段（枚举、字数、镜数）。
3. 设置 → 创作 Skills → 导入包；在场次工作台绑定后再点生成分镜。
