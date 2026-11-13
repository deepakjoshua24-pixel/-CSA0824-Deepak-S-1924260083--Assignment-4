import csv
from pathlib import Path

def read_department(path):
    """Read one comma-separated department file with semicolon-separated events."""
    rows = []
    with open(path, "r", encoding="utf-8", newline="") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                fields = next(csv.reader([line]))
            except csv.Error as error:
                rows.append((line_number, None, f"CSV error: {error}"))
                continue
            if len(fields) != 5:
                rows.append((line_number, None, f"expected 5 fields, found {len(fields)}"))
                continue
            register, name, department, email, events_text = (field.strip() for field in fields)
            events = [event.strip() for event in events_text.split(";") if event.strip()]
            rows.append((line_number, {"register": register, "name": name, "department": department,
                                       "email": email, "events": events}, None))
    return rows

def email_is_valid(email):
    """Simple course-level email check using string operations, not a regular expression."""
    if " " in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    labels = domain.split(".")
    return bool(local and len(labels) >= 2 and all(labels) and all(label[0].isalnum() for label in labels))
