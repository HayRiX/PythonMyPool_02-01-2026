def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(f"{file.read()}\n")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found.\n       Run data generator "
              "first.\n")

    with open("file.txt", "w") as file:
        print("SECURE PRESERVATION:")
        file.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
