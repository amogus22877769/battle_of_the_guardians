from sys import winver

import numpy

import pygame

from pathlib import Path

from Source.bar import Bar
from Source.button import Button
from Source.object import Object
from Source.point import Point
from Source.string import String


class Card:

    def __init__(self, card: Object, outline: Object, relative_outline_thickness, window_size: tuple[int, int], hp_bar: Bar,
                 hp_icon: Button, hitpoint: Point, health: float,
                 damage: float, hp_string: String) -> None:
        self.hp_bar: Bar = hp_bar
        self.hp_icon: Button = hp_icon
        self.hitpoints: list[Point] = []
        self.window_size = window_size
        self.health: float = health
        self._current_health: float = self.health
        self.damage: float = damage
        self.max_count_of_visible_hitpoints: int = int((self.hp_bar.relative_size[0] - self.hp_bar.relative_thickness[0] * 2) * self.window_size[0] / (
                self.hp_bar.relative_size[1] - self.hp_bar.relative_thickness[1] * 2) / self.window_size[1])
        self.count_of_visible_hitpoints = self.max_count_of_visible_hitpoints
        [self.hitpoints.append(hitpoint.copy()) for _ in range(self.count_of_visible_hitpoints)]
        self.hp_string = hp_string
        self.hp_string.text = f'{self._current_health}'
        self.sprite = card
        self.outline = outline
        self.relative_outline_thickness = relative_outline_thickness

    def place(self, relative_center_coordinates: tuple[float, float]) -> None:
        self.sprite.place(relative_center_coordinates)
        self.outline.place(relative_center_coordinates)

    def place_hp_bar(self, relative_distance: float) -> None:
        self.hp_bar.place((self.outline.relative_center_coordinates[0], self.outline.relative_center_coordinates[1] - self.outline.relative_size[1] / 2 - relative_distance))
        self.hp_icon.place((self.hp_bar.relative_center_coordinates[0] - self.hp_bar.relative_size[0] / 2 - self.hp_icon.relative_size[0] / 2,
                                 self.hp_bar.relative_center_coordinates[1]))
        self.place_hitpoints()
        self.hp_string.place((self.hp_bar.relative_center_coordinates[0],
                              self.hp_bar.relative_center_coordinates[1] - self.hp_bar.relative_size[1] / 2 - self.hp_string.relative_size / 2))

    def place_hitpoints(self) -> None:
        for hitpoint_index, hitpoint in enumerate(self.hitpoints):
            hitpoint.rect.update((self.hp_bar.relative_thickness[0] + self.hp_bar.relative_center_coordinates[0] - self.hp_bar.relative_size[0] / 2) * self.window_size[0] + (hitpoint_index + 0.5) * hitpoint.rect.width - hitpoint.rect.width / 2,
                                  self.hp_bar.relative_center_coordinates[1] * self.window_size[1] - hitpoint.rect.height / 2,
                                  hitpoint.rect.width,
                                  hitpoint.rect.height)
            hitpoint.relative_center_coordinates = ((hitpoint.rect.left + hitpoint.rect.width / 2) / self.window_size[0],
                                                    (hitpoint.rect.top + hitpoint.rect.height / 2) / self.window_size[1])

    @property
    def current_health(self) -> float:
        return self._current_health

    @current_health.setter
    def current_health(self, value: float) -> None:
        self._current_health = value
        self.count_of_visible_hitpoints = int(self._current_health / self.health * self.max_count_of_visible_hitpoints)
        self.hp_string.text = f'{value}'

    def to_draw_on_draft(self) -> list[Object]:
        return [self.outline, self.sprite]

    def to_draw_on_battle(self) -> list[Object | Bar | Button | String]:
        return [self.outline, self.sprite, self.hp_bar, self.hp_icon, self.hitpoints[0:self.count_of_visible_hitpoints],
                self.hp_string]

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.window_size = new_window_size
        self.hp_string.update(new_window_size)
        self.sprite.update(new_window_size)
        self.outline.update(new_window_size)
        self.hp_bar.update(new_window_size)
        self.update_hitpoints(new_window_size)
        self.hp_icon.update(new_window_size)

    def update_hitpoints(self, new_window_size: tuple[int, int]) -> None:
        new_max_count_of_visible_hitpoints: int = int((self.hp_bar.relative_size[0] - self.hp_bar.relative_thickness[0] * 2) * self.window_size[0] / (
                self.hp_bar.relative_size[1] - self.hp_bar.relative_thickness[1] * 2) / self.window_size[1])
        if new_max_count_of_visible_hitpoints >= self.max_count_of_visible_hitpoints:
            [hitpoint.update(new_window_size) for hitpoint in self.hitpoints]
            [self.hitpoints.append(self.hitpoints[0].copy()) for _ in range(new_max_count_of_visible_hitpoints - self.max_count_of_visible_hitpoints)]
        else:
            [self.hitpoints[i].update(new_window_size) for i in range(new_max_count_of_visible_hitpoints)]
        self.max_count_of_visible_hitpoints = new_max_count_of_visible_hitpoints
        self.count_of_visible_hitpoints = int(self._current_health / self.health * self.max_count_of_visible_hitpoints)
        self.place_hitpoints()

    def copy(self):
        return Card(self.sprite.copy(), self.outline.copy(), self.relative_outline_thickness, self.window_size, self.hp_bar.copy(), self.hp_icon.copy(), self.hitpoints[0].copy(), self.health, self.damage, self.hp_string.copy())
