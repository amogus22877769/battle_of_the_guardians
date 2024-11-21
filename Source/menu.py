# Импортируем библиотеку pygame, которая позволяет создавать игры и мультимедийные приложения.
import pygame

# Из модуля event библиотеки pygame используется класс event,  
# который отвечает за обработку событий, таких как нажатия клавиш или движения мыши.
from pygame import event

from Source.action import Action
from Source.classes import Background, Button
# Импортируем необходимые элементы из пользовательского модуля 'Source.init',
# такие как 'menu' для графики меню, 'battle_button' для кнопки боя и 'screen' для экрана отображения.
from Source.init import menu, battle_button, screen, stage, element


# Определяем класс Menu. 
# Этот класс будет отвечать за отображение меню игры и взаимодействие с пользователем.
class Menu:

    # Метод инициализации. 
    # Название должно быть __init__, чтобы работал конструктор класса
    def __init__(self) -> None:
        # Словарь 'objects' будет хранить все графические элементы интерфейса, 
        # как фон, так и кнопки, для легкого доступа по ключам.
        self.objects: dict[element: Background | dict[element: Button]] = {
            "background": menu,  # Устанавливаем фон меню в объект 'menu'.
            "buttons": {"battle_button": battle_button}  # Устанавливаем объект кнопки боя.
        }

    # Метод для обработки обновлений, связанным с взаимодействием пользователя.
    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.objects["buttons"]["battle_button"].rect.collidepoint(action.value):
                        # Возвращаем значение 1, чтобы указать, что кнопка была нажата.
                        return "draft"
        return "menu"

    # Метод для отрисовки всех объектов меню на экране.
    def draw(self) -> None:
        # Создаем группу спрайтов с помощью значений из словаря 'objects' и отрисовываем их на 'screen'.
        pygame.sprite.Group(self.objects["background"]).draw(screen)
        pygame.sprite.Group(self.objects["buttons"].values()).draw(screen)

    # Метод для обновления состояния меню, принимает параметр stage.
    def update(self, actions: list[Action]) -> stage:
        # Обрабатываем обновления и возвращаем сумму с текущим значением stage.
        return self.handle_updates(actions)
