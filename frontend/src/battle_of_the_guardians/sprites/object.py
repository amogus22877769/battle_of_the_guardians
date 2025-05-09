import pygame


class Object(pygame.sprite.Sprite):

    def __init__(self, surface, relative_size: tuple[float, float], window_size: tuple[int, int],
                 relative_center_coordinates: tuple[float, float] = (0, 0), alpha: int = 255):
        pygame.sprite.Sprite.__init__(self)
        self.real_image: pygame.Surface = surface
        self.real_image.set_alpha(alpha)
        self.relative_size: tuple[float, float] = relative_size
        self.window_size: tuple[int, int] = window_size
        self.image: pygame.Surface = pygame.transform.scale(self.real_image, (
        self.window_size[0] * self.relative_size[0], self.window_size[1] * self.relative_size[1]))
        self.rect: pygame.Rect = self.image.get_rect()
        self.relative_center_coordinates: tuple[float, float] = relative_center_coordinates
        self._alpha: int = alpha
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def update(self, new_window_size: tuple[int, int]):
        self.window_size = new_window_size
        self.image = pygame.transform.scale(self.real_image, (
        self.window_size[0] * self.relative_size[0], self.window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def copy_consts(self, new_surface: pygame.Surface):
        return Object(new_surface, self.relative_size, self.window_size)

    def copy(self):
        return Object(self.real_image, self.relative_size, self.window_size,
                      relative_center_coordinates=self.relative_center_coordinates, alpha=self._alpha)

    def resize(self, new_relative_size: tuple[float, float]):
        self.relative_size = new_relative_size
        self.image = pygame.transform.scale(self.real_image, (
        self.window_size[0] * self.relative_size[0], self.window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def place(self, relative_center_coordinates: tuple[float, float]):
        self.relative_center_coordinates = relative_center_coordinates
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, new_alpha: int):
        self._alpha = new_alpha
        self.real_image.set_alpha(self._alpha)
        self.real_image.set_alpha(self._alpha)
