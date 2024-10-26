import pygame
import sys
from config import *

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображения
menu = pygame.image.load('Images/DeckMap.jpeg')
menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))  # Изменение размера изображения под экран
menu_rect = menu.get_rect(center=(WIDTH / 2, HEIGHT / 2))
battle = pygame.image.load('Images/MainGameTable.jpeg')
battle = pygame.transform.scale(battle, (WIDTH, HEIGHT))
# Шрифты
font = pygame.font.Font(None, 74)
start_text = font.render('Начать', True, BLACK)
exit_text = font.render('Выйти', True, BLACK)

# Кнопки
battle_button = pygame.image.load('Images/BattleButton.png')
battle_button = pygame.transform.scale(battle_button, (WIDTH * BATTLE_BUTTON_SIZE, HEIGHT * BATTLE_BUTTON_SIZE))
battle_button_rect = battle_button.get_rect()


def draw_menu():
    screen.blit(source=menu, dest=(0, 0))
    screen.blit(source=battle_button,
                dest=menu_rect.center)


def draw_battle():
    screen.blit(source=battle, dest=(0, 0))


def main():
    current_event = "Menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левый клик мыши
                mouse_pos = event.pos
                if battle_button_rect.collidepoint(mouse_pos):
                    current_event = "Battle"

        if current_event == "Menu":
            draw_menu()
        elif current_event == "Battle":
            draw_battle()

        pygame.display.update()


if __name__ == "__main__":
    main()
