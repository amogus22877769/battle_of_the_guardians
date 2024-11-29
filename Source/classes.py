import pygame


class Background(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, surface, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.real_image = surface
        self.image = pygame.transform.scale(surface, size)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self, new_size: tuple[int, int]) -> None:
        self.image = pygame.transform.scale(self.real_image, new_size)
        self.rect = self.image.get_rect()


class Button(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, surface, coordinates, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.real_image = surface
        self.image = pygame.transform.scale(surface, size)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.update(coordinates[0] - self.rect.width / 2, coordinates[1] - self.rect.height / 2, self.rect.width,
                         self.rect.height)

    def update(self, new_coordinates: tuple[int, int], new_size: tuple[int, int]) -> None:
        self.image = pygame.transform.scale(self.real_image, new_size)
        self.rect.update(new_coordinates[0] - new_size[0] / 2, new_coordinates[1] - new_size[1] / 2, new_size[0],
                         new_size[1])


class Bar(pygame.sprite.Sprite):
    def __init__(self, bar_surface, hp_bar_size, thickness) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image = bar_surface
        self.image = pygame.transform.scale(bar_surface, hp_bar_size)
        self.rect = self.image.get_rect()
        self.thickness = thickness

    def update(self, new_size: tuple[int, int], new_thickness: int) -> None:
        self.image = pygame.transform.scale(self.real_image, new_size)
        self.rect = self.image.get_rect()
        self.thickness = new_thickness


class Point(pygame.sprite.Sprite):
    def __init__(self, point_surface, bar_size, bar_thickness) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.real_image = point_surface
        self.image = pygame.transform.scale(point_surface,
                                               (bar_size[1] - bar_thickness[1] * 2, bar_size[1] - bar_thickness[1] * 2))
        self.rect = self.image.get_rect()
    def update(self, new_size: tuple[int,  int]) -> None:
        self.image = pygame.transform.scale(self.real_image, new_size)
        self.rect = self.image.get_rect()


class String(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, surface, pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = surface

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.update(pos[0], pos[1], self.rect.width, self.rect.height)
