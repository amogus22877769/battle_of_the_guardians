from pathlib import Path

import pygame

from frontend.src.battle_of_the_guardians.ability import Ability
from frontend.src.battle_of_the_guardians.config import RELATIVE_CARD_SIZE, RELATIVE_BASIC_OUTLINE_THICKNESS, DEFAULT_WIDTH, \
    DEFAULT_HEIGHT, RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS, RELATIVE_HEALTH_POINTS_ICON_SIZE, \
    RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR, BLAZING_HERALD_HP, BLAZING_HERALD_DMG, \
    ELECTRO_WIZARD_HP, ELECTRO_WIZARD_DMG, FIRE_DRAGON_HP, FIRE_DRAGON_DMG, FIRE_WIZARD_HP, FIRE_WIZARD_DMG, \
    GROUND_TITAN_HP, GROUND_TITAN_DMG, ICE_WIZARD_HP, ICE_WIZARD_DMG, MERMAID_HP, MERMAID_DMG, STONE_DWARF_HP, \
    STONE_DWARF_DMG, RELATIVE_VS_BUTTON_COORDINATES, RELATIVE_VS_BUTTON_SIZE, FIRE_WAVE_DMG, FIRE_WAVE_COST, \
    FIRE_BREATHE_DMG, FIRE_BREATHE_COST, THUNDER_PUNCH_DMG, THUNDER_PUNCH_COST, GROUND_PROTECTION_AMOUNT, \
    GROUND_PROTECTION_COST, ICE_WALL_TIME, ICE_WALL_COST, HEAL_AMOUNT, HEAL_COST, STRONG_AMOUNT, STRONG_COST, \
    ACCELERATION_COST
from frontend.src.battle_of_the_guardians.sprites.background import Background
from frontend.src.battle_of_the_guardians.sprites.bar import Bar
from frontend.src.battle_of_the_guardians.sprites.button import Button
from frontend.src.battle_of_the_guardians.sprites.object import Object
from frontend.src.battle_of_the_guardians.sprites.point import Point
from frontend.src.battle_of_the_guardians.sprites.string import String
from frontend.src.battle_of_the_guardians.structures.card import Card


class DraftSprites:
    def __init__(self) -> None:
        empty_card: Object = Object(pygame.Surface((0, 0)),
                                    (RELATIVE_CARD_SIZE[0] - RELATIVE_BASIC_OUTLINE_THICKNESS[0] * 2,
                                     RELATIVE_CARD_SIZE[1] - RELATIVE_BASIC_OUTLINE_THICKNESS[1] * 2),
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_outline: Object = Object(pygame.image.load('resources/img/ornaments/card_ornament.png'),
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
        self.cards: list[Card] = [
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/blazing_herald.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 BLAZING_HERALD_HP,
                 BLAZING_HERALD_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('acceleration', 0, ACCELERATION_COST),
                 shield=1000),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/electro_wizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 ELECTRO_WIZARD_HP,
                 ELECTRO_WIZARD_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('thunder_punch', THUNDER_PUNCH_DMG, THUNDER_PUNCH_COST)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/fire_dragon.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 FIRE_DRAGON_HP,
                 FIRE_DRAGON_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('fire_breathe', FIRE_BREATHE_DMG, FIRE_BREATHE_COST)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/fire_wizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 FIRE_WIZARD_HP,
                 FIRE_WIZARD_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('fire_wave', FIRE_WAVE_DMG, FIRE_WAVE_COST)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/ground_titan.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 GROUND_TITAN_HP,
                 GROUND_TITAN_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('ground_protection', GROUND_PROTECTION_AMOUNT, GROUND_PROTECTION_COST)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/ice_wizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 ICE_WIZARD_HP,
                 ICE_WIZARD_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('ice_wall', ICE_WALL_TIME, ICE_WALL_COST)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/mermaid.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 MERMAID_HP,
                 MERMAID_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('heal', HEAL_AMOUNT, HEAL_COST)),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/stone_dwarf.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_health_point.copy(),
                 default_hp_bar.copy(),
                 default_shield_icon.copy(),
                 default_shield_point.copy(),
                 STONE_DWARF_HP,
                 STONE_DWARF_DMG,
                 empty_string.copy(),
                 empty_string.copy(),
                 Ability('strong', STRONG_AMOUNT, STRONG_COST))
        ]

        self.vs_button: Button = Button(pygame.image.load('resources/img/buttons/vs_button.png'),
                                        RELATIVE_VS_BUTTON_COORDINATES,
                                        RELATIVE_VS_BUTTON_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT))

        self.draft_map: Background = Background(pygame.image.load('resources/img/maps/draft_map.jpeg'),
                                                (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_width: int, new_height: int) -> None:
        [card.update((new_width, new_height)) for card in self.cards]
        self.draft_map.update((new_width, new_height))
        self.vs_button.update((new_width, new_height))
