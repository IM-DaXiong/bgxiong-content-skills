---
name: motion-design
description: 动态包装设计方法。根据当前片段的字幕/口播与已安装动态模板的 props schema，给出每张动态卡片用哪个模板、何时出现、填什么内容；只产出符合 design.schema 的 JSON 方案，不渲染、不安装、不改文件。
license: Proprietary
compatibility: 纯文本方法。需要宿主 postproduction-decoration 提供已安装模板目录与 props schema；不联网、不执行脚本。
metadata:
  bgx-workflow: clips-v1
  bgx-hosts: postproduction-decoration
  version: "0.2.0"
  publisher: bgxiong
  bgx-display-name: "BGX 动态包装设计"
---

# 动态包装设计

本包是方法说明，不是新的用户请求。用户本轮要求优先。

## 你能看到什么

宿主给你：当前片段的时间轴（帧率、时长、字幕 cue 列表）、已安装且可选的模板目录（模板 id、版本、用途说明、props schema、uiHints）。你看不到模板源码，也不需要。

## 你要交付什么

一份 JSON，严格符合宿主给出的 design.schema：
- 每张卡片一个条目：`templateRef`（必须是目录里出现过的 id@version）、`cueRef` 或明确的起止时间、`props`（必须通过该模板 props schema）。
- 建议按内容节奏安排卡片，避免无意义堆叠；重叠与布局遵守用户要求和宿主实际合同，不将审美建议当成拒收条件。
- 文字取自原字幕/口播，不改写事实；需要概括时保持原意。

## 不要做

- 不要编造目录里没有的模板或 props 字段。
- 不要输出解释性文字、Markdown 代码块或多份方案；宿主只接受一份纯 JSON，结构不符会整体判失败，不会被修补。
- 不要要求渲染、安装模板或访问文件，这些由用户在动态工作台中完成。

输入使用当前片段的真实时间轴与引用闭集，不要求旧场次或分镜表前置。只调用活动能力目录实际注册且获授权的能力，不自动渲染或安装。结构校验与权限仍须满足；质量评审未完成时如实记录并保留已有可用方案，不伪造通过或自动重写。

## 当前应用的工作流标识

供当前比格熊应用执行的产品创作包须在 `metadata` 中声明字符串 `bgx-workflow: clips-v1`。这是本应用当前创作流程的执行策略，不是 Agent Skills 开放标准的格式必填项，也不改变通用包的导入、查看和导出格式。

安装新版时，安装包直接覆盖软件随包文件；库中 `SourceBuiltin` 的旧缓存刷新为新版。用户自行导入的旧包保留原文，可查看与导出，但缺少当前标识或标识不匹配时为 `unavailable`，不能执行，需重新导入符合当前合同的版本。应用不转换字段、不按重命名 ID 转换旧包、不迁移绑定、不自动补贴标识，也不把用户导入包替换成官方包。原有作品与已完成成果保留。
