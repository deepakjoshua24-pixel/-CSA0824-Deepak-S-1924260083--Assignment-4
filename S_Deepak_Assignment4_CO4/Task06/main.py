from pathlib import Path
from festreg.pipeline import process_department_files
BASE = Path(__file__).resolve().parent
EXPECTED = ["cse.txt", "ece.txt", "me.txt", "civil.txt", "eee.txt"]
result = process_department_files(BASE / "input", BASE / "output", EXPECTED)
print("COLLEGE FEST REGISTRATION DESK")
print("Expected department files:", len(EXPECTED))
print("Valid unique registrations:", len(result["master"]))
print("Duplicate registrations:", len(result["duplicates"]))
print("Invalid / damaged records:", len(result["errors"]))
print("Missing files:", len(result["missing"]))
print("Master:")
for row in result["master"]:
    print(f"{row['register']} | {row['name']} | {row['department']} | {row['email']} | {', '.join(row['events'])}")
print("Error log:")
for item in result["errors"] + result["duplicates"] + result["missing"]:
    print(item)
print("Created: master.csv, event_*.csv, summary.txt, error_log.txt")
print("DEMO includes clean input, duplicate register, invalid email, damaged row, and one missing department file.")
