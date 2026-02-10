from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "effect_type": self.effect_type,
            "targets_affected": len(targets),
            "resolved": True
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({
            "type": "Spell",
            "effect_type": self.effect_type
        })
        return info
