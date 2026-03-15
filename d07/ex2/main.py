from ex2.EliteCard import EliteCard
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


def main() -> None:
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    print("Card: ['play', 'get_card_info', 'is_playable']")
    print("Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior = EliteCard("Arcane Warrior", 6, Rarity.EPIC.value, 5, 3, 4)

    print("\nCombat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("\nMagic phase:")
    print("Spell cast: "
          f"{arcane_warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
