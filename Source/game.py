import sys

from os import environ

import numpy

from Source.battle import Battle
from Source.config import Config
from Source.draft import Draft

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from Source.action import Action
from Source.menu import Menu

from Source.defines import stage

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.config: Config = Config()
        self.screen: pygame.display = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT), pygame.RESIZABLE)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.stage: stage = "menu"
        self.stages: dict[stage: Menu | Draft | Battle] = {"menu": Menu(),
                       "draft": Draft(),
                       "battle": Battle()}
        self.actions: list[Action] = []
        self.old_screen_size: tuple[int, int] = (self.config.WIDTH, self.config.HEIGHT)
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.actions.append(Action("click", event.pos))
        if self.screen.get_width() != self.old_screen_size[0] or self.screen.get_height() != self.old_screen_size[1]:
            self.actions.append(Action("resize", (self.screen.get_width(), self.screen.get_height())))
            self.old_screen_size = (self.screen.get_width(), self.screen.get_height())


    def run(self) -> None:
        while True:
            self.handle_events()

            self.stages[self.stage].draw().draw(self.screen)
            self.stage = self.stages[self.stage].update(self.actions)
            #self.clock.tick_busy_loop(FRAME_RATE)
            pygame.display.update()
            self.actions.clear()
