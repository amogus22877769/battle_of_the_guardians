from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.buffer import score
from src.battle_of_the_guardians.controllers.front import set_score
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.you_lost_sprites import YouLostSprites


class YouLost:
    def __init__(self):
        self.sprites = YouLostSprites()
        self.is_this_the_first_iteration: bool = True

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.return_button.collide_point(*action.value):
                        self.is_this_the_first_iteration = True
                        return "menu"
                    if self.sprites.share.collide_point(*action.value):
                        res = set_score()['result']
                        if res != 'success'
                case "resize":
                    self.sprites.update(action.value)
        return "you_lost"

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=((self.sprites.background.image, self.sprites.background.rect),
                                    (self.sprites.return_button.image, self.sprites.return_button.rect),
                                    (self.sprites.you_lost.image, self.sprites.you_lost.rect),
                                    (self.sprites.result.image, self.sprites.result.rect),
                                    (self.sprites.share.image, self.sprites.share.rect)))

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            self.sprites.result.text = self.sprites.result.text[:12] + score[0]
            self.is_this_the_first_iteration = False
        return self.handle_updates(actions)
