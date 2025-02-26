import pygame

from pathlib import Path


class String(pygame.sprite.Sprite):
    def __init__(self, text: str, color: pygame.Color, relative_center_coordinates: tuple[float, float],
                 font_path: Path,
                 relative_size: float, window_size: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self._text = text
        self.color = color
        self.path = font_path
        self.relative_size = relative_size
        self.font = pygame.font.Font(font_path, size=int(self.relative_size * window_size[1]))
        self.relative_center_coordinates: tuple[float, float] = relative_center_coordinates
        self.window_size: tuple[int, int] = window_size
        self.image: pygame.Surface = self.font.render(self._text, None, self.color)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text
        self.image = self.font.render(self._text, None, self.color)
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def update(self, new_window_size) -> None:
        self.window_size = new_window_size
        self.font = pygame.font.Font(self.path, size=int(self.relative_size * new_window_size[1]))
        self.image = self.font.render(self._text, None, self.color)
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def place(self, new_relative_center_coordinates: tuple[float, float]) -> None:
        self.relative_center_coordinates = new_relative_center_coordinates
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def copy(self):
        return String(self.text, self.color, self.relative_center_coordinates, self.path, self.relative_size,
                      self.window_size)
