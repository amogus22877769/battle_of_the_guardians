from pathlib import Path

import pygame.image

from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_YOU_LOST_COORDINATES, \
    RELATIVE_FANTASY_FONT_FOR_YOU_LOST_SIZE, RELATIVE_RETURN_BUTTON_COORDINATES, RELATIVE_RETURN_BUTTON_SIZE
from src.battle_of_the_guardians.sprites.background import Background
from src.battle_of_the_guardians.sprites.button import Button
from src.battle_of_the_guardians.sprites.string import String


class YouLostSprites:
    def __init__(self):
        self.background = Background(pygame.image.load('resources/img/maps/after_battle_map.jpeg'),
                                     (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.you_lost = String('YOU LOST', pygame.Color('red'), RELATIVE_YOU_LOST_COORDINATES,
                               Path('resources/fonts/fantasy_capitals.otf'), RELATIVE_FANTASY_FONT_FOR_YOU_LOST_SIZE,
                               (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.return_button = Button(pygame.image.load('resources/img/buttons/return_button.png'),
                                    RELATIVE_RETURN_BUTTON_COORDINATES, RELATIVE_RETURN_BUTTON_SIZE,
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_window_size: tuple[int, int]):
        self.background.update(new_window_size)
        self.you_lost.update(new_window_size)
        self.return_button.update(new_window_size)
