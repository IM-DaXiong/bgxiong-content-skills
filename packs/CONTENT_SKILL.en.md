# Content Skill Package Contract (content-skill-v1)

> **Project external author standard (English)**  
> For people who write or import Content Skills.  
> 中文: [`CONTENT_SKILL.zh-CN.md`](CONTENT_SKILL.zh-CN.md)

## What it is

A Content Skill is an **importable creative orchestration package**: without changing client source, you declare what to plan and in what order, then run it in the app to produce chapters / scenes / shots, etc.

A **generation-policy Skill** does not click Generate for you; it replaces multi-view slot copy or storyboard still style lines.

## Where to look

| Material | Location |
|----------|----------|
| This doc (EN) | Install dir `user-examples/content-skills/CONTENT_SKILL.en.md` (repo: `fixtures/content-skills/local-samples/`) |
| Chinese | `CONTENT_SKILL.zh-CN.md` |
| Importable samples | Same folder `01-…`–`14-…` (see `README.md`) |
| Machine closed sets | `packages/app-contracts/v1/content-skill-*.json` |
| Tooling | Repo `tools/content-skill/` |

## End-user path

1. Settings → **Content Skills** → **Import package** (folder or zip). On installed builds, copy a sample from `user-examples/content-skills/` to a writable folder first.
2. Import success = package on disk (**L1**), not content yet.
3. Open **Generate chapters** or **One-click screenplay**, pick the Skill as orchestration, confirm the plan (**L2**), then run (**L3**).
4. User package `id` must start with `local.`. `official.*` fixtures are rejected on import.

## Package layout

```
<skill-dir>/
  skill.manifest.json     # required
  pipeline.json           # required
  pack-pin.json           # required after install (tooling can generate)
  produce-plan.component.wasm  # optional
  generation-policy.json  # required when generation.policy capability is claimed
  README.md               # optional
```

### `skill.manifest.json`

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | User packages must use `local.` prefix |
| `version` | yes | semver; reinstall same id = overwrite |
| `protocol` | yes | Must be `content-skill-v1` |
| `displayName` / `description` | no | Management UI |
| `entry` | no | Defaults to `pipeline.json` |

### `pipeline.json`

| Field | Required | Meaning |
|-------|----------|---------|
| `steps` | yes | Non-empty step list |
| `steps[].id` | yes | Unique in package |
| `steps[].op` | yes | Public op only (below) |
| `steps[].dependsOn` | no | Prior step ids; no cycles |
| `steps[].when` | no | Keep step only if predicate holds |
| `coverage` | no | Artifact layers; default derived from steps. Do not hand-write coverage that conflicts with `when` skips |

### Public ops (allowed in user packages)

| op | Purpose |
|----|---------|
| `plan_bible` | Story bible |
| `plan_chapters` | Chapters |
| `plan_roles` | Roles |
| `plan_scenes` | Scenes (usually after chapters) |
| `plan_shots` | Shots (usually after scenes) |
| `plan_package` | Package layer |

Do not use internal ops such as `materialize_*`, `assemble_package`, `plan_appearance`, `plan_continuity`. `plan_image` may appear in contracts but is not release-available — do not treat it as generate-ready.

### `when` predicates

`exists` / `notEmpty` / `equals` / `count`. v1 prepare context is mainly `$ctx.storyId`, `$ctx.sourceText`.

### `pack-pin.json`

Pins raw SHA-256 of `pipeline.json` (and wasm when present). Mismatch → hard reject on import/load.

## Generation-policy Skills

Optional `generation-policy.json` with `generation.policy` capability.  
A generation-policy Skill does **not** click Generate for you. It replaces multi-view slot copy, optional sheet layout for single-image composition, or storyboard still style lines.  
Samples: `10-generation-policy-*` … `13-…`; `14-…` is an intentional invalid negative sample; `15-generation-policy-expression-9grid` is an expression sheet (9 views, optional single-image 3×3).

## Hard rules

1. If a selected Skill fails, the app will **not** silently fall back to built-in orchestration.
2. L1 import ≠ L2 plan OK ≠ L3 content produced.
3. Sample folders are specimens; the field standard is this doc + contract JSON.

## Suggested start

Copy `01-chapters-only`, change `id` (keep `local.`), `displayName`, and `pipeline.json`, import, then select it under Generate chapters. Move to `02` / `03` when ready.
