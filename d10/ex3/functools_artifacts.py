import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations_map = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }

    if operation not in operations_map:
        raise ValueError("Unsupported operation")

    return functools.reduce(operations_map[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, 'Fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'Ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50,
                                               'Lightning')
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @functools.singledispatch
    def cast_spell(arg: Any) -> str:
        return "Unknown magic type"

    @cast_spell.register(int)
    def _(arg: int) -> str:
        return f"Casting damage spell with {arg} power"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Casting enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-casting {len(arg)} spells"

    return cast_spell


def main() -> None:
    magic_numbers = [20, 30, 10, 40]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(magic_numbers, 'add')}")
    print(f"Product: {spell_reducer(magic_numbers, 'multiply')}")
    print(f"Max: {spell_reducer(magic_numbers, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
