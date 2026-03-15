from typing import Callable


test_values = [6, 8, 7]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence_spell


def main() -> None:
    print("\nTesting spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"
    combined = spell_combiner(fireball, heal)
    target = test_targets[0]
    result1, result2 = combined(target)
    print(f"Combined spell result: {result1}, {result2}")

    print("\nTesting power amplifier...")

    def simple_damage(power: int) -> int:
        return power
    mega_spell = power_amplifier(simple_damage, 3)
    base_power = 10
    amplified = mega_spell(base_power)
    print(f"Original: {base_power}, Amplified: {amplified}")


if __name__ == "__main__":
    main()
