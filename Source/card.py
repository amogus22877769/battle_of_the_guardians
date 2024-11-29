import numpy

import pygame

from Source.classes import Bar, Point, String, Button
from Source.object import Object

class Card:

    def __init__(self, card_surface: pygame.Surface, outline_surface: pygame.Surface, card_size: tuple[int, int], outline_thickness: tuple[int], hp_bar: Bar, hp_icon: Button, hitpoints: list[Point], health: float, damage: float, font: pygame.font.Font) -> None:
        self.hp_bar: Bar = hp_bar
        self.hp_icon: Button = hp_icon
        self._hitpoints: list[Point] = []
        for hitpoint in hitpoints:
            self._hitpoints.append(hitpoint)
        self.health: float = health
        self._current_health: float = self.health
        self.damage: float = damage
        self.count_of_visible_hitpoints: int = len(self._hitpoints)
        self.font: pygame.font.Font = font
        self.health_sprite = String(self.font.render(f'{self._current_health}', None, DARK_RED), (
            self.hp_bar.rect.left + self.hp_bar.rect.width / 2 - self.font.size(f'{self._current_health}')[0] / 2,
            self.hp_bar.rect.top - self.font.size(f'{self._current_health}')[1]))
        max_size_of_card: tuple[int, int] = (min(card_surface.get_width(), outline_surface.get_width()) + outline_thickness[0] * 2,
                                             min(card_surface.get_height(), outline_surface.get_height()) + outline_thickness[1] * 2)
        card_surface = pygame.transform.scale(card_surface, (
            max_size_of_card[0] - 2 * outline_thickness[0], max_size_of_card[1] - 2 * outline_thickness[1]))
        card_surface_pixel_array = pygame.surfarray.array3d(card_surface)
        outline_surface = pygame.transform.scale(outline_surface, max_size_of_card)
        outline_surface_pixel_array = pygame.surfarray.array3d(outline_surface)
        left_section = outline_surface_pixel_array[0:outline_thickness[0], :]
        mid_section = numpy.hstack((
            outline_surface_pixel_array[outline_thickness[0]:max_size_of_card[0] - outline_thickness[0],
            0:outline_thickness[1]],
            card_surface_pixel_array,
            outline_surface_pixel_array[outline_thickness[0]:max_size_of_card[0] - outline_thickness[0],
            max_size_of_card[1] - outline_thickness[1]:max_size_of_card[1]]))
        right_section = outline_surface_pixel_array[max_size_of_card[0] - outline_thickness[0]:max_size_of_card[0], :]
        final_card_pixel_array = numpy.vstack((left_section, mid_section, right_section))
        final_surface = pygame.surfarray.make_surface(final_card_pixel_array)
        final_surface.set_colorkey(pygame.Color(0, 0, 0))
        self.sprite: Object = Object(final_surface, card_size)
    def place(self, pos: tuple[int]) ->  None:
        self.sprite.rect.update(pos[0] - self.sprite.rect.width / 2,
                                pos[1] - self.sprite.rect.height / 2,
                                self.sprite.rect.width,
                                self.sprite.rect.height)
    def place_hp_bar(self, distance: int) -> None:
        self.hp_bar.rect.update(self.sprite.rect.left,
                                self.sprite.rect.top - distance - self.hp_bar.rect.height,
                                self.hp_bar.rect.width,
                                self.hp_bar.rect.height)
        self.hp_icon.rect.update(self.hp_bar.rect.left - self.hp_icon.rect.width,
                                 self.hp_bar.rect.top + (self.hp_bar.rect.height - self.hp_icon.rect.height) / 2,
                                 self.hp_icon.rect.width,
                                 self.hp_icon.rect.height)
        for hitpoint_index in range(len(self.hitpoints)):
            self.hitpoints[hitpoint_index].rect.update(self.hp_bar.rect.left + self.hp_bar.thickness[0] + hitpoint_index * self.hitpoints[hitpoint_index].rect.width,
                                 self.hp_bar.rect.top + self.hp_bar.thickness[1],
                                 self.hitpoints[hitpoint_index].rect.width,
                                 self.hitpoints[hitpoint_index].rect.height)
    @property
    def current_health(self) -> float:
        return self._current_health
    @current_health.setter
    def current_health(self, value: float) -> None:
        self._current_health = value
        self.count_of_visible_hitpoints = int(self._current_health / self.health * len(self._hitpoints))
        self.health_sprite = String(self.font.render(f'{self._current_health}', None, pygame.Color('red')), (
        self.hp_bar.rect.left + self.hp_bar.rect.width / 2 - self.font.size(f'{self._current_health}')[0] / 2,
        self.hp_bar.rect.top - self.font.size(f'{self._current_health}')[1]))
    @property
    def hitpoints(self) -> list[Point]:
        return self._hitpoints[:self.count_of_visible_hitpoints]




