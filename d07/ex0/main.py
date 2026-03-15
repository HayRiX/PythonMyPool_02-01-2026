from .CreatureCard import CreatureCard
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    dragon = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY.value, 7, 5)

    print("\nCreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
