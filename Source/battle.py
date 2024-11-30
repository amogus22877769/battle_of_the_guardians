import pygame
from Source.action import Action
from Source.buffer import buffer_deck
from Source.card import Card
from Source.classes import Background, Bar, String


class Battle:
    def __init__(self) -> None:
        self.waves_counter: int = 0
        self.objects: dict[element: Background | list[Card] | list[Bar] | String] = {
            "background": battle,
            "deck": [],
            "opps": [shadow_monster_raw],
        }
        self.is_this_the_first_iteration: bool = True

    def draw(self) -> None:
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        pygame.sprite.Group([[card.sprite, card.hp_bar, card.hitpoints, card.health_sprite, card.hp_icon] for card in
                             self.objects["deck"]]).draw(screen)
        pygame.sprite.Group(String(fantasy_font_for_waves_counter.render(f'Wave: {self.waves_counter}', None, DARK_RED),
                                   (WAVES_COUNTER_RIGHT_CORNER_POS[0] -
                                    fantasy_font_for_waves_counter.size(f'Wave: {self.waves_counter}')[0],
                                    WAVES_COUNTER_RIGHT_CORNER_POS[1]))).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            for card in buffer_deck:
                self.objects["deck"].append(card)
        self.is_this_the_first_iteration = False
        for card_index in range(len(self.objects["deck"])):
            self.objects["deck"][card_index].place(ALL_CARD_COORDINATES[card_index])
            self.objects["deck"][card_index].place_hp_bar(DISTANCE_BETWEEN_CARD_AND_HP_BAR)
            self.objects["deck"][card_index].current_health = 2000
        return "battle"
