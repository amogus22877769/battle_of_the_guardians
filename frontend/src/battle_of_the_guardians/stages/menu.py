from frontend.src.battle_of_the_guardians.action import Action
from frontend.src.battle_of_the_guardians.interfaces import stage
from frontend.src.battle_of_the_guardians.sprites_loaders.menu_sprites import MenuSprites


class Menu:
    def __init__(self) -> None:
        self.sprites: MenuSprites = MenuSprites()
        self.is_this_the_first_iteration: bool = True

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.battle_button.collide_point(*action.value):
                        return "draft"
                    if self.sprites.leaderboard_button.collide_point(*action.value):
                        return "leaderboard"
                case "resize":
                    self.sprites.update(*action.value)
        return "menu"

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=((self.sprites.menu.image, self.sprites.menu.rect),
                                    (self.sprites.battle_button.image, self.sprites.battle_button.rect),
                                    (self.sprites.leaderboard_button.image, self.sprites.leaderboard_button.rect)))

    def update(self, actions: list[Action]) -> stage:
        return self.handle_updates(actions)
