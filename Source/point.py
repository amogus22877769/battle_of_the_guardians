import pygame


class Point(pygame.sprite.Sprite):
    def __init__(self, point_surface, relative_bar_size, relative_bar_thickness, window_size: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image = point_surface
        self.relative_bar_size = relative_bar_size
        self.relative_bar_thickness = relative_bar_thickness
        self.image = pygame.transform.scale(point_surface,
                                            (relative_bar_size[1] * window_size[1] - relative_bar_thickness[1] * 2 *
                                             window_size[1],
                                             relative_bar_size[1] * window_size[1] - relative_bar_thickness[1] * 2 *
                                             window_size[1]))
        self.rect = self.image.get_rect()

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.image = pygame.transform.scale(self.real_image,
                                            (self.relative_bar_size[1] * new_window_size[1] -
                                             self.relative_bar_thickness[1] * 2 * new_window_size[1],
                                             self.relative_bar_size[1] * new_window_size[1] -
                                             self.relative_bar_thickness[1] * 2 * new_window_size[1]))
        self.rect = self.image.get_rect()
