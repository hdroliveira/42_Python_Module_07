from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, starting_rating: int = 1000):
        super().__init__(name, cost, rarity)

        self.attack_val = attack
        self.health = health
        self.max_health = health

        self.rating = starting_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "effect": "Entered tournament arena"
        }

    def attack(self, target: Any) -> Dict:
        target_name = getattr(target, 'name', str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_val
        }

    def defend(self, incoming_damage: int) -> Dict:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_val,
            "health": self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, count: int) -> None:
        self.wins += count
        self.rating += (16 * count)

    def update_losses(self, count: int) -> None:
        self.losses += count
        self.rating -= (16 * count)

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> Dict:
        return {
            **self.get_card_info(),
            **self.get_combat_stats(),
            **self.get_rank_info()
        }
