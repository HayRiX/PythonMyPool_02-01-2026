from .Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int
            ) -> None:

        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers.")

        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> dict:

        info = super().get_card_info()
        info['type'] = self.type
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> Dict[str, Any]:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
