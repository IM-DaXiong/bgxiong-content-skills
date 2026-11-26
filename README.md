## H3 multi-reference content 1.0.0

[Download ZIP and SHA256](https://github.com/IM-DaXiong/bgxiong-content-skills/releases/tag/h3-multi-reference-content-v1.0.0). Published archive was downloaded without credentials and matched all package files. Format and reproducible packaging checks passed; application installation and real model execution remain unverified.

## H3-Image 图片提示词下载与实测

[1.0.0 ZIP / SHA256](https://github.com/IM-DaXiong/bgxiong-content-skills/releases/tag/h3-image-prompt-writing-v1.0.0) · [应用实测与 A/B 结论](docs/skills/h3-image-prompt-writing-20261111-acceptance.md)。已安装并通过真实优化调用；本例未证明稳定质量提升。

# 比格熊创作技能

比格熊官网 [www.bgxiong.com](https://www.bgxiong.com)｜微信公众号：天途影像｜[比格熊开发治理 Skill](https://www.bgxiong.com/goods/9p65SRB2Sl)

本仓库是创作技能正文的可编辑源。比格熊数字导演工作站负责安装、权限、用途闭集和执行。这里不能新增宿主能力。

许可是仓库根 `LICENSE` 的自定义许可：可以学习，也可以在自有项目中使用；不能把这些材料单独做成付费技能包出售。这不是 OSI 开源许可证。

## 最新更新 · 武戏分镜与静帧

- **武戏片段分镜规划 1.2.0** 用于生成片段稿。根据剧情选择交手、错身、停手或反应，机位与剪辑跟随这一镜需要交代的信息。人物造型和道具沿用已绑定素材。[技能说明](docs/skills/action-clip-storyboard-planning.zh-CN.md)
- **武戏片段静帧设计 1.2.0** 用于镜帧规划与图片提示词。同一时刻提供 35 mm 腰高侧拍和 85 mm 过肩近景两例，可分别突出人物间距与即时反应。[技能说明](docs/skills/action-clip-keyframe-design.zh-CN.md)

在工作站「设置 → 创作 → 技能更新」检查更新，也可下载 ZIP 手动导入。[安装包](https://github.com/IM-DaXiong/bgxiong-content-skills/releases/tag/action-clip-methods-20261126)

## 先读什么

1. [规范](docs/SPECIFICATION.zh-CN.md)
2. [从零写一个技能](docs/CREATE-FROM-SCRATCH.zh-CN.md)
3. [修改已有技能](docs/EDIT-EXISTING.zh-CN.md)
4. [技能目录](docs/skills/INDEX.zh-CN.md)

`skills/` 是从应用内置包原样收下的正式素材。`examples/teaching/` 只保留和正式包字节不同的教学变体。`packs/`、`examples/content-plan/`、`examples/generation-policy/`、`examples/optimize/` 和旧的 `contracts/v1/` 是历史私有包格式，不再是当前安装格式。

当前产品执行标识是 `metadata.bgx-workflow: clips-v1`。只有具有该标识并通过宿主兼容性校验的包可以执行。官方在线目录由本仓库按当前内容目录签名发行，客户端负责检查和安装。 [正式在线目录](https://r.bgxiong.com/client/ai-story/bgxiong-content-skills/latest.json)

## 官方 Skills CDN 上传

本地上传目录为统一交付根下的 `cdn-bgxiong-content-skills/`。目录平铺全部 ZIP、正式签名 `latest.json` 和 `SHA256SUMS.txt`。在 SFTP 打开 `/var/www/r.bgxiong.com/client/ai-story/bgxiong-content-skills/`，把本地上传目录内的文件一起拖进去。上传工具可调整顺序时，把 `latest.json` 放在队尾。全部传完后，从公网读回索引，并在「设置 → 创作 → 技能更新」点「检查更新」。

2026-11-26 已发布序号 5，含 19 个包，宿主范围为 `>=0.6.1123, <0.7.0`。已从公网回读签名索引和全部 ZIP。索引 SHA-256 为 `b66cfbb9a7466724985c69742043ade3fa1c4a3e45642502b7258e599a294e8b`。

`scripts/publish_online_index.py` 复用标准包构建器，只接收 `source-approved` 的包。使用 `--prior-commit` 登记已核对的历史来源指纹，使用 `--signing-host` 和 `--public-trust` 在服务器完成签名并验证回执。CDN 源站用 `scripts/publish_online_cdn.py` 校验签名，先发布并回读不可变 ZIP，再更新并回读目录。正式首发序号为 1，兼容 `=0.6.1119`，已回读 16 个 ZIP，目录 SHA-256 为 `2030593f86e50474be9cdd4c1b6f24ead0696ff66155fd9d86b0bdc27bfc7ac3`。

<!-- BEGIN GENERATED SKILL CATALOG -->

正式收录、教学变体和未发行项分开列出。已发布的安装包见各技能说明。

### 当前可按 clips-v1 阅读的正式素材

- **电商短视频创作**（`product-short-video`，1.2.0）：根据单件商品的参考图与可选演员、场景、简要说明，规划 15 秒或 30 秒电商短视频（含人物出镜试吃、推荐与对戏的剧情带货小段），按演示底板与投放包装两层拆三条投放变体，并展开为连续分镜。 详见 [说明](docs/skills/product-short-video.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。

- **动作打斗提示词**（`action-fight-prompt`，1.6.0）：从用户的关键动作或旧稿编排连续表演，按观众需要看清的变化重写分镜、节奏和机位，保留事件结果、参考图与明确锁定项。 详见 [说明](docs/skills/action-fight-prompt.zh-CN.md)。效果：1.6.0 经 MiniMax-M3 实测。四动作短稿保住了人物归属及空中结尾，但只返回一句动作概述。14 秒英文稿仍沿用旧切点，并重复第 3 镜，整场重排未通过。仅验证提示词文本。
- **角色服装参考**（`character-costume-reference`，1.1.0）：为同一人物设计可选服装参考：正背全身、脸部及服装细节，可按工作台选择分张或合成参考板；不作为片段或视频创作的前置。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/character-costume-reference.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色表情九宫格**（`character-expression-nine-grid`，1.1.0）：为同一人物设计可选表情参考，按工作台所选子模式分张或合成参考板；保持已有身份和服装，不要求先制作九张图片。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/character-expression-nine-grid.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色多角度定妆**（`character-multi-angle-reference`，1.1.0）：为同一人物设计可选多角度与材质细节参考，按所选模板提供全身、脸部和局部视图；用于独立资产创作，不强制固定视频镜头或帧数。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/character-multi-angle-reference.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **通用视频提示词**（`generic-video-prompt-writing`，1.1.0）：冻结目标为 generic@1 时，将片段视频内容整理为中立自然语言，保留来源、时序与逐字原话；不替代损坏或缺失的专属格式绑定。 详见 [说明](docs/skills/generic-video-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **H3 视频提示词**（`h3-prompt-writing`，1.2.9）：把应用提供的视频母版整理成项目内 h3@1 兼容提示词。适用于 T2VA、I2VA、FL2VA、L2VA 和 Ref2VA；保留母版事实、台词、时间与参考素材绑定，不负责新增剧情或猜测模型能力。 详见 [说明](docs/skills/h3-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **可灵视频提示词**（`kling-prompt-writing`，1.1.1）：依据冻结的 Kling Classic 或 Omni 目标，将片段视频稿表达为当前模式所需内容，保留真实引用与原话；经典版和 Omni 的资源与能力不混用。 详见 [说明](docs/skills/kling-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **LTX-2.5 视频提示词**（`ltx-2-5-prompt-writing`，1.4.0）：为 LTX 的文生视频、图生视频和首尾帧视频适配连贯段落，按时间组织动作、镜头、光线和声音，逐字保留原语言对白、歌词与用户画面文字，并按应用合同交付正负提示词。 详见 [说明](docs/skills/ltx-2-5-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **Qwen Image 2.1 图像提示词**（`qwen-image-2-1-prompt-writing`，1.1.0）：为 Qwen Image 2.1 优化文生图与参考图编辑提示词。文生图整理为英文画面描述，图片编辑明确修改与保留内容，多图编号严格沿用输入顺序；画面文字保留用户指定语言。用于生图工作台点击优化提示词后审阅结果，不负责提交生图或改变画幅。 详见 [说明](docs/skills/qwen-image-2-1-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **场景四视角**（`scene-four-angle-reference`，1.2.0）：为同一环境编写空间参考或普通图片提示词，可选正左右后四向模板；用于片段环境及独立图像，不要求旧场次、场景实体或故事板。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/scene-four-angle-reference.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **Seedance 视频提示词**（`seedance-prompt-writing`，1.1.0）：把冻结的片段视频内容表达成 Seedance（2.0 系列）视频提示词的写法：主体定义与绑定、镜头1/镜头2 分镜时序、动作与运镜措辞、参考图／视频／音频的用途说法，以及文生、首帧／首尾帧、多图与多模态参考、编辑、延长等模式差异。只改写表达，不新增、删改或重排母版事实。为 Seedance 目标投影或整理视频提示词时使用。 详见 [说明](docs/skills/seedance-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **万相视频提示词**（`wan-prompt-writing`，1.1.0）：依据实际绑定的 Wan 目标和输入模式表达片段视频内容，保留来源、声音用途、时序与原话；不从历史名称推断模型能力。 详见 [说明](docs/skills/wan-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **H3-Image 图片提示词**（`h3-image-prompt-writing`，1.0.0）：为 MiniMax H3-Image 整理文生图与参考图编辑提示词，使用有序 Picture 引用、稳定 Subject 定义和明确的保留关系，保留用户事实与画内文字。供图片工作台优化提示词使用。 详见 [说明](docs/skills/h3-image-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **H3 多参内容整理**（`h3-multi-reference-content`，1.0.2）：整理 MiniMax H3 多参视频的片段原稿，明确参考图、视频、音频的用途与归属，保留动作顺序、说话人和逐字对白。 详见 [说明](docs/skills/h3-multi-reference-content.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- [按参考素材写剧本与分镜](docs/skills/reference-led-clip-writing.zh-CN.md)。优化剧集剧本或撰写视频片段稿时，按用户原文和指定素材绑定主体、环境与音色，精简重复的外观描写和分镜说明。
- [武戏片段静帧设计](docs/skills/action-clip-keyframe-design.zh-CN.md)。为动作戏、武戏片段选关键帧，为已选帧写图片提示词；可诊断动作摆拍、人物遮挡和前后时相混杂，给出局部改词。
- **文戏片段分镜规划**（`literary-clip-storyboard-planning`，1.1.0）：为生成片段稿约束文戏片段中的分镜提示词写法。不负责把剧集拆成多个片段，也不覆盖武戏分镜规划。 详见 [说明](docs/skills/literary-clip-storyboard-planning.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **武戏片段分镜规划**（`action-clip-storyboard-planning`，1.2.0）：根据已有剧本为武戏片段写视频分镜，按剧情选择动作时刻、人物视角和镜头衔接，沿用本次参考素材绑定。 详见 [说明](docs/skills/action-clip-storyboard-planning.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **Seedream 5.5 图片提示词**（`seedream-5-5-prompt-writing`，1.0.0）：为豆包 Seedream 5.5 优化文生图、单图编辑和多参考图合成提示词。沿用用户语言和素材顺序，明确改动范围、保留项、画内文字与透明区域。供图片工作台的优化助手使用。 详见 [说明](docs/skills/seedream-5-5-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。

### 教学变体

- **剧本与片段创作**（`bgx-screenwriter`，0.5.1）：文学剧本与片段创作方法：用人物欲望、行动因果、关系与对白写出完整正文，或把已保存单集忠实组织为视频片段规划。 详见 [说明](docs/skills/bgx-screenwriter.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **设定约束与片段规划**（`bible-roles-chapters`，1.0.1）：结合完整单集正文中的世界规则、人物目标和因果，把既有剧情组织为可直接编辑的视频片段规划。 详见 [说明](docs/skills/bible-roles-chapters.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **剧集创作**（`chapters-only`，2.0.1）：根据当前故事原文创作剧集正文，按人物目标与事件因果组织各集起承转合。用户要把故事写成剧集，或修改已有剧集正文时使用；不生成场次、分镜或名单。 详见 [说明](docs/skills/chapters-only.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **武打动作片段**（`clip-action-fight`，1.0.2）：用清晰的行动因果、空间关系和对手反应组织武打、追逐与对决的视频片段。 详见 [说明](docs/skills/clip-action-fight.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **片段环境描述**（`clip-environment-description`，1.0.0）：依据已冻结的整集计划、当前环境候选和真实原文，编写单张普通环境图片的提示词，建立可延续的空间与光照关系。 详见 [说明](docs/skills/clip-environment-description.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **混合叙事片段方法**（`clip-method-selection`，1.0.2）：为同集动作、文戏与环境过渡选择适合的表达方法，保持统一剧情与空间连续性。 详见 [说明](docs/skills/clip-method-selection.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **文戏微表情片段**（`clip-micro-expression`，1.0.2）：用局部可见变化表现文戏中的刺激、掩饰与回应，保留对白节奏和人物连续性。 详见 [说明](docs/skills/clip-micro-expression.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色表演与调度**（`clip-performance`，1.0.2）：以触发、反应、选择和余波组织角色表演，让视线、呼吸、动作与对手关系形成可见因果。 详见 [说明](docs/skills/clip-performance.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **渐进完善片段**（`clip-progressive-drafting`，1.0.2）：先忠实分配整集剧情，再在单片段成稿用途按当前目标细化动作、声音和衔接。 详见 [说明](docs/skills/clip-progressive-drafting.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **叙事节拍与镜头组织**（`clip-visual-continuity`，1.0.2）：按剧情变化组织片段内部镜头，让每次切换都带来新信息；镜数和摄影表达随内容决定。 详见 [说明](docs/skills/clip-visual-continuity.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **武侠剧情片段规划**（`clip-wuxia-planning`，2.0.2）：从完整武侠单集正文直接规划视频片段，以白话表达人物目标、招式因果和转折。 详见 [说明](docs/skills/clip-wuxia-planning.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **整集到视频片段**（`episode-clip-planning`，1.0.1）：从完整单集正文直接规划按叙事排列的视频片段，保留原文内容与跨段连续性。 详见 [说明](docs/skills/episode-clip-planning.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **九视角细节定妆**（`generation-policy-eye-garment`，1.0.1）：演员与角色定妆的 9 视角变体：前 7 张保持官方转身角，最后两张改为眼睛特写和衣服特写。在需要既有转身参考又要眼部与服装细节图、并选择 9 视角分张批量时使用；不适用于单图九宫格合成。 详见 [说明](docs/skills/generation-policy-eye-garment.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **巨幕胶片光化质感**（`generation-policy-imax-65mm-authentic-photochemical`，1.0.1）：以大画幅光化摄影为视觉参考，细腻颗粒、自然光学、稳定色彩与时间连续性；保留用户已定内容。 详见 [说明](docs/skills/generation-policy-imax-65mm-authentic-photochemical.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **巨幕胶片通用风格**（`generation-policy-imax-65mm-generic`，1.0.1）：用大画幅胶片细节、颗粒、宽容度与自然色彩改善图片或视频的摄影表达。 详见 [说明](docs/skills/generation-policy-imax-65mm-generic.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **巨幕胶片环境风格**（`generation-policy-imax-65mm-large-scene`，1.0.1）：强调环境尺度、空间层次与大气透视，适用于环境图片及环境为主的视频表达。 详见 [说明](docs/skills/generation-policy-imax-65mm-large-scene.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **巨幕胶片人像风格**（`generation-policy-imax-65mm-portrait-closeup`，1.0.1）：强调皮肤、眼神、面部立体感与自然光学，适用于人物图片及表演视频。 详见 [说明](docs/skills/generation-policy-imax-65mm-portrait-closeup.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **四视角局部半身定妆**（`generation-policy-one-slot-framing`，1.0.1）：只改一个槽位取景的 4 视角变体：其余槽位保持官方，仅 4 视角里右侧转身那一张改成右侧半身。在需要官方 4 视角、但右侧一张要半身而不是全身时使用。 详见 [说明](docs/skills/generation-policy-one-slot-framing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **IMAX大画幅胶片·通用·图片**（`large-format-film-general-image`，2.0.2）：为通用图片提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。 详见 [说明](docs/skills/large-format-film-general-image.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **IMAX大画幅胶片·通用·视频**（`large-format-film-general-video`，2.0.1）：为通用视频提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。 详见 [说明](docs/skills/large-format-film-general-video.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **IMAX大画幅胶片·大场景·图片**（`large-format-film-large-scene-image`，2.0.2）：为大场景图片提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。 详见 [说明](docs/skills/large-format-film-large-scene-image.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **IMAX大画幅胶片·大场景·视频**（`large-format-film-large-scene-video`，2.0.1）：为大场景视频提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。 详见 [说明](docs/skills/large-format-film-large-scene-video.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **IMAX大画幅胶片·人像·图片**（`large-format-film-portrait-image`，2.0.2）：为人像图片提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。 详见 [说明](docs/skills/large-format-film-portrait-image.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **IMAX大画幅胶片·人像·视频**（`large-format-film-portrait-video`，2.0.1）：为人像视频提供简短的大画幅胶片摄影质感；保留用户已定镜头、画幅与内容。 详见 [说明](docs/skills/large-format-film-portrait-video.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **BGX 动态包装设计**（`motion-design`，0.2.0）：动态包装设计方法。根据当前片段的字幕/口播与已安装动态模板的 props schema，给出每张动态卡片用哪个模板、何时出现、填什么内容；只产出符合 design.schema 的 JSON 方案，不渲染、不安装、不改文件。 详见 [说明](docs/skills/motion-design.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **标准多视角定妆**（`native-image-policy`，1.0.1）：内置多视图槽位。提示词正文仍在应用的官方生成策略合同里，本包只列出演员与角色共用的转面顺序。 详见 [说明](docs/skills/native-image-policy.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **武打片段优化**（`optimize-clip-fight`，1.0.2）：优化动作片段的空间与接触结果，保护原稿事实、对白及用户风格。 详见 [说明](docs/skills/optimize-clip-fight.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **微表情片段优化**（`optimize-clip-micro-expression`，1.0.2）：优化人物局部表演与情绪因果，让细微反应清楚而自然，保持对白和镜头意图。 详见 [说明](docs/skills/optimize-clip-micro-expression.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **片段连续性优化**（`optimize-segment-continuity`，1.0.2）：连接当前片段与前后状态，保留对白、画面文字、关键事实及用户否定要求。 详见 [说明](docs/skills/optimize-segment-continuity.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **短视频创意片段**（`short-video-creative`，1.0.2）：围绕观看理由、核心视觉机制和信息推进组织短视频片段，声音锚点以真实素材为准。 详见 [说明](docs/skills/short-video-creative.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **简洁胶片风格示例**（`simple-film-style`，1.0.1）：用简短胶片颗粒与低调光建议描述图片或视频质感，示范可编辑的摄影方法。 详见 [说明](docs/skills/simple-film-style.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色与道具提炼**（`story-entity-extraction`，1.0.1）：从当前单集正文独立提炼角色或重要道具候选，严格区分本次选择的对象种类，保留原文证据与身份区别。适用于单集角色提炼或道具提炼；不自动整合总名单。 详见 [说明](docs/skills/story-entity-extraction.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **故事名单整合**（`story-entity-integration`，1.0.2）：对照本次候选与当前故事名单，提出明确的角色或道具身份整合决定。同名不默认同人，引用只来自宿主给定闭集；适用于独立名单整合或显式审核已有对象。 详见 [说明](docs/skills/story-entity-integration.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **格式适配扩写示例**（`video-format-expansion`，1.0.1）：根据已审视频母版调整表达，允许补充必要镜头、光线和环境声音，保留原有主体、主要事件、对白与用户否定要求。用于视频格式适配阶段的扩写方法示例。 详见 [说明](docs/skills/video-format-expansion.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **音乐影像片段策划**（`viral-song-mv`，1.0.2）：依据歌词、可判断的音乐结构与情绪变化组织连续音乐影像，形成独立可编辑的视频片段计划。 详见 [说明](docs/skills/viral-song-mv.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **设定与人物驱动片段**（`world-and-character-planning`，1.0.1）：用世界规则与人物欲望梳理单集剧情，形成忠实原文、动机清楚的视频片段计划。 详见 [说明](docs/skills/world-and-character-planning.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。

<!-- END GENERATED SKILL CATALOG -->




比格熊官网 [www.bgxiong.com](https://www.bgxiong.com)｜微信公众号：天途影像｜[比格熊开发治理 Skill](https://www.bgxiong.com/goods/9p65SRB2Sl)
