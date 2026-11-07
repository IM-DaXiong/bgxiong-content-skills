# -*- coding: utf-8 -*-
"""Generate catalog, explanation records, and skill pages from package bytes."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_lib import CURRENT_WORKFLOW, ROOT, host_tokens, load_hosts, load_skill, package_digest

HOST_EFFECT = {
    "multi-view": "按所选布局产出同一主体的多张参考图或一张合成参考图。槽位数量以该包 layout 的当前模式为准，不是固定视频帧数。",
    "image-photography-style": "整理可交给图片工作台的画面风格与取景建议，不直接生成图片。",
    "video-photography-style": "整理可交给视频工作台的镜头与画面建议，不直接生成视频。",
    "optimize-image-prompt": "在已有图片提示词上标出可改进处并给出修订稿，保留原稿。",
    "optimize-segment": "检查片段连续性或表演问题，并给出仍可执行的修订建议。",
    "video-prompt-projection": "把片段意图写成目标视频模型可阅读的提示词投影，不提交生成任务。",
    "postproduction-decoration": "为已有画面补充后期装饰或动效方法，不替换成片成片文件。",
    "story-chapters": "把故事材料整理成剧集章节结构。",
    "chapter-roles": "从章节材料整理角色条目。",
    "chapter-props": "从章节材料整理道具条目。",
    "story-entity-integration": "把分散的角色、场景和道具整理进同一套故事实体。",
    "episode-clip-plan": "按剧情行动规划有序片段，而不是按固定秒数切段。",
    "clip-environment-prompt": "为片段中的环境候选写普通图片提示词。",
    "clip-video-draft": "为单个片段写可独立提交的视频完整稿。",
    "clip-frame-plan": "为片段规划画面帧，不把规划本身当成已生成视频。",
    "clip-frame-prompt": "为已规划的画面帧写提示词。",
}


def headings(body: str) -> list[str]:
    found = []
    for line in body.splitlines():
        if line.startswith("## "):
            found.append(line[3:].strip())
    return found[:8]


def classify(meta: dict[str, str], kind: str, name: str) -> str:
    if name == "h3-prompt-writing":
        return "blocked"
    current, _historical = load_hosts()
    tokens = host_tokens(meta)
    workflow_ok = meta.get("bgx-workflow") == CURRENT_WORKFLOW
    hosts_ok = bool(tokens) and all(token in current for token in tokens)
    if kind == "builtin" and workflow_ok and hosts_ok:
        return "source-approved"
    if kind == "builtin":
        return "source-retained-not-current"
    if workflow_ok and hosts_ok:
        return "teaching"
    return "teaching-not-current"


def explanation(name: str, meta: dict[str, str], body: str, distribution: str, path: str) -> dict:
    tokens = host_tokens(meta)
    effects = [HOST_EFFECT.get(token, f"只在宿主用途 {token} 中使用。") for token in tokens] or [
        "未声明当前用途，不能当作当前可执行方法。"
    ]
    return {
        "name": name,
        "displayName": meta.get("bgx-display-name") or name,
        "packagePath": path,
        "version": meta.get("version") or None,
        "workflow": meta.get("bgx-workflow") or None,
        "hosts": tokens,
        "distribution": distribution,
        "scenario": meta.get("description", ""),
        "audience": "正在使用比格熊创作工作台、并选择了上述用途的作者。",
        "painPoints": headings(body) or ["见该包 SKILL.md 正文"],
        "intendedOutcome": effects,
        "observedEvidence": {
            "status": "not-run",
            "statement": "设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。",
        },
        "exampleStatus": "pending",
        "limits": [
            "不新增宿主工具、权限或输出 schema。",
            "缺少 clips-v1 或当前用途时，包可以阅读，当前执行不可用。",
            "效果没有量化承诺。",
        ],
        "download": None,
    }


def page(record: dict) -> str:
    evidence = record["observedEvidence"]["statement"]
    hosts = "、".join(record["hosts"]) or "（未声明）"
    outcomes = "\n".join(f"- {item}" for item in record["intendedOutcome"])
    pains = "\n".join(f"- {item}" for item in record["painPoints"])
    download = "没有公开安装包下载地址。源码页不是单包安装包。"
    if record["distribution"] == "blocked":
        install = "不提供安装步骤，也不进入案例目录。应用里可能仍有历史内置副本，那不是本仓库的再分发许可。"
    else:
        install = (
            f"在比格熊中使用目录或 ZIP 导入 `{record['packagePath']}`，预览后确认替换。"
            "单文件导入会丢掉 references 等附件，带布局的包不要只用单文件。"
        )
    return f"""# {record['displayName']}

状态：`{record['distribution']}`。版本：`{record['version']}`。工作流：`{record['workflow']}`。包目录：`{record['packagePath']}`。

## 用途

{record['scenario']}

## 适用场景

{record['audience']} 声明用途：{hosts}。

## 优化什么

{pains}

这些标题来自该包正文的章节，不是另一套执行规则。真正执行以包内 `SKILL.md` 为准。

## 输入

使用当前工作台已经提供的描述、选定素材和冻结参数。布局包还会读取自己的 `references/layout.json`。没有被该包声明的素材不是必需项。

## 输出

{outcomes}

## 可预期效果

{evidence}

## 安装与启用

