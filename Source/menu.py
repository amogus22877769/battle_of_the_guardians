import pygame

from Source.action import Action
from Source.config import Config
from Source.defines import stage
from Source.menu_sprites import MenuSprites


class Menu:
    def __init__(self) -> None:
        # Словарь 'objects' будет хранить все графические элементы интерфейса, 
        # как фон, так и кнопки, для легкого доступа по ключам.
        self.sprites: MenuSprites = MenuSprites(Config())
        self.objects = {
            "background": self.sprites.menu,  # Устанавливаем фон меню в объект 'menu'.
            "buttons": {"battle_button": self.sprites.battle_button}  # Устанавливаем объект кнопки боя.
        }

    # Метод для обработки обновлений, связанным с взаимодействием пользователя.
    def handle_updates(self, actions: list[Action]) -> stage:
        for action in actions:
            match action.kind:
                case "click":
                    if self.objects["buttons"]["battle_button"].rect.collidepoint(action.value):
                        # Возвращаем значение 1, чтобы указать, что кнопка была нажата.
                        return "draft"
                case "resize":
                    self.sprites.update(action.value[0], action.value[1])
        return "menu"

    # Метод для отрисовки всех объектов меню на экране.
    def draw(self) -> pygame.sprite.Group:
        # Создаем группу спрайтов с помощью значений из словаря 'objects' и отрисовываем их на 'screen'.
        return pygame.sprite.Group(self.objects["background"], self.objects["buttons"].values())
    # Метод для обновления состояния меню, принимает параметр stage.
    def update(self, actions: list[Action]) -> stage:
        # Обрабатываем обновления и возвращаем сумму с текущим значением stage.
        return self.handle_updates(actions)
