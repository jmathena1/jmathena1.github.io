import asyncio
import logging
import re
import subprocess
from pathlib import Path
from typing import Set

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from watchfiles import awatch

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()
connected_clients: Set[WebSocket] = set()
is_rebuilding = False

PUBLIC_DIR = Path("public")
SRC_DIR = Path("src")
WATCH_PATTERNS = ["**/*.md", "**/*.html", "**/*.css"]
REBUILD_TIMEOUT = 60
DEBOUNCE_MS = 500


def run_build() -> tuple[bool, str]:
    """
    Run the build script.
    Returns: (success: bool, output: str)
    """
    try:
        logger.info("Running build...")
        result = subprocess.run(
            ["uv", "run", "build.py"],
            capture_output=True,
            text=True,
            timeout=REBUILD_TIMEOUT,
        )

        if result.returncode == 0:
            # Extract the success message from stdout
            output = result.stdout.strip()
            logger.info(f"Build successful: {output}")
            return True, output
        else:
            # Build failed, capture error
            error_msg = (
                result.stderr.strip() or result.stdout.strip() or "Unknown error"
            )
            logger.error(f"Build failed: {error_msg}")
            return False, error_msg

    except subprocess.TimeoutExpired:
        error_msg = "Rebuild exceeded 60 second timeout"
        logger.error(f"Build failed: {error_msg}")
        return False, error_msg
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Build failed: {error_msg}")
        return False, error_msg


async def notify_clients(status: str, error: str = None):
    """
    Send rebuild status to all connected WebSocket clients.
    """
    message = {"status": status}
    if error:
        message["error"] = f"Build failed: {error}"

    disconnected = set()
    for client in connected_clients:
        try:
            await client.send_json(message)
        except Exception as e:
            logger.warning(f"Failed to send message to client: {e}")
            disconnected.add(client)

    # Remove disconnected clients
    connected_clients.difference_update(disconnected)


async def file_watcher():
    """
    Watch for file changes in src/ directory and trigger rebuilds.
    """
    global is_rebuilding

    logger.info("File watcher started")

    try:
        async for changes in awatch(
            SRC_DIR,
            watch_filter=lambda change: any(
                str(change).endswith(ext) for ext in [".md", ".html", ".css"]
            ),
        ):
            if is_rebuilding:
                logger.debug("Build already in progress, skipping change detection")
                continue

            # Debounce: wait a bit to catch multiple rapid changes
            await asyncio.sleep(DEBOUNCE_MS / 1000.0)

            is_rebuilding = True
            logger.info(f"File changes detected: {changes}")

            # Run the build
            success, output = run_build()

            # Notify clients
            if success:
                await notify_clients("rebuild_complete")
            else:
                await notify_clients("rebuild_failed", output)

            is_rebuilding = False

    except Exception as e:
        logger.error(f"File watcher error: {e}")


def inject_live_reload(html_content: str) -> str:
    """
    Inject live-reload.js script into HTML content.
    Adds the script right before the closing </body> tag.
    """
    reload_script = '<script src="/js/live-reload.js"></script>'

    # Try to insert before </body>
    if "</body>" in html_content:
        return html_content.replace("</body>", f"{reload_script}\n</body>")

    # Fallback: append at the end
    return html_content + f"\n{reload_script}"


@app.on_event("startup")
async def startup_event():
    """
    On startup:
    1. Run initial build
    2. Start file watcher task
    """
    logger.info("Dev server starting...")

    # Run initial build
    success, output = run_build()
    if success:
        logger.info("✓ Initial build successful")
    else:
        logger.error(f"✗ Initial build failed: {output}")

    # Start file watcher as a background task
    asyncio.create_task(file_watcher())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for live reload notifications.
    """
    await websocket.accept()
    connected_clients.add(websocket)
    logger.info(f"Client connected. Total clients: {len(connected_clients)}")

    try:
        # Keep connection alive and handle incoming messages
        while True:
            # Just receive messages to keep connection alive
            # We don't need to process anything from the client
            await websocket.receive_text()
    except Exception as e:
        logger.debug(f"WebSocket error: {e}")
    finally:
        connected_clients.discard(websocket)
        logger.info(f"Client disconnected. Total clients: {len(connected_clients)}")


@app.get("/{full_path:path}")
async def serve_file(full_path: str):
    """
    Serve files from the public directory.
    Inject live-reload.js into HTML files.
    """
    # Handle root path
    if not full_path or full_path == "/":
        full_path = "index.html"

    file_path = PUBLIC_DIR / full_path

    # Prevent directory traversal attacks
    try:
        file_path = file_path.resolve()
        if not str(file_path).startswith(str(PUBLIC_DIR.resolve())):
            return {"error": "Invalid path"}, 400
    except Exception:
        return {"error": "Invalid path"}, 400

    # If it's a directory, try to serve index.html
    if file_path.is_dir():
        file_path = file_path / "index.html"

    # Check if file exists
    if not file_path.exists():
        return {"error": "Not found"}, 404

    # For HTML files, inject live-reload script
    if file_path.suffix == ".html":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            content = inject_live_reload(content)
            return FileResponse(
                path=file_path,
                media_type="text/html",
                content=content.encode("utf-8"),
            )
        except Exception as e:
            logger.error(f"Error serving HTML file: {e}")
            return {"error": "Internal server error"}, 500

    # For other files, serve normally
    return FileResponse(path=file_path)


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting dev server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
