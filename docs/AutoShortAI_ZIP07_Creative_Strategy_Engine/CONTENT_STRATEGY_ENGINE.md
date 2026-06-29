# Content Strategy Engine

The Content Strategy Engine coordinates strategic planning before execution.

It accepts a `StrategyRequest` and returns a `CreativeStrategyPlan`.

Responsibilities:

- resolve creation profile;
- normalize the content idea;
- build a script blueprint;
- plan variants;
- validate rules;
- score quality dimensions;
- expose hook points;
- declare asset requirements for ZIP06.

Non-responsibilities:

- video rendering;
- upload scheduling;
- analytics scraping;
- cache storage;
- provider billing;
- dashboard UI.
