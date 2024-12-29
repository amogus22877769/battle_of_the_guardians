from pygame.sprite import Group

from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.menu_sprites import MenuSprites


class Menu:
    def __init__(self) -> None:
        self.sprites: MenuSprites = MenuSprites()

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.battle_button.rect.collidepoint(action.value):
                        return "draft"
                case "resize":
                    self.sprites.update(*action.value)
        return "menu"

    def draw(self, screen) -> None:
        Group(self.sprites.menu, self.sprites.battle_button).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        return self.handle_updates(actions)
