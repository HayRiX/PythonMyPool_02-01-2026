from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    dragon = TournamentCard(
        "Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5, 1200, "dragon_001")
    print("\nFire Dragon (ID: dragon_001):")
    print("Interfaces: [Card, Combatable, Rankable]")
    print(f"Rating: {dragon.rating}")
    print(f"Record: {dragon.wins}-{dragon.losses}")

    wizard = TournamentCard(
        "Ice Wizard", 4, Rarity.EPIC.value, 4, 3, 1150, "wizard_001")
    print("\nIce Wizard (ID: wizard_001):")
    print("Interfaces: [Card, Combatable, Rankable]")
    print(f"Rating: {wizard.rating}")
    print(f"Record: {wizard.wins}-{wizard.losses}")

    platform = TournamentPlatform()
    platform.register_card(dragon)
    platform.register_card(wizard)

    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, stats in enumerate(leaderboard, 1):
        print(f"{i}. {stats['name']} - Rating: "
              f"{stats['rating']} ({stats['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
