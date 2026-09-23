# CASE-MATRIX（starter · from PLAN 184500 §15）

> 产品侧建议另有 `fixtures/content-skills/CASE-MATRIX.md`；本文件为开源仓文档。状态随抽取更新。

| 戏种 \ 能力 | content.plan | optimize.storyboard_shot | optimize.segment | generation.policy | 状态 |
|---|---|---|---|---|---|
| 通用流程 | 01,02,03 | 官方 default | 官方 default | 10–14,16–19,22（含 IMAX） | 有 |
| 武打武侠 | 25（强化） | **30** | 32（共用连续） | 可选 | P0/P1 |
| 微表情 | 26（强化） | **31** | 可选 | **15** | P0/P1 |
| 表演 | **28** | 28 内嵌 / 变体 | **33**（可选） | — | P0 |
| 玄幻 | **40** | **41** | **42** | **43** | P2 [待核] |
| 古偶 | **50** | **51** | **52** | **53** | P2 [待核] |
| 都市 | **60** | **61** | **62** | — | P3 [待核] |
| 悬疑 | **70** | **71** | **72** | — | P3 [待核] |
| 场次绑定教学 | 27 | — | — | — | 有 |
| 六镜 schema | 21 | — | — | — | 有 |
| 多角度定妆/角色表 | — | — | — | **23** | 有 |
| 病毒歌曲 MV | **33** | — | — | — | 有 |
| 短视频创意 | **34** | — | — | — | 有 |

| 负例 | — | — | — | 14 / `_negative` | 有 |

**图例**：粗体 = 总工程关键交付编号。

### 互链规则

- plan README `seeAlso` → 同戏种 optimize / generation  
- optimize README 声明上游镜级字段  
- generation README 声明不消费 plan 的 MJ/SD 语法  
