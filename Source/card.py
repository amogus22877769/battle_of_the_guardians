import numpy

import pygame

from Source.classes import Bar, Point
from Source.config import CARD_SIZE
from Source.object import Object

class Card:

    def __init__(self, card_surface: pygame.Surface, outline_surface: pygame.Surface, outline_thickness: tuple[int], hp_bar: Bar, hitpoints: list[Point], health: float, damage: float) -> None:
        self.hp_bar: Bar = hp_bar
        self.hitpoints: list[Point] = []
        for hitpoint in hitpoints:
            self.hitpoints.append(hitpoint)
        self.health: float = health
        self.damage: float = damage
        # Call the parent class (Sprite) constructor
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
        self.sprite: Object = Object(final_surface)
    def place(self, pos: tuple[int]) ->  None:
        self.sprite.rect.update(pos[0] - self.sprite.rect.width / 2,
                                pos[1] - self.sprite.rect.height / 2,
                                self.sprite.rect.width,
                                self.sprite.rect.height)
    def place_hp_bar(self, distance: int) -> None:
        self.hp_bar.rect.update(self.sprite.rect.left,
                                self.sprite.rect.top - distance - self.hp_bar.rect.height,
                                self.hp_bar.rect.width,
                                self.hp_bar.rect.height)

        for hitpoint_index in range(len(self.hitpoints)):
            self.hitpoints[hitpoint_index].rect.update(self.hp_bar.rect.left + self.hp_bar.thickness[0] + hitpoint_index * self.hitpoints[hitpoint_index].rect.width,
                                 self.hp_bar.rect.top + self.hp_bar.thickness[1],
                                 self.hitpoints[hitpoint_index].rect.width,
                                 self.hitpoints[hitpoint_index].rect.height)


