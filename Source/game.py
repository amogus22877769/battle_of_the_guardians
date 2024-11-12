import sys

import pygame

from Source.config import WIDTH, HEIGHT, FRAME_RATE
from Source.draft import Draft
from Source.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.stage = 0
        self.stages = []
        self.stages.append(Menu())
        self.stages.append(Draft())

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def run(self):
        while True:
            self.handleEvents()

            self.stages[self.stage].draw()
            self.stage = self.stages[self.stage].update(self.stage)
            #self.clock.tick_busy_loop(FRAME_RATE)
            pygame.display.update()
