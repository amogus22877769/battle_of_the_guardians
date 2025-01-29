from binascii import Error

import pygame

from src.battle_of_the_guardians.config import ALL_CARD_COORDINATES, RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR, \
    ALL_EVEN_OPPS_COORDINATES, ALL_ODD_OPPS_COORDINATES, CARD_SIZE_MULTIPLIER, TOTAL_ENERGY
from src.battle_of_the_guardians.defines import flag
from src.battle_of_the_guardians.sprites.string import String
from src.battle_of_the_guardians.structures.card import Card
from random import choice, choices

from src.battle_of_the_guardians.structures.energy_bar import EnergyBar


class BattleController:
    def __init__(self, deck: list[Card], opps: list[Card], opposition: list[Card], waves_counter: String, energy_bar:EnergyBar) -> None:
        self.deck: list[Card] = deck
        self.opps: list[Card] = opps
        self.opposition: list[Card] = opposition
        self.waves_counter: String = waves_counter
        self.energy_bar = energy_bar
        self.integer_waves_counter: int = int(waves_counter.text[6:])
        self.flags: dict[str, set[Card] | list[set[Card]]] = {'ready': set(),
                                             'dead': set()}
        self.dict_of_strong_opps = {self.opposition[0]: 2,
                                    self.opposition[1]: 3,
                                    self.opposition[2]: 3,
                                    self.opposition[3]: 7,
                                    self.opposition[4]: 8,
                                    self.opposition[5]: 5,
                                    self.opposition[6]: 4,
                                    self.opposition[7]: 6
                                    }

    def place_cards(self):
        for card_index, card in enumerate(self.deck):
            card.place(ALL_CARD_COORDINATES[card_index])
            card.place_hp_bar(RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR)
            card.place_shield_bar()

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
            self.opps[len(ALL_EVEN_OPPS_COORDINATES)].place(free_coordinates)
            self.opps[len(ALL_EVEN_OPPS_COORDINATES)].place_hp_bar(RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR)
            for opp_index, opp_position in enumerate(ALL_EVEN_OPPS_COORDINATES):
                if free_coordinates[0] == opp_position[0]:
                    self.opps.insert(opp_index, self.opps.pop(len(ALL_EVEN_OPPS_COORDINATES)))

    def new_wave(self) -> None:
        self.integer_waves_counter += 1
        self.waves_counter.text = self.waves_counter.text[:6] + f'{self.integer_waves_counter}'
        max_force: int = self.integer_waves_counter * 10 + 5
        force: int = 0
        print(f'got there, {max_force}, {max(self.dict_of_strong_opps.values())}')
        while max_force - force >= max(self.dict_of_strong_opps.values()):
            chosen_opp = choice(self.opposition)
            self.opps.append(chosen_opp.copy())
            force += self.dict_of_strong_opps[chosen_opp]
        self.place_cards()
        self.place_opps()
        self.energy_bar.energy = TOTAL_ENERGY

    def ready(self, card: Card) -> None:
        if card not in self.flags['dead'] and card.ability.cost <= self.energy_bar.energy:
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
            #opp.current_health -= card.damage
            #for opp in self.opps:
                #if opp.current_health <= 0:
                    #self.opps.remove(opp)
                    #self.place_opps(free_coordinates=opp.outline.relative_center_coordinates)
            if self.energy_bar.energy - card.ability.cost >= 0:
                opp.current_health -= card.damage
                self.energy_bar.energy -= card.ability.cost
                card.ability.cast(card, self.deck, opp, self.opps, self.flags, self.energy_bar)
            to_remove: list[Card] = []
            for opp in self.opps:
                print(opp.current_health)
                if opp.current_health <= 0:
                    to_remove.append(opp)
                    #self.place_opps(free_coordinates=opp.outline.relative_center_coordinates)
            print(len(self.opps))
            [self.opps.remove(opp) for opp in to_remove]
            self.revenge()
            if not len(self.opps) or self.energy_bar.energy < min([c.ability.cost for c in self.deck]):
                self.new_wave()


    def revenge(self):
        shadow_energy: int = 15
        print(f'frozen: {self.flags.get('frozen', [])}')
        frozen = set()
        for opp in self.opps:
            for froze_stage in range(len(self.flags.get('frozen', []))):
                if opp in self.flags.get('frozen', [])[froze_stage]:
                    self.flags.get('frozen', [])[froze_stage].remove(opp)
                    if froze_stage:
                        self.flags.get('frozen', [])[froze_stage - 1].add(opp)
                        frozen.add(opp)
        print(f'frozen: {self.flags.get('frozen', [])}')
        not_frozen_opps = [opp for opp in self.opps if opp not in frozen]
        agro = choices(not_frozen_opps, k = min(5, len(not_frozen_opps)))
        for opp in agro:
            alive_deck = [card for card in self.deck if card not in self.flags['dead']]
            print(f'len {len(alive_deck)}')
            target = choice(self.deck)
            if target.current_health + target.current_shield - opp.damage > 0:
                if target.shield:
                    target.current_shield -= opp.damage
                    if target.current_shield <= opp.damage:
                        target.current_health -= (opp.damage - target.current_shield)
                        target.shield = 0
                else:
                    target.current_health -= opp.damage
            else:
                target.current_health = 0
                target.shield = 0
                self.flags['dead'].add(target)
                if len(alive_deck) == 1:
                    pygame.quit()
                    print(f'sucker')
            shadow_energy -= 3





