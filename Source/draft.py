import pygame  # Импортируем модуль Pygame для работы с графикой и звуком.

from Source.action import Action
from Source.buffer import buffer_deck
from Source.card import Card
from Source.classes import Background, Button
# Импортируем константы для координат карточек на этапе драфта.
from Source.config import LEFT_DRAFT_CARD_COORDINATES, RIGHT_DRAFT_CARD_COORDINATES

# Импортируем объекты из модуля init - это фон, кнопки, и изображения для карточек.
from Source.init import draft_map, screen, blazing_herald_raw, electro_wizard_raw, fire_dragon_raw, fire_wizard_raw, \
    ground_titan_raw, ice_wizard_raw, mermaid_raw, stone_dwarf_raw, vs_button, stage, element

import random  # Импортируем модуль random для перемешивания карточек.

class Draft:  # Определяем класс Draft для управления процессом драфта.
    def __init__(self) -> None:  # Инициализируем состояние драфта.
        # Создаем словарь объектов, где храним фон, кнопки и карточки.
        self.objects: dict[element: Background | dict[element: Button] | list[Card]] = {"background": draft_map,
                        "buttons": {"vs_button": vs_button},
                        "cards": [blazing_herald_raw, electro_wizard_raw, fire_dragon_raw, fire_wizard_raw,
                                  ground_titan_raw, ice_wizard_raw, mermaid_raw, stone_dwarf_raw]}
        # Перемешиваем карточки в случайном порядке.
        random.shuffle(self.objects["cards"])
        # Инициализируем переменную, которая отслеживает, сколько карточек уже выбрано.
        self.stage_multiplied_by_two: int =  0
        # Создаем пустой список для выбранных карточек.
        self.deck: list[Card] = []

    def handle_events(self, actions: list[Action]) -> stage:  # Обрабатываем события, такие как клики мышкой.
        for action in actions:
            match action.kind:
                case "click":
                    if self.objects["cards"][self.stage_multiplied_by_two].sprite.rect.collidepoint(action.value):
                        # Добавляем выбранную карточку в колоду.
                        self.deck.append(self.objects["cards"][self.stage_multiplied_by_two])
                        # Если да, то увеличиваем счетчик выбранных карточек на 2.
                        self.stage_multiplied_by_two += 2
                    # Проверяем, была ли нажата левая кнопка мыши на второй из двух доступных карточек.
                    elif self.objects["cards"][self.stage_multiplied_by_two + 1].sprite.rect.collidepoint(action.value):
                        # Добавляем выбранную карточку в колоду.
                        self.deck.append(self.objects["cards"][self.stage_multiplied_by_two + 1])
                        # Если да, то увеличиваем счетчик выбранных карточек на 2.
                        self.stage_multiplied_by_two += 2
        # Проверяем, выбраны ли все карточки.
        if self.stage_multiplied_by_two == 8:
            for card in self.deck:
                buffer_deck.append(card)
            # Если да, то возвращаем 1.
            self.clear()
            return "battle"
        else:
            # Если нет, то возвращаем 0.
            return "draft"

    def draw(self) -> None:  # Отрисовываем все объекты на экране.
        # Отрисовываем фон.
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        # Отрисовываем кнопки.
        pygame.sprite.Group(self.objects["buttons"].values()).draw(screen)
        # Отрисовываем две доступные карточки.
        pygame.sprite.Group(self.objects["cards"][self.stage_multiplied_by_two].sprite, self.objects["cards"][self.stage_multiplied_by_two + 1].sprite).draw(
            screen)

    def update(self, actions: list[Action]) -> str:  # Обновляем состояние игры.
        # Обновляем позицию первой доступной карточки.
        self.objects["cards"][self.stage_multiplied_by_two].place(LEFT_DRAFT_CARD_COORDINATES)
        # Обновляем позицию второй доступной карточки.
        self.objects["cards"][self.stage_multiplied_by_two + 1].place(RIGHT_DRAFT_CARD_COORDINATES)
        # Обрабатываем события и возвращаем 1, если все карточки выбраны, иначе возвращаем 0.
        return self.handle_events(actions)
    def clear(self) -> None:
        random.shuffle(self.objects["cards"])
        self.stage_multiplied_by_two = 0
        self.deck.clear()

