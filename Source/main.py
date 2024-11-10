import pygame
import sys
import random
from Source.classes import Background
from config import *
from classes import *
from init import *
import time
import numpy

# Инициализация Pygame
pygame.init()

menu_sprites = pygame.sprite.Group(menu, battle_button)

draft = []

deck = pygame.sprite.Group()

draft_stage = 0

current_draft_tuple = pygame.sprite.Group()


def main():
    current_event = "Menu"
    flag = True
    battle_flag = True
    while True:
        click = False
        mouse_pos = (0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Левый клик мыши
                mouse_pos = event.pos
                click = True
        match current_event:
            case "Menu":
                menu_sprites.draw(screen)
                if click:
                    if battle_button.rect.collidepoint(mouse_pos):
                        global draft, draft_stage, current_draft_tuple
                        draft = raw_card_sprites.sprites()
                        random.shuffle(draft)
                        print(draft)
                        draft_stage = 0
                        current_event = "Draft"
                        current_draft_tuple.empty()
            case "Draft":
                if draft_stage <= 7:
                    if flag:
                        current_draft_tuple.add(draft[draft_stage], draft[draft_stage + 1])
                        left_card = current_draft_tuple.sprites()[0]
                        left_card.rect.update(LEFT_DRAFT_CARD_COORDINATES[0] - left_card.rect.width / 2,
                                              LEFT_DRAFT_CARD_COORDINATES[1] - left_card.rect.height / 2,
                                              left_card.rect.width, left_card.rect.height)
                        right_card = current_draft_tuple.sprites()[1]
                        right_card.rect.update(RIGHT_DRAFT_CARD_COORDINATES[0] - right_card.rect.width / 2,
                                               RIGHT_DRAFT_CARD_COORDINATES[1] - right_card.rect.height / 2,
                                               right_card.rect.width, right_card.rect.height)
                        flag = False
                    if click:
                        if left_card.rect.collidepoint(mouse_pos):
                            deck.add(left_card)
                            draft_stage += 2
                            current_draft_tuple.empty()
                            flag = True
                        elif right_card.rect.collidepoint(mouse_pos):
                            deck.add(right_card)
                            draft_stage += 2
                            current_draft_tuple.empty()
                            flag = True
                else:
                    current_event = "Battle"
                    battle_flag = True
                draft_sprites.draw(screen)
                current_draft_tuple.draw(screen)
            case "Battle":
                if battle_flag:
                    for i in range(0, 4):
                        deck.sprites()[i].rect.update(ALL_CARD_COORDINATES[i][0] - CARD_SIZE[0] / 2, ALL_CARD_COORDINATES[i][1] - CARD_SIZE[1] / 2, deck.sprites()[i].rect.width, deck.sprites()[i].rect.height)
                        hp_bars_raw.sprites()[i].rect.update(deck.sprites()[i].rect.left, deck.sprites()[i].rect.top - DISTANCE_BETWEEN_CARD_AND_HP_BAR - HP_BAR_SIZE[1], hp_bars_raw.sprites()[i].rect.width, hp_bars_raw.sprites()[i].rect.height)
                    battle_flag = False
                pygame.sprite.GroupSingle(battle).draw(screen)
                deck.draw(screen)
                hp_bars_raw.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
