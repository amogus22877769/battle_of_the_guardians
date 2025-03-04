from pathlib import Path

import pygame

from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_BATTLE_BUTTON_COORDINATES, \
    RELATIVE_BATTLE_BUTTON_SIZE, INPUT_BOX_RELATIVE_SIZE, INPUT_BOX_RELATIVE_COORDINATES, \
    INPUT_BOX_RELATIVE_OUTLINE_THICKNESS
from src.battle_of_the_guardians.sprites.background import Background
from src.battle_of_the_guardians.sprites.button import Button
from src.battle_of_the_guardians.sprites.object import Object
from src.battle_of_the_guardians.sprites.string import String


class MenuSprites:
    def __init__(self) -> None:
        self.menu: Background = Background(pygame.image.load('resources/img/maps/deck_map.jpeg'),
                                           (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.battle_button: Button = Button(pygame.image.load('resources/img/buttons/battle_button.png'),
                                            RELATIVE_BATTLE_BUTTON_COORDINATES,
                                            RELATIVE_BATTLE_BUTTON_SIZE,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                                            circular=True)
        self.box = Object(pygame.image.load('resources/img/ornaments/input_box.png'), INPUT_BOX_RELATIVE_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                          relative_center_coordinates=INPUT_BOX_RELATIVE_COORDINATES)
        self.username = String('', pygame.Color('red'), INPUT_BOX_RELATIVE_COORDINATES, Path('resources/fonts/fantasy_capitals.otf'),
                               INPUT_BOX_RELATIVE_SIZE[1] - INPUT_BOX_RELATIVE_OUTLINE_THICKNESS[1] * 2, (DEFAULT_WIDTH, DEFAULT_HEIGHT))


    def update(self, new_width: int, new_height: int) -> None:
        self.menu.update((new_width, new_height))
        self.battle_button.update((new_width, new_height))
