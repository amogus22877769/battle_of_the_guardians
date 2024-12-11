from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from Source.game import Game

if __name__ == "__main__":
    Game().run()
