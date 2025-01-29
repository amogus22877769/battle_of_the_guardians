import random

from src.battle_of_the_guardians.structures.card import Card


class Ability:
    def __init__(self, kind: str, value: int, cost):
        self.kind: str = kind
        self.value: int = value
        self.cost: int = cost

    def cast(self, target_card: Card, cards: list[Card], target_opponent: Card, opponents: list[Card],
             flags: dict[str, set[Card], list[set[Card]]], energy_bar) -> None:
        match self.kind:
            case 'fire_wave':
                opponent_index: int = opponents.index(target_opponent) - 1
                for _ in range(3):
                    if opponent_index in range(len(opponents)):
                        opponents[opponent_index].current_health -= self.value
                    opponent_index += 1
            case 'fire_breathe':
                for opponent in opponents:
                    opponent.current_health -= self.value
            case 'ice_wall':
                if 'frozen' not in flags.keys():
                    print(f'setting frozen')
                    flags['frozen'] = [set() for _ in range(self.value)]
                print(flags['frozen'])
                frozen: bool = False
                for froze_set in flags['frozen']:
                    if target_opponent in froze_set:
                        frozen = True
                        break
                if not frozen:
                    flags['frozen'][self.value - 1].add(target_opponent)
                print(self.value - 1)
                print(flags['frozen'][0], flags['frozen'][1])
            case 'heal':
                random.choice(cards).current_health += self.value
            case 'ground_protection':
                for card in cards:
                    card.shield = card.current_shield + self.value
                    print(f'card.shield: {card.shield}')
            case 'strong':
                if cards.index(target_card) - 1 in range(len(cards)):
                    cards[cards.index(target_card) - 1].current_health += self.value
                if cards.index(target_card) + 1 in range(len(cards)):
                    cards[cards.index(target_card) + 1].current_health += self.value
            case 'acceleration':
                energy_bar.energy += min([card.ability.cost for card in cards])
            case 'thunder_punch':
                target_opponent.current_health -= self.value






