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


from datetime import date as Date, timedelta
def summarize(rows):
    counts = {}
    by_date = {}
    for register, date, status in rows:
        pair = counts.setdefault(register, [0, 0])
        pair[0 if status == "P" else 1] += 1
        by_date.setdefault(register, {})[date] = status
    percentages = {reg: round(100 * p / (p + a), 1) for reg, (p, a) in counts.items()}
    absent_three_days = []
    for reg, dates in by_date.items():
        ordered = sorted(dates)
        for i in range(max(0, len(ordered)-2)):
            days = ordered[i:i+3]
            consecutive = (Date.fromisoformat(days[1]) == Date.fromisoformat(days[0]) + timedelta(days=1)
                           and Date.fromisoformat(days[2]) == Date.fromisoformat(days[1]) + timedelta(days=1))
            if consecutive and [dates[day] for day in days] == ["A", "A", "A"]:
                absent_three_days.append(reg)
                break
    return percentages, sorted(absent_three_days)


def format_report(percentages, absent_three_days):
    lines = [f"{reg}: {pct:.1f}%" for reg, pct in sorted(percentages.items())]
    lines.append("Absent 3 consecutive days: " + (", ".join(absent_three_days) or "None"))
    return "\n".join(lines)
