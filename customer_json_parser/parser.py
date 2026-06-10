import json

INPUT_FILE = "customer_json_parser/lab/customers.json"
OUTPUT_FILE = "customer_json_parser/lab/active_customers.json"

def load_customers(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def is_active_customer(record):
    return record.get("status") == "active"

def format_customer(record):
    return {
        "customerId": record.get("id"),
        "customerName": record.get("name"),
        "email": record.get("email"),
        "customerStatus": record.get("status")
    }

def save_customers(file_path, customers):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(customers, f, indent=2)

def main():
    try:
        customers = load_customers(INPUT_FILE)
    except FileNotFoundError:
        print(f"Error: input file '{INPUT_FILE}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: invalid JSON in '{INPUT_FILE}'.")
        return

    active_customers = [
        format_customer(record)
        for record in customers
        if is_active_customer(record)
    ]

    if not active_customers:
        print("No active customers found.")
    else:
        save_customers(OUTPUT_FILE, active_customers)
        print(f"Saved {len(active_customers)} active customers to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