{install}

## 示例

示例状态：待制作。没有前后对照，不能写成已经证明的提升。

## 限制

- 宿主只执行当前合同里存在的用途和 `clips-v1`。
- 本页不保证跨模型质量、身份完全一致或固定帧数。
- {download}
"""


def main() -> int:
    inventory = json.loads((ROOT / "docs" / "maintenance" / "import-inventory.json").read_text(encoding="utf-8"))
    descriptions = ROOT / "catalog" / "descriptions"
    descriptions.mkdir(parents=True, exist_ok=True)
    pages = ROOT / "docs" / "skills"
    pages.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list] = {}
    for item in inventory["packages"]:
        grouped.setdefault(item["name"], []).append(item)
    packages = []
    catalog_rows = []
    from skill_lib import parse_frontmatter

    for name, items in grouped.items():
        variants = []
        for item in items:
            if item["name"] == "h3-prompt-writing":
                host_skill = ROOT.parent / "bgxiong-ai-story" / item["sourcePath"] / "SKILL.md"
                meta, body = parse_frontmatter(host_skill.read_text(encoding="utf-8"))
                variants.append((item, meta, body, None, "blocked", item["sourcePath"]))
                continue
            if item.get("disposition") == "same-bytes-as-builtin":
                continue
            if not item.get("copiedTo"):
                continue
            package = ROOT / item["copiedTo"]
            meta, body, files = load_skill(package)
            distribution = classify(meta, "builtin" if item["kind"] == "builtin" else "fixture", name)
            variants.append((item, meta, body, files, distribution, item["copiedTo"]))
        if not variants:
            continue
        primary = variants[0]
        record = explanation(name, primary[1], primary[2], primary[4], primary[5])
        if len(variants) > 1:
            record["variants"] = [
                {
                    "path": item[5],
                    "distribution": item[4],
                    "scenario": item[1].get("description", ""),
                    "version": item[1].get("version"),
                }
                for item in variants
            ]
            record["scenario"] = record["scenario"] + " 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。"
        (descriptions / f"{name}.zh-CN.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (pages / f"{name}.zh-CN.md").write_text(page(record), encoding="utf-8")
        for item, meta, _body, files, distribution, path in variants:
            if files is not None and distribution == "source-approved":
                catalog_rows.append(
                    {
                        "name": name,
                        "version": meta.get("version"),
                        "path": path,
                        "packageDigest": package_digest(files),
                        "hosts": host_tokens(meta),
                        "workflow": meta.get("bgx-workflow"),
                        "distribution": distribution,
                        "rights": "project-license",
                    }
                )
        packages.append(record)
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "SkillExplanation",
        "type": "object",
        "required": ["name", "scenario", "intendedOutcome", "observedEvidence", "exampleStatus", "distribution"],
        "properties": {
            "name": {"type": "string"},
            "scenario": {"type": "string"},
            "intendedOutcome": {"type": "array"},
            "observedEvidence": {"type": "object"},
            "exampleStatus": {"enum": ["pending", "recorded"]},
            "distribution": {"type": "string"},
            "download": {"type": ["string", "null"]},
        },
    }
    (ROOT / "catalog" / "descriptions" / "schema.json").write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    (ROOT / "catalog" / "schema.json").write_text(
        json.dumps({"title": "PublicSkillCatalog", "required": ["packages"]}, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "catalog" / "packages.json").write_text(
        json.dumps({"packages": catalog_rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = ["# 技能详细说明索引", "", "页面由 `scripts/build_skill_docs.py` 生成。讲解事实来自各包正文和 `catalog/descriptions/`。", ""]
    for record in packages:
        lines.append(f"- [{record['displayName']}]({record['name']}.zh-CN.md)：{record['distribution']}。{record['scenario']}")
    (pages / "INDEX.zh-CN.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    begin = "<!-- BEGIN GENERATED SKILL CATALOG -->"
    end = "<!-- END GENERATED SKILL CATALOG -->"
    generated = [begin, "", "正式收录、教学变体和未发行项分开列出。下载链接在公开资产发布前保持为空。", ""]
    groups = {}
    for record in packages:
        groups.setdefault(record["distribution"], []).append(record)
    titles = {
        "source-approved": "当前可按 clips-v1 阅读的正式素材",
        "teaching": "教学变体",
        "teaching-not-current": "可导入阅读但当前执行未就绪",
        "source-retained-not-current": "保留素材但不是当前执行入口",
        "blocked": "不发行",
    }
    for key, title in titles.items():
        rows = groups.get(key, [])
        if not rows:
            continue
        generated.append(f"### {title}")
        generated.append("")
        for record in rows:
            generated.append(
                f"- **{record['displayName']}**（`{record['name']}`，{record['version'] or '无包内版本'}）：{record['scenario']} 详见 [说明](docs/skills/{record['name']}.zh-CN.md)。效果：{record['observedEvidence']['statement']}"
            )
        generated.append("")
    generated.append(end)
    block = "\n".join(generated) + "\n"
    if begin in text and end in text:
        text = text[: text.index(begin)] + block + text[text.index(end) + len(end) :]
    else:
        text = text.rstrip() + "\n\n" + block
    readme.write_text(text, encoding="utf-8")
    print(f"documented {len(packages)} packages; catalog {len(catalog_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
