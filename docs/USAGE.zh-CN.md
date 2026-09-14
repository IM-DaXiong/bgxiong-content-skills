# 用法（导入到比格熊数字导演工作站）

本仓库的 Skills **不是**独立可运行程序，需要导入 [比格熊数字导演工作站](https://www.bgxiong.com) 后由 Host 执行。

## 步骤

1. 从官网安装客户端：[https://www.bgxiong.com](https://www.bgxiong.com)
2. 打开 **设置 → 创作 Skills**
3. 导入 `examples/` 下某个完整包目录（含 `skill.manifest.json`）
4. 在分镜 / 优化提示词 / 生图策略相关入口选用该 Skill

## 推荐先试

| 包 | 能力 |
|----|------|
| `examples/content-plan/28-storyboard-performance` | `content.plan` + `optimize.storyboard_shot` |
| `examples/optimize/30-optimize-storyboard-fight` | `optimize.storyboard_shot`（武打） |
| `examples/optimize/31-optimize-storyboard-micro-cu` | `optimize.storyboard_shot`（微表情特写） |
| `examples/optimize/32-optimize-segment-continuity` | `optimize.segment` |
| `examples/generation-policy/15-generation-policy-expression-9grid` | `generation.policy` |

## 校验

```bash
python scripts/validate-example.py examples/.../<pack>
```

详见根目录 [README.md](../README.md)。
