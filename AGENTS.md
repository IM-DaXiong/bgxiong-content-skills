# 作者与智能体规则

- **SDK 联动开发（用户2026-11-10）**：主程序提出需求后在同级 SDK 仓改公共协议/内核，主程序默认同步最新 SDK 并联合验证。依赖锁记录本批实际提交与产物，不是长期固定旧版的门槛；同步/构建失败不得静默回退。只做内容 Skill 的任务不因此扩成 SDK 编译或功能改造；冻结任务身份不随开发依赖更新改写。

- **四仓平级唯一治理规范（用户2026-11-10）**：先定位同级主仓 `../bgxiong-ai-story` 的实际 Git 根 H，以 `parent(H)` 为准，四个目录固定为 `bgxiong-ai-story`、`bgxiong-third-party-adapters`、`bgxiong-adapter-sdk`、`bgxiong-content-skills`，不写死盘符、不嵌套或另设真源。缺仓从 `https://github.com/IM-DaXiong/` 下对应 Git 仓 clone 到准确同级目录；主仓远程名为 `bgxiong-ai-story-dev.git`，另三仓远程名与目录名相同。目标占用或远程不可达时保留现场报阻断，不建空目录冒充；SDK 远程在本轮尚未确认可达，迁移待实施。先读各仓 AGENTS.md 与主仓[唯一规范正文](../bgxiong-ai-story/docs/dev/guides/20261107-GUIDE-三仓平级与创作Skill唯一治理目录.md)。全部产品 Skill（含 H3）只在本仓治理，提交推送后主仓按锁同步；SDK 拉新后须构建验证并记录主仓实际消费身份。

先读 `docs/SPECIFICATION.zh-CN.md`、`contracts/snapshots/` 里的宿主合同快照，以及 `docs/HOST-CAPABILITIES.zh-CN.md`。

- 只使用快照里的当前用途和 `clips-v1`。
- 不要发明工具、字段、权限、输出 schema 或宿主没有读取的布局键。
- 不要把技能正文写回应用业务代码，不要要求用户改安装目录。
- 讲解效果时区分设计用途和已经做过的样例。没有样例就写待制作。
- 所有技能按实际来源与当前合同统一校验，不按模型或包名禁止发行。H3 当前为项目自编兼容方法，与其余技能同等收录、修改和安装；不收录未获许可的第三方原文。
- 旧的 `skill.manifest.json`、`local.*` 和 pipeline 私有包只作为历史材料，不作为新技能模板。
