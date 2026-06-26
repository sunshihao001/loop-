# Framework Card: Trellis

## Role

工程任务生命周期：PRD → design → implement → verify

## Trigger phrases

- 变成项目
- 做成长任务
- 需要 PRD
- 建任务
- 项目治理

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `task.json`
- `prd.md`
- `design.md`
- `implement.md`
- `verify.md`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "Trellis",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

task 文件完整，验收清单可读

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
