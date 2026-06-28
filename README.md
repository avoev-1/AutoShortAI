# AutoShortAI — ZIP00 v3 Final LLM Operating System

This is the final bootstrap package for AutoShortAI.

AutoShortAI is a private project whose goal is to build a reliable platform for producing original YouTube Shorts and growing monetizable YouTube channels.

This ZIP contains no application code. It contains the AI operating system that lets Claude, GPT, Gemini, Qwen, DeepSeek, or another LLM resume development from the repository, self-validate, update documentation, and prepare the next task.

## Start Here

1. `.llm/core/LLM_CORE.md`
2. `.llm/core/BOOT_PROTOCOL.md`
3. `.llm/core/OPERATING_LOOP.md`
4. `.llm/policies/AI_CONSTITUTION.md`
5. `state/PROJECT_STATE.json`
6. `state/NEXT_TASK.md`

## Human Owner Goal

Maximum automation, but with safety rails:
- AI may self-validate routine work.
- AI must not publish real public content without approval.
- AI must not spend money through paid APIs without approval.
- AI must not delete production data without approval.

## First Command

```bash
bash scripts/validate_zip00_v3.sh
```
