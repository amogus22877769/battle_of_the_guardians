import pygame

from pathlib import Path

from Source.background import Background
from Source.card import Card
from Source.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE, \
    RELATIVE_WAVES_COUNTER_RIGHT_CORNER_POS, RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR
from Source.string import String


class BattleSprites:
    def __init__(self, deck: list[Card]) -> None:
        self.deck: list[Card] = deck
        self.battle: Background = Background(pygame.image.load('Resources/Images/MainGameTable.jpeg'),
                                             (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.waves_counter: String = String(f'Wave: {0}', pygame.Color('black'),
                                            RELATIVE_WAVES_COUNTER_RIGHT_CORNER_POS,
                                            Path('Resources/Fonts/FantasyCapitals.otf'),
                                            RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.battle.update(new_window_size)
        self.waves_counter.update(new_window_size)
        for card in self.deck:
            card.update(new_window_size)
