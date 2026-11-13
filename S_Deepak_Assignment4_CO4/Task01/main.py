from decimal import Decimal, InvalidOperation
from pathlib import Path

BASE = Path(__file__).resolve().parent

DEFECTS = [
    ("Hard-coded file path", "The program only works on one computer and one folder."),
    ("No with statement", "An error can leave the file open and its data unflushed."),
    ("Whole-file read", "A large file is copied into memory even though rows are processed one at a time."),
    ("Bare except with pass", "Malformed rows disappear without an explanation or record."),
    ("int amount conversion", "Valid currency such as 1250.50 raises ValueError."),
    ("Repeated string concatenation", "Building a long report repeatedly copies growing prefixes."),
    ("Blank final line", "A trailing newline can be mistaken for a malformed student record."),
    ("No rejected-row log", "The office cannot correct or audit records that were skipped."),
]

def process_file(filename):
    """Stream comma-separated register,name,amount rows and return totals and rejects."""
    totals = {}
    rejected = []
    with open(filename, "r", encoding="utf-8") as source:
        for line_number, raw_line in enumerate(source, start=1):
            line = raw_line.strip()
            if not line:
                continue
            fields = [field.strip() for field in line.split(",")]
            if len(fields) != 3:
                rejected.append((line_number, line, f"expected 3 fields, found {len(fields)}"))
                continue
            register, name, amount_text = fields
            try:
                amount = Decimal(amount_text)
                if not amount.is_finite() or amount < 0:
                    raise InvalidOperation
            except InvalidOperation:
                rejected.append((line_number, line, "amount must be a non-negative number"))
                continue
            if not register or not name:
                rejected.append((line_number, line, "register and name are required"))
                continue
            totals[register] = (name, totals.get(register, (name, Decimal("0.00")))[1] + amount)

    report_lines = [f"{register},{name},{amount:.2f}" for register, (name, amount) in sorted(totals.items())]
    (BASE / "repaired_report.csv").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    reject_lines = [f"line {number}: {reason} | {line}" for number, line, reason in rejected]
    (BASE / "rejected_lines.txt").write_text("\n".join(reject_lines) + ("\n" if reject_lines else ""), encoding="utf-8")
    return totals, rejected

def main():
    print("DESIGN DEFECTS")
    for index, (name, risk) in enumerate(DEFECTS, start=1):
        print(f"{index}. {name}: {risk}")
    totals, rejected = process_file(BASE / "input" / "mess_oct.txt")
    print("\nREPAIRED SCRIPT")
    print(f"Students totalled: {len(totals)}")
    for register, (name, amount) in sorted(totals.items()):
        print(f"{register} | {name} | {amount:.2f}")
    print(f"Rejected rows: {len(rejected)}")
    print("Rejected-row details: rejected_lines.txt")
    print("Safety: uses a parameter, with, streaming, Decimal, specific validation, and list + join.")

if __name__ == "__main__":
    main()
