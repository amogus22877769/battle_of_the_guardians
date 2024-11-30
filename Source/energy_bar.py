from Source.classes import Bar, Point, Button


class EnergyBar:
    def __init__(self, bar: Bar, icon: Button, point: Point) -> None:
        self.bar = bar
        self.icon = icon
        self.point = Point

    def place(self, center_coordinates) -> None:
        self.bar.rect.update(center_coordinates[0] - self.bar.rect.width / 2,
                             center_coordinates[1] - self.bar.rect.height,
                             self.bar.rect.width,
                             self.bar.rect.height)
        self.icon.rect.update(self.bar.rect.left - self.icon.rect.width,
                              self.bar.rect.top + (self.bar.rect.height - self.icon.rect.height) / 2,
                              self.icon.rect.width,
                              self.icon.rect.height)
