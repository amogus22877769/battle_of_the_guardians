import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, relative_size: tuple[float, float], relative_thickness: tuple[float, float], window_size: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image: pygame.Surface = surface
        self.relative_size: tuple[float, float] = relative_size
        self.relative_thickness: tuple[float, float] = relative_thickness
        self.image: pygame.Surface = pygame.transform.scale(surface, (window_size[0] * self.relative_size[0], window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.thickness: tuple[int, int] = (int(window_size[0] * self.relative_thickness[0]), int(window_size[1] * self.relative_thickness[0]))

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.image = pygame.transform.scale(self.real_image, (new_window_size[0] * self.relative_size[0], new_window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.thickness = (int(new_window_size[0] * self.relative_thickness[0]), int(new_window_size[1] * self.relative_thickness[0]))