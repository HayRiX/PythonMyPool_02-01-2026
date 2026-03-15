import sys
import importlib


def check_module(module_name: str, description: str) -> bool:
    """
    Checks if a Python module is installed and prints its status.
    Uses importlib to gracefully handle missing dependencies.
    """
    try:
        module = importlib.import_module(module_name)
        # Attempt to get the version, default to 'unknown' if not found
        version: str = getattr(module, '__version__', 'unknown')
        print(f"[OK] {module_name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[FAILED] {module_name} is missing. {description} unavailable.")
        return False


def main() -> None:
    """Main function to load programs and analyze Matrix data."""
    print("\nLOADING STATUS: Loading programs...")

    # Check dependencies matching the exact expected output sequence
    has_pandas: bool = check_module("pandas", "Data manipulation ready")

    print("\nChecking dependencies:")
    has_requests: bool = check_module("requests", "Network access ready")
    has_matplotlib: bool = check_module("matplotlib", "Visualization ready")

    # If any required module is missing, show instructions and exit
    if not (has_pandas and has_requests and has_matplotlib):
        print("\nSYSTEM ERROR: Missing dependencies detected!")
        print("To load the required programs, run one of the following:")
        print("  Using pip:    pip install -r requirements.txt")
        print("  Using Poetry: poetry install")
        sys.exit(1)

    # All modules loaded successfully, proceed with the analysis
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    try:
        # Simulate generating Matrix anomaly data using pandas and numpy
        data = {
            'time_ms': np.arange(1000),
            'anomaly_signal': np.random.randn(1000).cumsum()
        }
        df = pd.DataFrame(data)

        print("Generating visualization...")
        # Create a visual plot of the data
        plt.figure(figsize=(10, 6))
        plt.plot(df['time_ms'], df['anomaly_signal'],
                 color='#00FF41', linewidth=1.5)
        plt.title('Matrix Anomaly Signal Detection')
        plt.xlabel('Time (ms)')
        plt.ylabel('Signal Strength')

        # Save the visualization to a file
        plt.savefig('matrix_analysis.png')
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"ERROR: Analysis failed due to a glitch: {e}")


if __name__ == "__main__":
    main()
