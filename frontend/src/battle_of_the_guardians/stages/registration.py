from pathlib import Path

import pygame.key

from frontend.src.battle_of_the_guardians.action import Action
from frontend.src.battle_of_the_guardians.controllers.front import registration
from frontend.src.battle_of_the_guardians.controllers.input import Input
from frontend.src.battle_of_the_guardians.interfaces import stage
from frontend.src.battle_of_the_guardians.sprites_loaders.registration_sprites import RegistrationSprites


class Registration:
    def __init__(self) -> None:
        self.sprites: RegistrationSprites = RegistrationSprites()
        self.username_input = Input(self.sprites.username_box, self.sprites.username)
        self.password_input = Input(self.sprites.password_box, self.sprites.password)
        self.username_input_is_active: bool = True
        self.is_this_the_first_iteration: bool = True

    def handle_updates(self, actions: list[Action]) -> stage:
        if self.sprites.enter:
            actions.append(Action('enter'))
        for action in actions:
            match action.kind:
                case "click":
                    if self.sprites.username_box.rect.collidepoint(action.value):
                        self.username_input_is_active = True
                    if self.sprites.password_box.rect.collidepoint(action.value):
                        self.username_input_is_active = False
                case "resize":
                    self.sprites.update(action.value)
                case 'text':
                    self.username_input.update(action.value) if self.username_input_is_active else self.password_input.update(action.value)
                case 'backspace':
                    self.username_input.backspace() if self.username_input_is_active else self.password_input.backspace()
                case 'enter':
                    if not Path('auth_data.txt').is_file():
                        with open('auth_data.txt', 'w') as f:
                            f.write(f'{self.sprites.username.text}\n{self.sprites.password.text}')
                        f.close()
                    res = registration()['result']
                    if res == 'success':
                        pygame.key.stop_text_input()
                        if not Path('auth_data.txt').is_file():
                            with open('auth_data.txt', 'w') as f:
                                f.write(f'{self.sprites.username.text}\n{self.sprites.password.text}')
                            f.close()
                        self.is_this_the_first_iteration = True
                        return 'menu'
                    else:
                        self.sprites.try_again.text = 'TRY AGAIN'
                        return 'registration'
        return "registration"

    def draw(self, screen) -> None:
        screen.blits(blit_sequence=((self.sprites.background.image, self.sprites.background.rect),
                                    (self.sprites.username_box.image, self.sprites.username_box.rect),
                                    (self.sprites.username.image, self.sprites.username.rect),
                                    (self.sprites.password_box.image, self.sprites.password_box.rect),
                                    (self.sprites.password.image, self.sprites.password.rect),
                                    (self.sprites.registration_string.image, self.sprites.registration_string.rect),
                                    (self.sprites.username_string.image, self.sprites.username_string.rect),
                                    (self.sprites.password_string.image, self.sprites.password_string.rect),
                                    (self.sprites.try_again.image, self.sprites.try_again.rect)))

    def update(self, actions: list[Action]) -> stage:
        if self.is_this_the_first_iteration:
            pygame.key.start_text_input()
            self.is_this_the_first_iteration = False
        return self.handle_updates(actions)
