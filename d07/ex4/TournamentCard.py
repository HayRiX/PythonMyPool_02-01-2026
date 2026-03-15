from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable
from typing import Dict, Any


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
            self, name: str, cost: int, rarity: str, attack_power: int,
            defense_power: int, initial_rating: int, card_id: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.rating = initial_rating
        self.id = card_id
        self.wins = 0
        self.losses = 0

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'card_played': self.name, 'mana_used': self.cost,
            'effect': 'Tournament card deployed'}

    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            'attacker': self.name, 'target': target,
            'damage': self.attack_power}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        return {
            'defender': self.name,
            'damage_taken': max(0, incoming_damage - self.defense_power)}

    def get_combat_stats(self) -> Dict[str, Any]:
        return {'attack': self.attack_power, 'defense': self.defense_power}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating, 'wins': self.wins, 'losses': self.losses}

    def get_tournament_stats(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
