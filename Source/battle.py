import pygame
from Source.action import Action
from Source.background import Background
from Source.bar import Bar
from Source.battle_sprites import BattleSprites
from Source.buffer import buffer_deck
from Source.card import Card
from Source.config import ALL_CARD_COORDINATES, RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR, ALL_EVEN_OPPS_COORDINATES
from Source.defines import element, stage
from Source.game_controller import GameController
from Source.string import String


class Battle:
    def __init__(self) -> None:
        self.sprites: BattleSprites = BattleSprites(buffer_deck)
        self.game_controller: GameController = GameController(self.sprites.deck, self.sprites.opps, [self.sprites.shadow], self.sprites.waves_counter)
        self.is_this_the_first_iteration: bool = True

    def handle_events(self, actions: list[Action]) -> stage:

        for action in actions:
            match action.kind:
                case 'resize':
                    pass
                    self.sprites.update(action.value)
                case 'click':
                    for card in self.sprites.deck:
                        if card.outline.rect.collidepoint(action.value):
                            self.game_controller.ready(card)
                    for opp in self.sprites.opps:
                        if opp.outline.rect.collidepoint(action.value):
                            self.game_controller.attack(opp)
        return 'battle'

    def draw(self, screen) -> None:
        pygame.sprite.Group(self.sprites.battle).draw(screen)
        [pygame.sprite.Group(card.to_draw_on_battle()).draw(screen) for card in self.sprites.deck]
        [pygame.sprite.Group(card.to_draw_on_battle()).draw(screen) for card in self.sprites.opps]
        pygame.sprite.Group(self.sprites.waves_counter).draw(screen)
        pygame.sprite.Group(self.sprites.energy_bar.to_draw()).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            self.game_controller.new_wave()
        self.is_this_the_first_iteration = False
        return self.handle_events(actions)
