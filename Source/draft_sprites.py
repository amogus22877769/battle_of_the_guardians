import pygame

from pathlib import Path

from Source.object import Object
from Source.string import String
from Source.background import Background
from Source.bar import Bar
from Source.button import Button
from Source.card import Card
from Source.config import RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR, DEFAULT_HEIGHT, \
    RELATIVE_VS_BUTTON_COORDINATES, RELATIVE_VS_BUTTON_SIZE, DEFAULT_WIDTH, RELATIVE_CARD_SIZE, \
    RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS, RELATIVE_HITPOINTS_ICON_SIZE, \
    MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR, BLAZING_HERALD_HP, BLAZING_HERALD_DMG, \
    RELATIVE_BASIC_OUTLINE_THICKNESS, ELECTRO_WIZARD_HP, ELECTRO_WIZARD_DMG, FIRE_DRAGON_HP, FIRE_DRAGON_DMG, \
    FIRE_WIZARD_HP, FIRE_WIZARD_DMG, GROUND_TITAN_DMG, GROUND_TITAN_HP, ICE_WIZARD_HP, ICE_WIZARD_DMG, MERMAID_HP, \
    MERMAID_DMG, STONE_DWARF_HP, STONE_DWARF_DMG
from Source.point import Point


class DraftSprites:
    def __init__(self) -> None:
        empty_card: Object = Object(pygame.Surface((0, 0)),
                                    (RELATIVE_CARD_SIZE[0] - RELATIVE_BASIC_OUTLINE_THICKNESS[0] * 2,
                                     RELATIVE_CARD_SIZE[1] - RELATIVE_BASIC_OUTLINE_THICKNESS[1] * 2),
                                    (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_outline: Object = Object(pygame.image.load('Resources/Images/CardOrnament.png'), RELATIVE_CARD_SIZE,
                                         (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hp_bar: Bar = Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                                  RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hp_icon: Button = Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
            RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        default_hitpoint: Point = Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                        RELATIVE_DEFAULT_HP_BAR_SIZE, RELATIVE_DEFAULT_HP_BAR_THICKNESS,
                                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        empty_string: String = String(f'', pygame.Color('red'), (0, 0),
                                      Path('Resources/Fonts/FantasyCapitals.otf'),
                                      RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                                      (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.deck: list[Card] = [
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/BlazingHerald.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 BLAZING_HERALD_HP,
                 BLAZING_HERALD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/ElectroWizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 ELECTRO_WIZARD_HP,
                 ELECTRO_WIZARD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/FireDragon.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 FIRE_DRAGON_HP,
                 FIRE_DRAGON_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/FireWizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 FIRE_WIZARD_HP,
                 FIRE_WIZARD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/GroundTitan.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 GROUND_TITAN_HP,
                 GROUND_TITAN_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/IceWizard.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 ICE_WIZARD_HP,
                 ICE_WIZARD_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/Mermaid.jpeg')),
                 default_outline.copy(),
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 default_hp_bar.copy(),
                 default_hp_icon.copy(),
                 default_hitpoint.copy(),
                 MERMAID_HP,
                 MERMAID_DMG,
                 empty_string.copy()),
            Card(empty_card.copy_consts(pygame.image.load('Resources/Images/StoneDwarf.jpeg')),
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

        self.vs_button: Button = Button(pygame.image.load('Resources/Images/VSButton.png'),
                                        RELATIVE_VS_BUTTON_COORDINATES,
                                        RELATIVE_VS_BUTTON_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT))

        self.draft_map: Background = Background(pygame.image.load('Resources/Images/DraftMap.jpeg'),
                                                (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_width: int, new_height: int) -> None:
        [card.update((new_width, new_height)) for card in self.deck]
        self.draft_map.update((new_width, new_height))
        self.vs_button.update((new_width, new_height))
