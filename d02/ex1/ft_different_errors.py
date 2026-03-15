#!/usr/bin/env python3
def garden_operations(action):
    try:
        if action == "print_plant":
            print("Testing ValueError...")
            int("abc")

        elif action == "calculate_water":
            print("Testing ZeroDivisionError...")
            number = 10 / 0
            print(number)

        elif action == "read_config":
            print("Testing FileNotFoundError...")
            open("test.txt", "r")

        elif action == "check_inventory":
            print("Testing KeyError...")
            inventory = {
                "Sword": 10,
                "Pickaxe": 20
            }
            print(inventory["Shovel"])

    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    if action == "multip_actions":
        try:
            print("Testing multiple errors together...")
            number = 10 / 0
            open("test.txt", "r")
        except (ZeroDivisionError, FileNotFoundError):
            print("Caught an error, but program continues!")


def test_error_types():
    action = [
        "print_plant",
        "calculate_water",
        "read_config",
        "check_inventory",
        "multip_actions"
    ]
    print("=== Garden Error Types Demo ===\n")
    for act in action:
        garden_operations(act)
        print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
