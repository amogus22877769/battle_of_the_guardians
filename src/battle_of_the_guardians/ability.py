from src.battle_of_the_guardians.structures.card import Card


class Ability:
    def __init__(self, kind: str, value: int):
        self.kind: str = kind
        self.value: int = value

    def cast(self, target_card: Card, cards: list[Card], target_opponent: Card, opponents: list[Card],
             flags: dict[str, set[Card]]) -> None:
        match self.kind:
            case 'fire_wave':
                for opponent in opponents[cards.index(target_card) - 1: cards.index(target_card) + 1]:
                    opponent.current_health -= self.value
            case 'fire_breathe':
                for opponent in opponents:
                    opponent.current_health -= self.value
            case 'ice_wall':
                flags['frozen'].add(target_opponent)
            case 'heal':
                for card in cards:
                    card.current_health += self.value
            case 'ground_protection':
                pass
            case 'strong':
                cards[cards.index(target_card) - 1].current_health += self.value
                cards[cards.index(target_card) + 1].current_health += self.value
            case 'acceleration':
                pass
            case 'thunder_punch':
                target_opponent.current_health -= self.value





