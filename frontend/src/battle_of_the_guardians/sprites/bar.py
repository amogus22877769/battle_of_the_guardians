import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, relative_size: tuple[float, float],
                 relative_thickness: tuple[float, float], window_size: tuple[int, int],
                 relative_center_coordinates: tuple[float, float] = (0, 0)) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image: pygame.Surface = surface
        self.relative_size: tuple[float, float] = relative_size
        self.relative_thickness: tuple[float, float] = relative_thickness
        self.window_size: tuple[int, int] = window_size
        self.image: pygame.Surface = pygame.transform.scale(surface, (
        window_size[0] * self.relative_size[0], window_size[1] * self.relative_size[1]))
        self.rect: pygame.Rect = self.image.get_rect()
        self.relative_center_coordinates: tuple[float, float] = relative_center_coordinates
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.window_size = new_window_size
        self.image = pygame.transform.scale(self.real_image, (
        self.window_size[0] * self.relative_size[0], self.window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def copy(self):
        return Bar(self.real_image, self.relative_size, self.relative_thickness, self.window_size)

    def place(self, new_relative_center_coordinates: tuple[float, float]) -> None:
        self.relative_center_coordinates = new_relative_center_coordinates
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)
