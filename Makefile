install:
	uv sync
brain-games:
	uv run brain-games
brain-evens:
	uv run brain-even
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check brain_games