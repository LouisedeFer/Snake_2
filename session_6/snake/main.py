# ruff: noqa: D100,S311

# Standard
import logging 
import sys
from pathlib import Path

# First party
from .cmd_line import read_args
from .exceptions import SnakeError
from .game import Game

logger = logging.getLogger("foo")

def main() -> None: # noqa: D103

    try:
        # Read command line arguments
        args = read_args()

        # Start game
        logger.info("Starting the Snake game...")
        Game(width = args.width, height = args.height,
             tile_size = args.tile_size, fps = args.fps,
             fruit_color = args.fruit_color,
             snake_head_color = args.snake_head_color,
             snake_body_color = args.snake_body_color,
             gameover_on_exit = args.gameover_on_exit, scores_file=Path(args.scores_file),
             ).start()

    except SnakeError as e:
        logger.exception(f"Error: {e}") # noqa: T201
        sys.exit(1)
