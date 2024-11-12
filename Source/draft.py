import pygame  # Импортируем модуль Pygame для работы с графикой и звуком.

# Импортируем константы для координат карточек на этапе драфта.
from Source.config import LEFT_DRAFT_CARD_COORDINATES, RIGHT_DRAFT_CARD_COORDINATES

# Импортируем объекты из модуля init - это фон, кнопки, и изображения для карточек.
from Source.init import draft_map, screen, blazing_herald_raw, electro_wizard_raw, fire_dragon_raw, fire_wizard_raw, \
    ground_titan_raw, ice_wizard_raw, mermaid_raw, stone_dwarf_raw, vs_button

import random  # Импортируем модуль random для перемешивания карточек.


class Draft:  # Определяем класс Draft для управления процессом драфта.
    def __init__(self):  # Инициализируем состояние драфта.
        # Создаем словарь объектов, где храним фон, кнопки и карточки.
        self.objects = {"background": draft_map,
                        "buttons": vs_button,
                        "cards": [blazing_herald_raw, electro_wizard_raw, fire_dragon_raw, fire_wizard_raw, ground_titan_raw, ice_wizard_raw, mermaid_raw, stone_dwarf_raw]}
        # Перемешиваем карточки в случайном порядке.
        random.shuffle(self.objects["cards"])
        # Инициализируем переменную, которая отслеживает, сколько карточек уже выбрано.
        self.stage_multiplied_by_two = 0
        # Создаем пустой список для выбранных карточек.
        self.deck = []
    def handle_events(self):  # Обрабатываем события, такие как клики мышкой.
        # Проходим по всем событиям, которые произошли с момента последнего вызова.
        for event in pygame.event.get():
            # Проверяем, был ли клик мышки.
            if event.type == pygame.MOUSEBUTTONDOWN:  # Левый клик мыши
                # Проверяем, была ли нажата левая кнопка мыши на первой из двух доступных карточек.
                if self.objects["cards"][self.stage_multiplied_by_two].rect.collidepoint(event.pos):
                    # Если да, то увеличиваем счетчик выбранных карточек на 2.
                    self.stage_multiplied_by_two += 2
                    # Добавляем выбранную карточку в колоду.
                    self.deck.append(self.objects["cards"][self.stage_multiplied_by_two])
                # Проверяем, была ли нажата левая кнопка мыши на второй из двух доступных карточек.
                elif self.objects["cards"][self.stage_multiplied_by_two + 1].rect.collidepoint(event.pos):
                    # Если да, то увеличиваем счетчик выбранных карточек на 2.
                    self.stage_multiplied_by_two += 2
                    # Добавляем выбранную карточку в колоду.
                    self.deck.append(self.objects["cards"][self.stage_multiplied_by_two + 1])
        # Проверяем, выбраны ли все карточки.
        if self.stage_multiplied_by_two == 8:
            # Если да, то возвращаем 1.
            return 1
        else:
            # Если нет, то возвращаем 0.
            return 0
    def draw(self):  # Отрисовываем все объекты на экране.
        # Отрисовываем фон.
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        # Отрисовываем кнопки.
        pygame.sprite.Group(self.objects["buttons"]).draw(screen)
        # Отрисовываем две доступные карточки.
        pygame.sprite.Group(self.objects["cards"][self.stage_multiplied_by_two:self.stage_multiplied_by_two + 2]).draw(screen)
    def update(self, stage):  # Обновляем состояние игры.
        # Обновляем позицию первой доступной карточки.
        self.objects["cards"][self.stage_multiplied_by_two].rect.update(LEFT_DRAFT_CARD_COORDINATES[0] - self.objects["cards"][self.stage_multiplied_by_two].rect.width / 2,
                              LEFT_DRAFT_CARD_COORDINATES[1] - self.objects["cards"][self.stage_multiplied_by_two].rect.height / 2,
                              self.objects["cards"][self.stage_multiplied_by_two].rect.width, self.objects["cards"][self.stage_multiplied_by_two].rect.height)
        # Обновляем позицию второй доступной карточки.
        self.objects["cards"][self.stage_multiplied_by_two + 1].rect.update(RIGHT_DRAFT_CARD_COORDINATES[0] - self.objects["cards"][self.stage_multiplied_by_two + 1].rect.width / 2,
                               RIGHT_DRAFT_CARD_COORDINATES[1] - self.objects["cards"][self.stage_multiplied_by_two + 1].rect.height / 2,
                               self.objects["cards"][self.stage_multiplied_by_two + 1].rect.width, self.objects["cards"][self.stage_multiplied_by_two + 1].rect.height)
        # Обрабатываем события и возвращаем 1, если все карточки выбраны, иначе возвращаем 0.
        return self.handle_events() + stage