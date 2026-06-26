# Framework Card: Hermes

## Role

宿主、总控、跨会话上下文、工具调用、Telegram gateway、cron 调度

## Trigger phrases

- 继续推进
- 帮我判断
- 接着上次
- 定时
- 保存到记忆

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `routing_decision`
- `final_report`
- `hot/log update`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "Hermes",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

工具调用记录、文件读回、用户确认

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
