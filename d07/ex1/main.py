from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    deck = Deck()

    deck.add_card(
        CreatureCard(
            "Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal", 2, Rarity.RARE.value, 3, "+1 mana per turn"))
    deck.add_card(
        SpellCard(
            "Lightning Bolt", 3, Rarity.COMMON.value, "damage"))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    card1 = deck.draw_card()
    if card1:
        print(f"\nDrew: {card1.name} (Spell)")
        print(f"Play result: {card1.play({})}")

    card2 = deck.draw_card()
    if card2:
        print(f"\nDrew: {card2.name} (Artifact)")
        print(f"Play result: {card2.play({})}")

    card3 = deck.draw_card()
    if card3:
        print(f"\nDrew: {card3.name} (Creature)")
        print(f"play result: {card3.play({})}")

    print("\nPolymorphism in action: Same interface, different card behaviors!"
          )


if __name__ == "__main__":
    main()
