import pygame
from classes import *
from config import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

menu = Background(pygame.image.load('Images/DeckMap.jpeg'))
battle_button = Button(pygame.image.load('Images/BattleButton.png').convert_alpha(screen), BATTLE_BUTTON_COORDINATES, BATTLE_BUTTON_SIZE)

menu_sprites = pygame.sprite.Group(menu, battle_button)

battle = Background(pygame.image.load('Images/MainGameTable.jpeg'))

blazing_herald_raw = Card(pygame.image.load('Images/BlazingHerald.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

electro_wizard_raw = Card(pygame.image.load('Images/ElectroWizard.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

fire_dragon_raw = Card(pygame.image.load('Images/FireDragon.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

fire_wizard_raw = Card(pygame.image.load('Images/FireWizard.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

ground_titan_raw = Card(pygame.image.load('Images/GroundTitan.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

ice_wizard_raw = Card(pygame.image.load('Images/IceWizard.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

mermaid_raw = Card(pygame.image.load('Images/Mermaid.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

shadow_monster_raw = Card(pygame.image.load('Images/ShadowMonster.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

stone_dwarf_raw = Card(pygame.image.load('Images/StoneDwarf.jpeg'), pygame.image.load('Images/CardOrnament.png').convert_alpha(screen), OUTLINE_THICKNESS)

raw_card_sprites = pygame.sprite.Group(blazing_herald_raw, electro_wizard_raw, fire_dragon_raw, fire_wizard_raw, ground_titan_raw, ice_wizard_raw, mermaid_raw, stone_dwarf_raw)
vs_button = Button(pygame.image.load('Images/VSButton.png'), VS_BUTTON_COORDINATES, VS_BUTTON_SIZE)

draft_map = Background(pygame.image.load('Images/DraftMap.jpeg'))

draft_sprites = pygame.sprite.Group(draft_map, vs_button)