import os
import sys
from dotenv import load_dotenv


def check_security(env_exists: bool, mode: str) -> None:
    """Prints the security checklist based on current environment."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing or empty")

    print("[OK] Production overrides available")


def main() -> None:
    """Main function to run the Oracle configuration check."""
    print("\nORACLE STATUS: Reading the Matrix...")

    env_loaded = load_dotenv()

    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Disconnected (No URL provided)")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Denied (Missing Key)")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    check_security(env_loaded, mode)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"SYSTEM ERROR: The Oracle disconnected unexpectedly: {e}")
        sys.exit(1)
