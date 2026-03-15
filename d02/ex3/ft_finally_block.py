#!/usr/bin/env python3
def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    try:
        plants_list = ["tomato", "lettuce", "carrots"]
        water_plants(plants_list)
        print("Watering completed successfully!")
    except Exception as e:
        print(e)

    print("\nTesting with error...")
    try:
        bad_list = ["tomato", None, "carrots"]
        water_plants(bad_list)
    except Exception as e:
        print(e)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
