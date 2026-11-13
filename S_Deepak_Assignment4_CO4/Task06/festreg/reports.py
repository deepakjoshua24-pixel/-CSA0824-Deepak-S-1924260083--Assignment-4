import csv
from pathlib import Path

def write_outputs(output_folder, master, events, summary, errors):
    out = Path(output_folder)
    out.mkdir(parents=True, exist_ok=True)
    columns = ["register", "name", "department", "email", "events"]
    with (out / "master.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        for record in master:
            writer.writerow({**record, "events": ";".join(record["events"])})
    for event, records in sorted(events.items()):
        safe_name = "".join(ch.lower() if ch.isalnum() else "_" for ch in event).strip("_")
        with (out / f"event_{safe_name}.csv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=columns)
            writer.writeheader()
            for record in records:
                writer.writerow({**record, "events": ";".join(record["events"])})
    (out / "summary.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")
    (out / "error_log.txt").write_text("\n".join(errors) + ("\n" if errors else ""), encoding="utf-8")
