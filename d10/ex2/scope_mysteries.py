from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    enchantment_types = ['Frozen', 'Earthen', 'Flowing']
    items_to_enchant = ['Sword', 'Staff', 'Wand', 'Shield']

    print("\nTesting mage counter...")
    my_counter = mage_counter()

    print(f"Call 1: {my_counter()}")
    print(f"Call 2: {my_counter()}")
    print(f"Call 3: {my_counter()}")

    print("\nTesting enchantment factory...")

    fire_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory(enchantment_types[0])

    print(fire_factory(items_to_enchant[0]))
    print(frozen_factory(items_to_enchant[3]))


if __name__ == "__main__":
    main()
