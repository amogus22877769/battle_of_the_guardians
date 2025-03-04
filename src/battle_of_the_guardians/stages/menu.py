import pygame.key

from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.controllers.input import Input
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.sprites_loaders.menu_sprites import MenuSprites


class Menu:
    def __init__(self) -> None:
        self.sprites: MenuSprites = MenuSprites()
        self.input = Input(self.sprites.box, self.sprites.username)
        self.is_this_the_first_iteration: bool = True

    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.battle_button.collide_point(*action.value):
                        return "draft"
                case "resize":
                    self.sprites.update(*action.value)
                case 'text':
                    self.input.update_username(action.value)
                case 'backspace':
                    self.input.backspace()
        return "menu"

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=((self.sprites.menu.image, self.sprites.menu.rect),
                                    (self.sprites.battle_button.image, self.sprites.battle_button.rect),
                                    (self.input.box.image, self.input.box.rect),
                                    (self.input.username.image, self.input.username.rect)))

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            pygame.key.start_text_input()
        return self.handle_updates(actions)
