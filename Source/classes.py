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
       self.rect.update(coordinates[0] - self.rect.width / 2, coordinates[1] - self.rect.height / 2, self.rect.width, self.rect.height)

class Card(pygame.sprite.Sprite):

    def __init__(self, card_surface, outline_surface, outline_thickness):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       pygame.surfarray.use_arraytype('numpy')
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       card_surface = pygame.transform.scale(card_surface, (CARD_SIZE[0] - 2 * outline_thickness[0], CARD_SIZE[1] - 2 * outline_thickness[1]))
       card_surface_pixel_array = pygame.surfarray.array3d(card_surface)
       outline_surface = pygame.transform.scale(outline_surface, CARD_SIZE)
       outline_surface_pixel_array = pygame.surfarray.array3d(outline_surface)
       outline_surface_alpha_array = pygame.surfarray.array_alpha(outline_surface)
       left_section = outline_surface_pixel_array[0:outline_thickness[0], :]
       mid_section = numpy.hstack((outline_surface_pixel_array[outline_thickness[0]:CARD_SIZE[0] - outline_thickness[0], 0:outline_thickness[1]],
                                   card_surface_pixel_array,
                                  outline_surface_pixel_array[outline_thickness[0]:CARD_SIZE[0] - outline_thickness[0], CARD_SIZE[1] -  outline_thickness[1]:CARD_SIZE[1]]))
       right_section = outline_surface_pixel_array[CARD_SIZE[0] - outline_thickness[0]:CARD_SIZE[0], :]
       final_card_pixel_array = numpy.vstack((left_section, mid_section, right_section))
       empty_array = pygame.PixelArray(Surface(CARD_SIZE))
       print(final_card_pixel_array)
       print(outline_surface_alpha_array)
       """for x in range(0, CARD_SIZE[0]):
           for y in range(0, CARD_SIZE[1]):
               print(final_card_pixel_array[x][y][0], final_card_pixel_array[x][y][1], final_card_pixel_array[x][y][2], outline_surface_alpha_array[x][y])
               empty_array[x][y] = pygame.Color(int(final_card_pixel_array[x][y][0]), int(final_card_pixel_array[x][y][1]), int(final_card_pixel_array[x][y][2]), a = int(outline_surface_alpha_array[x][y]))"""

       self.image = final_card_pixel_array.make_surface()
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(-self.rect.width, -self.rect.height)
