NAME_OF_THE_GAME: str = "Battle of the guardians"
DEFAULT_WIDTH: int = 1000
DEFAULT_HEIGHT: int = 1000
MAX_WIDTH: int = 1980
MAX_HEIGHT: int = 1080
FRAME_RATE: int = 60
RELATIVE_BATTLE_BUTTON_COORDINATES: tuple[float, float] = (0.5, 0.5)
RELATIVE_VS_BUTTON_COORDINATES: tuple[float, float] = (0.5, 0.5)
RELATIVE_BATTLE_BUTTON_SIZE: tuple[float, float] = (0.4, 0.4)
RELATIVE_VS_BUTTON_SIZE: tuple[float, float] = (0.2, 0.2)
RELATIVE_CARD_SIZE: tuple[float, float] = (0.18, 0.32)
RELATIVE_BASIC_OUTLINE_THICKNESS: tuple[float, float] = (21 / 500, 29 / 500)
NUMBER_OF_CARDS: int = 8
RELATIVE_LEFT_DRAFT_CARD_COORDINATES: tuple[float, float] = (0.25, 0.5)
RELATIVE_RIGHT_DRAFT_CARD_COORDINATES: tuple[float, float] = (0.75, 0.5)
RELATIVE_DISTANCE_BETWEEN_CARDS: float = (1 - RELATIVE_CARD_SIZE[0] * 4) / 5
ALL_CARD_COORDINATES: list[tuple[float, float]] = [(RELATIVE_DISTANCE_BETWEEN_CARDS + RELATIVE_CARD_SIZE[0] / 2,
                                                    0.7),
                                                   (RELATIVE_DISTANCE_BETWEEN_CARDS * 2 + RELATIVE_CARD_SIZE[0] / 2 * 3,
                                                    0.7),
                                                   (RELATIVE_DISTANCE_BETWEEN_CARDS * 3 + RELATIVE_CARD_SIZE[0] / 2 * 5,
                                                    0.7),
                                                   (RELATIVE_DISTANCE_BETWEEN_CARDS * 4 + RELATIVE_CARD_SIZE[0] / 2 * 7,
                                                    0.7)]
ALL_EVEN_OPPS_COORDINATES: list[tuple[float, float]] = [(ALL_CARD_COORDINATES[0][0], 77 / 300),
                                                        (ALL_CARD_COORDINATES[1][0], 77 / 300),
                                                        (ALL_CARD_COORDINATES[2][0], 77 / 300),
                                                        (ALL_CARD_COORDINATES[3][0], 77 / 300)]
RELATIVE_DISTANCE_BETWEEN_ODD_CARDS: float = (1 - RELATIVE_CARD_SIZE[0] * 3) / 4
ALL_ODD_OPPS_COORDINATES: list[tuple[float, float]] = [(RELATIVE_DISTANCE_BETWEEN_ODD_CARDS + RELATIVE_CARD_SIZE[0] / 2,
                                                        ALL_EVEN_OPPS_COORDINATES[0][1]),
                                                       (RELATIVE_DISTANCE_BETWEEN_ODD_CARDS * 2 + RELATIVE_CARD_SIZE[0]
                                                        / 2 * 3,
                                                        ALL_EVEN_OPPS_COORDINATES[0][1]),
                                                       (RELATIVE_DISTANCE_BETWEEN_ODD_CARDS * 3 + RELATIVE_CARD_SIZE[0]
                                                        / 2 * 5,
                                                        ALL_EVEN_OPPS_COORDINATES[0][1])]

FIRE_WIZARD_HP = 5000
FIRE_WIZARD_DMG = 3000
FIRE_DRAGON_HP = 8000
FIRE_DRAGON_DMG = 5000
ICE_WIZARD_HP = 4000
ICE_WIZARD_DMG = 2000
MERMAID_HP = 6000
MERMAID_DMG = 3000
GROUND_TITAN_HP = 10000
GROUND_TITAN_DMG = 4000
STONE_DWARF_HP = 5000
STONE_DWARF_DMG = 3000
BLAZING_HERALD_HP = 4000
BLAZING_HERALD_DMG = 4000
ELECTRO_WIZARD_HP = 6000
ELECTRO_WIZARD_DMG = 5000

