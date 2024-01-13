from OpenAIInterface import openAI_Interface
import json
from pathlib import Path
from DnDGame import DnDGame


if __name__ == "__main__":
    f = open(Path(__file__).parent.parent / "keys.json")
    keys = json.load(f)
    game = DnDGame(keys["gpt_secret"], Path(__file__).parent.parent / "prompts.json")
    game.start_game()
