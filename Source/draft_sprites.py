import pygame

from Source.card import Card
from Source.classes import Bar, Button, Background, Point
from Source.config import Config


class DraftSprites:
    def __init__(self, local_config: Config) -> None:
        self.config = local_config
        self.fantasy_font_for_card_health_using_default_hp_bar: pygame.font.Font = pygame.font.Font("Resources/Fonts/FantasyCapitals.otf", size=int(self.config.FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR))
        self.blazing_herald_raw: Card = Card(pygame.image.load('Resources/Images/BlazingHerald.jpeg'),
                                             pygame.image.load('Resources/Images/CardOrnament.png'),
                                             self.config.BASIC_OUTLINE_THICKNESS,
                                             Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                            self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                            Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                                  self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                            range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                             self.config.BLAZING_HERALD_HP, self.config.BLAZING_HERALD_DMG,
                                             self.fantasy_font_for_card_health_using_default_hp_bar)

        self.electro_wizard_raw: Card = Card(pygame.image.load('Resources/Images/ElectroWizard.jpeg'),
                                             pygame.image.load('Resources/Images/CardOrnament.png'),
                                             self.config.BASIC_OUTLINE_THICKNESS,
                                             Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                            self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                            Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                                  self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                            range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                             self.config.ELECTRO_WIZARD_HP, self.config.ELECTRO_WIZARD_DMG,
                                             self.fantasy_font_for_card_health_using_default_hp_bar)

        self.fire_dragon_raw: Card = Card(pygame.image.load('Resources/Images/FireDragon.jpeg'),
                                          pygame.image.load('Resources/Images/CardOrnament.png'),
                                          self.config.BASIC_OUTLINE_THICKNESS,
                                          Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                         self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                         Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                               self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                         range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                          self.config.FIRE_DRAGON_HP, self.config.FIRE_DRAGON_DMG,
                                          self.fantasy_font_for_card_health_using_default_hp_bar)

        self.fire_wizard_raw: Card = Card(pygame.image.load('Resources/Images/FireWizard.jpeg'),
                                          pygame.image.load('Resources/Images/CardOrnament.png'),
                                          self.config.BASIC_OUTLINE_THICKNESS,
                                          Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                         self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                         Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                               self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                         range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                          self.config.FIRE_WIZARD_HP, self.config.FIRE_WIZARD_DMG,
                                          self.fantasy_font_for_card_health_using_default_hp_bar)

        self.ground_titan_raw: Card = Card(pygame.image.load('Resources/Images/GroundTitan.jpeg'),
                                           pygame.image.load('Resources/Images/CardOrnament.png'),
                                           self.config.BASIC_OUTLINE_THICKNESS,
                                           Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                          self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                          Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                                self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                          range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                           self.config.GROUND_TITAN_HP, self.config.GROUND_TITAN_DMG,
                                           self.fantasy_font_for_card_health_using_default_hp_bar)

        self.ice_wizard_raw: Card = Card(pygame.image.load('Resources/Images/IceWizard.jpeg'),
                                         pygame.image.load('Resources/Images/CardOrnament.png'),
                                         self.config.BASIC_OUTLINE_THICKNESS,
                                         Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                        self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                        Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                              self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                        range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                         self.config.ICE_WIZARD_HP, self.config.ICE_WIZARD_DMG,
                                         self.fantasy_font_for_card_health_using_default_hp_bar)

        self.mermaid_raw: Card = Card(pygame.image.load('Resources/Images/Mermaid.jpeg'),
                                      pygame.image.load('Resources/Images/CardOrnament.png'),
                                      self.config.BASIC_OUTLINE_THICKNESS,
                                      Bar(pygame.image.load('Resources/Images/HitpointBar.png'), self.config.DEFAULT_HP_BAR_SIZE,
                                     self.config.DEFAULT_HP_BAR_THICKNESS),
                                      Button(pygame.image.load('Resources/Images/HitpointsIcon.png'),
                                        (0, 0), (self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                                                 self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)),
                                      [Point(pygame.image.load('Resources/Images/Hitpoint.png'), self.config.DEFAULT_HP_BAR_SIZE,
                                        self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                  range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                      self.config.MERMAID_HP, self.config.MERMAID_DMG,
                                      self.fantasy_font_for_card_health_using_default_hp_bar)

        self.shadow_monster_raw: Card = Card(pygame.image.load('Resources/Images/ShadowMonster.jpeg'),
                                             pygame.image.load('Resources/Images/RedCardOrnament.png'),
                                             self.config.BASIC_OUTLINE_THICKNESS,
                                             Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                            self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                            Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                                  self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                            range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                             self.config.SHADOW_MONSTER_HP, self.config.SHADOW_MONSTER_DMG,
                                             self.fantasy_font_for_card_health_using_default_hp_bar)

        self.stone_dwarf_raw: Card = Card(pygame.image.load('Resources/Images/StoneDwarf.jpeg'),
                                          pygame.image.load('Resources/Images/CardOrnament.png'),
                                          self.config.BASIC_OUTLINE_THICKNESS,
                                          Bar(pygame.image.load('Resources/Images/HitpointBar.png'),
                                         self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS), Button(
                pygame.image.load('Resources/Images/HitpointsIcon.png'), (0, 0), (
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE,
                    self.config.DEFAULT_HP_BAR_SIZE[1] * self.config.RELATIVE_HITPOINTS_ICON_SIZE)), [
                                         Point(pygame.image.load('Resources/Images/Hitpoint.png'),
                                               self.config.DEFAULT_HP_BAR_SIZE, self.config.DEFAULT_HP_BAR_THICKNESS) for _ in
                                         range(self.config.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR)],
                                          self.config.STONE_DWARF_HP, self.config.STONE_DWARF_DMG,
                                          self.fantasy_font_for_card_health_using_default_hp_bar)

        self.vs_button: Button = Button(pygame.image.load('Resources/Images/VSButton.png'), self.config.VS_BUTTON_COORDINATES,
                                   self.config.VS_BUTTON_SIZE)

        self.draft_map: Background = Background(pygame.image.load('Resources/Images/DraftMap.jpeg'), (self.config.WIDTH, self.config.HEIGHT))

    def update(self, new_width: int, new_height: int) -> None:
        self.config.update_const(new_width, new_height)
        self.fantasy_font_for_card_health_using_default_hp_bar: pygame.font.Font = pygame.font.Font("Resources/Fonts/FantasyCapitals.otf", size=int(self.config.FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR))

        self.draft_map.update((self.config.WIDTH, self.config.HEIGHT))
        self.vs_button.update(self.config.VS_BUTTON_COORDINATES, self.config.VS_BUTTON_SIZE)

