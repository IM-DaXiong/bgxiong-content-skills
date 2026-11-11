# H3-Image 图片提示词 1.0.0 应用实测

2026-11-11。本文补充 1.0.0 冻结包和自动生成说明发布时的待验状态，不改写包内方法或同版本字节。

[可导入 ZIP 与 SHA256](https://github.com/IM-DaXiong/bgxiong-content-skills/releases/tag/h3-image-prompt-writing-v1.0.0)。ZIP SHA256 `9e4b967eba2a6245c97c47ccae915ef538ef57aacadca847e047d4cc3b7a6f22`，已从公开链接重新下载核对。

应用 0.6.1112 实际安装后可在图片工作台的“优化助手”选择“H3-Image 图片提示词”。使用配置中的 MiniMax-M3 和两张参考图，经过应用真实优化执行器保存并激活提示词版本。普通开发数据环境已通过现有登录会话安装，available/enabled 均为 true。

同两张输入、同顺序、2048×2048、seed 20261111，对比“只把底图白杯改为图2蓝色”的原始中文指令与一次生成的英文 Picture/Subject 指令，两张都达成目标。优化图杯沿较浅蓝、杯身颜色/高光有细微差别；没有证据宣称稳定质量提升。模型返回还存在冗余背景复述和 matte/glaze 表述张力，应保留原稿供选择，不把更长提示词当作必然更好。

原词图 SHA256 `402b4aead68c79cd8a6e6b4a228c164fe2a685103a3d2eaec3bcc2cb8e13334d`；优化图 SHA256 `50acecae507436a5129a2790f3f3b7e5751fac3b4022ad023f5a0a15b8efc40a`。样例图和完整回执在主仓本机 logs/h3-image-app-live-20261111，未作为公开素材发行。源正文为项目自编兼容方法；官方受限原文未复制分发。
