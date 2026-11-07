# 宿主能力边界

用途闭集以 `contracts/snapshots/agent-skill-hosts/agent-skill-hosts.json` 为准。`currentAuthoringHosts` 是现在可以新写的用途；`hosts` 里其余值是历史可读用途。

`clips-v1` 是应用当前执行策略。格式正确、用途历史可读、当前可执行，是三件不同的事。

技能不能授予新的模型、工具或权限，也不能改变应用的输出 schema。外部目录里的用途名称不会让一个旧工作流变成可执行。

快照来自主仓合同文件的副本。要改变闭集，先改主仓合同，再更新快照和 `source.json`。
