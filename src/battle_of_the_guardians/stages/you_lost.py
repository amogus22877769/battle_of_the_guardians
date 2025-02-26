from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.you_lost_sprites import YouLostSprites


class YouLost:
    def __init__(self):
        self.sprites = YouLostSprites()

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.return_button.collide_point(*action.value):
                        return "menu"
                case "resize":
                    self.sprites.update(action.value)
        return "you_lost"

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=((self.sprites.background.image, self.sprites.background.rect),
                                    (self.sprites.return_button.image, self.sprites.return_button.rect),
                                    (self.sprites.you_lost.image, self.sprites.you_lost.rect)))

    def update(self, actions: list[Action]) -> stage:
        return self.handle_updates(actions)
