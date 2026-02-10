from typing import Dict, List, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int, mana: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.defense = defense
        self.mana = mana

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "effect": "Elite card entered the battlefield"
        }

    def attack(self, target: Any) -> Dict:
        target_name = getattr(target, 'name', str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = max(0, incoming_damage - self.defense)
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        mana_cost = 4
        self.mana -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "mana": self.mana,
            "spell_power": 10
        }
