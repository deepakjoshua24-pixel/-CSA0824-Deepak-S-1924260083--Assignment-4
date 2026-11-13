import runpy
from pathlib import Path
BASE = Path(__file__).resolve().parent
print("COMPLETED SUPPLIED TODO PROGRAM")
namespace = runpy.run_path(str(BASE / "complete_code.py"), run_name="completed_todo")
print("MISSING FILE CHECK")
print(namespace["summarise"]("missing_attendance.csv"))
print("\nBROAD-EXCEPTION MISUSE EXPERIMENT")
runpy.run_path(str(BASE / "misuse_experiment.py"), run_name="__main__")
