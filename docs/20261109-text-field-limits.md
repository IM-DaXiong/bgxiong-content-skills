# 创作文本字段取消字数上限

用户2026-11-09要求取消创作模块文本字段上限。内容仓的优化回包正文、镜头正文/节拍/信息增量/执行说明等文本字段不再使用maxLength；generation-policy的风格和排版说明字数上限删除。ID/引用字段长度、类型、必填与结构合同保留。

正式skills/templates本轮未发现JSON文本maxLength；本次修改contracts/v1及11个历史示例包，历史包各自patch升版，保持历史身份，不宣称可供当前clips-v1执行。主仓须按本次推送提交锁定同步。

验证：所有修改JSON解析成功；受影响历史示例使用现有validate-example.py --legacy-historical定向检查。当前安装/模型调用未验，无正式技能包发行字节变更。

实际验收：26个取消maxLength的字段使用100000字符样本逐字段验证，新合同全部接收、旧合同全部拒收。11个历史示例定向校验10通过；03-staged-to-shots因原有manifest缺capabilities失败（HEAD同样缺失），本轮未扩修。JSON解析及git diff --check通过。
