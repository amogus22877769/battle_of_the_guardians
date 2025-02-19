from binascii import Error
from pathlib import Path

import pygame

from src.battle_of_the_guardians.animations import Animation
from src.battle_of_the_guardians.buffer import CURRENT_WINDOW_SIZE
from src.battle_of_the_guardians.config import ALL_CARD_COORDINATES, RELATIVE_DISTANCE_BETWEEN_CARD_AND_HP_BAR, \
    ALL_EVEN_OPPS_COORDINATES, ALL_ODD_OPPS_COORDINATES, CARD_SIZE_MULTIPLIER, TOTAL_ENERGY, \
    RELATIVE_CHANGE_HEALTH_FONT_SIZE, DEFAULT_WIDTH, DEFAULT_HEIGHT, CHANGE_HEALTH_DURATION, SHADOW_ENERGY, \
    SHADOW_HIT_COST
from src.battle_of_the_guardians.defines import flag
from src.battle_of_the_guardians.sprites.string import String
from src.battle_of_the_guardians.structures.card import Card
from random import choice, choices

from src.battle_of_the_guardians.structures.energy_bar import EnergyBar


class BattleController:
    def __init__(self, deck: list[Card], opps: list[Card], opposition: list[Card], waves_counter: String, energy_bar:EnergyBar, strings) -> None:
        self.deck: list[Card] = deck
        self.opps: list[Card] = opps
        self.opposition: list[Card] = opposition
        self.waves_counter: String = waves_counter
        self.energy_bar = energy_bar
        self.strings = strings
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
        self.pair = ()
        self.first_revenge: bool = True
        self.revenge_opps = []
        self.current_opp_index: int = 0
        self.old_target = None

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
        self.strings.clear()
        if self.opps:
            opp = self.opps[self.current_opp_index - 1]
            opp.sprite.resize((opp.sprite.relative_size[0] / CARD_SIZE_MULTIPLIER,
                               opp.sprite.relative_size[1] / CARD_SIZE_MULTIPLIER))
            opp.outline.resize((opp.outline.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                opp.outline.relative_size[1] / CARD_SIZE_MULTIPLIER))
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

    def hit(self, opp: Card) -> None:
        if self.flags['ready']:
            card = self.flags['ready'].pop()
            card.sprite.resize((card.sprite.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                card.sprite.relative_size[1] / CARD_SIZE_MULTIPLIER))
            card.outline.resize((card.outline.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                 card.outline.relative_size[1] / CARD_SIZE_MULTIPLIER))
            self.energy_bar.energy -= card.ability.cost
            self.pair = (card, opp)
            s = String(f'-{card.damage if card.damage <= opp.current_health else opp.current_health}',
                               pygame.Color('red'),
                               (opp.hp_bar.relative_center_coordinates[0] + opp.hp_bar.relative_size[0] / 2,
                                opp.hp_bar.relative_center_coordinates[1]),
                               Path('resources/fonts/fantasy_capitals.otf'),
                               RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                               (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
            self.strings.append(s)
            Animation([s],
                      CHANGE_HEALTH_DURATION,
                      (opp.hp_bar.relative_center_coordinates[0] + opp.hp_bar.relative_size[0] / 2,
                       opp.sprite.relative_center_coordinates[1])
                      ).start(on_stop=self.ability)


    def ability(self):
        self.strings.clear()
        card, opp = self.pair
        opp.current_health -= card.damage
        if opp.current_health <= 0:
            self.opps.remove(opp)
            self.place_opps(free_coordinates=opp.sprite.relative_center_coordinates)
        card.ability.cast(card, self.deck, opp, self.opps, self.flags, self.energy_bar, self.strings, next_action=self.revenge)\
            if self.opps else self.new_wave()# and self.energy_bar.energy >= min([card.ability.cost for card in self.deck if card not in self.flags['dead']])\

    def revenge(self):
        to_remove = []
        for opp in self.opps:
            if opp.current_health <= 0:
                to_remove.append(opp)
                self.place_opps(free_coordinates=opp.sprite.relative_center_coordinates)
        [self.opps.remove(killed_opp) for killed_opp in to_remove]
        print(f'revenge (i might swerve bend that corner woa - - a a -')
        if self.first_revenge:
            self.strings.clear()
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
            self.revenge_opps = choices(not_frozen_opps, k = min(int(SHADOW_ENERGY / SHADOW_HIT_COST), len(not_frozen_opps)))
            self.first_revenge = False
            self.current_opp_index = 0
            self.revenge() if not_frozen_opps else self.new_wave()
        else:
            print(f'opp: {self.current_opp_index}')
            if self.current_opp_index:
                target = self.old_target
                opp = self.opps[self.current_opp_index - 1]
                opp.sprite.resize((opp.sprite.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                   opp.sprite.relative_size[1] / CARD_SIZE_MULTIPLIER))
                opp.outline.resize((opp.outline.relative_size[0] / CARD_SIZE_MULTIPLIER,
                                    opp.outline.relative_size[1] / CARD_SIZE_MULTIPLIER))
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
                    if not [card for card in self.deck if card not in self.flags['dead']]:
                        pygame.quit()
                        print(f'sucker')
            self.strings.clear()
            opp = self.opps[self.current_opp_index]
            alive_deck = [card for card in self.deck if card not in self.flags['dead']]
            opp.sprite.resize((opp.sprite.relative_size[0] * CARD_SIZE_MULTIPLIER,
                                opp.sprite.relative_size[1] * CARD_SIZE_MULTIPLIER))
            opp.outline.resize((opp.outline.relative_size[0] * CARD_SIZE_MULTIPLIER,
                                 opp.outline.relative_size[1] * CARD_SIZE_MULTIPLIER))
            target = choice(alive_deck)
            s = String(
                f'-{opp.damage if opp.damage <= target.current_health else opp.current_health}',
                pygame.Color('red'),
                (target.hp_bar.relative_center_coordinates[0] + target.hp_bar.relative_size[0] / 2,
                 target.hp_bar.relative_center_coordinates[1]),
                Path('resources/fonts/fantasy_capitals.otf'),
                RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
            self.strings.append(s)
            self.old_target = target
            self.current_opp_index += 1
            Animation([s],
                      CHANGE_HEALTH_DURATION,
                      (target.hp_bar.relative_center_coordinates[0] + target.hp_bar.relative_size[0] / 2,
                       target.sprite.relative_center_coordinates[1])
                      ).start(on_stop=self.revenge if self.current_opp_index != len(self.revenge_opps) - 1 else self.new_wave)





