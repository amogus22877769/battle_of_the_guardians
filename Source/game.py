import sys

from os import environ

import numpy

from Source.config import update_const, WIDTH, HEIGHT

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from Source.action import Action
from Source.battle import Battle
from Source.draft import Draft
from Source.init import stage, update_sprites, screen
from Source.menu import Menu


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()
        self.stage: stage =  "menu"
        self.stages: dict[stage: Menu | Draft | Battle] = {"menu": Menu(),
                                                           "draft": Draft(),
                                                           "battle": Battle()}
        self.actions: list[Action] = []
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.actions.append(Action("click", event.pos))


    def run(self) -> None:
        old: tuple[int, int] = (0, 0)
        while True:
            if screen.get_width() != old[0] or screen.get_height() != old[1]:
                update_const(screen.get_width(), screen.get_height())
                update_sprites()
                print(f'new: {WIDTH, HEIGHT}')
                old = (screen.get_width(), screen.get_height())
                print(1)
            self.handle_events()

            self.stages[self.stage].draw()
            self.stage = self.stages[self.stage].update(self.actions)
            #self.clock.tick_busy_loop(FRAME_RATE)
            pygame.display.update()
            self.actions.clear()
