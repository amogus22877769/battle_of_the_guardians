import pygame
from Source.action import Action
from Source.buffer import buffer_deck
from Source.card import Card
from Source.classes import Background, Bar, String
from Source.config import ALL_CARD_COORDINATES, DISTANCE_BETWEEN_CARD_AND_HP_BAR
from Source.init import stage, element, battle, waves_counter, screen


class Battle:
    def __init__(self) -> None:
        self.waves_counter: int = 0
        self.objects: dict[element: Background | list[Card] | list[Bar] | String] = {
            "background": battle,
            "deck": [],
            "waves_counter": waves_counter,
        }
        self.is_this_the_first_iteration: bool = True
    def draw(self) -> None:
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        pygame.sprite.Group([[card.sprite, card.hp_bar, card.hitpoints] for card in self.objects["deck"]]).draw(screen)
        pygame.sprite.Group(self.objects["waves_counter"]).draw(screen)
    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            for card in buffer_deck:
                self.objects["deck"].append(card)
        self.is_this_the_first_iteration = False
        for card_index in range(len(self.objects["deck"])):
            self.objects["deck"][card_index].place(ALL_CARD_COORDINATES[card_index])
            self.objects["deck"][card_index].place_hp_bar(DISTANCE_BETWEEN_CARD_AND_HP_BAR)
        return "battle"