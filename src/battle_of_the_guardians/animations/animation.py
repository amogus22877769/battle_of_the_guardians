from typing import Callable, Any

import pygame.time

from src.battle_of_the_guardians.animations.effects import _Effects

_running = []


class Animation:
    def __init__(self, targets: Any, duration: int, relative_destination: tuple[float, float], effect=_Effects.linear):
        self.targets = targets
        self.duration = duration
        self.relative_destination: tuple[float, float] = relative_destination
        self.effect: Callable[[float], float] = effect
        self._starting_relative_center_coordinates = None
        self._start: bool = False
        self._start_ticks: int = 0
        self._relative_path_vectors: list[tuple[int, int]] = []
        [self._relative_path_vectors.append((relative_destination[0] - target.relative_center_coordinates[0],
                                             relative_destination[1] - target.relative_center_coordinates[1]))
         for target in self.targets]
        self._on_stop = None

    def start(self, on_stop=None) -> None:
        if not self._start:
            _running.append(self)
        self._start_ticks = pygame.time.get_ticks()
        self._starting_relative_center_coordinates: list[tuple[float, float]] = []
        [self._starting_relative_center_coordinates.append(target.relative_center_coordinates)
         for target in self.targets]
        self._on_stop = on_stop

    def _stop(self) -> None:
        self._start = False
        _running.remove(self)
        self._on_stop() if self._on_stop else self._on_stop

    def update(self) -> None:
        delta_ticks: int = pygame.time.get_ticks() - self._start_ticks
        if delta_ticks / self.duration >= 1:
            self._stop()
        [self.targets[i].place((self._starting_relative_center_coordinates[i][0] +
                                self._relative_path_vectors[i][0] * self.effect(delta_ticks / self.duration),
                                self._starting_relative_center_coordinates[i][1] +
                                self._relative_path_vectors[i][1] * self.effect(delta_ticks / self.duration)))
         for i in range(len(self.targets))]
