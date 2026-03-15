from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")

    turn_result = engine.simulate_turn()
    print(f"Actions: {turn_result}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
