from src.battle_of_the_guardians.config import ALL_CARD_COORDINATES, RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR, \
    ALL_EVEN_OPPS_COORDINATES, ALL_ODD_OPPS_COORDINATES, CARD_SIZE_MULTIPLIER
from src.battle_of_the_guardians.defines import flag
from src.battle_of_the_guardians.sprites.string import String
from src.battle_of_the_guardians.structures.card import Card


def how_many_need_to_spawn(wave: int) -> int:
    return wave ** 2


class GameController:
    def __init__(self, deck: list[Card], opps: list[Card], opp: list[Card], waves_counter: String) -> None:
        self.deck: list[Card] = deck
        self.opps: list[Card] = opps
        self.opp: list[Card] = opp
        self.waves_counter: String = waves_counter
        self.integer_waves_counter: int = int(waves_counter.text[6:])
        self.flags: dict[flag, set[Card]] = {'ready': set()}

    def place_cards(self):
        for card_index, card in enumerate(self.deck):
            card.place(ALL_CARD_COORDINATES[card_index])
            card.place_hp_bar(RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR)

    def place_opps(self, free_coordinates: tuple[float, float] = tuple()):
        if not free_coordinates or len(self.opps) <= len(ALL_EVEN_OPPS_COORDINATES):
            for opp_index, opp in enumerate(self.opps):
                match len(self.opps):
                    case 1:
                        opp.place(ALL_ODD_OPPS_COORDINATES[1])
                    case 2:
                        opp.place(ALL_EVEN_OPPS_COORDINATES[opp_index + 1])
                    case 3:
                        opp.place(ALL_ODD_OPPS_COORDINATES[opp_index])
                    case _:
                        opp.place(ALL_EVEN_OPPS_COORDINATES[opp_index]) if opp_index < len(
                            ALL_EVEN_OPPS_COORDINATES) else opp.place(
                            (-opp.outline.relative_size[0] / 2, -opp.outline.relative_size[1] / 2))
                opp.place_hp_bar(RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR)
        else:
            self.opps[len(ALL_EVEN_OPPS_COORDINATES) - 1].place(free_coordinates)
            self.opps[len(ALL_EVEN_OPPS_COORDINATES) - 1].place_hp_bar(RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR)

    def new_wave(self) -> None:
        self.integer_waves_counter += 1
        self.waves_counter.text = self.waves_counter.text[:6] + f'{self.integer_waves_counter}'
        [self.opps.append(self.opp[0].copy()) for _ in range(how_many_need_to_spawn(self.integer_waves_counter))]
        self.place_cards()
        self.place_opps()

    def ready(self, card: Card) -> None:
        if not self.flags['ready']:
            card.sprite.resize((card.sprite.relative_size[0] * CARD_SIZE_MULTIPLIER,
                                card.sprite.relative_size[1] * CARD_SIZE_MULTIPLIER))
            card.outline.resize((card.outline.relative_size[0] * CARD_SIZE_MULTIPLIER,
                                 card.outline.relative_size[1] * CARD_SIZE_MULTIPLIER))
            self.flags['ready'].add(card)
        elif card in self.flags['ready']:
            card.sprite.resize((card.sprite.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                card.sprite.relative_size[1] / CARD_SIZE_MULTIPLIER))
            card.outline.resize((card.outline.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                 card.outline.relative_size[1] / CARD_SIZE_MULTIPLIER))
            self.flags['ready'].remove(card)
        else:
            past_card = self.flags['ready'].pop()
            past_card.sprite.resize((past_card.sprite.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                     past_card.sprite.relative_size[1] / CARD_SIZE_MULTIPLIER))
            past_card.outline.resize((past_card.outline.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                      past_card.outline.relative_size[1] / CARD_SIZE_MULTIPLIER))
            self.ready(card)

    def attack(self, opp: Card) -> None:
        if self.flags['ready']:
            card = self.flags['ready'].pop()
            card.sprite.resize((card.sprite.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                card.sprite.relative_size[1] / CARD_SIZE_MULTIPLIER))
            card.outline.resize((card.outline.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                 card.outline.relative_size[1] / CARD_SIZE_MULTIPLIER))
            opp.current_health -= card.damage
            if opp.current_health <= 0:
                self.opps.remove(opp)
                if not len(self.opps):
                    self.new_wave()
                else:
                    self.place_opps(free_coordinates=opp.outline.relative_center_coordinates)
