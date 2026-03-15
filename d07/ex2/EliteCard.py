import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, Any, List


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self, name: str, cost: int, rarity: str, attack_power: int,
            defense_power: int, mana_capacity: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.mana_capacity = mana_capacity
        self.current_mana = mana_capacity
        self.serial_number = f"ELITE-{random.randint(1000, 9999)}"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite Card deployed'
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_taken = max(0, incoming_damage - self.defense_power)
        damage_blocked = min(incoming_damage, self.defense_power)
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': True
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {'attack': self.attack_power, 'defense': self.defense_power}

    def cast_spell(
            self, spell_name: str, targets: List[Any]) -> Dict[str, Any]:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.current_mana += amount
        return {
            'channeled': amount,
            'total_mana': self.current_mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {'mana': self.current_mana}
