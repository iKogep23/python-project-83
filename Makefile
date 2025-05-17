install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run

all: db-create schema-load

dev-setup: db-reset schema-load

db-create:
	createdb mydb

db-reset:
	dropdb mydb
	createdb mydb

schema-load:
	psql mydb < database.sql

connect:
	psql -d mydb

PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

local-start:
	uv run flask --app page_analyzer:app run --port 8000

build:
	./build.sh

render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app
