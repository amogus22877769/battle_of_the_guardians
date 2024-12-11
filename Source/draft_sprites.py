import pygame

from pathlib import Path
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
        self.deck: list[Card] = [
            Card(pygame.image.load('Resources/Images/BlazingHerald.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 BLAZING_HERALD_HP,
                 BLAZING_HERALD_DMG,
                 String(f'{BLAZING_HERALD_HP}', pygame.Color('black'), (0, 0),
                        Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/ElectroWizard.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 ELECTRO_WIZARD_HP,
                 ELECTRO_WIZARD_DMG,
                 String(f'{ELECTRO_WIZARD_HP}', pygame.Color('red'), (0, 0),
                        Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/FireDragon.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 FIRE_DRAGON_HP,
                 FIRE_DRAGON_DMG,
                 String(f'{FIRE_DRAGON_HP}', pygame.Color('red'), (0, 0), Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/FireWizard.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 FIRE_WIZARD_HP,
                 FIRE_WIZARD_DMG,
                 String(f'{FIRE_WIZARD_DMG}', pygame.Color('red'), (0, 0), Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/GroundTitan.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 GROUND_TITAN_HP,
                 GROUND_TITAN_DMG,
                 String(f'{GROUND_TITAN_HP}', pygame.Color('red'), (0, 0), Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/IceWizard.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 ICE_WIZARD_HP,
                 ICE_WIZARD_DMG,
                 String(f'{ICE_WIZARD_HP}', pygame.Color('red'), (0, 0), Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/Mermaid.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 MERMAID_HP,
                 MERMAID_DMG,
                 String(f'{MERMAID_HP}', pygame.Color('red'), (0, 0), Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
            Card(pygame.image.load('Resources/Images/StoneDwarf.jpeg'),
                 pygame.image.load('Resources/Images/CardOrnament.png'),
                 RELATIVE_CARD_SIZE,
                 RELATIVE_BASIC_OUTLINE_THICKNESS,
                 (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), RELATIVE_DEFAULT_HP_BAR_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_THICKNESS, (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                     RELATIVE_DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE), (DEFAULT_WIDTH, DEFAULT_HEIGHT)),
                 Path('Resources/Images/Hitpoint.png'),
                 STONE_DWARF_HP,
                 STONE_DWARF_DMG,
                 String(f'{STONE_DWARF_HP}', pygame.Color('red'), (0, 0), Path('Resources/Fonts/FantasyCapitals.otf'),
                        RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR,
                        (DEFAULT_WIDTH, DEFAULT_HEIGHT))),
        ]

        self.vs_button: Button = Button(pygame.image.load('Resources/Images/VSButton.png'),
                                        RELATIVE_VS_BUTTON_COORDINATES,
                                        RELATIVE_VS_BUTTON_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT))

        self.draft_map: Background = Background(pygame.image.load('Resources/Images/DraftMap.jpeg'),
                                                (DEFAULT_WIDTH, DEFAULT_HEIGHT))

    def update(self, new_width: int, new_height: int) -> None:
        for card in self.deck:
            card.update((new_width, new_height))
        self.draft_map.update((new_width, new_height))
        self.vs_button.update((new_width, new_height))
