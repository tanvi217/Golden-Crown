import argparse
import sys

from config import SENDER_KINGDOM
from src.main.controller.universe_controller import UniverseController
from src.main.models.universe import Universe
from src.main.views.show_ruler_allies import UniverseView

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('secret_messages_file_path', type=str, help="The file path for input")
    parser.add_argument('sender_kingdom', nargs='?', type=str, default=SENDER_KINGDOM, help="The kingdom sending messages")
    args = parser.parse_args()

    universe_controller = UniverseController(Universe(args.sender_kingdom, args.secret_messages_file_path), UniverseView())
    universe_controller.send_messages()
    universe_controller.show_ruler()

if __name__ == "__main__":
    main()