SHADOW_MONSTER_HP = 3000
SHADOW_MONSTER_DMG = 1000
TERRIBLE_USURPER_HP = 6000
TERRIBLE_USURPER_DMG = 4000
ASH_DEMON_HP = 8000
ASH_DEMON_DMG = 5000
WATER_STORM_HP = 7000
WATER_STORM_DMG = 3000
BLACKOUT_SHADOW_HP = 5000
BLACKOUT_SHADOW_DMG = 4000
DESTROYER_OF_EARTH_HP = 9000
DESTROYER_OF_EARTH_DMG = 4000
MALIGNANT_INFESTATION_HP = 6000
MALIGNANT_INFESTATION_DMG = 3000
WINDSTORM_SHADOW_HP = 5000
WINDSTORM_SHADOW_DMG = 5000
GHOST_BIRD_HP = 4000
GHOST_BIRD_DMG = 2000

RELATIVE_DEFAULT_HP_BAR_SIZE: tuple[float, float] = (RELATIVE_CARD_SIZE[0], RELATIVE_CARD_SIZE[1] / 10)

RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR: float = RELATIVE_CARD_SIZE[0] / 10

RELATIVE_DEFAULT_HP_BAR_THICKNESS: tuple[float, float] = (RELATIVE_DEFAULT_HP_BAR_SIZE[0] / 36,
                                                          RELATIVE_DEFAULT_HP_BAR_SIZE[1] / 8)

MAXIMUM_AMOUNT_OF_HEALTH_POINTS_IN_DEFAULT_HP_BAR: int = int(RELATIVE_DEFAULT_HP_BAR_SIZE[0] * MAX_WIDTH)

RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE: float = 0.04

RELATIVE_FANTASY_FONT_FOR_CARD_HEALTH_SIZE_USING_THE_DEFAULT_HP_BAR: float = RELATIVE_DEFAULT_HP_BAR_SIZE[1]

RELATIVE_WAVES_COUNTER_RELATIVE_CENTER_COORDINATES: tuple[float, float] = (0.9,
                                                                           RELATIVE_FANTASY_FONT_FOR_WAVES_COUNTER_SIZE
                                                                           / 2 * 1.4)

RELATIVE_HEALTH_POINTS_ICON_SIZE: float = 1.3

RELATIVE_DEFAULT_ENERGY_BAR_SIZE: tuple[float, float] = (0.5, 0.1)

RELATIVE_ENERGY_ICON_SIZE: float = 1

DEFAULT_ENERGY_BAR_ALPHA = 100

RELATIVE_DEFAULT_ENERGY_BAR_COORDINATES: tuple[float, float] = (0.5, 0.95)

NUMBER_OF_POINTS_IN_DEFAULT_ENERGY_BAR: int = 5

TOTAL_ENERGY: int = 5

CARD_SIZE_MULTIPLIER: float = 1.2

DRAFT_PICK_ANIMATION_DURATION: int = 10

FIRE_WAVE_DMG = 2000
FIRE_WAVE_COST = 2
FIRE_BREATHE_DMG = 5000
FIRE_BREATHE_COST = 4
HEAL_AMOUNT = 3000
HEAL_COST = 3
GROUND_PROTECTION_AMOUNT = 2000
GROUND_PROTECTION_COST = 1
STRONG_AMOUNT = 1000
STRONG_COST = 1
THUNDER_PUNCH_DMG = 6000
THUNDER_PUNCH_COST = 5
ICE_WALL_TIME = 2
ICE_WALL_COST = 2
ACCELERATION_COST = 1

