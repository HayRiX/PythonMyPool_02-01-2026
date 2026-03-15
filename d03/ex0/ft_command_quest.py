import sys

print("=== Command Quest ===")

if len(sys.argv) == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")

elif len(sys.argv) > 1:
    received = 1
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    while received < len(sys.argv):
        print(f"Argument {received}: {sys.argv[received]}")
        received += 1

print(f"Total arguments: {len(sys.argv)}")
