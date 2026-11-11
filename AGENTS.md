# 作者与智能体规则

- **四仓平级与 SDK（用户2026-11-10）**：从同级主仓 `../bgxiong-ai-story` 定位同一开发根。四个 checkout 固定为 bgxiong-ai-story、bgxiong-third-party-adapters、bgxiong-adapter-sdk、bgxiong-content-skills。SDK 远程为 `https://github.com/IM-DaXiong/bgxiong-adapter-sdk.git`，2026-11-11 起公开，说明文档采用该仓根目录 LICENSE 的 MIT 许可。主程序按需求驱动 SDK 更新，默认同步最新并在本批固定输入。缺仓从登记远程克隆到准确目录，禁止替代真源。创作 Skill（含 H3）只在本仓治理，提交推送后按锁生成宿主副本。见[四仓规范](../bgxiong-ai-story/docs/dev/guides/20261107-GUIDE-三仓平级与创作Skill唯一治理目录.md)。

先读 `docs/SPECIFICATION.zh-CN.md`、`contracts/snapshots/` 里的宿主合同快照，以及 `docs/HOST-CAPABILITIES.zh-CN.md`。

- 只使用快照里的当前用途和 `clips-v1`。
- 不要发明工具、字段、权限、输出 schema 或宿主没有读取的布局键。
- 不要把技能正文写回应用业务代码，不要要求用户改安装目录。
- 讲解效果时区分设计用途和已经做过的样例。没有样例就写待制作。
- 所有技能按实际来源与当前合同统一校验，不按模型或包名禁止发行。H3 当前为项目自编兼容方法，与其余技能同等收录、修改和安装；不收录未获许可的第三方原文。
- 旧的 `skill.manifest.json`、`local.*` 和 pipeline 私有包只作为历史材料，不作为新技能模板。
