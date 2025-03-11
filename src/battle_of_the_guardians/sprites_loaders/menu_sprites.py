from pathlib import Path

import pygame

from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_BATTLE_BUTTON_COORDINATES, \
    RELATIVE_BATTLE_BUTTON_SIZE, INPUT_BOX_RELATIVE_SIZE, USERNAME_BOX_RELATIVE_COORDINATES, \
    INPUT_BOX_RELATIVE_OUTLINE_THICKNESS, RELATIVE_LEADERBOARD_BUTTON_COORDINATES, RELATIVE_LEADERBOARD_BUTTON_SIZE
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
        self.leaderboard_button: Button = Button(pygame.image.load('resources/img/buttons/leaderboard_button.png'),
                                                 RELATIVE_LEADERBOARD_BUTTON_COORDINATES,
                                                 RELATIVE_LEADERBOARD_BUTTON_SIZE,
                                                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                                                  circular=True)


    def update(self, new_width: int, new_height: int) -> None:
        self.menu.update((new_width, new_height))
        self.battle_button.update((new_width, new_height))
        self.leaderboard_button.update((new_width, new_height))
