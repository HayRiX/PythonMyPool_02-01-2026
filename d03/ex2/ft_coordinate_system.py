import math
import sys


data = [(10, 20, 5), (31, -36, -24), (44, -15, -10), (-22, -33, 22),
        (-37, 36, 22), (19, -39, 12), (4, -46, -24), (-39, -23, -11),
        (14, 27, -24)]


def process(pos: str):
    try:
        parts = pos.split(",")    # parts = ["10", "20", "0"]
        x_str, y_str, z_str = parts
        x = int(x_str)
        y = int(y_str)
        z = int(z_str)
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: {e.args}')


def print_usage():
    print("Usage:")
    print("  python3 ft_coordinate_system.py teleport: x,y,z")
    print("  or")
    print("  python3 ft_coordinate_system.py teleport: x1,y1,z1 x2,y2,z2")


if __name__ == "__main__":
    arg_len = 0
    for count in sys.argv:
        arg_len += 1

    if arg_len == 1:
        print("=== Game Coordinate System ===")
        original = (0, 0, 0)
        x, y, z = (0, 0, 0)
        for coordinate in data:
            position_1 = coordinate
            print(f"\nPosition created: {position_1}")
            x, y, z = position_1
            dist_1 = math.sqrt(x**2 + y**2 + z**2)
            print(f"Distance between {original} and {position_1}: "
                  f"{dist_1:.2f}")
        print("\nUnpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

    if arg_len > 1:
        if sys.argv[1] == "teleport:" and arg_len == 3:
            position_1 = (0, 0, 0)
            print(f'\nParsing coordinates: "{sys.argv[2]}"')
            position_2 = process(sys.argv[2])
            if position_2 is not None:
                print(f"Parsed position: {position_2}")
                x, y, z = position_2
                dist = math.sqrt(x**2 + y**2 + z**2)
                print(f"Distance between {position_1} and "
                      f"{position_2}: {dist:.2f}")
                print("\nUnpacking demonstration:")
                print(f"Player at x={x}, y={y}, z={z}")
                print(f"Coordinates: X={x}, Y={y}, Z={z}")

        elif sys.argv[1] == "teleport:" and arg_len == 4:
            print(f'\nParsing coordinates: "{sys.argv[2]}" and '
                  f'"{sys.argv[3]}"')
            position_1 = process(sys.argv[2])
            position_2 = process(sys.argv[3])
            if position_1 is not None and position_2 is not None:
                print(f"Parsed position: {position_1} and {position_2}")
                x1, y1, z1 = position_1
                x2, y2, z2 = position_2
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 +
                                 (z2 - z1)**2)
                print(f"Distance between {position_1} and "
                      f"{position_2}: {dist:.2f}")
                print("\nUnpacking demonstration:")
                print(f"Player at x={x2}, y={y2}, z={z2}")
                print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")

        elif arg_len > 4 or arg_len < 3:
            print("Error: Invalid number of arguments.")
            print_usage()

        elif sys.argv[1] != "teleport:":
            print("Error: Unknown command.")
            print_usage()

# test :
# python3 ft_coordinate_system.py
# python3 ft_coordinate_system.py teleport:
# python3 ft_coordinate_system.py teleport: 5,9,4 7,5,3 7,4,9
# python3 ft_coordinate_system.py teleprt: 5,9,4 7,5,3
# python3 ft_coordinate_system.py teleport: 5,9,4 7,5,abc
# python3 ft_coordinate_system.py teleport: 5,9,4 7,5,3
