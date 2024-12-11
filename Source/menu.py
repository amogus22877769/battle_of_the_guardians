import pygame

from Source.action import Action
from Source.defines import stage
from Source.menu_sprites import MenuSprites


class Menu:
    def __init__(self) -> None:
        self.sprites: MenuSprites = MenuSprites()
        self.objects = {
            "background": self.sprites.menu,
            "buttons": {"battle_button": self.sprites.battle_button}
        }

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.objects["buttons"]["battle_button"].rect.collidepoint(action.value):
                        return "draft"
                case "resize":
                    self.sprites.update(*action.value)
        return "menu"

    def draw(self, screen) -> pygame.sprite.Group:
        pygame.sprite.Group(self.objects["background"], self.objects["buttons"].values()).draw(screen)

    def update(self, actions: list[Action]) -> stage:
        return self.handle_updates(actions)
