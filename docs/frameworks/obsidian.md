# Framework Card: ObsidianVault

## Role

长期知识沉淀：source → note → wikilink → index → hot/log

## Trigger phrases

- 写进知识库
- 保存认知
- 下次接上
- 整理文章
- 形成主题页

## Inputs

- 用户自然语言意图；
- 当前 Instance 配置；
- 必要的上下文文件或任务文件；
- 相关权限/确认状态。

## Outputs

- `source note`
- `understanding note`
- `index`
- `hot/log`

## Participating Patterns

- Plan-Act-Verify
- State Outside Context
- Learning Loop

具体是否启用其他 Pattern，以 `docs/ROUTING_MATRIX.md` 和 Instance 配置为准。

## Instance fields

```json
{
  "framework": "ObsidianVault",
  "enabled": true,
  "inputs": [],
  "outputs": [],
  "verification": [],
  "persistence_sinks": []
}
```

## Verification

read-back + search + index/hot 更新

## Failure modes

- 只有项目名，没有触发条件；
- 有输出但没有验证；
- 结果没有沉淀；
- 被错误用于不适合的任务类型；
- demo 结果被误当作真实生产验证。
