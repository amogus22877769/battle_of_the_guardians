from Source.classes import Background, Button, Bar, Point, String

from Source.config import Config

config = Config()

import pygame

from Source.card import Card
from Source.energy_bar import EnergyBar

screen: pygame.Surface = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.RESIZABLE)

pygame.display.set_icon(pygame.image.load('Resources/Images/icon.jpg'))

pygame.display.set_caption(config.NAME_OF_THE_GAME)

pygame.surfarray.use_arraytype('numpy')

menu: Background = Background(pygame.image.load('Resources/Images/DeckMap.jpeg'))

battle_button: Button = Button(pygame.image.load('Resources/Images/BattleButton.png').convert_alpha(screen), config.BATTLE_BUTTON_COORDINATES,
                       config.BATTLE_BUTTON_SIZE)

battle: Background = Background(pygame.image.load('Resources/Images/MainGameTable.jpeg'))

pygame.font.init()

fantasy_font_for_waves_counter: pygame.font.Font = pygame.font.Font("Resources/Fonts/FantasyCapitals.otf", size=int(config.FANTASY_FONT_FOR_WAVES_COUNTER_SIZE))

fantasy_font_for_card_health_using_default_hp_bar: pygame.font.Font = pygame.font.Font("Resources/Fonts/FantasyCapitals.otf", size=int(config.FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR))

blazing_herald_raw: Card = Card(pygame.image.load('Resources/Images/BlazingHerald.jpeg'),
                          pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                          config.BLAZING_HERALD_HP, config.BLAZING_HERALD_DMG, fantasy_font_for_card_health_using_default_hp_bar)

electro_wizard_raw: Card = Card(pygame.image.load('Resources/Images/ElectroWizard.jpeg'),
                          pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                          config.ELECTRO_WIZARD_HP, config.ELECTRO_WIZARD_DMG, fantasy_font_for_card_health_using_default_hp_bar)

fire_dragon_raw: Card = Card(pygame.image.load('Resources/Images/FireDragon.jpeg'),
                       pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                       config.FIRE_DRAGON_HP, config.FIRE_DRAGON_DMG, fantasy_font_for_card_health_using_default_hp_bar)

fire_wizard_raw: Card = Card(pygame.image.load('Resources/Images/FireWizard.jpeg'),
                       pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                       config.FIRE_WIZARD_HP, config.FIRE_WIZARD_DMG, fantasy_font_for_card_health_using_default_hp_bar)

ground_titan_raw: Card = Card(pygame.image.load('Resources/Images/GroundTitan.jpeg'),
                        pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                        config.GROUND_TITAN_HP, config.GROUND_TITAN_DMG, fantasy_font_for_card_health_using_default_hp_bar)

ice_wizard_raw: Card = Card(pygame.image.load('Resources/Images/IceWizard.jpeg'),
                      pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                      config.ICE_WIZARD_HP, config.ICE_WIZARD_DMG, fantasy_font_for_card_health_using_default_hp_bar)

mermaid_raw: Card = Card(pygame.image.load('Resources/Images/Mermaid.jpeg'),
                   pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                   config.MERMAID_HP, config.MERMAID_DMG, fantasy_font_for_card_health_using_default_hp_bar)

shadow_monster_raw: Card = Card(pygame.image.load('Resources/Images/ShadowMonster.jpeg'),
                          pygame.image.load('Resources/Images/RedCardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                          config.SHADOW_MONSTER_HP, config.SHADOW_MONSTER_DMG, fantasy_font_for_card_health_using_default_hp_bar)

stone_dwarf_raw: Card = Card(pygame.image.load('Resources/Images/StoneDwarf.jpeg'),
                       pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), config.BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS), Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE, config.DEFAULT_HP_BAR_SIZE[1] * config.RELATIVE_HITPOINTS_ICON_SIZE)), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), config.DEFAULT_HP_BAR_SIZE, config.DEFAULT_HP_BAR_THICKNESS) for _ in range(config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                       config.STONE_DWARF_HP, config.STONE_DWARF_DMG, fantasy_font_for_card_health_using_default_hp_bar)

vs_button: Button = Button(pygame.image.load('Resources/Images/VSButton.png'), config.VS_BUTTON_COORDINATES, config.VS_BUTTON_SIZE)

draft_map: Background = Background(pygame.image.load('Resources/Images/DraftMap.jpeg'))

stage: type = str

element: type = str

