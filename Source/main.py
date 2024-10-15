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
image = pygame.image.load('cat_image.jpg')
image = pygame.transform.scale(image, (WIDTH, HEIGHT))  # Изменение размера изображения под экран

# Шрифты
font = pygame.font.Font(None, 74)
start_text = font.render('Начать', True, BLACK)
exit_text = font.render('Выйти', True, BLACK)

# Кнопки
start_button_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
exit_button_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))


def draw_menu():
    screen.fill(WHITE)
    screen.blit(start_text, start_button_rect)
    screen.blit(exit_text, exit_button_rect)


def main():
    menu = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левый клик мыши
                mouse_pos = event.pos
                if start_button_rect.collidepoint(mouse_pos):
                    menu = False
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        if menu:
            draw_menu()
        else:
            screen.blit(image, (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()