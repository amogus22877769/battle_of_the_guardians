from random import shuffle

from pygame.sprite import Group

from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.buffer import buffer_deck
from src.battle_of_the_guardians.config import RELATIVE_LEFT_DRAFT_CARD_COORDINATES, \
    RELATIVE_RIGHT_DRAFT_CARD_COORDINATES
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.draft_sprites import DraftSprites
from src.battle_of_the_guardians.structures.card import Card


class Draft:
    def __init__(self) -> None:
        self.sprites = DraftSprites()
        shuffle(self.sprites.deck)
        self.stage_multiplied_by_two: int = 0
        self.deck: list[Card] = []
        self.is_this_the_first_iteration_on_stage: bool = True

    def handle_events(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.deck[self.stage_multiplied_by_two].sprite.rect.collidepoint(action.value):
                        self.deck.append(self.sprites.deck[self.stage_multiplied_by_two])
                        self.stage_multiplied_by_two += 2
                        self.is_this_the_first_iteration_on_stage = True
                    elif self.sprites.deck[self.stage_multiplied_by_two + 1].sprite.rect.collidepoint(action.value):
                        self.deck.append(self.sprites.deck[self.stage_multiplied_by_two + 1])
                        self.stage_multiplied_by_two += 2
                        self.is_this_the_first_iteration_on_stage = True
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
        Group(self.sprites.draft_map).draw(screen)
        Group(self.sprites.vs_button).draw(screen)
        Group(self.sprites.deck[self.stage_multiplied_by_two].to_draw_on_draft(),
                            self.sprites.deck[self.stage_multiplied_by_two + 1].to_draw_on_draft()).draw(screen)

    def update(self, actions: list[Action]) -> str:
        if self.is_this_the_first_iteration_on_stage is True:
            self.sprites.deck[self.stage_multiplied_by_two].place(RELATIVE_LEFT_DRAFT_CARD_COORDINATES)
            self.sprites.deck[self.stage_multiplied_by_two + 1].place(RELATIVE_RIGHT_DRAFT_CARD_COORDINATES)
        self.is_this_the_first_iteration_on_stage = False
        return self.handle_events(actions)

    def clear(self) -> None:
        shuffle(self.sprites.deck)
        self.stage_multiplied_by_two = 0
        self.deck.clear()
        self.is_this_the_first_iteration_on_stage = True
