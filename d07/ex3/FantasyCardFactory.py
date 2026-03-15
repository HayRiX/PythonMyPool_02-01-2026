from enum import Enum
from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return CreatureCard("Goblin Warrior", 2, Rarity.COMMON.value, 3, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return SpellCard("Lightning Bolt", 3, Rarity.COMMON.value, "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArtifactCard("Mana Ring", 2, Rarity.RARE.value, 3, "+1 mana")

    def create_themed_deck(self, size: int) -> dict:
        return {'size': size, 'theme': 'Fantasy'}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
