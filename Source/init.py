from Source.classes import Background, Button, Bar, Point, String

from Source.config import WIDTH, HEIGHT, BATTLE_BUTTON_SIZE, BATTLE_BUTTON_COORDINATES, DEFAULT_HP_BAR_SIZE, \
    DEFAULT_HP_BAR_THICKNESS, BASIC_OUTLINE_THICKNESS, BLAZING_HERALD_HP, BLAZING_HERALD_DMG, ELECTRO_WIZARD_HP, \
    ELECTRO_WIZARD_DMG, FIRE_DRAGON_HP, FIRE_DRAGON_DMG, FIRE_WIZARD_HP, FIRE_WIZARD_DMG, GROUND_TITAN_HP, \
    GROUND_TITAN_DMG, ICE_WIZARD_HP, ICE_WIZARD_DMG, MERMAID_HP, MERMAID_DMG, SHADOW_MONSTER_HP, SHADOW_MONSTER_DMG, \
    STONE_DWARF_HP, STONE_DWARF_DMG, VS_BUTTON_COORDINATES, VS_BUTTON_SIZE, FANTASY_FONT_SIZE, \
    WAVES_COUNTER_RIGHT_CORNER_POS, NAME_OF_THE_GAME, MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR

import pygame

from Source.card import Card


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_icon(pygame.image.load('Resources/Images/icon.jpg'))

pygame.display.set_caption(NAME_OF_THE_GAME)

pygame.surfarray.use_arraytype('numpy')

menu = Background(pygame.image.load('Resources/Images/DeckMap.jpeg'))
battle_button = Button(pygame.image.load('Resources/Images/BattleButton.png').convert_alpha(screen), BATTLE_BUTTON_COORDINATES,
                       BATTLE_BUTTON_SIZE)

menu_sprites = pygame.sprite.Group(menu, battle_button)

battle = Background(pygame.image.load('Resources/Images/MainGameTable.jpeg'))

default_hp_bar = Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS)
blazing_herald_raw = Card(pygame.image.load('Resources/Images/BlazingHerald.jpeg'),
                          pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                          BLAZING_HERALD_HP, BLAZING_HERALD_DMG)

electro_wizard_raw = Card(pygame.image.load('Resources/Images/ElectroWizard.jpeg'),
                          pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                          ELECTRO_WIZARD_HP, ELECTRO_WIZARD_DMG)

fire_dragon_raw = Card(pygame.image.load('Resources/Images/FireDragon.jpeg'),
                       pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                       FIRE_DRAGON_HP, FIRE_DRAGON_DMG)

fire_wizard_raw = Card(pygame.image.load('Resources/Images/FireWizard.jpeg'),
                       pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                       FIRE_WIZARD_HP, FIRE_WIZARD_DMG)

ground_titan_raw = Card(pygame.image.load('Resources/Images/GroundTitan.jpeg'),
                        pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                        GROUND_TITAN_HP, GROUND_TITAN_DMG)

ice_wizard_raw = Card(pygame.image.load('Resources/Images/IceWizard.jpeg'),
                      pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                      ICE_WIZARD_HP, ICE_WIZARD_DMG)

mermaid_raw = Card(pygame.image.load('Resources/Images/Mermaid.jpeg'),
                   pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                   MERMAID_HP, MERMAID_DMG)

shadow_monster_raw = Card(pygame.image.load('Resources/Images/ShadowMonster.jpeg'),
                          pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                          SHADOW_MONSTER_HP, SHADOW_MONSTER_DMG)

stone_dwarf_raw = Card(pygame.image.load('Resources/Images/StoneDwarf.jpeg'),
                       pygame.image.load('Resources/Images/CardOrnament.png').convert_alpha(screen), BASIC_OUTLINE_THICKNESS, Bar(pygame.image.load('Resources/Images/HitpointBar.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS), [Point(pygame.image.load('Resources/Images/Hitpoint.png'), DEFAULT_HP_BAR_SIZE, DEFAULT_HP_BAR_THICKNESS) for _ in range(MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                       STONE_DWARF_HP, STONE_DWARF_DMG)

vs_button = Button(pygame.image.load('Resources/Images/VSButton.png'), VS_BUTTON_COORDINATES, VS_BUTTON_SIZE)

draft_map = Background(pygame.image.load('Resources/Images/DraftMap.jpeg'))

draft_sprites = pygame.sprite.Group(draft_map, vs_button)

pygame.font.init()
fantasy_font = pygame.font.Font("Resources/Fonts/FantasyCapitals.otf", size=int(FANTASY_FONT_SIZE))
waves_counter = String(fantasy_font.render("Wave: 0", None, pygame.Color(204, 44, 52)), (WAVES_COUNTER_RIGHT_CORNER_POS[0] - fantasy_font.size("Wave: 100")[0], WAVES_COUNTER_RIGHT_CORNER_POS[1]))
stage = str
element = str