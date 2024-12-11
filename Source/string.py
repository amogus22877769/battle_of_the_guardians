import pygame

from pathlib import Path


class String(pygame.sprite.Sprite):
    def __init__(self, text: str, color: pygame.Color, right_corner_relative_pos: tuple[float, float], font_path: Path,
                 relative_size: float, window_size: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self._text = text
        self.color = color
        self.path = font_path
        self.relative_size = relative_size
        self.font = pygame.font.Font(font_path, size=int(self.relative_size * window_size[1]))
        self.right_corner_relative_pos: tuple[float, float] = right_corner_relative_pos
        self.window_size: tuple[int, int] = window_size
        self.image = self.font.render(self._text, None, self.color)
        self.rect = self.image.get_rect()
        self.rect.update(self.right_corner_relative_pos[0] * self.window_size[0] - self.rect.width,
                         self.right_corner_relative_pos[1] * self.window_size[1],
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
        self.rect.update(self.right_corner_relative_pos[0] * self.window_size[0] - self.rect.width,
                         self.right_corner_relative_pos[1] * self.window_size[1],
                         self.rect.width,
                         self.rect.height)

    def update(self, new_window_size) -> None:
        self.window_size = new_window_size
        self.font = pygame.font.Font(self.path, size=int(self.relative_size * new_window_size[1]))
        self.image = self.font.render(self._text, None, self.color)
        self.rect.update(self.right_corner_relative_pos[0] * self.window_size[0] - self.rect.width,
                         self.right_corner_relative_pos[1] * self.window_size[1],
                         self.rect.width,
                         self.rect.height)

    def place(self, new_right_corner) -> None:
        self.right_corner_relative_pos = new_right_corner
        self.rect.update(self.right_corner_relative_pos[0] * self.window_size[0] - self.rect.width,
                         self.right_corner_relative_pos[1] * self.window_size[1],
                         self.rect.width,
                         self.rect.height)
