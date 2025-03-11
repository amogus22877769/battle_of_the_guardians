import pygame


class Point(pygame.sprite.Sprite):
    def __init__(self, point_surface, relative_bar_size, relative_bar_thickness, window_size: tuple[int, int],
                 relative_center_coordinates: tuple[float, float] = (0, 0), relative_width: float = 0) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image: pygame.Surface = point_surface
        self.relative_bar_size = relative_bar_size
        self.relative_bar_thickness = relative_bar_thickness
        self.window_size: tuple[int, int] = window_size
        self.relative_center_coordinates: tuple[float, float] = relative_center_coordinates
        self.relative_width: float = relative_width
        if self.relative_width == 0:
            self.image: pygame.Surface = pygame.transform.scale(self.real_image,
                                                                (self.relative_bar_size[1] * self.window_size[1] -
                                                                 self.relative_bar_thickness[1] * 2 *
                                                                 self.window_size[1],
                                                                 self.relative_bar_size[1] * self.window_size[1] -
                                                                 self.relative_bar_thickness[1] * 2 *
                                                                 self.window_size[1]))
        else:
            self.image: pygame.Surface = pygame.transform.scale(self.real_image,
                                                                (self.relative_width * self.window_size[0],
                                                                 self.relative_bar_size[1] * self.window_size[1] -
                                                                 self.relative_bar_thickness[1] * 2 * self.window_size[
                                                                     1]))
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.window_size = new_window_size
        if self.relative_width == 0:
            self.image = pygame.transform.scale(self.real_image,
                                                (self.relative_bar_size[1] * self.window_size[1] -
                                                 self.relative_bar_thickness[1] * 2 *
                                                 self.window_size[1],
                                                 self.relative_bar_size[1] * self.window_size[1] -
                                                 self.relative_bar_thickness[1] * 2 *
                                                 self.window_size[1]))
        else:
            self.image = pygame.transform.scale(self.real_image,
                                                (self.relative_width * self.window_size[0],
                                                 self.relative_bar_size[1] * self.window_size[1] -
                                                 self.relative_bar_thickness[1] * 2 * self.window_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)

    def copy(self):
        return Point(self.real_image, self.relative_bar_size, self.relative_bar_thickness, self.window_size,
                     relative_width=self.relative_width)

    def place(self, relative_center_coordinates: tuple[float, float]):
        self.relative_center_coordinates = relative_center_coordinates
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)
