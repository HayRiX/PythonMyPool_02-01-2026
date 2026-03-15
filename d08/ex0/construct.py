import os
import sys
import site


def in_environment() -> bool:
    """
    Detects if the script is running inside a virtual environment.
    It compares the current prefix with the base global prefix.
    """
    return sys.prefix != sys.base_prefix


def get_site_packages():
    """
    Retrieves the path where packages are installed in this environment.
    """
    return site.getsitepackages()[0]


def main() -> None:
    """Main function to display the matrix environment status."""
    try:
        current_python = sys.executable
        if in_environment():
            # Inside the Matrix / Virtual Environment
            venv_path = sys.prefix
            venv_name = os.path.basename(venv_path)

            print("\nMATRIX STATUS: Welcome to the construct")
            print(f"\nCurrent Python: {current_python}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {venv_path}")
            print("\nSUCCESS: You're in an isolated environment!")
            print(
                "Safe to install packages without "
                "affecting the global system.")
            print("\nPackage installation path:")
            print(get_site_packages())

        else:
            # Outside the Matrix / Global Environment
            print("\nMATRIX STATUS: You're still plugged in")
            print(f"\nCurrent Python: {current_python}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate   # On Windows")
            print("\nThen run this program again.")

    except Exception as e:
        print(
            f"SYSTEM ERROR: An unexpected glitch in the matrix occurred: {e}")


if __name__ == "__main__":
    main()
