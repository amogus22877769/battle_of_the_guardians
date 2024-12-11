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

    def __init__(self, card_surface: pygame.Surface, outline_surface: pygame.Surface, relative_card_size: tuple[float, float],
                 relative_outline_thickness: tuple[float, float], window_size: tuple[int, int], hp_bar: Bar, hp_icon: Button, hitpoint_path: Path, health: float,
                 damage: float, hp_string: String) -> None:
        self.hp_bar: Bar = hp_bar
        self.hp_icon: Button = hp_icon
        self.hitpoints: list[Point] = []
        self.hitpoint_path = hitpoint_path
        self.window_size = window_size
        self.health: float = health
        self._current_health: float = self.health
        self.damage: float = damage
        self.max_count_of_visible_hitpoints: int = int((self.hp_bar.rect.width - 2 * self.hp_bar.thickness[1]) / (
                                                    self.hp_bar.rect.height - self.hp_bar.thickness[1] * 2))
        self.count_of_visible_hitpoints = self.max_count_of_visible_hitpoints
        for _ in range(self.count_of_visible_hitpoints):
            self.hitpoints.append(Point(pygame.image.load(self.hitpoint_path), self.hp_bar.relative_size, self.hp_bar.relative_thickness, self.window_size))
        self.hp_string = hp_string
        self.sprite = Object(card_surface,
                             (relative_card_size[0] - relative_outline_thickness[0] * 2, relative_card_size[1] - relative_outline_thickness[1] * 2),
                             window_size)
        self.outline = Object(outline_surface, relative_card_size, window_size)
        self.relative_outline_thickness = relative_outline_thickness
    def place(self, relative_pos: tuple[float, float]) -> None:
        self.sprite.rect.update(relative_pos[0] * self.window_size[0] - self.sprite.rect.width / 2,
                                 relative_pos[1] * self.window_size[1] - self.sprite.rect.height / 2,
                                 self.sprite.rect.width,
                                 self.sprite.rect.height)
        self.outline.rect.update(self.sprite.rect.left - self.relative_outline_thickness[0] * self.window_size[0],
                                self.sprite.rect.top - self.relative_outline_thickness[1] * self.window_size[1],
                                self.outline.rect.width,
                                self.outline.rect.height)

    def place_hp_bar(self, relative_distance: float) -> None:
        self.hp_bar.rect.update(self.outline.rect.left,
                                self.outline.rect.top - relative_distance * self.window_size[1] - self.hp_bar.rect.height,
                                self.hp_bar.rect.width,
                                self.hp_bar.rect.height)
        self.hp_icon.rect.update(self.hp_bar.rect.left - self.hp_icon.rect.width,
                                 self.hp_bar.rect.top + (self.hp_bar.rect.height - self.hp_icon.rect.height) / 2,
                                 self.hp_icon.rect.width,
                                 self.hp_icon.rect.height)
        for hitpoint_index in range(len(self.hitpoints)):
            self.hitpoints[hitpoint_index].rect.update(
                self.hp_bar.rect.left + self.hp_bar.thickness[0] + hitpoint_index * self.hitpoints[
                    hitpoint_index].rect.width,
                self.hp_bar.rect.top + self.hp_bar.thickness[1],
                self.hitpoints[hitpoint_index].rect.width,
                self.hitpoints[hitpoint_index].rect.height)
        self.hp_string.place(((self.hp_bar.rect.left + self.hp_bar.rect.width / 2 + self.hp_string.rect.width / 2) / self.window_size[0], (self.hp_bar.rect.top - self.hp_string.rect.height) / self.window_size[1]))

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
        return [self.outline, self.sprite, self.hp_bar, self.hp_icon, self.hitpoints[0:self.count_of_visible_hitpoints], self.hp_string]

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.window_size = new_window_size
        self.hp_string.update(new_window_size)
        self.sprite.update(new_window_size)
        self.outline.update(new_window_size)
        self.hp_bar.update(new_window_size)
        self.update_hitpoints(new_window_size)
        self.hp_icon.update(new_window_size)

    def update_hitpoints(self, new_window_size: tuple[int, int]) -> None:
        new_max_count_of_visible_hitpoints: int = int((self.hp_bar.rect.width - 2 * self.hp_bar.thickness[1]) / (
                                                    self.hp_bar.rect.height - self.hp_bar.thickness[1] * 2))
        if new_max_count_of_visible_hitpoints >= self.max_count_of_visible_hitpoints:
            for hitpoint in self.hitpoints:
                hitpoint.update(new_window_size)
            for _ in range(new_max_count_of_visible_hitpoints - self.max_count_of_visible_hitpoints):
                self.hitpoints.append(Point(pygame.image.load(self.hitpoint_path), self.hp_bar.relative_size, self.hp_bar.relative_thickness, new_window_size))
        else:
            for i in range(new_max_count_of_visible_hitpoints):
                self.hitpoints[i].update(new_window_size)
        self.max_count_of_visible_hitpoints = new_max_count_of_visible_hitpoints

