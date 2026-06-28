# AutoShortAI — ZIP01 Production Foundation

ZIP01 is the first production-grade software foundation for AutoShortAI.

## Important

ZIP00 is frozen and must not be modified. ZIP01 only adds the runnable application foundation.

## Product Direction

AutoShortAI is a platform-neutral AI content automation system.

YouTube, TikTok, Instagram, AI providers, voice providers, video engines, storage backends, and notification providers are plugins.

## Run

```bash
cp .env.example .env
docker compose up --build
```

Backend:
- http://localhost:8000/health
- http://localhost:8000/api/v1/system/status
- http://localhost:8000/api/v1/plugins

Frontend:
- http://localhost:5173

## Validate

```bash
bash scripts/validate_zip01.sh
```
