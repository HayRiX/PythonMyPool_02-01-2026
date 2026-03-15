#!/usr/bin/env python3
class SecurePlant:
    """A class to represent a plant with secure data encapsulation."""
    def __init__(self, name: str) -> None:
        """
        Initialize the secure plant with a name and default private attributes.
        """
        self.name = name
        self.__height = 0
        self.__age = 0

    def get_height(self):
        """Return the current height of the plant."""
        return self.__height

    def get_age(self):
        """Return the current age of the plant."""
        return self.__age

    def set_height(self, value: int):
        """
        Set the height with validation.
        Rejects negative values to ensure data integrity.
        """
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int):
        """
        Set the age with validation.
        Rejects negative values to ensure data integrity.
        """
        if value < 0:
            print()
            print(f"Invalid operation attempted: "
                  f"age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")


print("=== Garden Security System ===")
plant1 = SecurePlant("Rose")
print(f"Plant created: {plant1.name}")
plant1.set_height(25)
plant1.set_age(30)
plant1.set_height(-5)
print(f"\nCurrent plant: {plant1.name} "
      f"({plant1.get_height()}cm, {plant1.get_age()} days)")
