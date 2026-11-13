from .reader import email_is_valid

def validate_record(record):
    issues = []
    if not record["register"]:
        issues.append("register is empty")
    if not record["name"]:
        issues.append("name is empty")
    if not record["department"]:
        issues.append("department is empty")
    if not email_is_valid(record["email"]):
        issues.append(f"invalid email {record['email']!r}")
    if not record["events"]:
        issues.append("no events selected")
    return issues
