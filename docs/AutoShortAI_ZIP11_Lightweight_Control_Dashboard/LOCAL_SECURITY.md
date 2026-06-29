# Local Dashboard Security

The dashboard is local-first.

Default future behavior should favor:

- localhost binding
- masked secrets
- no public exposure by default
- explicit user consent for remote access
- action audit trail
- minimal permissions per adapter

ZIP11 does not implement a credentials vault. That belongs to a future dedicated security ZIP.
