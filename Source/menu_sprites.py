import pygame

from Source.background import Background
from Source.button import Button
from Source.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_BATTLE_BUTTON_COORDINATES, RELATIVE_BATTLE_BUTTON_SIZE


class MenuSprites:
    def __init__(self) -> None:
        self.menu: Background = Background(pygame.image.load('Resources/Images/DeckMap.jpeg'),
                                           (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.battle_button: Button = Button(pygame.image.load('Resources/Images/BattleButton.png'),
                                            RELATIVE_BATTLE_BUTTON_COORDINATES,
                                            RELATIVE_BATTLE_BUTTON_SIZE,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_width: int, new_height: int) -> None:
        self.menu.update((new_width, new_height))
        self.battle_button.update((new_width, new_height))
