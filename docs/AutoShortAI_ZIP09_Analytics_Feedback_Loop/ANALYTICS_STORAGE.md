# Analytics Storage Contracts

ZIP09 storage must stay lightweight and optional.

## Default future path

- JSON files for local snapshots
- append-only report files
- storage providers from ZIP06 when needed

## Optional future paths

- SQLite provider
- remote object storage provider
- warehouse export provider

## Rule

No database should become mandatory for ZIP09. The software must remain usable locally and lightly.
