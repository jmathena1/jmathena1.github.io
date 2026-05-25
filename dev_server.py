import logging

from livereload import Server, shell

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    server = Server()

    server.watch("src/", shell("make build"))

    server.serve(port=8000, liveport=8001, root="public")
