# 宿主能力边界

用途闭集以 `contracts/snapshots/agent-skill-hosts/agent-skill-hosts.json` 为准。`currentAuthoringHosts` 是现在可以新写的用途；`hosts` 里其余值是历史可读用途。

`clips-v1` 是应用当前执行策略。格式正确、用途历史可读、当前可执行，是三件不同的事。

技能不能授予新的模型、工具或权限，也不能改变应用的输出 schema。外部目录里的用途名称不会让一个旧工作流变成可执行。

快照来自主仓合同文件的副本。要改变闭集，先改主仓合同，再更新快照和 `source.json`。

## 批量商品短视频

`batch-product-expand` 对单件商品规划创意，`batch-product-storyboard` 将同一件商品的方案拆成镜头。同一 clips-v1 包可以声明两个用途，按本次阶段工作。需要含这两项用途的宿主和已启用的包。生成任务由外挂调度。

## 使用已声明的图视频操作

从运行中应用用 `capabilities.get` 的 `schemaToolIds` 读取所需工具的入参合同。连接方式和完整示例见应用随附的 Creator 客户端手册，也可通过 MCP `resources/read` 读取 `bgxiong-creator://docs/handbook/zh-CN`。

1. 调用 `canvas.models.list` 获取候选，使用返回的 `bindingId` 和 `modelId` 调用 `canvas.model.describe`。对于返回了完整操作声明的适配器模型，从 `capabilities.imageExtensions.adapterV2` 或 `capabilities.videoExtensions.adapterV2` 读取 `selection` 和 `operationInput`。声明给出 schema、控件和素材槽。换模型或包版本后重新读取。
2. 用 `workspaceKind`、`workspaceId` 和 `nodeId` 调用 `canvas.workbench.read`。只在用户要求修改配置时，用 `canvas.configuration.change.prepare` 准备 `configuration.patch`，把刚读到的 `configurationRevision` 作为 `expectedConfigurationRevision`。将返回的 `changeSetId` 交给 `change.apply`，再读回配置。保存配置和生成是独立的动作。
3. 声明型参数写入 `changes` 中的 `parameters.patch`。把读到的完整 `selection` 原样作为 `adapterSelection`，把本次参数草稿作为 `operationInput`。该字段整体替换所选操作的草稿，需一起提交本次要保留的字段，按声明保留对象、数组顺序、小数和零值。已明确支持旧标量参数的操作使用 `adapterParameters` 和声明的 JSON Pointer。每个参数动作只使用所属操作对应的参数形式。
4. 用户授权生成后，重新调用 `canvas.workbench.read` 核对实际提交投影和缺项。把此时的 `configDigest` 作为 `expectedConfigDigest` 传给 `canvas.image.submitRemembered` 或 `canvas.video.submitRemembered`。仅视频提交允许其运行时 schema 公布的时长或分辨率覆盖，取值遵循当前工作台约束。结果用原回执的 `jobId` 作为 `task.get` 的 `taskId` 查询。

下面是已选模型的参数保存示例。将返回的 `workbench.configurationRevision`、`adapter.selection` 和按实际声明整理的 `draftValues` 组装为 `canvas.configuration.change.prepare` 参数。这里的 `target` 只含节点的 `workspaceKind`、`workspaceId` 和 `nodeId`。

```javascript
const prepareArgs = {
  actions: [{
    actionId: "save-operation-input",
    type: "configuration.patch",
    request: {
      ...target,
      expectedConfigurationRevision: workbench.configurationRevision,
      changes: [{
        type: "parameters.patch",
        adapterSelection: adapter.selection,
        operationInput: draftValues
      }]
    }
  }]
};
```

提示词文本和画布素材选择各走其公开入口。尺寸、时长、分辨率、素材数量和角色以当前操作实际返回的声明为准。缺少所需声明时，报告当前入口缺项。字段被拒绝时按回执的字段路径校对原输入。
