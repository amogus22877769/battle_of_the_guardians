import pygame

from frontend.src.battle_of_the_guardians.sprites.bar import Bar
from frontend.src.battle_of_the_guardians.sprites.button import Button
from frontend.src.battle_of_the_guardians.sprites.object import Object
from frontend.src.battle_of_the_guardians.sprites.point import Point
from frontend.src.battle_of_the_guardians.sprites.string import String


class Card:

    def __init__(self, card: Object,
                 outline: Object,
                 relative_outline_thickness,
                 window_size: tuple[int, int],
                 hp_bar: Bar,
                 hp_icon: Button,
                 health_point: Point,
                 shield_bar: Bar,
                 shield_icon: Button,
                 shield_point: Point,
                 health: float,
                 damage: float,
                 hp_string: String,
                 shield_string: String,
                 ability,
                 shield: int = 0) -> None:
        self.sprite = card
        self.outline = outline
        self.relative_outline_thickness = relative_outline_thickness
        self.window_size = window_size
        self.hp_bar: Bar = hp_bar
        self.hp_icon: Button = hp_icon

        self.max_count_of_visible_health_points: int = int(
            (self.hp_bar.relative_size[0] - self.hp_bar.relative_thickness[0] * 2) * self.window_size[0] / (
                    self.hp_bar.relative_size[1] - self.hp_bar.relative_thickness[1] * 2) / self.window_size[1])
        self.count_of_visible_health_points = self.max_count_of_visible_health_points

        self.health_points: list[Point] = [health_point.copy() for _ in range(self.count_of_visible_health_points)]
        self.shield_bar: Bar = shield_bar
        self.shield_icon: Button = shield_icon

        self.max_count_of_visible_shield_points: int = int(
            (self.shield_bar.relative_size[0] - self.shield_bar.relative_thickness[0] * 2) * self.window_size[0] / (
                    self.shield_bar.relative_size[1] - self.shield_bar.relative_thickness[1] * 2) / self.window_size[1])
        self.count_of_visible_shield_points = self.max_count_of_visible_shield_points

        self.shield_points: list[Point] = [shield_point.copy() for _ in range(self.count_of_visible_shield_points)]
        self.health: float = health
        self._current_health: float = self.health
        self.damage: float = damage
        self.hp_string = hp_string
        self.shield_string = shield_string
        self.hp_string.text = f'{self._current_health}'
        self._shield = shield
        self.default_shield = self._shield
        self._current_shield = self.shield
        self.shield_string.text = f'{self._current_shield}'
        self.ability = ability

    def place(self, relative_center_coordinates: tuple[float, float]) -> None:
        self.sprite.place(relative_center_coordinates)
        self.outline.place(relative_center_coordinates)

    def place_hp_bar(self, relative_distance: float) -> None:
        self.hp_bar.place((self.outline.relative_center_coordinates[0],
                           self.outline.relative_center_coordinates[1] - self.outline.relative_size[
                               1] / 2 - relative_distance))
        self.hp_icon.place((self.hp_bar.relative_center_coordinates[0] - self.hp_bar.relative_size[0] / 2 -
                            self.hp_icon.relative_size[0] / 2,
                            self.hp_bar.relative_center_coordinates[1]))
        self.place_health_points()
        self.hp_string.place((self.hp_bar.relative_center_coordinates[0],
                              self.hp_bar.relative_center_coordinates[1] - self.hp_bar.relative_size[
                                  1] / 2 - self.hp_string.relative_size / 2))

    def place_shield_bar(self) -> None:
        self.shield_bar.place((self.hp_string.relative_center_coordinates[0],
                               self.hp_string.relative_center_coordinates[1] - self.hp_string.relative_size / 2
                               - self.shield_bar.relative_size[1] / 2))
        self.shield_icon.place((self.shield_bar.relative_center_coordinates[0] - self.shield_bar.relative_size[0] / 2 -
                                self.shield_icon.relative_size[0] / 2,
                                self.shield_bar.relative_center_coordinates[1]))
        self.place_shield_points()
        self.shield_string.place((self.shield_bar.relative_center_coordinates[0],
                                  self.shield_bar.relative_center_coordinates[1] - self.shield_bar.relative_size[
                                      1] / 2 - self.shield_string.relative_size / 2))

    def place_health_points(self) -> None:
        for health_point_index, health_point in enumerate(self.health_points):
            health_point.rect.update((self.hp_bar.relative_thickness[0] + self.hp_bar.relative_center_coordinates[0] -
                                      self.hp_bar.relative_size[0] / 2) * self.window_size[0] +
                                     (health_point_index + 0.5) * health_point.rect.width - health_point.rect.width / 2,
                                     self.hp_bar.relative_center_coordinates[1] * self.window_size[
                                         1] - health_point.rect.height / 2,
                                     health_point.rect.width,
                                     health_point.rect.height)
            health_point.relative_center_coordinates = ((health_point.rect.left + health_point.rect.width / 2) /
                                                        self.window_size[0],
                                                        (health_point.rect.top + health_point.rect.height / 2) /
                                                        self.window_size[1])

    def place_shield_points(self) -> None:
        for shield_point_index, shield_point in enumerate(self.shield_points):
            shield_point.rect.update((self.shield_bar.relative_thickness[0] +
                                      self.shield_bar.relative_center_coordinates[0] -
                                      self.shield_bar.relative_size[0] / 2) * self.window_size[0] +
                                     (shield_point_index + 0.5) * shield_point.rect.width - shield_point.rect.width / 2,
                                     self.shield_bar.relative_center_coordinates[1] * self.window_size[
                                         1] - shield_point.rect.height / 2,
                                     shield_point.rect.width,
                                     shield_point.rect.height)
            shield_point.relative_center_coordinates = ((shield_point.rect.left + shield_point.rect.width / 2) /
                                                        self.window_size[0],
                                                        (shield_point.rect.top + shield_point.rect.height / 2) /
                                                        self.window_size[1])

    @property
    def current_health(self) -> float:
        return self._current_health

    @current_health.setter
    def current_health(self, value: float) -> None:
        self._current_health = value
        if self._current_health > self.health:
            self._current_health = self.health
        self.count_of_visible_health_points = int(self._current_health /
                                                  self.health * self.max_count_of_visible_health_points)
        self.hp_string.text = f'{self._current_health}'

    @property
    def current_shield(self):
        return self._current_shield

    @current_shield.setter
    def current_shield(self, value: int):
        self._current_shield = value if value >= 0 else 0
        self.count_of_visible_shield_points = int(self._current_shield / self.shield *
                                                  self.max_count_of_visible_shield_points)
        self.shield_string.text = f'{self._current_shield}'

    @property
    def shield(self):
        return self._shield

    @shield.setter
    def shield(self, value):
        self._shield = value
        self._current_shield = self._shield
        self.count_of_visible_shield_points = int(self._current_shield / self.shield *
                                                  self.max_count_of_visible_shield_points) if self._shield else 0
        self.shield_string.text = f'{self._current_shield}'

    def to_draw_on_draft(self) -> list[tuple[pygame.Surface, pygame.Rect]]:

        # return [self.outline, self.sprite]

        return [(self.sprite.image, self.sprite.rect), (self.outline.image, self.outline.rect)]

    def to_draw_on_battle(self) -> list[tuple[pygame.Surface, pygame.Rect]]:

        # return [self.outline, self.sprite, self.hp_bar, self.hp_icon,
        # self.health_points[0:self.count_of_visible_health_points], self.hp_string]

        return [(self.sprite.image, self.sprite.rect), (self.outline.image, self.outline.rect),
                (self.hp_bar.image, self.hp_bar.rect), (self.hp_icon.image, self.hp_icon.rect),
                (self.hp_string.image, self.hp_string.rect),
                *[(self.shield_string.image, self.shield_string.rect) for _ in [0] if
                  self._shield and self._current_shield],
                *[(self.shield_bar.image, self.shield_bar.rect) for _ in [0] if
                  self._shield and self._current_shield],
                *[(self.shield_icon.image, self.shield_icon.rect) for _ in [0] if
                  self._shield and self._current_shield],
                *[(health_point.image, health_point.rect) for
                  health_point in
                  self.health_points[:self.count_of_visible_health_points]],
                *[(shield_point.image, shield_point.rect) for
                  shield_point in
                  self.shield_points[:self.count_of_visible_shield_points] if self._shield and self._current_shield]
                ]

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.window_size = new_window_size
        self.hp_string.update(new_window_size)
        self.sprite.update(new_window_size)
        self.outline.update(new_window_size)
        self.hp_bar.update(new_window_size)
        self.update_health_points(new_window_size)
        self.hp_icon.update(new_window_size)
        self.shield_string.update(new_window_size)
        self.shield_bar.update(new_window_size)
        self.shield_icon.update(new_window_size)
        self.update_shield_points(new_window_size)

    def update_health_points(self, new_window_size: tuple[int, int]) -> None:
        new_max_count_of_visible_health_points: int = int(
            (self.hp_bar.relative_size[0] - self.hp_bar.relative_thickness[0] * 2) * self.window_size[0] / (
                    self.hp_bar.relative_size[1] - self.hp_bar.relative_thickness[1] * 2) / self.window_size[1])
        if new_max_count_of_visible_health_points >= self.max_count_of_visible_health_points:
            [health_point.update(new_window_size) for health_point in self.health_points]
            [self.health_points.append(self.health_points[0].copy())
             for _ in range(new_max_count_of_visible_health_points - self.max_count_of_visible_health_points)]
        else:
            [self.health_points[i].update(new_window_size) for i in range(new_max_count_of_visible_health_points)]
        self.max_count_of_visible_health_points = new_max_count_of_visible_health_points
        self.count_of_visible_health_points = int(self._current_health /
                                                  self.health * self.max_count_of_visible_health_points)
        self.place_health_points()

    def update_shield_points(self, new_window_size: tuple[int, int]) -> None:
        new_max_count_of_visible_shield_points: int = int(
            (self.shield_bar.relative_size[0] - self.shield_bar.relative_thickness[0] * 2) * self.window_size[0] / (
                    self.shield_bar.relative_size[1] - self.shield_bar.relative_thickness[1] * 2) / self.window_size[1])
        if new_max_count_of_visible_shield_points >= self.max_count_of_visible_shield_points:
            [shield_point.update(new_window_size) for shield_point in self.shield_points]
            [self.shield_points.append(self.shield_points[0].copy())
             for _ in range(new_max_count_of_visible_shield_points - self.max_count_of_visible_shield_points)]
        else:
            [self.shield_points[i].update(new_window_size) for i in range(new_max_count_of_visible_shield_points)]
        self.max_count_of_visible_shield_points = new_max_count_of_visible_shield_points
        self.count_of_visible_shield_points = int(self._current_shield /
                                                  self._shield * self.max_count_of_visible_shield_points) if self._shield else self.count_of_visible_shield_points
        self.place_shield_points()

    def copy(self):
        return Card(self.sprite.copy(), self.outline.copy(), self.relative_outline_thickness,
                    self.window_size, self.hp_bar.copy(), self.hp_icon.copy(), self.health_points[0].copy(),
                    self.shield_bar.copy(), self.shield_icon.copy(), self.shield_points[0].copy(),
                    self.health, self.damage, self.hp_string.copy(), self.shield_string.copy(), self.ability,
                    shield=self._shield)

    def resize(self, multiplier):
        self.sprite.resize((self.sprite.relative_size[0] * multiplier,
                            self.sprite.relative_size[1] * multiplier))
        self.outline.resize((self.outline.relative_size[0] * multiplier,
                             self.outline.relative_size[1] * multiplier))

    def __repr__(self):
        return {'fire_wave': 'fire_wizard',
                'fire_breathe': 'fire_dragon',
                'heal': 'mermaid',
                'ground_protection': 'ground_titan',
                'strong': 'stone_dwarf',
                'thunder_punch': 'electro_wizard',
                'ice_wall': 'ice_wizard',
                'acceleration': 'blazing_herald'}[self.ability.kind] + f' current_shield: {self.current_shield}, shield: {self.shield}'
