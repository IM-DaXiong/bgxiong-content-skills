# AUTHORING_PROMPT_PACK.zh-CN

把本文件整份复制给其它 LLM，让它为「比格熊数字导演」生成 content-skill-v1.1 包。

## 你的角色

你为「比格熊数字导演」生成 **content-skill-v1.1.0** 声明式包。只输出可导入文件，不写客户端源码。协议 `content-skill-v1` / `1.1.0`。Skill 的本质是 **LLM 返回格式 SSOT**（outputSchema），不是一段风格形容词。

## 用户会提供的输入

题材、场次用途（武打/文戏）、镜数、角度/景别/运镜词表偏好、每镜字数、是否只要场次不要分镜。

## 你必须输出的文件

目录树 + 完整文件内容：

- `skill.manifest.json`（id 必须以 `local.` 开头）
- `pipeline.json`（bind + directives + outputSchema；禁止 `input`）
- `README.md`（必须含：这个 Skill 控制 LLM 返回什么格式 / 字段表 / 你可以改什么 / 用户怎么用 / 不合格时你会看到什么 / 拷给其它 LLM 时如何改成自己的包）
- 若做分镜优化：`optimize-storyboard-shot.json`（emptyPolicy.forbidHostFabrication=true）

## 硬约束摘录

- 公开 op 仅：plan_bible, plan_chapters, plan_roles, plan_scenes, plan_shots, plan_package
- `plan_shots` 必须有非空 `outputSchema.shots`，否则拒装 `CONTENT_SKILL_OUTPUT_SCHEMA_REQUIRED`
- 禁止 `steps[].input`
- 禁止解冻 plan_image；禁止把 generation-policy 写成 plan_shots
- bind 只允许 `$ctx.storyId|sourceText|sceneNodeId|chapterNodeId|writeMode|anchor`
- prose.budget 必须与 schema minLength/maxLength 一致
- 一场 6 镜：`shots.count.const=6` 且编译后 minItems=maxItems=6
- 自定义字段只能进 skillExtension，不得覆盖核心键

## 两个完整范例

### 范例 A · 固定 6 镜武打

```json
{
  "id": "shots",
  "op": "plan_shots",
  "bind": { "storyId": "$ctx.storyId", "sceneNodeId": "$ctx.sceneNodeId", "sourceText": "$ctx.sourceText" },
  "directives": { "prose": { "style": { "mode": "authorText", "text": "武打：动作因果清晰。" }, "budget": { "unit": "chars", "perShot": { "min": 40, "max": 160 } } } },
  "outputSchema": {
    "shots": {
      "count": { "const": 6 },
      "item": {
        "required": ["shotIndex", "content", "angleId", "shotSize", "cameraMove", "fightBeat"],
        "properties": {
          "shotIndex": { "type": "integer", "minimum": 1, "maximum": 6 },
          "content": { "type": "string", "minLength": 40, "maxLength": 160 },
          "angleId": { "enum": ["wide", "low", "high", "medium"] },
          "shotSize": { "enum": ["EWS", "WS", "MS", "CU", "ECU"] },
          "cameraMove": { "enum": ["handheld", "dolly_in", "pan", "static"] },
          "fightBeat": { "type": "string", "maxLength": 80 }
        }
      }
    }
  }
}
```

### 范例 B · 微表情文戏

```json
{
  "id": "shots",
  "op": "plan_shots",
  "bind": { "storyId": "$ctx.storyId", "sceneNodeId": "$ctx.sceneNodeId", "sourceText": "$ctx.sourceText" },
  "outputSchema": {
    "shots": {
      "count": { "const": 6 },
      "item": {
        "required": ["shotIndex", "content", "angleId", "shotSize", "cameraMove", "faceBeat"],
        "properties": {
          "shotIndex": { "type": "integer", "minimum": 1, "maximum": 6 },
          "content": { "type": "string", "minLength": 40, "maxLength": 160 },
          "angleId": { "enum": ["closeup", "medium"] },
          "shotSize": { "enum": ["CU", "ECU"] },
          "cameraMove": { "enum": ["static"] },
          "faceBeat": { "type": "string", "maxLength": 80 }
        }
      }
    }
  }
}
```

优化容错范例：`emptyPolicy.ifContextFieldEmpty=omitFromPrompt`，空对白不要编造台词。

## 自检清单

- [ ] id 前缀 `local.`
- [ ] shots 有 outputSchema
- [ ] count 与 min/maxItems 一致
- [ ] 无未知字段、无 steps[].input
- [ ] README 含「能做/不能做/按钮」六段标题
- [ ] 未把 generation-policy 写成 plan_shots
- [ ] 中英文件名不混排协议

## 禁止

编造未文档化的 $ctx；解冻 plan_image；把 generation-policy 写成 plan_shots；中英混文件名协议；未绑场次指望入口 Skill 顶上。
