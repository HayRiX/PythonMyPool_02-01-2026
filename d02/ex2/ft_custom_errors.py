#!/usr/bin/env python3
class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is an issue with watering."""
    pass


def check_plant_status():
    """Simulates checking a plant and finding a problem."""
    print("Testing PlantError...")
    raise PlantError("The tomato plant is wilting!")


def check_water_level():
    """Simulates checking water level and finding it low."""
    print("Testing WaterError...")
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    try:
        check_plant_status()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
