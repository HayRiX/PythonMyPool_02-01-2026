#!/usr/bin/env python3
def check_temperature(temp_str: str):
    try:
        tmp = int(temp_str)
        if 0 <= tmp <= 40:
            print(f"Temperature {tmp}°C is perfect for plants!")
            return tmp
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    # return None


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_cases = [
        "25",
        "abc",
        "100",
        "-50"
    ]
    for value in test_cases:
        print(f"\nTesting temperature: {value}")
        check_temperature(value)
    print("\nAll tests completed - program didn't crash!")
