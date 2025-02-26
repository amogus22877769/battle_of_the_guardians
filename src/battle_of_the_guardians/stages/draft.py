from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.controllers.draft_controller import DraftController
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.draft_sprites import DraftSprites


class Draft:
    def __init__(self) -> None:
        self.sprites = DraftSprites()
        self.controller = DraftController(self.sprites.cards)

    def handle_events(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.cards[self.controller.local_stage_multiplied_by_two].outline.rect.collidepoint(
                            action.value):
                        self.controller.pick('left')
                    elif self.sprites.cards[
                        self.controller.local_stage_multiplied_by_two + 1].outline.rect.collidepoint(
                            action.value):
                        self.controller.pick('right')
                case "resize":
                    self.sprites.update(*action.value)
        if self.controller.stage == 'battle':
            self.controller.stage = 'draft'
            return 'battle'
        return 'draft'

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=[
            (self.sprites.draft_map.image, self.sprites.draft_map.rect),
            (self.sprites.vs_button.image, self.sprites.vs_button.rect),
            *self.sprites.cards[self.controller.local_stage_multiplied_by_two].to_draw_on_draft(),
            *self.sprites.cards[self.controller.local_stage_multiplied_by_two + 1].to_draw_on_draft()])

    def update(self, actions: list[Action]) -> stage:
        if self.controller.is_this_the_first_iteration:
            self.controller.place()
            self.controller.is_this_the_first_iteration = False
            print('first')
        return self.handle_events(actions)
