from pathlib import Path

import pygame

from src.battle_of_the_guardians.ability import Ability
from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, \
    RELATIVE_WAVES_COUNTER_RELATIVE_CENTER_COORDINATES, RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE, \
    RELATIVE_DEFAULT_ENERGY_BAR_SIZE, RELATIVE_ENERGY_ICON_SIZE, DEFAULT_ENERGY_BAR_ALPHA, TOTAL_ENERGY, \
    RELATIVE_DEFAULT_ENERGY_BAR_COORDINATES, NUMBER_OF_POINTS_IN_DEFAULT_ENERGY_BAR, RELATIVE_CARD_SIZE, \
    RELATIVE_BASIC_OUTLINE_THICKNESS, RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS, \
    RELATIVE_HEALTH_POINTS_ICON_SIZE, \
    RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR, TERRIBLE_USURPER_HP, TERRIBLE_USURPER_DMG, \
    ASH_DEMON_HP, ASH_DEMON_DMG, WATER_STORM_HP, WATER_STORM_DMG, BLACKOUT_SHADOW_HP, BLACKOUT_SHADOW_DMG, \
    DESTROYER_OF_EARTH_HP, DESTROYER_OF_EARTH_DMG, MALIGNANT_INFESTATION_HP, MALIGNANT_INFESTATION_DMG, \
    WINDSTORM_SHADOW_HP, WINDSTORM_SHADOW_DMG, GHOST_BIRD_HP, GHOST_BIRD_DMG, RELATIVE_CHANGE_HEALTH_FONT_SIZE
from src.battle_of_the_guardians.sprites.background import Background
from src.battle_of_the_guardians.sprites.bar import Bar
from src.battle_of_the_guardians.sprites.button import Button
from src.battle_of_the_guardians.sprites.object import Object
from src.battle_of_the_guardians.sprites.point import Point
from src.battle_of_the_guardians.sprites.string import String
from src.battle_of_the_guardians.structures.card import Card
from src.battle_of_the_guardians.structures.energy_bar import EnergyBar


class BattleSprites:
    def __init__(self, deck: list[Card]) -> None:
        empty_card: Object = Object(pygame.Surface((0, 0)),
                                    (RELATIVE_CARD_SIZE[0] - RELATIVE_BASIC_OUTLINE_THICKNESS[0] * 2,
                                     RELATIVE_CARD_SIZE[1] - RELATIVE_BASIC_OUTLINE_THICKNESS[1] * 2),
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_red_outline: Object = Object(pygame.image.load('resources/img/ornaments/red_card_ornament.png'),
                                             RELATIVE_CARD_SIZE,
                                             (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hp_bar: Bar = Bar(pygame.image.load('resources/img/bars/health_point_bar.png'),
                                  RELATIVE_DEFAULT_HP_BAR_SIZE,
                                  RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hp_icon: Button = Button(pygame.image.load('resources/img/buttons/health_points_icon.png'), (0, 0), (
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HEALTH_POINTS_ICON_SIZE,
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HEALTH_POINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_health_point: Point = Point(pygame.image.load('resources/img/points/health_point.png'),
                                            RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        empty_string: String = String(f'', pygame.Color('red'), (0, 0),
                                      Path('resources/fonts/fantasy_capitals.otf'),
                                      RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                                      (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_shield_icon: Button = Button(pygame.image.load('resources/img/buttons/shield_icon.png'), (0, 0), (
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HEALTH_POINTS_ICON_SIZE,
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HEALTH_POINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_shield_point: Point = Point(pygame.image.load('resources/img/points/shield_point.png'),
                                            RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.opposition = [
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/terrible_usurper.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 TERRIBLE_USURPER_HP,
                 TERRIBLE_USURPER_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/ash_demon.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 ASH_DEMON_HP,
                 ASH_DEMON_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/water_storm.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 WATER_STORM_HP,
                 WATER_STORM_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/blackout_shadow.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 BLACKOUT_SHADOW_HP,
                 BLACKOUT_SHADOW_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/destroyer_of_earth.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 DESTROYER_OF_EARTH_HP,
                 DESTROYER_OF_EARTH_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/malignant_infestation.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 MALIGNANT_INFESTATION_HP,
                 MALIGNANT_INFESTATION_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/windstorm_shadow.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 WINDSTORM_SHADOW_HP,
                 WINDSTORM_SHADOW_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/ghost_bird.jpg')),
                 default_red_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 GHOST_BIRD_HP,
                 GHOST_BIRD_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('',0,0))
        ]
        self.deck: list[Card] = deck
        self.battle: Background = Background(pygame.image.load('resources/img/maps/battle_map.jpeg'),
                                             (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.waves_counter: String = String(f'Wave: {0}', pygame.Color('purple'),
                                            RELATIVE_WAVES_COUNTER_RELATIVE_CENTER_COORDINATES,
                                            Path('resources/fonts/fantasy_capitals.otf'),
                                            RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE,
                                            (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.energy_bar = EnergyBar(
            Bar(pygame.image.load('resources/img/bars/energy_bar.png'), RELATIVE_DEFAULT_ENERGY_BAR_SIZE, (0, 0),
                (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
            Button(pygame.image.load('resources/img/buttons/energy_icon.png'), (0, 0), (
                RELATIVE_ENERGY_ICON_SIZE * RELATIVE_DEFAULT_ENERGY_BAR_SIZE[1],
                RELATIVE_ENERGY_ICON_SIZE * RELATIVE_DEFAULT_ENERGY_BAR_SIZE[1]), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
            DEFAULT_ENERGY_BAR_ALPHA,
            Point(pygame.image.load('resources/img/points/energy_effect.jpeg'), RELATIVE_DEFAULT_ENERGY_BAR_SIZE,
                  (0, 0),
                  (DEFAULT_WIDTH, DEFAULT_HEIGHT), relative_width=RELATIVE_DEFAULT_ENERGY_BAR_SIZE[0] / TOTAL_ENERGY),
            RELATIVE_DEFAULT_ENERGY_BAR_COORDINATES,
            (DEFAULT_WIDTH, DEFAULT_HEIGHT),
            NUMBER_OF_POINTS_IN_DEFAULT_ENERGY_BAR,
            TOTAL_ENERGY)
        self.opponents: list[Card] = []
        self.strings: list[String] = []

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.battle.update(new_window_size)
        self.waves_counter.update(new_window_size)
        [card.update(new_window_size) for card in self.deck]
        [opponent.update(new_window_size) for opponent in self.opponents]
        [opposition_member.update(new_window_size) for opposition_member in self.opposition]
        self.energy_bar.update(new_window_size)
        [st.update(new_window_size) for st in self.strings]
