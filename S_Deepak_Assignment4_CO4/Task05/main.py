from pathlib import Path
import subprocess, sys
BASE = Path(__file__).resolve().parent / "variants"
variants = ["single_script", "one_module", "three_modules", "package"]
results = {}
for name in variants:
    folder = BASE / name
    result = subprocess.run([sys.executable, str(folder / "main.py")], cwd=folder, text=True, capture_output=True, check=True)
    (folder / "output.txt").write_text(result.stdout, encoding="utf-8")
    results[name] = result.stdout.strip()
    print(f"{name}: {result.stdout.strip().replace(chr(10), ' | ')}")
print("All four results identical:", len(set(results.values())) == 1)
print("Requirement-change estimate (implementation files touched): single=1; one-module=2; three-modules=2 (stats + main output); package=2 (stats + main output).")
print("Import forms: import attendance.stats; from attendance import stats; from attendance.stats import summarize.")
print("Module objects are cached once in sys.modules, so importing a used package does not repeatedly load it per function call.")
