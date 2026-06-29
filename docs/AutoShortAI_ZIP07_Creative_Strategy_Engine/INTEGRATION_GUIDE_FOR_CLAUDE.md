# Integration Guide for Claude

Claude must treat ZIP07 as architecture authority.

Allowed implementation work:

- implement simple profile loading;
- implement deterministic strategy plan creation;
- implement simple rule checks;
- implement basic score aggregation;
- implement variant planning using ZIP07 models.

Forbidden work without a future ZIP:

- introduce a monolithic generator;
- add SaaS concepts;
- directly publish videos;
- directly call paid providers from ZIP07;
- rewrite previous ZIP contracts;
- add Guardian Engine logic;
- implement analytics-driven auto-learning.

When unsure, create a small adapter or plugin boundary instead of coupling modules.
