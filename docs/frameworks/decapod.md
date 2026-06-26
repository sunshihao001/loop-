# Framework Card: Decapod

## Role

治理与 proof：todo claim、orientation、workspace ensure、validate、proof gate

## Trigger phrases

- 要改代码
- 需要 proof
- 多 agent
- 不要裸执行
- 隔离工作区

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `todo`
- `orientation packet`
- `worktree`
- `validate result`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "Decapod",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

decapod validate 或等价 proof gate

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
