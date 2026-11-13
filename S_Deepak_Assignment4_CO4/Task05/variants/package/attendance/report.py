def format_report(percentages, absent_three_days):
    lines = [f"{reg}: {pct:.1f}%" for reg, pct in sorted(percentages.items())]
    lines.append("Absent 3 consecutive days: " + (", ".join(absent_three_days) or "None"))
    return "\n".join(lines)
