# 案例21 · 一场固定 6 镜

## 这个 Skill 控制 LLM 返回什么格式
顶层 shots 数组长度必须是 6。每镜必填 content、angleId、shotSize、cameraMove。

## 字段表（只列本包用到的）
| 字段 | 含义 |
| shotIndex | 1-6 |
| content | 40-160 字 |
| angleId | wide/medium/closeup/low/high/pov |
| shotSize | EWS/WS/MS/CU/ECU |
| cameraMove | static/pan/tilt/dolly_in/handheld |

## 你可以改什么 / 不要改什么
可以改枚举词表，但 count.const 必须保持 6，且与 minItems/maxItems 一致。

## 用户怎么用（导入 → 绑定到哪 → 点哪个按钮）
导入 → 场次分镜工作台绑定本 Skill → 点生成分镜。不绑定则走官方默认格式，不会整单失败。

## 不合格时你会看到什么（人话）
缺 cameraMove 会验收失败；自动修一次仍缺则任务结束并出现挂起卡片。

## 拷给其它 LLM 时如何改成自己的包（3 步）
1. 复制本目录，改 skill.manifest.json 的 id（必须 local. 开头）和 displayName。
2. 只改 pipeline.json 里本 README 允许改的字段（枚举、字数、镜数）。
3. 设置 → 创作智能体 → Skills 库 → 导入包；在场次工作台绑定后再点生成分镜。
