class Config:
    def __init__(self) -> None:
        self.NAME_OF_THE_GAME = "Battle of the guardians"
        self.WIDTH, self.HEIGHT = 1000, 1000
        self.FRAME_RATE = 1000
        self.BATTLE_BUTTON_COORDINATES = (self.WIDTH / 2, self.HEIGHT / 2)
        self.VS_BUTTON_COORDINATES = (self.WIDTH / 2, self.HEIGHT / 2)
        self.RELATIVE_BATTLE_BUTTON_SIZE = 0.4
        self.RELATIVE_VS_BUTTON_SIZE = 0.2
        self.BATTLE_BUTTON_SIZE = (self.WIDTH * self.RELATIVE_BATTLE_BUTTON_SIZE, self.HEIGHT * self.RELATIVE_BATTLE_BUTTON_SIZE)
        self.VS_BUTTON_SIZE = (self.WIDTH * self.RELATIVE_VS_BUTTON_SIZE, self.HEIGHT * self.RELATIVE_VS_BUTTON_SIZE)
        self.CARD_SIZE = (int(self.WIDTH / 50 * 9), int(self.HEIGHT / 25 * 8))
        self.BASIC_OUTLINE_THICKNESS = (int(self.WIDTH / 1000 * 42), int(self.HEIGHT / 1000 * 58))
        self.NUMBER_OF_CARDS = 8
        self.LEFT_DRAFT_CARD_COORDINATES = (self.WIDTH / 4, self.HEIGHT / 2)
        self.RIGHT_DRAFT_CARD_COORDINATES = (self.WIDTH * 3 / 4, self.HEIGHT / 2)
        self.DISTANCE_BETWEEN_CARDS = (self.WIDTH - self.CARD_SIZE[0] * 4) / 5
        self.ALL_CARD_COORDINATES = [(self.DISTANCE_BETWEEN_CARDS + self.CARD_SIZE[0] / 2, self.HEIGHT / 3 * 2),
                                (self.DISTANCE_BETWEEN_CARDS * 2 + self.CARD_SIZE[0] / 2 * 3, self.HEIGHT / 3 * 2),
                                (self.DISTANCE_BETWEEN_CARDS * 3 + self.CARD_SIZE[0] / 2 * 5, self.HEIGHT / 3 * 2),
                                (self.DISTANCE_BETWEEN_CARDS * 4 + self.CARD_SIZE[0] / 2 * 7, self.HEIGHT / 3 * 2)]
        self.FIRE_WIZARD_HP = 5000
        self.FIRE_WIZARD_DMG = 3000
        self.FIRE_DRAGON_HP = 8000
        self.FIRE_DRAGON_DMG = 5000
        self.ICE_WIZARD_HP = 4000
        self.ICE_WIZARD_DMG = 2000
        self.MERMAID_HP = 6000
        self.MERMAID_DMG = 3000
        self.GROUND_TITAN_HP = 10000
        self.GROUND_TITAN_DMG = 4000
        self.STONE_DWARF_HP = 5000
        self.STONE_DWARF_DMG = 3000
        self.BLAZING_HERALD_HP = 4000
        self.BLAZING_HERALD_DMG = 4000
        self.ELECTRO_WIZARD_HP = 6000
        self.ELECTRO_WIZARD_DMG = 5000
        self.SHADOW_MONSTER_HP = 3000
        self.SHADOW_MONSTER_DMG = 1000

        self.DEFAULT_HP_BAR_SIZE = (self.CARD_SIZE[0], self.CARD_SIZE[1] / 10)

        self.DISTANCE_BETWEEN_CARD_AND_HP_BAR = self.CARD_SIZE[0] / 10

        self.DEFAULT_HP_BAR_THICKNESS = (self.DEFAULT_HP_BAR_SIZE[0] / 36, self.DEFAULT_HP_BAR_SIZE[1] / 8)

        self.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR = int((self.DEFAULT_HP_BAR_SIZE[0] - 2 * self.DEFAULT_HP_BAR_THICKNESS[0]) / (
                    self.DEFAULT_HP_BAR_SIZE[1] - self.DEFAULT_HP_BAR_THICKNESS[1] * 2))

        self.FANTASY_FONT_FOR_WAVES_COUNTER_SIZE =self. HEIGHT / 10

        self.FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR = self.DEFAULT_HP_BAR_SIZE[1]

        self.WAVES_COUNTER_RIGHT_CORNER_POS = (self.WIDTH, 0)

        self.DARK_RED = (204, 44, 52)

        self.RELATIVE_HITPOINTS_ICON_SIZE = 1.3

        self.DEFAULT_ENERGY_BAR_SIZE = (self.WIDTH / 2, self.HEIGHT / 10)


    def update_const(self, new_width: int, new_height: int) -> None:
        self.WIDTH, self.HEIGHT = new_width, new_height
        self.BATTLE_BUTTON_COORDINATES = (self.WIDTH / 2, self.HEIGHT / 2)
        self.VS_BUTTON_COORDINATES = (self.WIDTH / 2, self.HEIGHT / 2)
        self.BATTLE_BUTTON_SIZE = (self.WIDTH * self.RELATIVE_BATTLE_BUTTON_SIZE, self.HEIGHT * self.RELATIVE_BATTLE_BUTTON_SIZE)
        self.VS_BUTTON_SIZE = (self.WIDTH * self.RELATIVE_VS_BUTTON_SIZE, self.HEIGHT * self.RELATIVE_VS_BUTTON_SIZE)
        self.CARD_SIZE = (int(self.WIDTH / 50 * 9), int(self.HEIGHT / 25 * 8))
        self.BASIC_OUTLINE_THICKNESS = (int(self.WIDTH / 1000 * 42), int(self.HEIGHT / 1000 * 58))
        self.LEFT_DRAFT_CARD_COORDINATES = (self.WIDTH / 4, self.HEIGHT / 2)
        self.RIGHT_DRAFT_CARD_COORDINATES = (self.WIDTH * 3 / 4, self.HEIGHT / 2)
        self.DISTANCE_BETWEEN_CARDS = (self.WIDTH - self.CARD_SIZE[0] * 4) / 5
        self.ALL_CARD_COORDINATES = [(self.DISTANCE_BETWEEN_CARDS + self.CARD_SIZE[0] / 2, self.HEIGHT / 3 * 2),
                                (self.DISTANCE_BETWEEN_CARDS * 2 + self.CARD_SIZE[0] / 2 * 3, self.HEIGHT / 3 * 2),
                                (self.DISTANCE_BETWEEN_CARDS * 3 + self.CARD_SIZE[0] / 2 * 5, self.HEIGHT / 3 * 2),
                                (self.DISTANCE_BETWEEN_CARDS * 4 + self.CARD_SIZE[0] / 2 * 7, self.HEIGHT / 3 * 2)]
        self.DEFAULT_HP_BAR_SIZE = (self.CARD_SIZE[0], self.CARD_SIZE[1] / 10)

        self.DISTANCE_BETWEEN_CARD_AND_HP_BAR = self.CARD_SIZE[0] / 10

        self.DEFAULT_HP_BAR_THICKNESS = (self.DEFAULT_HP_BAR_SIZE[0] / 36, self.DEFAULT_HP_BAR_SIZE[1] / 8)

        self.MAXIMUM_AMOUNT_OF_HITPOINTS_IN_DEFAULT_HP_BAR = int((self.DEFAULT_HP_BAR_SIZE[0] - 2 * self.DEFAULT_HP_BAR_THICKNESS[0]) / (
                self.DEFAULT_HP_BAR_SIZE[1] - self.DEFAULT_HP_BAR_THICKNESS[1] * 2))

        self.FANTASY_FONT_FOR_WAVES_COUNTER_SIZE = self.HEIGHT / 10

        self.FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR = self.DEFAULT_HP_BAR_SIZE[1]

        self.WAVES_COUNTER_RIGHT_CORNER_POS = (self.WIDTH, 0)

        self.DEFAULT_ENERGY_BAR_SIZE = (self.WIDTH / 2, self.HEIGHT / 10)
