from os import environ
from pathlib import Path

import pygame.image

from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, INPUT_BOX_RELATIVE_SIZE, \
    USERNAME_BOX_RELATIVE_COORDINATES, INPUT_BOX_RELATIVE_OUTLINE_THICKNESS, PASSWORD_BOX_RELATIVE_COORDINATES, \
    REGISTRATION_RELATIVE_COORDINATES, RELATIVE_FANTASY_FONT_FOR_REGISTRATION_SIZE, \
    USERNAME_STRING_RELATIVE_COORDINATES, PASSWORD_STRING_RELATIVE_COORDINATES, TRY_AGAIN_RELATIVE_COORDINATES
from src.battle_of_the_guardians.sprites.background import Background
from src.battle_of_the_guardians.sprites.object import Object
from src.battle_of_the_guardians.sprites.string import String


class RegistrationSprites:
    def __init__(self):
        self.enter = False
        self.background: Background = Background(pygame.image.load('resources/img/maps/registration_map.jpeg'), (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.registration_string = String('REGISTRATION/SIGN UP', pygame.Color('red'), REGISTRATION_RELATIVE_COORDINATES, Path('resources/fonts/fantasy_capitals.otf'), RELATIVE_FANTASY_FONT_FOR_REGISTRATION_SIZE,
                                          (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.username_string = self.registration_string.copy()
        self.username_string.place(USERNAME_STRING_RELATIVE_COORDINATES)
        self.username_string.text = 'USERNAME'
        self.password_string = self.registration_string.copy()
        self.password_string.place(PASSWORD_STRING_RELATIVE_COORDINATES)
        self.password_string.text = 'PASSWORD'
        self.username_box = Object(pygame.image.load('resources/img/ornaments/input_box.png'), INPUT_BOX_RELATIVE_SIZE, (DEFAULT_WIDTH, DEFAULT_HEIGHT),
                          relative_center_coordinates=USERNAME_BOX_RELATIVE_COORDINATES)
        self.username = String('', pygame.Color('red'), USERNAME_BOX_RELATIVE_COORDINATES, Path('resources/fonts/fantasy_capitals.otf'),
                               INPUT_BOX_RELATIVE_SIZE[1] - INPUT_BOX_RELATIVE_OUTLINE_THICKNESS[1] * 2, (DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.password_box = self.username_box.copy()
        self.password_box.place(PASSWORD_BOX_RELATIVE_COORDINATES)
        self.password = self.username.copy()
        self.password.place(PASSWORD_BOX_RELATIVE_COORDINATES)
        if Path('auth_data.txt').is_file():
            with open('auth_data.txt') as f:
                s = f.read()
                self.username.text, self.password.text = s.split()
            f.close()
            self.enter = True
        self.try_again = self.registration_string.copy()
        self.try_again.place(TRY_AGAIN_RELATIVE_COORDINATES)
        self.try_again.text = 'TRY AGAIN'

    def update(self, new_window_size: tuple[int, int]):
        self.background.update(new_window_size)
        self.registration_string.update(new_window_size)
        self.username_box.update(new_window_size)
        self.username.update(new_window_size)
        self.password.update(new_window_size)
        self.password_box.update(new_window_size)
        self.username_string.update(new_window_size)
        self.password_string.update(new_window_size)
        self.try_again.update(new_window_size)
