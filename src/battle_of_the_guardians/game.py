import sys

import pygame

from src.battle_of_the_guardians import animations
from src.battle_of_the_guardians.action import Action
from src.battle_of_the_guardians.buffer import CURRENT_WINDOW_SIZE
from src.battle_of_the_guardians.config import DEFAULT_WIDTH, DEFAULT_HEIGHT, NAME_OF_THE_GAME, FRAME_RATE
from src.battle_of_the_guardians.defines import stage
from src.battle_of_the_guardians.stages.battle import Battle
from src.battle_of_the_guardians.stages.draft import Draft
from src.battle_of_the_guardians.stages.menu import Menu
from src.battle_of_the_guardians.stages.you_lost import YouLost


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.screen: pygame.display = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_icon(pygame.image.load('resources/img/icon.jpg'))
        pygame.display.set_caption(NAME_OF_THE_GAME)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.stage: stage = "menu"
        self.stages: dict[stage, Menu | Draft] = {"menu": Menu(),
                                                  "draft": Draft(),
                                                  "battle": Battle(),
                                                  "you_lost": YouLost()}
        self.actions: list[Action] = []
        self.old_screen_size: tuple[int, int] = (DEFAULT_WIDTH, DEFAULT_HEIGHT)

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
            CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1] = self.screen.get_width(), self.screen.get_height()
            print(CURRENT_WINDOW_SIZE)

    def run(self) -> None:
        while True:
            self.handle_events()
            animations.update_animations()
            old_stage: stage = self.stage
            self.stage = self.stages[self.stage].update(self.actions)
            self.stages[old_stage].draw(self.screen)
            self.clock.tick_busy_loop(FRAME_RATE)
            pygame.display.update()
            self.actions.clear()
            if self.stage is not old_stage:
                self.actions.append(Action("resize", (self.screen.get_width(), self.screen.get_height())))