def update_sprites() -> None:
    global menu, battle_button, battle, fantasy_font_for_waves_counter, fantasy_font_for_card_health_using_default_hp_bar, blazing_herald_raw, electro_wizard_raw, fire_wizard_raw, fire_dragon_raw, stone_dwarf_raw, shadow_monster_raw, ground_titan_raw, mermaid_raw, ice_wizard_raw, vs_button, draft_map
    menu = Background(pygame.image.load('Resources/Images/DeckMap.jpeg'))

    battle_button = Button(pygame.image.load('Resources/Images/BattleButton.png').convert_alpha(screen),
                                   BATTLE_BUTTON_COORDINATES,
                                   BATTLE_BUTTON_SIZE)

    battle = Background(pygame.image.load('Resources/Images/MainGameTable.jpeg'))
    fantasy_font_for_waves_counter = pygame.font.Font("Resources/Fonts/FantasyCapitals.otf",
                                                                        size=int(FANTASY_FONT_FOR_WAVES_COUNTER_SIZE))

    fantasy_font_for_card_health_using_default_hp_bar = pygame.font.Font(
        "Resources/Fonts/FantasyCapitals.otf", size=int(FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR))

    blazing_herald_raw = Card(pygame.image.load('Resources/Images/BlazingHerald.jpeg'),
                                    pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                    BASIC_OUTLINE_THICKNESS,
                                    Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                        DEFAULT_HP_BAR_THICKNESS), Button(
            pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (
            DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
            DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                        Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                              DEFAULT_HP_BAR_THICKNESS) for _ in
                                        range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                    BLAZING_HERALD_HP, BLAZING_HERALD_DMG,
                                    fantasy_font_for_card_health_using_default_hp_bar)

    electro_wizard_raw = Card(pygame.image.load('Resources/Images/ElectroWizard.jpeg'),
                                    pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                    BASIC_OUTLINE_THICKNESS,
                                    Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                        DEFAULT_HP_BAR_THICKNESS), Button(
            pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (
            DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
            DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                        Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                              DEFAULT_HP_BAR_THICKNESS) for _ in
                                        range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                    ELECTRO_WIZARD_HP, ELECTRO_WIZARD_DMG,
                                    fantasy_font_for_card_health_using_default_hp_bar)

    fire_dragon_raw = Card(pygame.image.load('Resources/Images/FireDragon.jpeg'),
                                 pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                 BASIC_OUTLINE_THICKNESS,
                                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                     DEFAULT_HP_BAR_THICKNESS),
                                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen),
                                        (0, 0), (DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                                 DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                     Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                           DEFAULT_HP_BAR_THICKNESS) for _ in
                                     range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                 FIRE_DRAGON_HP, FIRE_DRAGON_DMG, fantasy_font_for_card_health_using_default_hp_bar)

    fire_wizard_raw = Card(pygame.image.load('Resources/Images/FireWizard.jpeg'),
                                 pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                 BASIC_OUTLINE_THICKNESS,
                                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                     DEFAULT_HP_BAR_THICKNESS),
                                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen),
                                        (0, 0), (DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                                 DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                     Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                           DEFAULT_HP_BAR_THICKNESS) for _ in
                                     range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                 FIRE_WIZARD_HP, FIRE_WIZARD_DMG, fantasy_font_for_card_health_using_default_hp_bar)

    ground_titan_raw = Card(pygame.image.load('Resources/Images/GroundTitan.jpeg'),
                                  pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                  BASIC_OUTLINE_THICKNESS,
                                  Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                      DEFAULT_HP_BAR_THICKNESS),
                                  Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen),
                                         (0, 0), (DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                                  DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                      Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                            DEFAULT_HP_BAR_THICKNESS) for _ in
                                      range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                  GROUND_TITAN_HP, GROUND_TITAN_DMG, fantasy_font_for_card_health_using_default_hp_bar)

    ice_wizard_raw = Card(pygame.image.load('Resources/Images/IceWizard.jpeg'),
                                pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                BASIC_OUTLINE_THICKNESS,
                                Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                    DEFAULT_HP_BAR_THICKNESS),
                                Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen),
                                       (0, 0), (DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                                DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                    Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                          DEFAULT_HP_BAR_THICKNESS) for _ in
                                    range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                ICE_WIZARD_HP, ICE_WIZARD_DMG, fantasy_font_for_card_health_using_default_hp_bar)

    mermaid_raw = Card(pygame.image.load('Resources/Images/Mermaid.jpeg'),
                             pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                             BASIC_OUTLINE_THICKNESS,
                             Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                 DEFAULT_HP_BAR_THICKNESS),
                             Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen),
                                    (0, 0), (DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                             DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                 Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                       DEFAULT_HP_BAR_THICKNESS) for _ in
                                 range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                             MERMAID_HP, MERMAID_DMG, fantasy_font_for_card_health_using_default_hp_bar)

    shadow_monster_raw = Card(pygame.image.load('Resources/Images/ShadowMonster.jpeg'),
                                    pygame.image.load('Resources/Images/RedCardOrnament.png').convert_alpha(screen),
                                    BASIC_OUTLINE_THICKNESS,
                                    Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                        DEFAULT_HP_BAR_THICKNESS), Button(
            pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen), (0, 0), (
            DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
            DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                        Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                              DEFAULT_HP_BAR_THICKNESS) for _ in
                                        range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                    SHADOW_MONSTER_HP, SHADOW_MONSTER_DMG,
                                    fantasy_font_for_card_health_using_default_hp_bar)

    stone_dwarf_raw = Card(pygame.image.load('Resources/Images/StoneDwarf.jpeg'),
                                 pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen),
                                 BASIC_OUTLINE_THICKNESS,
                                 Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE,
                                     DEFAULT_HP_BAR_THICKNESS),
                                 Button(pygame.image.load('Resources/Images/HitpointsIcon.png').convert_alpha(screen),
                                        (0, 0), (DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE,
                                                 DEFAULT_HP_BAR_SIZE[1] * RELATIVE_HITPOINTS_ICON_SIZE)), [
                                     Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE,
                                           DEFAULT_HP_BAR_THICKNESS) for _ in
                                     range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                 STONE_DWARF_HP, STONE_DWARF_DMG, fantasy_font_for_card_health_using_default_hp_bar)

    vs_button = Button(pygame.image.load('Resources/Images/VSButton.png'), VS_BUTTON_COORDINATES,
                               VS_BUTTON_SIZE)

    draft_map = Background(pygame.image.load('Resources/Images/DraftMap.jpeg'))