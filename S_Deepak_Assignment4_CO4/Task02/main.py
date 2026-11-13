from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
INPUT = BASE / "input"

def process_month(folder):
    counts = defaultdict(lambda: [0, 0])
    rejects = []
    files = sorted(Path(folder).glob("*.csv"))
    for file_path in files:
        with file_path.open("r", encoding="utf-8") as source:
            for line_number, raw_line in enumerate(source, start=1):
                line = raw_line.strip()
                if not line:
                    continue
                fields = [field.strip() for field in line.split(",")]
                if len(fields) != 3:
                    rejects.append((file_path.name, line_number, f"expected 3 fields, found {len(fields)}"))
                    continue
                register, date, status = fields
                if len(date) != 10 or date[4] != "-" or date[7] != "-":
                    rejects.append((file_path.name, line_number, "date must use YYYY-MM-DD"))
                    continue
                if status not in {"P", "A"}:
                    rejects.append((file_path.name, line_number, f"invalid status {status!r}"))
                    continue
                counts[register][0 if status == "P" else 1] += 1
    summaries = []
    for register, (present, absent) in sorted(counts.items()):
        total = present + absent
        percent = 100 * present / total if total else 0
        summaries.append((register, present, absent, total, percent))
    return files, summaries, rejects

def main():
    files, rows, rejects = process_month(INPUT)
    print(f"Daily files: {len(files)}")
    print("MODEL: counts[register] = [present_days, absent_days]; malformed rows -> (file, line, reason).")
    print("PSEUDOCODE: for each sorted daily file: open UTF-8; for each line: skip blank; split; validate fields/date/status; update one count; otherwise record reject. Then calculate each percentage and write both reports.")
    print("TRACE: 192311001,2026-10-01,P -> counts[192311001] = [1, 0]; damaged line -> reject, counts unchanged.")
    print("Register | Present | Absent | Valid days | Attendance | Below 75%")
    for reg, present, absent, total, percent in rows:
        print(f"{reg} | {present} | {absent} | {total} | {percent:.1f}% | {'YES' if percent < 75 else 'no'}")
    print(f"Rejected damaged rows: {len(rejects)}")
    for filename, line_number, reason in rejects:
        print(f"{filename}:{line_number}: {reason}")
    (BASE / "attendance_summary.csv").write_text("register,present,absent,valid_days,percentage\n" + "".join(f"{reg},{p},{a},{d},{pct:.1f}\n" for reg,p,a,d,pct in rows), encoding="utf-8")
    (BASE / "below_75_percent.csv").write_text("register,percentage\n" + "".join(f"{reg},{pct:.1f}\n" for reg,p,a,d,pct in rows if pct < 75), encoding="utf-8")
    (BASE / "rejected_lines.txt").write_text("".join(f"{name}:{line}: {reason}\n" for name,line,reason in rejects), encoding="utf-8")
    print("Reports: attendance_summary.csv, below_75_percent.csv, rejected_lines.txt")
    print("Complexity: S students, f files, l total lines -> O(l + S log S) time; O(S + r) memory for counts and r rejects.")
    print("Alternative per-student rereading: O(S*f*l) time; O(1) count space per student (plus report output).")

if __name__ == "__main__":
    main()
