def broad_handler_hides_typo():
    present = 0
    try:
        presnt += 1  # deliberate misspelling for the required misuse experiment
    except Exception:
        pass
    return present

print("With except Exception: pass, deliberate NameError is swallowed.")
print("Program continues and returns a misleading count:", broad_handler_hides_typo())
print("The record is omitted with no error log, so the defect is hidden from the user.")
