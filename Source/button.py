import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, relative_coordinates: tuple[float, float], relative_size: tuple[float, float], window_size: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image = surface
        self.relative_coordinates: tuple[float, float] = relative_coordinates
        self.relative_size: tuple[float, float] = relative_size
        self.image = pygame.transform.scale(surface, (window_size[0] * self.relative_size[0], window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_coordinates[0] * window_size[0] - self.rect.width / 2,
                         self.relative_coordinates[1] * window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.image = pygame.transform.scale(self.real_image, (new_window_size[0] * self.relative_size[0], new_window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_coordinates[0] * new_window_size[0] - self.rect.width / 2,
                         self.relative_coordinates[1] * new_window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)