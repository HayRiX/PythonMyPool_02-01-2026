import time
import functools
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None:
                ints = [arg for arg in args if isinstance(arg, int)]
                power = ints[0] if ints else 0
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... (attempt "
                          f"{attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Kai"))
    print(MageGuild.validate_mage_name("Jo"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))


if __name__ == "__main__":
    main()
