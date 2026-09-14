# 案例25 · 武打场故事板

## 这个 Skill 控制 LLM 返回什么格式
与案例 21 相同的 6 镜骨架，另强制 fightBeat；角度偏低机位与手持。

## 字段表（只列本包用到的）
| 字段 | 含义 |
| fightBeat | 本镜打斗节拍（扩展袋） |
| 其余 | 同案例 21 核心字段 |

## 你可以改什么 / 不要改什么
可以改武打风格句子和 fightBeat 字数。不要删 outputSchema。

## 用户怎么用（导入 → 绑定到哪 → 点哪个按钮）
导入后把武打场绑到本 Skill，文戏场绑案例 26。点场次生成分镜。

## 不合格时你会看到什么（人话）
未绑或绑了生图策略包会人话失败。自定义 fightBeat 只进 skillExtension。

## 拷给其它 LLM 时如何改成自己的包（3 步）
1. 复制本目录，改 skill.manifest.json 的 id（必须 local. 开头）和 displayName。
2. 只改 pipeline.json 里本 README 允许改的字段（枚举、字数、镜数）。
3. 设置 → 创作 Skills → 导入包；在场次工作台绑定后再点生成分镜。
