import random
from typing import List, Dict, Any
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop()
        raise IndexError("Cannot draw from an empty deck")

    def get_deck_stats(self) -> Dict[str, Any]:
        creatures = sum(1 for c in self.cards
                        if type(c).__name__ == "CreatureCard")
        spells = sum(1 for c in self.cards
                     if type(c).__name__ == "SpellCard")
        artifacts = sum(1 for c in self.cards
                        if type(c).__name__ == "ArtifactCard")

        total_cost = sum(c.cost for c in self.cards)
        avg_cost = total_cost / len(self.cards) if self.cards else 0.0

        return {
            'total_cards': len(self.cards),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 2)
        }
