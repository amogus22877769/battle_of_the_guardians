from src.battle_of_the_guardians.sprites.bar import Bar
from src.battle_of_the_guardians.sprites.button import Button
from src.battle_of_the_guardians.sprites.point import Point


class EnergyBar:
    def __init__(self, bar: Bar, icon: Button, alpha: int, point: Point, relative_coordinates: tuple[float, float],
                 window_size: tuple[int, int], number_of_points: int, energy: int) -> None:
        self.bar = bar
        self.icon = icon
        self.points: list[Point] = []
        [self.points.append(point.copy()) for _ in range(number_of_points)]
        [point.real_image.set_alpha(alpha) for point in self.points]
        self.window_size: tuple[int, int] = window_size
        self.number_of_points: int = number_of_points
        self.max_energy = energy
        self._energy = self.max_energy
        self.count_of_visible_points = int(self._energy / self.max_energy * len(self.points))
        self.relative_coordinates: tuple[float, float] = relative_coordinates
        self.place()

    def update(self, new_window_size: tuple[int, int]):
        self.window_size = new_window_size
        self.bar.update(self.window_size)
        self.icon.update(self.window_size)
        [point.update(self.window_size) for point in self.points]
        self.place()

    def to_draw(self):
        return [self.bar, self.icon, self.points[:self.count_of_visible_points]]

    def place(self):
        self.bar.place(self.relative_coordinates)
        self.icon.place((self.bar.relative_center_coordinates[0] - self.bar.relative_size[0] / 2 -
                         self.icon.relative_size[0], self.bar.relative_center_coordinates[1]))
        for point_index, point in enumerate(self.points):
            point.place((self.bar.relative_center_coordinates[0] - self.bar.relative_size[0] / 2 +
                         self.bar.relative_thickness[0] + (
                                     point.relative_bar_size[1] - point.relative_bar_thickness[1] * 2) * (
                                     point_index + 0.5),
                         self.bar.relative_center_coordinates[1]))

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, new_energy: int):
        self._energy = new_energy
        self.count_of_visible_points = int(self._energy / self.max_energy * len(self.points))
