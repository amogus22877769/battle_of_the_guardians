from frontend.src.battle_of_the_guardians.buffer import CURRENT_WINDOW_SIZE
from frontend.src.battle_of_the_guardians.config import INPUT_BOX_RELATIVE_SIZE, INPUT_BOX_RELATIVE_OUTLINE_THICKNESS
from frontend.src.battle_of_the_guardians.sprites.object import Object
from frontend.src.battle_of_the_guardians.sprites.string import String


class Input:
    def __init__(self, box: Object, username: String):
        self.box: Object = box
        self.username: String = username

    def update(self, new_text):
        self.username.text += new_text if self.username.font.size(self.username.text + new_text)[0] / CURRENT_WINDOW_SIZE[0] <= INPUT_BOX_RELATIVE_SIZE[0] - INPUT_BOX_RELATIVE_OUTLINE_THICKNESS[0] * 2 else ''

    def backspace(self):
        self.username.text = self.username.text[:len(self.username.text) - 1] if self.username.text else ''
        print(self.username.text)


