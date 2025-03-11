from pathlib import Path

import pygame.image

from frontend.src.battle_of_the_guardians.buffer import score
from frontend.src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_YOU_LOST_COORDINATES, \
    RELATIVE_FANTASY_FONT_FOR_YOU_LOST_SIZE, RELATIVE_RETURN_BUTTON_COORDINATES, RELATIVE_RETURN_BUTTON_SIZE, \
    RELATIVE_RESULT_COORDINATES, RELATIVE_SHARE_BUTTON_COORDINATES, RELATIVE_SHARE_RESULT_COORDINATES
from frontend.src.battle_of_the_guardians.sprites.background import Background
from frontend.src.battle_of_the_guardians.sprites.button import Button
from frontend.src.battle_of_the_guardians.sprites.string import String


class YouLostSprites:
    def __init__(self):
        self.background = Background(pygame.image.load('resources/img/maps/after_battle_map.jpeg'),
                                     (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.you_lost = String('YOU LOST', pygame.Color('red'), RELATIVE_YOU_LOST_COORDINATES,
                               Path('resources/fonts/fantasy_capitals.otf'), RELATIVE_FANTASY_FONT_FOR_YOU_LOST_SIZE,
                               (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.return_button = Button(pygame.image.load('resources/img/buttons/return_button.png'),
                                    RELATIVE_RETURN_BUTTON_COORDINATES, RELATIVE_RETURN_BUTTON_SIZE,
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                                    circular=True)
        self.result = self.you_lost.copy()
        self.result.place(RELATIVE_RESULT_COORDINATES)
        self.result.text = f'YOU SCORE: {score[0]}'
        self.share = Button(pygame.image.load('resources/img/buttons/share_button.png'), RELATIVE_SHARE_BUTTON_COORDINATES, RELATIVE_RETURN_BUTTON_SIZE,
                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.share_result = self.you_lost.copy()
        self.share_result.place(RELATIVE_SHARE_RESULT_COORDINATES)
        self.share_result.text = ''

    def update(self, new_window_size: tuple[int, int]):
        self.background.update(new_window_size)
        self.you_lost.update(new_window_size)
        self.return_button.update(new_window_size)
        self.share.update(new_window_size)
        self.result.update(new_window_size)
        self.share_result.update(new_window_size)
