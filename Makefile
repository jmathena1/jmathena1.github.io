build:
	uv run build.py
	uv run python -m pagefind --site public/wiki-pages --output-path public/pagefind

serve:
	uv run python -m http.server 8000 --directory public
