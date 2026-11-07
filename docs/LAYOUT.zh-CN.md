# 多视角布局

应用读取 `references/layout.json` 时，已经实现并在源码注释中写明的字段包括：

- `identityAnchor`：身份锚槽位，必须是对应 `views` 清单的第一项。
- `views`：`view3`、`view4`、`view9` 到槽位 ID 清单。`view9` 这个键名不等于九张图，也不等于视频帧数，张数以该清单长度为准。
- `slotDetails`：自定义槽位的说明。官方机位不能在这里重定义。
- `slotOverrides`：只替换某个视图、某个槽位的一段提示词。
- `sheet` 与 `sheetModes`：单图合成。两边声明的模式要一致。
- `aspectRatio`：顶层和 `sheet` 内的比例需要一致。
- `visualStyleOverlay`：可选的风格覆盖文字。

三种定妆包里的具体槽位以各自 `references/layout.json` 为准。本页不增加上述字段以外的布局能力。
