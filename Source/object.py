import pygame


class Object(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, surface, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.real_image = surface
        self.image = pygame.transform.scale(surface, size)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
    def update(self, new_size: tuple[int, int]):
        self.image = pygame.transform.scale(self.real_image, new_size)
        self.rect = self.image.get_rect()