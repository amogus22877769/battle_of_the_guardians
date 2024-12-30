import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, relative_center_coordinates: tuple[float, float], relative_size: tuple[float, float], window_size: tuple[int, int], circular: bool = False) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image = surface
        self.relative_center_coordinates: tuple[float, float] = relative_center_coordinates
        self.relative_size: tuple[float, float] = relative_size
        self.window_size: tuple[int, int] = window_size
        self.image = pygame.transform.scale(self.real_image, (self.window_size[0] * self.relative_size[0], self.window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)
        self.circular: bool = circular
        if self.circular:
            self.h = self.window_size[0] * self.relative_center_coordinates[0]
            self.k = self.window_size[1] * self.relative_center_coordinates[1]
            self.a = self.window_size[0] * self.relative_size[0] / 2
            self.b = self.window_size[1] * self.relative_size[1] / 2

    def update(self, new_window_size: tuple[int, int]) -> None:
        self.window_size = new_window_size
        self.image = pygame.transform.scale(self.real_image, (self.window_size[0] * self.relative_size[0], self.window_size[1] * self.relative_size[1]))
        self.rect = self.image.get_rect()
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)
        if self.circular:
            self.h = self.window_size[0] * self.relative_center_coordinates[0]
            self.k = self.window_size[1] * self.relative_center_coordinates[1]
            self.a = self.window_size[0] * self.relative_size[0] / 2
            self.b = self.window_size[1] * self.relative_size[1] / 2

    def copy(self):
        return Button(self.real_image, self.relative_center_coordinates, self.relative_size, self.window_size, circular=self.circular)

    def place(self, relative_center_coordinates: tuple[float, float]):
        self.relative_center_coordinates = relative_center_coordinates
        self.rect.update(self.relative_center_coordinates[0] * self.window_size[0] - self.rect.width / 2,
                         self.relative_center_coordinates[1] * self.window_size[1] - self.rect.height / 2,
                         self.rect.width,
                         self.rect.height)
        if self.circular:
            self.h = self.window_size[0] * self.relative_center_coordinates[0]
            self.k = self.window_size[1] * self.relative_center_coordinates[1]


    def collide_point(self, x: int, y: int) -> bool:
        if self.circular:
            if ((x - self.h) ** 2 / self.a ** 2) + ((y - self.k) ** 2 / self.b ** 2) <= 1:
                return True
            return False
        return self.rect.collidepoint((x, y))