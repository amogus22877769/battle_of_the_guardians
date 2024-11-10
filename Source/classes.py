import pygame
from pygame import Surface

from config import *
import numpy


class Background(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, surface):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.transform.scale(surface, (WIDTH, HEIGHT))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


class Button(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, surface, coordinates, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.transform.scale(surface, size)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.update(coordinates[0] - self.rect.width / 2, coordinates[1] - self.rect.height / 2, self.rect.width,
                         self.rect.height)


class Card(pygame.sprite.Sprite):

    def __init__(self, card_surface, outline_surface, outline_thickness):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        card_surface = pygame.transform.scale(card_surface, (
            CARD_SIZE[0] - 2 * outline_thickness[0], CARD_SIZE[1] - 2 * outline_thickness[1]))
        card_surface_pixel_array = pygame.surfarray.array3d(card_surface)
        outline_surface = pygame.transform.scale(outline_surface, CARD_SIZE)
        outline_surface_pixel_array = pygame.surfarray.array3d(outline_surface)
        left_section = outline_surface_pixel_array[0:outline_thickness[0], :]
        mid_section = numpy.hstack((
            outline_surface_pixel_array[outline_thickness[0]:CARD_SIZE[0] - outline_thickness[0],
            0:outline_thickness[1]],
            card_surface_pixel_array,
            outline_surface_pixel_array[outline_thickness[0]:CARD_SIZE[0] - outline_thickness[0],
            CARD_SIZE[1] - outline_thickness[1]:CARD_SIZE[1]]))
        right_section = outline_surface_pixel_array[CARD_SIZE[0] - outline_thickness[0]:CARD_SIZE[0], :]
        final_card_pixel_array = numpy.vstack((left_section, mid_section, right_section))
        final_surface = pygame.surfarray.make_surface(final_card_pixel_array)
        final_surface.set_colorkey(pygame.Color(0, 0, 0))
        self.image = final_surface
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(-self.rect.width, -self.rect.height)


class HPBar(pygame.sprite.Sprite):
    def __init__(self, bar_surface):
        pygame.sprite.Sprite.__init__(self)
        bar_surface = pygame.transform.scale(bar_surface, HP_BAR_SIZE)
        self.image = bar_surface
        self.rect = self.image.get_rect()
class Hitpoint(pygame.sprite.Sprite):
    bar = None
    hitpoint = None

    def __init__(self, hitpoint_surface):
        pygame.sprite.Sprite.__init__(self)
        hitpoint_surface = pygame.transform.scale(hitpoint_surface,
                               (HP_BAR_SIZE[1] - HP_BAR_THICKNESS[1] * 2, HP_BAR_SIZE[1] - HP_BAR_THICKNESS[1] * 2))
        self.image = hitpoint_surface
        self.rect = self.image.get_rect()
