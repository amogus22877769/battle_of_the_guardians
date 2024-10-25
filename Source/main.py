import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображения
Menu = pygame.image.load('Images/DeckMap.jpeg')
Menu = pygame.transform.scale(Menu, (WIDTH, HEIGHT))  # Изменение размера изображения под экран
Battle = pygame.image.load('Images/MainGameTable.jpeg')
Battle = pygame.transform.scale(Battle, (WIDTH, HEIGHT))
# Шрифты
font = pygame.font.Font(None, 74)
start_text = font.render('Начать', True, BLACK)
exit_text = font.render('Выйти', True, BLACK)

# Кнопки
BattleButton = pygame.image.load('Images/BattleButton.png')
BattleButton = pygame.transform.scale(BattleButton, (WIDTH / 5, HEIGHT / 5))


def draw_menu():
    screen.blit(source=Menu, dest=(0, 0))
    screen.blit(source=BattleButton, dest=pygame.rect(BattleButton).scale_by(5))


def draw_battle():
    screen.blit(Battle)


def main():
    current_event = "Menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левый клик мыши
                mouse_pos = event.pos

        if current_event == "Menu":
            draw_menu()
        elif current_event == "Battle":
            draw_battle()

        pygame.display.update()


if __name__ == "__main__":
    main()
