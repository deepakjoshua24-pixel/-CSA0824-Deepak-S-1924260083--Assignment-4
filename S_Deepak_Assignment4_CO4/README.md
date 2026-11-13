# CSA08 Assignment 4 CO4 - S Deepak

**Register number:** 1924260083  
**Python:** 3.12.14  
**Libraries:** Python standard library; Pillow 13.0.0 is used only to render the evidence images.  
**GitHub repository:** [PASTE WORKING LINK HERE]

This project contains one folder for each assignment task. Each folder has runnable Python source, the sample input files it uses, captured output, and an output image. Task 3 also contains the completed supplied TODO program. Task 5 includes the four requested code organizations. Task 6 is a separate package with module files and generated reports.

The PDF follows the Assignment 3 report layout and includes explanations, the runnable source listings, and the captured execution output. Exact runnable source files are also kept in these task folders:

- [Task 1 source](Task01/main.py)
- [Task 2 source](Task02/main.py)
- [Task 3 runner](Task03/main.py) and [completed supplied program](Task03/complete_code.py)
- [Task 4 source](Task04/main.py)
- [Task 5 runner and four variants](Task05/main.py)
- [Task 6 runner](Task06/main.py) and [registration package](Task06/festreg/)
- [SIMATS logo used on the report cover](assets/simats_logo_banner.png)

| Task | Run command from this folder | Result |
|---|---|---|
| 1 | `python Task01/main.py` | Lists design defects, streams and totals valid mess records, writes repaired and rejected-row reports. |
| 2 | `python Task02/main.py` | Processes daily attendance files, computes percentages, reports below 75%, and logs damaged rows. |
| 3 | `python Task03/main.py` | Runs the completed exception-handling TODO program and demonstrates how a broad exception hides a typo. |
| 4 | `python Task04/main.py` | Reproduces overwritten/malformed logs and shows the append-mode repair and logged missing-file error. |
| 5 | `python Task05/main.py` | Runs identical attendance reporting in a script, a single imported module, three modules, and a package. |
| 6 | `python Task06/main.py` | Validates five expected department files, removes duplicate registrations, and writes master, event, summary, and error reports. |

The report is available as `S_Deepak_Assignment4_CO4.docx` (editable Word file) and `S_Deepak_Assignment4_CO4.pdf` (PDF). Execution evidence in the report is captured from the included programs. Timing or complexity statements are analytical; no machine-dependent benchmark is claimed for this CO4 set.

Install the optional image-rendering library with `python -m pip install -r requirements.txt`. No third-party package is needed to run the assignment programs.

Before repository submission, create the required repository named `CSA08-1924260083-Assignment4`, replace the GitHub placeholder in the README and report cover, commit each task progressively, and share the working link with course faculty.
