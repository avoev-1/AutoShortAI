# Learning Memory

Learning Memory stores historical conclusions so AutoShortAI does not relearn the same facts repeatedly.

Default storage is local JSON.

Future storage may use ZIP06 storage providers or optional SQLite. A mandatory database is not allowed in ZIP10.

Stored records should include:

- insight ID,
- source evidence IDs,
- platform scope,
- confidence,
- proposed adjustment,
- decision status,
- created timestamp.
