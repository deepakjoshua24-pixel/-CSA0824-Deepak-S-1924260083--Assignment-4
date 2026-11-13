from pathlib import Path

def buggy_save_returns(books, log_path):
    log = open(log_path, "w", encoding="utf-8")
    for book in books:
        log.write(book)
    log.close()

def buggy_process(day_file, log_path, save=buggy_save_returns):
    try:
        source = open(day_file, "r", encoding="utf-8")
        books = source.read().split("\n")
        save(books, log_path)
        source.close()
    except FileNotFoundError:
        print("missing")

def repaired_process(day_file, log_path, error_path):
    try:
        with open(day_file, "r", encoding="utf-8") as source:
            books = [line.strip() for line in source if line.strip()]
        with open(log_path, "a", encoding="utf-8", newline="") as log:
            for book in books:
                log.write(book + "\n")
        return True
    except OSError as error:
        with open(error_path, "a", encoding="utf-8", newline="") as errors:
            errors.write(f"{Path(day_file).name}: {error.__class__.__name__}: {error.strerror}\n")
        return False

def main():
    base = Path(__file__).resolve().parent
    data = base / "input"
    out = base / "repaired_returns.log"
    errors = base / "error_log.txt"
    out.write_text("", encoding="utf-8")
    errors.write_text("", encoding="utf-8")
    print("FAULTY VERSION: three-day evidence")
    faulty_log = base / "faulty_returns.log"
    for name in ("day1.txt", "day2.txt", "day3.txt"):
        buggy_process(data / name, faulty_log)
    print("After 3 days, log:", repr(faulty_log.read_text(encoding="utf-8")))
    def fail_to_write(_books, _path):
        raise PermissionError("simulated write denial")
    try:
        buggy_process(data / "day1.txt", faulty_log, save=fail_to_write)
    except PermissionError as error:
        print(f"Write failure escapes handler: {error.__class__.__name__}; no error message was saved.")
    print("\nREPAIRED VERSION")
    for name in ("day1.txt", "day2.txt", "day3.txt"):
        print(f"{name}: {'saved' if repaired_process(data / name, out, errors) else 'failed'}")
    missing = data / "day4_missing.txt"
    print(f"{missing.name}: {'saved' if repaired_process(missing, out, errors) else 'failed and logged'}")
    print("Repaired log:", repr(out.read_text(encoding="utf-8")))
    print("Error log:", errors.read_text(encoding="utf-8").strip())
    print("Prevention: use append mode for history; write one newline-terminated record per book; use with; catch and log OSError.")

if __name__ == "__main__":
    main()
