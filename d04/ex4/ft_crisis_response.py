def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            print(f"{file.read()}")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("security_protocols.txt", "r") as file:
            print(f"{file.read()}")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            print("SUCCESS: Archive recovered - "
                  f"[{file.read()}]")
    except (FileNotFoundError, PermissionError):
        print("Error")
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
