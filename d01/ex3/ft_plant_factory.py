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
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]
print("=== Plant Factory Output ===")
plant_number = 0
while plant_number < 5:
    print(plants[plant_number].get_info())
    plant_number += 1
print(f"\nTotal plants created: {plant_number}")
