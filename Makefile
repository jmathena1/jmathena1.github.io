build:
	uv run build.py
	uv run python -m pagefind --site public --output-path public/pagefind --exclude-selectors "body:not(.wiki-page)"

serve:
	uv run python -m http.server 8000 --directory public
