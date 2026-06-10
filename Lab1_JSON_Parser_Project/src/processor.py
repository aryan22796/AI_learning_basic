def is_active_customer(record):
    return record.get("status") == "active"


def format_customer(record):
    return {
        "customerId": record.get("id"),
        "customerName": record.get("name"),
        "email": record.get("email"),
        "status": record.get("status")
    }


def filter_active_customers(records):
    return [format_customer(record) for record in records if is_active_customer(record)]


def build_report(active_customers):
    report_lines = ["Active Customer Report", "======================", f"Total active customers: {len(active_customers)}", ""]
    report_lines += [f"{cust['customerId']} - {cust['customerName']} ({cust['email']})" for cust in active_customers]
    return report_lines
