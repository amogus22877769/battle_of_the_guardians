from pathlib import Path

import pygame

from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_LEADERBOARD_STRING_COORDINATES, \
    RELATIVE_FANTASY_FONT_FOR_LEADERBOARD_STRING_SIZE, RELATIVE_LEADERS_STRING_COORDINATES, \
    RELATIVE_FANTASY_FONT_FOR_LEADERS_STRING_SIZE, RELATIVE_LEADERBOARD_RETURN_BUTTON_COORDINATES, \
    RELATIVE_LEADERBOARD_RETURN_BUTTON_SIZE
from src.battle_of_the_guardians.sprites.background import Background
from src.battle_of_the_guardians.sprites.button import Button
from src.battle_of_the_guardians.sprites.string import String


class LeaderboardSprites:
    def __init__(self):
        self.background: Background = Background(pygame.image.load('resources/img/maps/leaderboard_map.jpeg'), (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.leaderboard_string: String = String('LEADERBOARD', pygame.Color('red'), RELATIVE_LEADERBOARD_STRING_COORDINATES, Path('resources/fonts/fantasy_capitals.otf'),
                                                 RELATIVE_FANTASY_FONT_FOR_LEADERBOARD_STRING_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.leaders: list[String] = [String('', pygame.Color('black'), RELATIVE_LEADERS_STRING_COORDINATES[i], Path('resources/fonts/fantasy_capitals.otf'),
                                      RELATIVE_FANTASY_FONT_FOR_LEADERS_STRING_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT)) for i in range(10)]
        self.return_button = Button(pygame.image.load('resources/img/buttons/return_button.png'),
                                    RELATIVE_LEADERBOARD_RETURN_BUTTON_COORDINATES, RELATIVE_LEADERBOARD_RETURN_BUTTON_SIZE,
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                                    circular=True)

    def fill(self, data: list[tuple[str, int]]):
        for i in range(min(10, len(data))):
            self.leaders[i].text = f'{i + 1}. {data[i][0]}: {data[i][1]}'

    def update(self, new_windows_size: tuple[int, int]):
        self.background.update(new_windows_size)
        self.leaderboard_string.update(new_windows_size)
        [leader.update(new_windows_size) for leader in self.leaders]
        self.return_button.update(new_windows_size)
