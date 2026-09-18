# 案例20 · 只做到场次（武侠字数）

## 这个 Skill 控制 LLM 返回什么格式
本包没有分镜。LLM 只返回场次规划。风格与字数写在 directives.prose。

## 字段表（只列本包用到的）
| 字段 | 含义 |
| prose.style.text | 文案风格 |
| prose.budget.perScene | 每场字数 80-280 |

## 你可以改什么 / 不要改什么
可以改风格句子和字数上下限。不要加 plan_shots，不要写 input。

## 用户怎么用（导入 → 绑定到哪 → 点哪个按钮）
导入后在生成剧集/一键直出选这个 Skill。不要绑到场次故事板。

## 不合格时你会看到什么（人话）
旧 input 包会提示按 1.1 重写。字数和 schema 冲突会拒装。

## 拷给其它 LLM 时如何改成自己的包（3 步）
1. 复制本目录，改 skill.manifest.json 的 id（必须 local. 开头）和 displayName。
2. 只改 pipeline.json 里本 README 允许改的字段（枚举、字数、镜数）。
3. 设置 → 创作智能体 → Skills 库 → 导入包；在场次工作台绑定后再点生成分镜。
