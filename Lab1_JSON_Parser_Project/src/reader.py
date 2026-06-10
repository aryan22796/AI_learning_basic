import json


def load_customers(file_path):
    """Load customer records from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as source:
        return json.load(source)


def save_report(file_path, report_lines):
    """Write the report text lines to a file."""
    with open(file_path, "w", encoding="utf-8") as destination:
        destination.write("\n".join(report_lines))
