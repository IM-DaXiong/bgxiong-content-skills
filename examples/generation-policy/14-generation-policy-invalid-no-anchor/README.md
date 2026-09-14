# 负例14 · 无第 0 锚（应拒装）

## 能做什么

无。这是门禁与文档用的**故意非法**包。

## 不能做什么

- 导入必须失败。
- 不要把它当成功案例发给用户当「能用的 Skill」。

## 导入应看到什么人话

第 0 张必须标成身份锚。请把 `view3`/`view4`/`view9` 下标 0 的 `identityAnchor` 设为 true，且只有第 0 张为 true。

机码 `GENERATION_POLICY_IDENTITY_ANCHOR` 只进日志。
