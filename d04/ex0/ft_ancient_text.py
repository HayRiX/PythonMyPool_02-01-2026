def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        file = open("ancient_fragment.txt", "r")
        print(r"Accessing Storage Vault: ancient\_fragment.txt")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(file.read())
        file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found.\n       Run data generator "
              "first.\n")


if __name__ == "__main__":
    main()
