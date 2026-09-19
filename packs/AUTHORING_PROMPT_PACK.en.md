# AUTHORING_PROMPT_PACK.en

Copy this entire file to another LLM to generate a content-skill-v1.1 pack for BigBear Digital Director.

## Your role

You generate **content-skill-v1.1.0** declarative packs for BigBear Digital Director. Output importable files only. Protocol `content-skill-v1` / `1.1.0`. A Skill is the **LLM return-format SSOT** (outputSchema), not a pile of style adjectives.

## User input you will receive

Genre, scene use (fight / drama), shot count, preferred angle/size/move vocab, per-shot length, whether to stop at scenes.

## Files you must output

A directory tree plus full file bodies:

- `skill.manifest.json` (id must start with `local.`)
- `pipeline.json` (bind + directives + outputSchema; never `input`)
- `README.md` (must include: what format the LLM returns / field table / what you may change / how users run it / what failure looks like / how to fork for another LLM)
- Optional `optimize-storyboard-shot.json` with `emptyPolicy.forbidHostFabrication=true`

## Hard constraints excerpt

- Public ops only: plan_bible, plan_chapters, plan_roles, plan_scenes, plan_shots, plan_package
- `plan_shots` must have non-empty `outputSchema.shots` or install fails with `CONTENT_SKILL_OUTPUT_SCHEMA_REQUIRED`
- No `steps[].input`
- Do not unfreeze plan_image; do not write generation-policy as plan_shots
- bind may only use `$ctx.storyId|sourceText|sceneNodeId|chapterNodeId|writeMode|anchor`
- prose.budget must match schema minLength/maxLength
- Six shots: `shots.count.const=6` and compiled minItems=maxItems=6
- Custom fields only in skillExtension; never overwrite core keys

## Two complete examples

### Example A — fixed 6-shot fight

```json
{
  "id": "shots",
  "op": "plan_shots",
  "bind": { "storyId": "$ctx.storyId", "sceneNodeId": "$ctx.sceneNodeId", "sourceText": "$ctx.sourceText" },
  "directives": { "prose": { "style": { "mode": "authorText", "text": "Fight: clear action causality." }, "budget": { "unit": "chars", "perShot": { "min": 40, "max": 160 } } } },
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

### Example B — micro-expression drama

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

Empty-context example: `emptyPolicy.ifContextFieldEmpty=omitFromPrompt`. Never fabricate dialogue.

## Self-check

- [ ] id prefix `local.`
- [ ] shots have outputSchema
- [ ] count matches min/maxItems
- [ ] no unknown fields, no steps[].input
- [ ] README has the six required headings
- [ ] generation-policy not written as plan_shots
- [ ] no mixed zh/en protocol filenames

## Forbidden

Invent undocumented `$ctx`; unfreeze plan_image; write generation-policy as plan_shots; mix zh/en protocol names; cover unbound scenes with the entry Skill.
