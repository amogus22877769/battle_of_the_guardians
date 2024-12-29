import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, surface, window_size: tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)
        self.real_image = surface
        self.image = pygame.transform.scale(surface, window_size)
        self.rect = self.image.get_rect()

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.image = pygame.transform.scale(self.real_image, new_window_size)
        self.rect = self.image.get_rect()
