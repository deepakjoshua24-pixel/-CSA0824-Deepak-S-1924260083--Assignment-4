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
