from os import environ

from Source.game import Game

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

if __name__ == "__main__":
    Game().run()