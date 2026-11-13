from pathlib import Path
from datetime import date as Date, timedelta
def run(folder):
    rows=[]
    for path in sorted(Path(folder).glob("*.csv")):
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                parts=[part.strip() for part in line.strip().split(",")]
                if len(parts)==3 and parts[2] in {"P","A"}: rows.append(tuple(parts))
    counts={}; by_date={}
    for reg,date,status in rows:
        pair=counts.setdefault(reg,[0,0]); pair[0 if status=="P" else 1]+=1
        by_date.setdefault(reg,{})[date]=status
    percentages={reg:round(100*p/(p+a),1) for reg,(p,a) in counts.items()}
    absent=[]
    for reg,dates in by_date.items():
        ordered=sorted(dates)
        for i in range(max(0,len(ordered)-2)):
            days=ordered[i:i+3]
            consecutive=(Date.fromisoformat(days[1])==Date.fromisoformat(days[0])+timedelta(days=1) and
                         Date.fromisoformat(days[2])==Date.fromisoformat(days[1])+timedelta(days=1))
            if consecutive and [dates[d] for d in days]==["A","A","A"]:
                absent.append(reg); break
    output=Path(folder).parent/"output"; output.mkdir(exist_ok=True)
    percentage_text="\n".join(f"{reg},{pct:.1f}%" for reg,pct in sorted(percentages.items()))+"\n"
    absent_text="\n".join(sorted(absent))+(("\n") if absent else "")
    (output/"attendance_percentage.txt").write_text(percentage_text,encoding="utf-8")
    (output/"absent_three_days.txt").write_text(absent_text,encoding="utf-8")
    lines=[f"{reg}: {pct:.1f}%" for reg,pct in sorted(percentages.items())]
    lines.append("Absent 3 consecutive days: "+(", ".join(sorted(absent)) or "None"))
    return "\n".join(lines)
if __name__ == "__main__": print(run(Path(__file__).parent/"input"))
