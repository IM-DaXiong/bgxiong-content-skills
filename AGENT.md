# AGENT.md — 为智能体写 Content Skill 包

## 目标

产出可导入 Host 的目录树；禁止发明 Host API、禁止扩 capabilities 闭集外字符串。

## 合同入口

1. `contracts/v1/content-skill-capabilities.json` — 闭集  
2. `contracts/v1/content-skill-*.json` — 包协议  
3. `packs/AUTHORING_PROMPT_PACK.*.md` / `CONTENT_SKILL.*.md` — 人读+生成约束  

## 生成步骤

1. 选能力：`content.plan` | `generation.policy` | `optimize.storyboard_shot` | `optimize.segment`  
2. 建目录：`examples/<bucket>/<nn>-<slug>/`  
3. 写 `skill.manifest.json`：`id` 必须以 `local.` 开头；`capabilities` ⊆ 闭集  
4. 按能力写文件：  
   - plan → `pipeline.json`  
   - generation → `generation-policy.json`  
   - optimize.shot → `optimize-storyboard-shot.json`（`outputSchema` 非空；建议 `forbidHostFabrication=true`）  
   - optimize.segment → `optimize-segment.json`  
5. 写 `README.md`（用途/导入/可改字段/非法改法/SOURCES）  
6. 更新 `docs/CASE-MATRIX.md`  
7. 跑 `python scripts/validate-example.py <pack-dir>`  

## 禁改

- 勿改 `contracts/` 语义后要求 Host 跟随  
- 勿写入产品仓路径或回写脚本  
- 勿提交专有 IP 名、大段抄袭原文  

## 验收清单

- [ ] validate 绿  
- [ ] README + SOURCES  
- [ ] CASE-MATRIX 有行  
- [ ] capabilities 闭集内  
