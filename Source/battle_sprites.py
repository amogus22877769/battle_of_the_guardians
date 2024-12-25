import pygame

from pathlib import Path

from pygame.display import update

from Source.background import Background
from Source.bar import Bar
from Source.button import Button
from Source.card import Card
from Source.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE, \
    RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR, \
    RELATIVE_DEFAULT_ENERGY_BAR_SIZE, RELATIVE_ENERGY_ICON_SIZE, DEFAULT_ENERGY_BAR_ALPHA, \
    RELATIVE_DEFAULT_ENERGY_BAR_COORDINATES, NUMBER_OF_POINTS_IN_DEFAULT_ENERGY_BAR, TOTAL_ENERGY, RELATIVE_CARD_SIZE, \
    RELATIVE_BASIC_OUTLINE_THICKNESS, RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS, \
    RELATIVE_HITPOINTS_ICON_SIZE, SHADOW_MONSTER_HP, SHADOW_MONSTER_DMG, \
    RELATIVE_WAVES_COUNTER_RELATIVE_CENTER_COORDINATES
from Source.energy_bar import EnergyBar
from Source.object import Object
from Source.point import Point
from Source.string import String


class BattleSprites:
    def __init__(self, deck: list[Card]) -> None:
        self.deck: list[Card] = deck
        self.battle: Background = Background(pygame.image.load('Resources/Images/MainGameTable.jpeg'),
                                             (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.waves_counter: String = String(f'Wave: {0}', pygame.Color('deeppink'),
                                            RELATIVE_WAVES_COUNTER_RELATIVE_CENTER_COORDINATES,
                                            Path('Resources/Fonts/FantasyCapitals.otf'),
                                            RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.energy_bar = EnergyBar(Bar(pygame.image.load('Resources/Images/EnergyBar.png'), RELATIVE_DEFAULT_ENERGY_BAR_SIZE, (0, 0), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                                    Button(pygame.image.load('Resources/Images/EnergySign.png'), (0, 0), (RELATIVE_ENERGY_ICON_SIZE * RELATIVE_DEFAULT_ENERGY_BAR_SIZE[1], RELATIVE_ENERGY_ICON_SIZE * RELATIVE_DEFAULT_ENERGY_BAR_SIZE[1]), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                                    DEFAULT_ENERGY_BAR_ALPHA,
                                    Point(pygame.image.load('Resources/Images/EnergyEffect.jpeg'), RELATIVE_DEFAULT_ENERGY_BAR_SIZE, (0, 0), (DEFAULT_WIDTH, DEFAULT_HEIGHT), relative_width=RELATIVE_DEFAULT_ENERGY_BAR_SIZE[0] / TOTAL_ENERGY),
                                    RELATIVE_DEFAULT_ENERGY_BAR_COORDINATES,
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                                    NUMBER_OF_POINTS_IN_DEFAULT_ENERGY_BAR,
                                    TOTAL_ENERGY)
        self.shadow = Card(Object(pygame.image.load('Resources/Images/ShadowMonster.jpeg'),
                             (RELATIVE_CARD_SIZE[0] - RELATIVE_BASIC_OUTLINE_THICKNESS[0] * 2,
                              RELATIVE_CARD_SIZE[1] - RELATIVE_BASIC_OUTLINE_THICKNESS[1] * 2),
                             (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                           Object(pygame.image.load('Resources/Images/RedCardOrnament.png'),
                                  RELATIVE_CARD_SIZE,
                                  (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                           RELATIVE_BASIC_OUTLINE_THICKNESS,
                           (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                           Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                               RELATIVE_DEFAULT_HP_BAR_SIZE,
                               RELATIVE_DEFAULT_HP_BAR_THICKNESS,
                               (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                           Button(pygame.image.load('Resources/Images/HitpointsIcon.png'),
                                  (0, 0),
                                  (RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                             RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE),
                                  (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                           Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                 RELATIVE_DEFAULT_HP_BAR_SIZE,
                                 RELATIVE_DEFAULT_HP_BAR_THICKNESS,
                                 (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                           SHADOW_MONSTER_HP,
                           SHADOW_MONSTER_DMG,
                           String(f'', pygame.Color('red'), (0, 0),
                                  Path('Resources/Fonts/FantasyCapitals.otf'),
                                  RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                                  (DEFAULT_WIDTH, DEFAULT_HEIGHT)))
        self.opps: list[Card] = []


    def update(self, new_window_size: tuple[int, int]) -> None:
        self.battle.update(new_window_size)
        self.waves_counter.update(new_window_size)
        [card.update(new_window_size) for card in self.deck]
        [opp.update(new_window_size) for opp in self.opps]
        self.energy_bar.update(new_window_size)

