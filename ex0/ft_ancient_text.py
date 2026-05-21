def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file_path = "ancient_fragment.txt"
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open(file_path, "r")
        text = file.read()
        print("Connection established...\n")
        print("Recovered Data:")
        print(text)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first. ")


if __name__ == "__main__":
    main()
