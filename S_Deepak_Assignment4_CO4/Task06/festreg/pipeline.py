from pathlib import Path
from .reader import read_department
from .validation import validate_record
from .reports import write_outputs

def process_department_files(input_folder, output_folder, expected_files):
    input_path = Path(input_folder)
    master = []
    duplicates = []
    errors = []
    missing = []
    seen = set()
    for filename in expected_files:
        path = input_path / filename
        if not path.exists():
            missing.append(f"{filename}: missing file")
            continue
        try:
            rows = read_department(path)
        except (OSError, UnicodeError) as error:
            missing.append(f"{filename}: {error.__class__.__name__}: {error}")
            continue
        for line_number, record, parse_error in rows:
            if parse_error:
                errors.append(f"{filename}:{line_number}: {parse_error}")
                continue
            issues = validate_record(record)
            if issues:
                errors.append(f"{filename}:{line_number}: " + "; ".join(issues))
                continue
            register = record["register"]
            if register in seen:
                duplicates.append(f"{filename}:{line_number}: duplicate register {register}")
                continue
            seen.add(register)
            master.append(record)
    event_map = {}
    for record in master:
        for event in record["events"]:
            event_map.setdefault(event, []).append(record)
    summary = [f"Unique registrations: {len(master)}", f"Duplicate registrations: {len(duplicates)}",
               f"Invalid or damaged records: {len(errors)}", f"Missing or unreadable files: {len(missing)}"]
    summary.extend(f"{event}: {len(records)} participant(s)" for event, records in sorted(event_map.items()))
    complete_errors = errors + duplicates + missing
    write_outputs(output_folder, master, event_map, summary, complete_errors)
    return {"master": master, "duplicates": duplicates, "errors": errors, "missing": missing, "events": event_map}
