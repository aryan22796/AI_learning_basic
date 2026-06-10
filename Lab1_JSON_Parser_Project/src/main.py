import os
import json
from reader import load_customers, save_report
from processor import filter_active_customers, build_report

BASE_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(BASE_DIR, "..", "data", "customers.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "..", "output", "report.txt")


def main():
    try:
        customers = load_customers(INPUT_FILE)
        active_customers = filter_active_customers(customers)
        report_lines = build_report(active_customers)
        save_report(OUTPUT_FILE, report_lines)
        print(f"Report saved: {OUTPUT_FILE}")
    except FileNotFoundError:
        print(f"Error: input file not found: {INPUT_FILE}")
    except json.JSONDecodeError:
        print(f"Error: invalid JSON format in file: {INPUT_FILE}")
    except KeyError as error:
        print(f"Error: missing expected field in data: {error}")
    except ValueError as error:
        print(f"Error: invalid value in data: {error}")


if __name__ == "__main__":
    main()
