# AUTHORING_SPEC.en — Content Skill 1.1.0

For authors and other LLMs. Machine contract: `packages/app-contracts/v1/content-skill-*.json`. Fixed `protocolId=content-skill-v1`, `protocolVersion=1.1.0` (window min=max=1.1.0).

Each section: meaning / type / required / mutable range / illegal / legal.

## 1. Pack manifest and skill.manifest.json

| Field | Meaning | Type | Required | Mutable range | Illegal | Legal |
|------|---------|------|----------|---------------|---------|-------|
| id | Install identity | string | yes | must start with `local.` | `official.foo` | `local.wuxia.fight` |
| version | Version | semver | yes | bump yourself | empty | `1.1.0` |
| protocol | Protocol family | string | yes | only `content-skill-v1` | `content-skill-v2` | `content-skill-v1` |
| protocolVersion | Protocol version | string | recommended | only `1.1.0` | dual-stack `1.0.0` | `1.1.0` |
| capabilities | Caps | string[] | content packs use `content.plan` | do not bind `generation.policy` as storyboard | policy-only on shot bind | `["content.plan"]` |

## 2. pipeline.json step graph

| Field | Meaning | Type | Required | Mutable range | Illegal | Legal |
|------|---------|------|----------|---------------|---------|-------|
| id | Step name | string | yes | unique in pack | duplicate ids | `"shots"` |
| op | Public op | string | yes | plan_bible/chapters/roles/scenes/shots/package | treating `plan_image` as live | `plan_shots` |
| dependsOn | Prerequisites | string[] | no | no cycles | coverage mismatch after `when` | `["scenes"]` |
| when | Predicate | object | no | exists/notEmpty/equals/count | invented `$ctx` paths | `{ "notEmpty": "$ctx.sourceText" }` |

`steps[].input` is removed in 1.1.0.

## 3. bind

Allowed `$ctx.storyId` / `$ctx.sourceText` / `$ctx.sceneNodeId` / `$ctx.chapterNodeId` / `$ctx.writeMode` / `$ctx.anchor`. Do not invent `$ctx.weather`.

| Field | Meaning | Type | Required | Mutable range | Illegal | Legal |
|------|---------|------|----------|---------------|---------|-------|
| storyId | Current story | template | recommended | only `$ctx.storyId` | hardcoded `"s1"` | `"$ctx.storyId"` |
| sceneNodeId | Current scene | template | storyboard-on-scene | only `$ctx.sceneNodeId` | entry skill covering unbound scenes | `"$ctx.sceneNodeId"` |

## 4. directives

| Field | Meaning | Type | Required | Mutable range | Illegal | Legal |
|------|---------|------|----------|---------------|---------|-------|
| prose.style.text | Prose style | string | no | natural language | using literaryMode as style | `"clear fight causality"` |
| prose.budget.perShot | Per-shot length | {min,max} | no | must match schema minLength/maxLength | budget 40-160 vs maxLength 2000 | aligned 40-160 |
| structure.maxChapters | Max chapters | number | no | positive int | negative | `8` |

literaryMode is a host hint, not prose.style.

## 5. outputSchema (primary contract)

Shots packs without `outputSchema.shots` **refuse install**.

| Field | Meaning | Type | Required | Mutable range | Illegal | Legal |
|------|---------|------|----------|---------------|---------|-------|
| shots.count.const | Fixed shot count | integer | use 6 for six shots | must match minItems=maxItems | const=6 and maxItems=8 | `{ "const": 6 }` |
| item.required | Per-shot required | string[] | include content/angleId/shotSize/cameraMove | Host must not add hidden required | empty required hoping official columns | sample 21 |
| content | Visual beat | string | common | minLength/maxLength | remote `$ref` | string 40-160 |
| angleId / shotSize / cameraMove | Camera fields | enum or string | prefer enum | closed vocab | HTML/script | `"enum":["CU","ECU"]` |

Core fields project to canonical shots; custom fields only go to bounded `skillExtension`.

## 6. Scene binding

Story-entry planning is not scene storyboard. Scene workbench may bind `sceneNodeId → skillId+planHash` to override the official format. Unbound uses official `native.content.plan`. Never cover with the entry Skill. `generation.policy` packs cannot bind here.

## 7. Repair and user decision

Host retries **exactly once** with the same schema. Still invalid: `ai_task` terminal failed, run=`awaiting_user_decision`, payload in a decision draft. User saves draft to edit or discards. Authors must not expect Host to loosen schema.

## 8. Boundary vs generation.policy

Image policy only replaces multi-view slots / style overlay. It does not unfreeze `plan_image` and is not a storyboard Skill.

## 9. Optimize files (optional)

`optimize-storyboard-shot.json` / `optimize-segment.json`: capability + outputSchema + emptyPolicy. `forbidHostFabrication` must be true. Empty dialogue is omitted; Host must not fabricate.
