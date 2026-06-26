# Framework Card: Codex

## Role

实现与调试执行体：代码修改、测试、长任务实现

## Trigger phrases

- 执行吧
- 修 bug
- 写代码
- 实现这个
- 跑测试

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `diff`
- `implementation notes`
- `test output`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "Codex",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

测试真实运行，diff 范围符合预期

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
