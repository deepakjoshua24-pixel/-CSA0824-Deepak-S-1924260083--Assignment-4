from pathlib import Path
def read_rows(folder):
    rows = []
    for path in sorted(Path(folder).glob("*.csv")):
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                parts = [part.strip() for part in line.strip().split(",")]
                if len(parts) == 3 and parts[2] in {"P", "A"}:
                    rows.append((parts[0], parts[1], parts[2]))
    return rows
