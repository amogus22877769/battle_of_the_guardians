from random import shuffle

from src.battle_of_the_guardians.buffer import buffer_deck
from src.battle_of_the_guardians.config import RELATIVE_LEFT_DRAFT_CARD_COORDINATES, \
    RELATIVE_RIGHT_DRAFT_CARD_COORDINATES
from src.battle_of_the_guardians.structures.card import Card


class DraftController:
    def __init__(self, cards: list[Card]) -> None:
        self.cards: list[Card] = cards
        self.deck: list[Card] = list()
        self.local_stage_multiplied_by_two: int = 0
        self.stage = 'draft'
        shuffle(self.cards)
        self.place()

    def pick(self, card):
        self.local_stage_multiplied_by_two += 2
        self.deck.append(card)
        if self.local_stage_multiplied_by_two == 8:
            buffer_deck.extend(self.deck)
            self.clear()
            self.stage = 'battle'
        self.place()

    def place(self):
        self.cards[self.local_stage_multiplied_by_two].place(RELATIVE_LEFT_DRAFT_CARD_COORDINATES)
        self.cards[self.local_stage_multiplied_by_two + 1].place(RELATIVE_RIGHT_DRAFT_CARD_COORDINATES)

    def clear(self):
        self.local_stage_multiplied_by_two = 0
        shuffle(self.cards)