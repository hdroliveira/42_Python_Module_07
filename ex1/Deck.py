import random
from typing import List, Dict, Optional
from ex0.Card import Card


class Deck:
    def __init__(self, name: str):
        self.name = name
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost
            info = card.get_card_info()
            c_type = info.get("type", "Unknown")

            if c_type == "Creature":
                stats["creatures"] += 1
            elif c_type == "Spell":
                stats["spells"] += 1
            elif c_type == "Artifact":
                stats["artifacts"] += 1

        if stats["total_cards"] > 0:
            stats["avg_cost"] = total_cost / stats["total_cards"]

        return stats
