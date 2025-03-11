from frontend.src.battle_of_the_guardians.action import Action
from frontend.src.battle_of_the_guardians.buffer import buffer_deck
from frontend.src.battle_of_the_guardians.controllers.battle_controller import BattleController
from frontend.src.battle_of_the_guardians.defines import stage
from frontend.src.battle_of_the_guardians.sprites_loaders.battle_sprites import BattleSprites


class Battle:
    def __init__(self) -> None:
        self.sprites: BattleSprites = BattleSprites(buffer_deck)
        self.game_controller: BattleController = BattleController(self.sprites.deck,
                                                                  self.sprites.opponents,
                                                                  self.sprites.opposition,
                                                                  self.sprites.waves_counter,
                                                                  self.sprites.energy_bar,
                                                                  self.sprites.strings,
                                                                  self.sprites.effects)

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
                    for opp in self.sprites.opponents:
                        if opp.outline.rect.collidepoint(action.value):
                            self.game_controller.hit(opp)
        if not self.game_controller.lost:
            return 'battle'
        else:
            self.game_controller.clear()
            return 'you_lost'

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=[
            (self.sprites.battle.image, self.sprites.battle.rect),
            (self.sprites.waves_counter.image, self.sprites.waves_counter.rect),
            *self.sprites.energy_bar.to_draw(),
            *[pair
              for card_pairs in [card.to_draw_on_battle() for card in self.sprites.deck]
              for pair in card_pairs],
            *[pair
              for opponent_pairs in [opponent.to_draw_on_battle() for opponent in self.sprites.opponents]
              for pair in opponent_pairs],
            *[(string.image, string.rect) for string in self.sprites.strings],
            *[(effect.image, effect.rect)
              for group_of_effects in self.sprites.effects.values()
              for effect in group_of_effects.values()]])

    def update(self, actions: list[Action]) -> stage:
        if self.game_controller.is_this_the_first_iteration:
            self.game_controller.new_wave()
        self.game_controller.is_this_the_first_iteration = False
        return self.handle_events(actions)
