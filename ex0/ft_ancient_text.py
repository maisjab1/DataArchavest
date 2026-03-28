def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file_path = "F:\\42\\data-generator-tools\\ancient_fragment.txt"
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open(file_path, "r") as file:
            text = file.read()
            print("Connection established...")
            print("Recovered Data:")
            print(text)
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first. ")


if __name__ == "__main__":
    main()
