build:
	uv run build.py

serve:
	uv run python -m http.server 8000 --directory public
