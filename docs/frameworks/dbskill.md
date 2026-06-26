# Framework Card: dbskill

## Role

快速诊断和问题分诊，尤其商业、内容、决策、行动问题

## Trigger phrases

- /dbs
- 商业问题
- 内容诊断
- 我不知道为什么不行动
- 帮我判断方向

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `diagnosis state`
- `problem statement`
- `next-action recommendation`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "dbskill",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

输出能进入下一步的诊断结论

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
