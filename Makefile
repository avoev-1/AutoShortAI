.PHONY: up down logs validate test-backend lint-backend build-frontend

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

validate:
	bash scripts/validate_zip01.sh

test-backend:
	docker compose run --rm backend pytest

lint-backend:
	docker compose run --rm backend ruff check app tests

build-frontend:
	docker compose run --rm frontend npm run build
