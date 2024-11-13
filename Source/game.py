import sys

import pygame

from Source.config import WIDTH, HEIGHT, FRAME_RATE
from Source.draft import Draft
from Source.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.stage = "menu"
        self.stages = {"menu": Menu(),
                       "draft": Draft()}
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return event.pos
            return 0


    def run(self):
        while True:
            pos = self.handle_events()

            self.stages[self.stage].draw()
            self.stage = self.stages[self.stage].update(pos)
            #self.clock.tick_busy_loop(FRAME_RATE)
            pygame.display.update()
