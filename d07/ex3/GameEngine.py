from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.strategy or not self.factory:
            raise ValueError("Engine is not configured properly!")

        hand: list = []
        battlefield: list = []
        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get('damage_dealt', 0)
        self.cards_created += 3

        return turn_result

    def get_engine_status(self) -> dict:
        if not self.strategy:
            return {}
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
