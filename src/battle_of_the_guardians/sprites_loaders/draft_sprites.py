from pathlib import Path

import pygame

from src.battle_of_the_guardians.config import RELATIVE_CARD_SIZE, RELATIVE_BASIC_OUTLINE_THICKNESS, DEFAULT_WIDTH, \
    DEFAULT_HEIGHT, RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS, RELATIVE_HITPOINTS_ICON_SIZE, \
    RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR, BLAZING_HERALD_HP, BLAZING_HERALD_DMG, \
    ELECTRO_WIZARD_HP, ELECTRO_WIZARD_DMG, FIRE_DRAGON_HP, FIRE_DRAGON_DMG, FIRE_WIZARD_HP, FIRE_WIZARD_DMG, \
    GROUND_TITAN_HP, GROUND_TITAN_DMG, ICE_WIZARD_HP, ICE_WIZARD_DMG, MERMAID_HP, MERMAID_DMG, STONE_DWARF_HP, \
    STONE_DWARF_DMG, RELATIVE_VS_BUTTON_COORDINATES, RELATIVE_VS_BUTTON_SIZE
from src.battle_of_the_guardians.sprites.background import Background
from src.battle_of_the_guardians.sprites.bar import Bar
from src.battle_of_the_guardians.sprites.button import Button
from src.battle_of_the_guardians.sprites.object import Object
from src.battle_of_the_guardians.sprites.point import Point
from src.battle_of_the_guardians.sprites.string import String
from src.battle_of_the_guardians.structures.card import Card


class DraftSprites:
    def __init__(self) -> None:
        empty_card: Object = Object(pygame.Surface((0, 0)),
                                    (RELATIVE_CARD_SIZE[0] - RELATIVE_BASIC_OUTLINE_THICKNESS[0] * 2,
                                     RELATIVE_CARD_SIZE[1] - RELATIVE_BASIC_OUTLINE_THICKNESS[1] * 2),
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_outline: Object = Object(pygame.image.load('resources/img/ornaments/card_ornament.png'), RELATIVE_CARD_SIZE,
                                         (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hp_bar: Bar = Bar(pygame.image.load('resources/img/bars/hitpoint_bar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                                  RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hp_icon: Button = Button(pygame.image.load('resources/img/buttons/hitpoints_icon.png'), (0, 0), (
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hitpoint: Point = Point(pygame.image.load('resources/img/points/hitpoint.png'),
                                        RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS,
                                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        empty_string: String = String(f'', pygame.Color('red'), (0, 0),
                                      Path('resources/fonts/fantasy_capitals.otf'),
                                      RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                                      (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.deck: list[Card] = [
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/blazing_herald.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 BLAZING_HERALD_HP,
                 BLAZING_HERALD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/electro_wizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 ELECTRO_WIZARD_HP,
                 ELECTRO_WIZARD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/fire_dragon.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 FIRE_DRAGON_HP,
                 FIRE_DRAGON_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/fire_wizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 FIRE_WIZARD_HP,
                 FIRE_WIZARD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/ground_titan.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 GROUND_TITAN_HP,
                 GROUND_TITAN_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/ice_wizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 ICE_WIZARD_HP,
                 ICE_WIZARD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/mermaid.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 MERMAID_HP,
                 MERMAID_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('resources/img/cards/stone_dwarf.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 STONE_DWARF_HP,
                 STONE_DWARF_DMG,
                 empty_string.copy())
        ]

        self.vs_button: Button = Button(pygame.image.load('resources/img/buttons/vs_button.png'),
                                        RELATIVE_VS_BUTTON_COORDINATES,
                                        RELATIVE_VS_BUTTON_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT))

        self.draft_map: Background = Background(pygame.image.load('resources/img/maps/draft_map.jpeg'),
                                                (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_width: int, new_height: int) -> None:
        [card.update((new_width, new_height)) for card in self.deck]
        self.draft_map.update((new_width, new_height))
        self.vs_button.update((new_width, new_height))
