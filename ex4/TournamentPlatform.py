from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        parts = card.name.lower().split()
        base_id = parts[-1] if len(parts) > 1 else parts[0]
        count = sum(1 for cid in self.cards if base_id in cid)
        card_id = f"{base_id}_{count + 1:03d}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            return {"error": "Invalid card IDs"}

        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]
        winner_id = None
        loser_id = None

        if c1.attack_val >= c2.attack_val:
            winner = c1
            winner_id = card1_id
            loser = c2
            loser_id = card2_id
        else:
            winner = c2
            winner_id = card2_id
            loser = c1
            loser_id = card1_id
        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[str]:
        sorted_cards = (sorted(self.cards.values(),
                        key=lambda c: c.rating, reverse=True))

        leaderboard = []
        for i, card in enumerate(sorted_cards, 1):
            info = card.get_rank_info()
            entry = (f"{i}. {card.name} - Rating: {info['rating']}"
                     f"({info['wins']}-{info['losses']})")
            leaderboard.append(entry)

        return leaderboard

    def generate_tournament_report(self) -> Dict:
        total_rating = sum(c.rating for c in self.cards.values())
        avg = total_rating / len(self.cards) if self.cards else 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
