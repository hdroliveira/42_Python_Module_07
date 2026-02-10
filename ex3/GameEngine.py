from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.turns_simulated += 1
        return {
            "status": "Turn completed"
        }

    def get_engine_status(self) -> dict:
        strat_name = (self.strategy.get_strategy_name() if
                      self.strategy else "None")
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strat_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
