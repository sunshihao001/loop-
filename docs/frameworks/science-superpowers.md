# Framework Card: Science Superpowers

## Role

深度方法论和验证门禁：framing、prior work、design、preregister、verify、red-team

## Trigger phrases

- 严谨分析
- 验证结论
- 不想拍脑袋
- 数据分析
- claim 前验证

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `research question`
- `prior work`
- `analysis plan`
- `preregistration`
- `verification report`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "Science Superpowers",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

是否先 preregister，claim 前是否 verify

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
