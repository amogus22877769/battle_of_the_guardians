import random
from _operator import delitem
from pathlib import Path

import pygame

from frontend.src.battle_of_the_guardians.animations import Animation
from frontend.src.battle_of_the_guardians.buffer import CURRENT_WINDOW_SIZE
from frontend.src.battle_of_the_guardians.config import RELATIVE_CHANGE_HEALTH_FONT_SIZE, CHANGE_HEALTH_DURATION
from frontend.src.battle_of_the_guardians.sprites.string import String
from frontend.src.battle_of_the_guardians.structures.card import Card


class Ability:
    def __init__(self, kind: str, value: int, cost):
        self.kind: str = kind
        self.value: int = value
        self.cost: int = cost

    def cast(self, target_card: Card, cards: list[Card], target_opponent: Card, opponents: list[Card],
             flags: dict[str, set[Card], list[set[Card]]], energy_bar, strings, effects, next_action=lambda: None,
             ability_on_dead_opp=-1) -> None:
        match self.kind:
            case 'fire_wave':
                print(f'ability_on_dead_opp: {ability_on_dead_opp}')

                def modifier():
                    def inner():
                        opponent_ind: int = opponents.index(
                            target_opponent) - 1 if ability_on_dead_opp == -1 else ability_on_dead_opp
                        for j in range(3):
                            if j in range(len(opponents)):
                                opponents[opponent_ind].current_health -= self.value
                        next_action()

                    return inner

                opponent_index: int = opponents.index(
                    target_opponent) - 1 if ability_on_dead_opp == -1 else ability_on_dead_opp
                flag: bool = False
                for i in range(3):
                    if opponent_index in range(len(opponents)):
                        opponent = opponents[opponent_index]
                        s = String(
                            f'-{self.value if self.value <= opponent.current_health else opponent.current_health}',
                            pygame.Color('red'),
                            (opponent.hp_bar.relative_center_coordinates[0] + opponent.hp_bar.relative_size[0] / 2,
                             opponent.hp_bar.relative_center_coordinates[1]),
                            Path('resources/fonts/fantasy_capitals.otf'),
                            RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                            (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                        strings.append(s)
                        Animation([s],
                                  CHANGE_HEALTH_DURATION,
                                  (
                                      opponent.hp_bar.relative_center_coordinates[0] + opponent.hp_bar.relative_size[
                                          0] / 2,
                                      opponent.sprite.relative_center_coordinates[1])
                                  ).start(on_stop=modifier() if not flag else lambda: None)
                        flag = True
                    opponent_index += 1
            case 'fire_breathe':
                def modifier():
                    def inner():
                        for opp in opponents:
                            opp.current_health -= self.value
                        next_action()

                    return inner

                for opponent_index, opponent in enumerate(opponents):
                    print(f'index: 000{opponent_index}')
                    s = String(f'-{self.value if self.value <= opponent.current_health else opponent.current_health}',
                               pygame.Color('red'),
                               (opponent.hp_bar.relative_center_coordinates[0] + opponent.hp_bar.relative_size[0] / 2,
                                opponent.hp_bar.relative_center_coordinates[1]),
                               Path('resources/fonts/fantasy_capitals.otf'),
                               RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                               (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                    strings.append(s)
                    Animation([s],
                              CHANGE_HEALTH_DURATION,
                              (opponent.hp_bar.relative_center_coordinates[0] + opponent.hp_bar.relative_size[0] / 2,
                               opponent.sprite.relative_center_coordinates[1])
                              ).start(on_stop=modifier() if not opponent_index else lambda: None)
            case 'ice_wall':
                if not flags['frozen']:
                    print(f'setting frozen')
                    flags['frozen'] = [set() for _ in range(self.value)]
                if target_opponent not in effects['frozen']:
                    flags['frozen'][self.value - 1].add(target_opponent)
                    effects['frozen'][target_opponent] = effects['frozen']['default'].copy()
                    effects['frozen'][target_opponent].place(target_opponent.sprite.relative_center_coordinates)
                next_action()

            case 'heal':
                chosen_card: Card = random.choice(cards)
                if chosen_card.current_health < chosen_card.health:

                    def modifier():
                        def inner():
                            if not chosen_card.current_health:
                                flags['dead'].remove(chosen_card)
                                delitem(effects['dead'], chosen_card)
                            chosen_card.current_health += self.value
                            next_action()

                        return inner

                    s = String(
                        f'+{self.value if self.value <= chosen_card.health - chosen_card.current_health else chosen_card.health - chosen_card.current_health}',
                        pygame.Color('green'),
                        (chosen_card.hp_bar.relative_center_coordinates[0] + chosen_card.hp_bar.relative_size[0] / 2,
                         chosen_card.sprite.relative_center_coordinates[1]),
                        Path('resources/fonts/fantasy_capitals.otf'),
                        RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                        (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                    strings.append(s)
                    Animation([s],
                              CHANGE_HEALTH_DURATION,
                              (chosen_card.hp_bar.relative_center_coordinates[0] + chosen_card.hp_bar.relative_size[
                                  0] / 2,
                               chosen_card.hp_bar.relative_center_coordinates[1])
                              ).start(on_stop=modifier())
                else:
                    next_action()
            case 'ground_protection':
                def modifier():
                    def inner():
                        for local_card in cards:
                            local_card.shield = local_card.current_shield + self.value if local_card not in flags['dead'] else local_card.current_shield
                        next_action()

                    return inner

                flag: bool = False
                for card in cards:
                    if card not in flags['dead']:
                        s = String(f'+{self.value}',
                                   pygame.Color('lightblue'),
                                   (card.hp_bar.relative_center_coordinates[0] + card.hp_bar.relative_size[0] / 2,
                                    card.sprite.relative_center_coordinates[1]),
                                   Path('resources/fonts/fantasy_capitals.otf'),
                                   RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                                   (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                        strings.append(s)
                        Animation([s],
                                  CHANGE_HEALTH_DURATION,
                                  (card.shield_bar.relative_center_coordinates[0] + card.shield_bar.relative_size[0] / 2,
                                   card.shield_bar.relative_center_coordinates[1])
                                  ).start(on_stop=modifier() if not flag else lambda: None)
                        flag = True

            case 'strong':
                def modifier():
                    def inner():
                        if cards.index(target_card) - 1 in range(len(cards)):
                            if not cards[cards.index(target_card) - 1].current_health:
                                flags['dead'].remove(cards[cards.index(target_card) - 1])
                                delitem(effects['dead'], cards[cards.index(target_card) - 1])
                            cards[cards.index(target_card) - 1].current_health += self.value
                        if cards.index(target_card) + 1 in range(len(cards)):
                            if not cards[cards.index(target_card) + 1].current_health:
                                flags['dead'].remove(cards[cards.index(target_card) + 1])
                                delitem(effects['dead'], cards[cards.index(target_card) + 1])
                            cards[cards.index(target_card) + 1].current_health += self.value
                        next_action()

                    return inner

                flag: bool = False
                if cards.index(target_card) - 1 in range(len(cards)):
                    card = cards[cards.index(target_card) - 1]
                    if card.current_health < card.health:
                        s = String(
                            f'+{self.value if self.value <= card.health - card.current_health else card.health - card.current_health}',
                            pygame.Color('green'),
                            (card.hp_bar.relative_center_coordinates[0] + card.hp_bar.relative_size[0] / 2,
                             card.sprite.relative_center_coordinates[1]),
                            Path('resources/fonts/fantasy_capitals.otf'),
                            RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                            (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                        strings.append(s)
                        Animation([s],
                                  CHANGE_HEALTH_DURATION,
                                  (card.hp_bar.relative_center_coordinates[0] + card.hp_bar.relative_size[0] / 2,
                                   card.hp_bar.relative_center_coordinates[1])
                                  ).start(on_stop=modifier() if not flag else lambda: None)
                        flag = True
                if cards.index(target_card) + 1 in range(len(cards)):
                    card = cards[cards.index(target_card) + 1]
                    if card.current_health < card.health:
                        s = String(
                            f'+{self.value if self.value <= card.health - card.current_health else card.health - card.current_health}',
                            pygame.Color('green'),
                            (card.hp_bar.relative_center_coordinates[0] + card.hp_bar.relative_size[0] / 2,
                             card.sprite.relative_center_coordinates[1]),
                            Path('resources/fonts/fantasy_capitals.otf'),
                            RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                            (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                        strings.append(s)
                        Animation([s],
                                  CHANGE_HEALTH_DURATION,
                                  (card.hp_bar.relative_center_coordinates[0] + card.hp_bar.relative_size[0] / 2,
                                   card.hp_bar.relative_center_coordinates[1])
                                  ).start(on_stop=modifier() if not flag else lambda: None)
                    elif not flag:
                        next_action()
            case 'acceleration':
                energy_bar.energy += min([card.ability.cost for card in cards])
            case 'thunder_punch':
                if ability_on_dead_opp == -1:
                    def modifier():
                        def inner():
                            target_opponent.current_health -= self.value
                            next_action()

                        return inner

                    s = String(
                        f'-{self.value if self.value <= target_opponent.current_health else target_opponent.current_health}',
                        pygame.Color('red'),
                        (target_opponent.hp_bar.relative_center_coordinates[0] + target_opponent.hp_bar.relative_size[
                            0] / 2,
                         target_opponent.hp_bar.relative_center_coordinates[1]),
                        Path('resources/fonts/fantasy_capitals.otf'),
                        RELATIVE_CHANGE_HEALTH_FONT_SIZE,
                        (CURRENT_WINDOW_SIZE[0], CURRENT_WINDOW_SIZE[1]))
                    strings.append(s)
                    Animation([s],
                              CHANGE_HEALTH_DURATION,
                              (target_opponent.hp_bar.relative_center_coordinates[0] +
                               target_opponent.hp_bar.relative_size[0] / 2,
                               target_opponent.sprite.relative_center_coordinates[1])
                              ).start(on_stop=modifier())
                else:
                    next_action()
