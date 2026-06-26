# Framework Card: repo-harness

## Role

agent 交接与恢复传输层：handoff、resume、checks、events

## Trigger phrases

- 多 agent 接力
- 恢复上下文
- 长任务交接
- 让 Codex 接手

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `resume.md`
- `checks/latest.json`
- `events.jsonl`
- `handoff packet`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "repo-harness",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

handoff 文件存在且新会话可恢复

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
