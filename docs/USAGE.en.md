# Usage (import into BGXiong Digital Director)

Skills in this repo are **not** a standalone runtime. Import them into the [BGXiong Digital Director](https://www.bgxiong.com) desktop app; the product Host executes them.

## Steps

1. Download the client: [https://www.bgxiong.com](https://www.bgxiong.com)
2. Open **Settings → Content Skills** (label may vary by build)
3. Import one full pack folder under `examples/` (must include `skill.manifest.json`)
4. Select the Skill in storyboard / optimize / generation-policy flows

## Validate

```bash
python scripts/validate-example.py examples/.../<pack>
```

See the root [README.md](../README.md) for purpose, ABS rules, and product footer.
