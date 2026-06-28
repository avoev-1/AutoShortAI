# Boot Protocol

Every session:

1. Read mandatory files.
2. Inspect git state.
3. Read `NEXT_TASK.md`.
4. Summarize current project state.
5. Execute only the current task.
6. Validate.
7. Update documentation and state.
8. Prepare next task.

If files conflict, stop and repair state before feature work.
