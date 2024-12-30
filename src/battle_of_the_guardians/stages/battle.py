from pygame.sprite import Group

from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.buffer import buffer_deck
from src.battle_of_the_guardians.controllers.battle_controller import BattleController
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.battle_sprites import BattleSprites


class Battle:
    def __init__(self) -> None:
        self.sprites: BattleSprites = BattleSprites(buffer_deck)
        self.game_controller: BattleController = BattleController(self.sprites.deck, self.sprites.opps, [self.sprites.shadow], self.sprites.waves_counter)
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
        Group(self.sprites.battle).draw(screen)
        [Group(card.to_draw_on_battle()).draw(screen) for card in self.sprites.deck]
        [Group(card.to_draw_on_battle()).draw(screen) for card in self.sprites.opps]
        Group(self.sprites.waves_counter).draw(screen)
        Group(self.sprites.energy_bar.to_draw()).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            self.game_controller.new_wave()
        self.is_this_the_first_iteration = False
        return self.handle_events(actions)
