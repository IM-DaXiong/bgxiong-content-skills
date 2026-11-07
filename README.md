# 比格熊创作技能

本仓库是创作技能正文的可编辑源。比格熊数字导演工作站负责安装、权限、用途闭集和执行。这里不能新增宿主能力。

官网：[https://www.bgxiong.com](https://www.bgxiong.com)。作者公开联系方式：微信公众号「天途影像」。

许可是仓库根 `LICENSE` 的自定义许可：可以学习，也可以在自有项目中使用；不能把这些材料单独做成付费技能包出售。这不是 OSI 开源许可证。

## 先读什么

1. [规范](docs/SPECIFICATION.zh-CN.md)
2. [从零写一个技能](docs/CREATE-FROM-SCRATCH.zh-CN.md)
3. [修改已有技能](docs/EDIT-EXISTING.zh-CN.md)
4. [技能目录](docs/skills/INDEX.zh-CN.md)

`skills/` 是从应用内置包原样收下的正式素材。`examples/teaching/` 只保留和正式包字节不同的教学变体。`packs/`、`examples/content-plan/`、`examples/generation-policy/`、`examples/optimize/` 和旧的 `contracts/v1/` 是历史私有包格式，不再是当前安装格式。

当前产品执行标识是 `metadata.bgx-workflow: clips-v1`。没有这个标识的包仍可能被导入阅读，但不能当作当前可执行方法。本仓库不提供在线自动升级，也不使用 WASM。

<!-- BEGIN GENERATED SKILL CATALOG -->

正式收录、教学变体和未发行项分开列出。下载链接在公开资产发布前保持为空。

### 当前可按 clips-v1 阅读的正式素材

- **动作打斗提示词**（`action-fight-prompt`，1.1.0）：为片段初稿或当前视频稿整理动作打斗表达，保持人物、空间、因果、声音与逐字原话；适用于现代格斗、持械和多人对抗，镜头与时长不套固定模板。 详见 [说明](docs/skills/action-fight-prompt.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色服装参考**（`character-costume-reference`，1.1.0）：为同一人物设计可选服装参考：正背全身、脸部及服装细节，可按工作台选择分张或合成参考板；不作为片段或视频创作的前置。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/character-costume-reference.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色表情九宫格**（`character-expression-nine-grid`，1.1.0）：为同一人物设计可选表情参考，按工作台所选子模式分张或合成参考板；保持已有身份和服装，不要求先制作九张图片。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/character-expression-nine-grid.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **角色多角度定妆**（`character-multi-angle-reference`，1.1.0）：为同一人物设计可选多角度与材质细节参考，按所选模板提供全身、脸部和局部视图；用于独立资产创作，不强制固定视频镜头或帧数。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/character-multi-angle-reference.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **通用视频提示词**（`generic-video-prompt-writing`，1.1.0）：冻结目标为 generic@1 时，将片段视频内容整理为中立自然语言，保留来源、时序与逐字原话；不替代损坏或缺失的专属格式绑定。 详见 [说明](docs/skills/generic-video-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **可灵视频提示词**（`kling-prompt-writing`，1.1.1）：依据冻结的 Kling Classic 或 Omni 目标，将片段视频稿表达为当前模式所需内容，保留真实引用与原话；经典版和 Omni 的资源与能力不混用。 详见 [说明](docs/skills/kling-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **LTX-2.5 视频提示词**（`ltx-2-5-prompt-writing`，1.4.0）：为 LTX 的文生视频、图生视频和首尾帧视频适配连贯段落，按时间组织动作、镜头、光线和声音，逐字保留原语言对白、歌词与用户画面文字，并按应用合同交付正负提示词。 详见 [说明](docs/skills/ltx-2-5-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **Qwen Image 2.1 图像提示词**（`qwen-image-2-1-prompt-writing`，1.1.0）：为 Qwen Image 2.1 优化文生图与参考图编辑提示词。文生图整理为英文画面描述，图片编辑明确修改与保留内容，多图编号严格沿用输入顺序；画面文字保留用户指定语言。用于生图工作台点击优化提示词后审阅结果，不负责提交生图或改变画幅。 详见 [说明](docs/skills/qwen-image-2-1-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **场景四视角**（`scene-four-angle-reference`，1.1.0）：为同一环境编写空间参考或普通图片提示词，可选正左右后四向模板；用于片段环境及独立图像，不要求旧场次、场景实体或故事板。 同名素材若正文不同，以下变体分别保留，不以较高版本覆盖。 详见 [说明](docs/skills/scene-four-angle-reference.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **Seedance 视频提示词**（`seedance-prompt-writing`，1.1.0）：把冻结的片段视频内容表达成 Seedance（2.0 系列）视频提示词的写法：主体定义与绑定、镜头1/镜头2 分镜时序、动作与运镜措辞、参考图／视频／音频的用途说法，以及文生、首帧／首尾帧、多图与多模态参考、编辑、延长等模式差异。只改写表达，不新增、删改或重排母版事实。为 Seedance 目标投影或整理视频提示词时使用。 详见 [说明](docs/skills/seedance-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。
- **万相视频提示词**（`wan-prompt-writing`，1.1.0）：依据实际绑定的 Wan 目标和输入模式表达片段视频内容，保留来源、声音用途、时序与原话；不从历史名称推断模型能力。 详见 [说明](docs/skills/wan-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。

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

### 不发行

- **H3 视频提示词**（`h3-prompt-writing`，1.2.4）：把应用提供的视频母版整理成项目内 h3@1 兼容提示词。适用于 T2VA、I2VA、FL2VA、L2VA 和 Ref2VA；保留母版事实、台词、时间与参考素材绑定，不负责新增剧情或猜测模型能力。 详见 [说明](docs/skills/h3-prompt-writing.zh-CN.md)。效果：设计用途来自该包正文。本仓库没有为这个方法附上模型实测前后对照。

<!-- END GENERATED SKILL CATALOG -->

