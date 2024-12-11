import pygame


class Object(pygame.sprite.Sprite):

    def __init__(self, surface, relative_size: tuple[float, float], window_size: tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)
        self.real_image = surface
        self.relative_size: tuple[float, float] = relative_size
        self.image = pygame.transform.scale(surface, (window_size[0] * self.relative_size[0], window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()

    def update(self, new_window_size: tuple[int, int]):
        self.image = pygame.transform.scale(self.real_image, (new_window_size[0] * self.relative_size[0], new_window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
