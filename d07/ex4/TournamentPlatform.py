import random
from .TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = card1
        loser = card2

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        self.matches_played += 1

        _ = random.choice([True, False])

        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> List[dict]:
        sorted_cards = sorted(
            self.cards.values(), key=lambda c: c.rating, reverse=True)
        return [c.get_tournament_stats() for c in sorted_cards]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        total_rating = sum(c.rating for c in self.cards.values())
        avg_rating = int(total_rating / total_cards) if total_cards > 0 else 0

        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
