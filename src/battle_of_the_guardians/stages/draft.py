from pygame.sprite import Group

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
                        self.controller.pick(self.sprites.cards[self.controller.local_stage_multiplied_by_two])
                    elif self.sprites.cards[self.controller.local_stage_multiplied_by_two + 1].outline.rect.collidepoint(
                            action.value):
                        self.controller.pick(self.sprites.cards[self.controller.local_stage_multiplied_by_two + 1])
                case "resize":
                    self.sprites.update(*action.value)
        return self.controller.stage

    def draw(self, screen) -> None:
        Group(self.sprites.draft_map).draw(screen)
        Group(self.sprites.vs_button).draw(screen)
        Group(self.sprites.cards[self.controller.local_stage_multiplied_by_two].to_draw_on_draft(),
              self.sprites.cards[self.controller.local_stage_multiplied_by_two + 1].to_draw_on_draft()).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        return self.handle_events(actions)
