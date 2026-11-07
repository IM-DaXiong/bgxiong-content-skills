# 标准技能包

当前可安装格式是目录或 ZIP，根上有 `SKILL.md`。需要附件时使用 `references/` 等相对路径。单文件只适合没有附件的方法。

`SKILL.md` 开头是 YAML frontmatter：

- `name`：与目录名相同，小写字母、数字和连字符。
- `description`：给人和目录看的用途说明。
- `metadata.bgx-hosts`：空格分隔的用途，必须来自宿主合同快照。
- `metadata.bgx-workflow`：当前执行写 `clips-v1`。这不是开放技能格式的必填项；缺少它时应用仍可导入，但当前执行不可用。
- `metadata.version`：自有发行包使用 `MAJOR.MINOR.PATCH`。
- `metadata.bgx-display-name`：可选的展示名。

正文写方法。机器真正读取的布局放在 `references/layout.json`，不要在讲解页再写一套会改变执行的规则。

包摘要按应用合同 `bgx-agent-skill-digest-v1` 计算，包含包内全部普通文件。给用户看的长说明放在本仓库 `docs/skills/`，不要为了写说明去改已经发布的包字节。若说明必须放进包内，先提高 `metadata.version`，再重新计算摘要。

旧格式要求 `skill.manifest.json` 和 `local.*` 标识。那是本仓库的历史材料，不是新技能的默认写法。
