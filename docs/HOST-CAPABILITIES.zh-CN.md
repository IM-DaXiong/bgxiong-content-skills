# 宿主能力边界

用途闭集以 `contracts/snapshots/agent-skill-hosts/agent-skill-hosts.json` 为准。`currentAuthoringHosts` 是现在可以新写的用途；`hosts` 里其余值是历史可读用途。

`clips-v1` 是应用当前执行策略。格式正确、用途历史可读、当前可执行，是三件不同的事。

技能不能授予新的模型、工具或权限，也不能改变应用的输出 schema。外部目录里的用途名称不会让一个旧工作流变成可执行。

快照来自主仓合同文件的副本。要改变闭集，先改主仓合同，再更新快照和 `source.json`。

## 使用已声明的图视频操作

通过 `canvas.models.list` 查找当前可选模型，再由 `canvas.model.describe` 读出所选模型的操作身份、参数和素材槽。适配器操作以包、版本、模型、操作版本和输入 schema 摘要归属本次配置。换模型或包版本后，应重新读取该操作的声明。用户已经保存的工作台配置可用 `canvas.workbench.read` 读回，生成时用原配置摘要调用已公开的 `canvas.image.submitRemembered` 或 `canvas.video.submitRemembered`。

提示词技能只提供创作内容。尺寸、时长、分辨率、素材数量和角色以当前操作声明为准。按需要读取准备结果和字段错误。成果沿原任务回执读取，任务续办继续使用原任务身份。
