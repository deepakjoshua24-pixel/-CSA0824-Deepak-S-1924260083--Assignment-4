from pathlib import Path
from attendance_module import read_rows, summarize, format_report
def run(folder):
    percentages, absent = summarize(read_rows(folder))
    output = Path(folder).parent / "output"; output.mkdir(exist_ok=True)
    (output / "attendance_percentage.txt").write_text("\n".join(f"{reg},{pct:.1f}%" for reg,pct in sorted(percentages.items()))+"\n",encoding="utf-8")
    (output / "absent_three_days.txt").write_text("\n".join(absent)+(("\n") if absent else ""),encoding="utf-8")
    return format_report(percentages, absent)
if __name__ == "__main__": print(run(Path(__file__).parent / "input"))
