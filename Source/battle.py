import pygame
from Source.action import Action
from Source.background import Background
from Source.bar import Bar
from Source.battle_sprites import BattleSprites
from Source.buffer import buffer_deck
from Source.card import Card
from Source.config import ALL_CARD_COORDINATES, RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR
from Source.defines import element, stage
from Source.string import String

class Battle:
    def __init__(self) -> None:
        self.sprites: BattleSprites = BattleSprites(buffer_deck)
        self.waves_counter: int = 0
        self.objects: dict[element: Background | list[Card] | list[Bar] | String] = {
            "background": self.sprites.battle,
            "deck": self.sprites.deck,
            "waves_counter": self.sprites.waves_counter,
            "opps": [],
        }

    def draw(self, screen) -> None:
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        for card in self.objects["deck"]:
            pygame.sprite.Group(card.to_draw_on_battle()).draw(screen)
        pygame.sprite.Group(self.objects["waves_counter"]).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        for card_index in range(len(self.objects["deck"])):
            self.objects["deck"][card_index].place(ALL_CARD_COORDINATES[card_index])
            self.objects["deck"][card_index].place_hp_bar(RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR)
            self.objects["deck"][card_index].current_health = 2000
        return "battle"
