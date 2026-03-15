#!/usr/bin/env python3
class Plant:
    """A class to represent a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Print a formatted string representation of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, size: int) -> None:
        """Append size to the plant."""
        self.height += size

    def age_plant(self) -> None:
        """Increase age by one day."""
        self.age += 1


plant1 = Plant("Rose", 25, 30)
initial_height = plant1.height
print("=== Day 1 ===")
print(plant1.get_info())
day = 1
while day < 7:
    plant1.grow(1)
    plant1.age_plant()
    day += 1
print("=== Day 7 ===")
print(plant1.get_info())
print(f"Growth this week: +{plant1.height - initial_height}cm")
