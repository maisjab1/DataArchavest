
def archive_manager(file_path: str) -> None:
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print("RESPONSE: Error occured")
        print("STATUS: Crisis handled\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to ’lost_archive.txt’...")
    archive_manager("lost_archive.txt")

    print("CRISIS ALERT: Attempting access to  ’classified_vault.txt’...")
    archive_manager("classified_vault.txt")
    file_path = "standard_archive.txt"

    print("ROUTINE ACCESS: Attempting access to ’standard_archive.txt’...")
    archive_manager(file_path)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
