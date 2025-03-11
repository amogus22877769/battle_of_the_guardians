from random import shuffle

from frontend.src.battle_of_the_guardians.animations import Animation
from frontend.src.battle_of_the_guardians.buffer import buffer_deck
from frontend.src.battle_of_the_guardians.config import RELATIVE_LEFT_DRAFT_CARD_COORDINATES, \
    RELATIVE_RIGHT_DRAFT_CARD_COORDINATES, RELATIVE_CARD_SIZE, \
    DRAFT_PICK_ANIMATION_DURATION
from frontend.src.battle_of_the_guardians.structures.card import Card


class DraftController:
    def __init__(self, cards: list[Card]) -> None:
        self.cards: list[Card] = cards
        self.deck: list[Card] = list()
        self.local_stage_multiplied_by_two: int = 0
        self.stage = 'draft'
        shuffle(self.cards)
        self.place()
        self.flags: dict[str, set[Card]] = {'animating': set()}
        self.is_this_the_first_iteration: bool = True

    def pick(self, position: str):
        left_card: Card = self.cards[self.local_stage_multiplied_by_two]
        right_card: Card = self.cards[self.local_stage_multiplied_by_two + 1]
        if not self.flags['animating']:
            if position == 'left':
                Animation([left_card.sprite, left_card.outline],
                          DRAFT_PICK_ANIMATION_DURATION,
                          (RELATIVE_CARD_SIZE[0] / 2, RELATIVE_CARD_SIZE[1] / 2)).start(on_stop=self.next_stage)
                Animation([right_card.sprite, right_card.outline],
                          DRAFT_PICK_ANIMATION_DURATION,
                          (1 - RELATIVE_CARD_SIZE[0] / 2, 1 - RELATIVE_CARD_SIZE[1] / 2)).start()
                self.deck.append(left_card)
            else:
                Animation([left_card.sprite, left_card.outline],
                          DRAFT_PICK_ANIMATION_DURATION,
                          (RELATIVE_CARD_SIZE[0] / 2, 1 - RELATIVE_CARD_SIZE[1] / 2)).start(on_stop=self.next_stage)
                Animation([right_card.sprite, right_card.outline],
                          DRAFT_PICK_ANIMATION_DURATION,
                          (1 - RELATIVE_CARD_SIZE[0] / 2, RELATIVE_CARD_SIZE[1] / 2)).start()
                self.deck.append(right_card)
            self.flags['animating'].update([left_card, right_card])

    def next_stage(self) -> None:
        self.local_stage_multiplied_by_two += 2
        if self.local_stage_multiplied_by_two == 8:
            buffer_deck.clear()
            buffer_deck.extend(self.deck)
            self.clear()
            self.stage = 'battle'
        self.flags['animating'].clear()
        self.place()

    def place(self):
        self.cards[self.local_stage_multiplied_by_two].place(RELATIVE_LEFT_DRAFT_CARD_COORDINATES)
        self.cards[self.local_stage_multiplied_by_two + 1].place(RELATIVE_RIGHT_DRAFT_CARD_COORDINATES)
        print(self.cards[self.local_stage_multiplied_by_two], self.cards[self.local_stage_multiplied_by_two + 1])
        print(self.cards[self.local_stage_multiplied_by_two].sprite.relative_center_coordinates)

    def clear(self):
        self.local_stage_multiplied_by_two = 0
        shuffle(self.cards)
        self.deck.clear()
        self.is_this_the_first_iteration = True
