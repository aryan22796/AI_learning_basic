import pandas as pd
from pathlib import Path

def read_csv(filepath):
    """Safely read CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"[INFO] Successfully read {filepath}")
        print(f"[INFO] Dataset shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None
    except Exception as e:
        print(f"[ERROR] Error reading file: {e}")
        return None

def write_report(filepath, content):
    """Write report to text file."""
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)
        print(f"[INFO] Report written to {filepath}")
        return True
    except Exception as e:
        print(f"[ERROR] Error writing report: {e}")
        return False

def export_csv(df, filepath):
    """Export DataFrame to CSV."""
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=True)
        print(f"[INFO] CSV exported to {filepath}")
        return True
    except Exception as e:
        print(f"[ERROR] Error exporting CSV: {e}")
        return False
