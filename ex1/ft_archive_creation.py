def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")

    try:
        with open("new_discovery.txt", "w") as file:
            print("Storage unit created successfully\n")
            print("Inscribing preservation data...")
            entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
            entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
            entry3 = "[ENTRY 003] Archived by Data Archivist trainee\n"

            file.write(entry1)
            file.write(entry2)
            file.write(entry3)

            print(entry1, end="")
            print(entry2, end="")
            print(entry3)
            print("Data inscription complete. Storage unit sealed.")
            print("Archive ’new_discovery.txt’ ready for long-term preservation.")

    except IOError:
        print("ERROR: Failed to create storage unit. Check permissions and disk space.")

if __name__ == "__main__":
    main()