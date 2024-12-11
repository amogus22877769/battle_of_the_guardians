import pygame

from Source.action import Action
from Source.background import Background
from Source.buffer import buffer_deck
from Source.button import Button
from Source.card import Card
from Source.config import RELATIVE_LEFT_DRAFT_CARD_COORDINATES, RELATIVE_RIGHT_DRAFT_CARD_COORDINATES
from Source.draft_sprites import DraftSprites
from Source.defines import stage, element
import random


class Draft:
    def __init__(self) -> None:
        self.sprites = DraftSprites()
        self.objects: dict[element: Background | dict[element: Button] | list[Card]] = {"background": self.sprites.draft_map,
                                                                                        "buttons": {
                                                                                            "vs_button": self.sprites.vs_button},
                                                                                        "cards": self.sprites.deck}
        random.shuffle(self.objects["cards"])
        self.stage_multiplied_by_two: int = 0
        self.deck: list[Card] = []

    def handle_events(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.objects["cards"][self.stage_multiplied_by_two].sprite.rect.collidepoint(action.value):
                        self.deck.append(self.objects["cards"][self.stage_multiplied_by_two])
                        self.stage_multiplied_by_two += 2
                    elif self.objects["cards"][self.stage_multiplied_by_two + 1].sprite.rect.collidepoint(action.value):
                        self.deck.append(self.objects["cards"][self.stage_multiplied_by_two + 1])
                        self.stage_multiplied_by_two += 2
                case "resize":
                    self.sprites.update(*action.value)
        if self.stage_multiplied_by_two == 8:
            for card in self.deck:
                buffer_deck.append(card)
            self.clear()
            return "battle"
        else:
            return "draft"

    def draw(self, screen) -> None:
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        pygame.sprite.Group(self.objects["buttons"].values()).draw(screen)
        pygame.sprite.Group(self.objects["cards"][self.stage_multiplied_by_two].to_draw_on_draft(),
                            self.objects["cards"][self.stage_multiplied_by_two + 1].to_draw_on_draft()).draw(screen)

    def update(self, actions: list[Action]) -> str:
        self.objects["cards"][self.stage_multiplied_by_two].place(RELATIVE_LEFT_DRAFT_CARD_COORDINATES)
        self.objects["cards"][self.stage_multiplied_by_two + 1].place(RELATIVE_RIGHT_DRAFT_CARD_COORDINATES)
        return self.handle_events(actions)

    def clear(self) -> None:
        random.shuffle(self.objects["cards"])
        self.stage_multiplied_by_two = 0
        self.deck.clear()
