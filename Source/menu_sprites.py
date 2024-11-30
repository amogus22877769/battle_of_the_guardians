import pygame

from Source.classes import Background, Button
from Source.config import Config


class MenuSprites:
    def __init__(self, local_config: Config) -> None:
        self.config = local_config
        self.menu: Background = Background(pygame.image.load('Resources/Images/DeckMap.jpeg'),
                                           (self.config.WIDTH, self.config.HEIGHT))
        self.battle_button: Button = Button(pygame.image.load('Resources/Images/BattleButton.png'),
                                            self.config.BATTLE_BUTTON_COORDINATES,
                                            self.config.BATTLE_BUTTON_SIZE)

    def update(self, new_width: int, new_height: int) -> None:
        self.config.update_const(new_width, new_height)
        self.menu.update((self.config.WIDTH, self.config.HEIGHT))
        self.battle_button.update(self.config.BATTLE_BUTTON_COORDINATES, self.config.BATTLE_BUTTON_SIZE)
