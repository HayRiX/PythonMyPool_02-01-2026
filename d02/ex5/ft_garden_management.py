#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name: str, water: int, sun: int):
        """Adds a plant to the garden with validation."""
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append({"name": name, "water": water, "sun": sun})
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print("Watering " + plant["name"] + " - success")
        except WaterError:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        for plant in self.plants:
            try:
                if not plant["name"]:
                    raise PlantError("Error: Plant name cannot be empty!")
                if plant["water"] > 10:
                    raise PlantError(f"Water level {plant['water']} "
                                     "is too high (max 10)")
                elif plant["water"] < 1:
                    raise PlantError(f"Water level {plant['water']} "
                                     "is too low (min 1)")
                if plant["sun"] < 2:
                    raise PlantError(f"Sunlight hours {plant['sun']} "
                                     "is too low (min 2)")
                elif plant["sun"] > 12:
                    raise PlantError(f"Sunlight hours {plant['sun']} "
                                     "is too high (max 12)")
                print(f"{plant['name']}: healthy (water: {plant['water']}, "
                      f"sun: {plant['sun']})")
            except PlantError as e:
                print(f"Error checking {plant['name']}: {e}")


def testing_error():
    print("=== Garden Management System ===")

    plant = GardenManager()

    print("\nAdding plants to garden...")
    plant.add_plant("tomato", 5, 8)
    plant.add_plant("lettuce", 15, 8)
    plant.add_plant("", 8, 5)

    print("\nWatering plants...")
    plant.water_plants()

    print("\nChecking plant health...")
    plant.check_health()

    print("\nTesting error recovery..")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    testing_error()
