import json
import os
import sys

from translations.cases_01_07 import DATA as D1
from translations.cases_08_14 import DATA as D2
from translations.cases_15_21 import DATA as D3
from translations.cases_22_28 import DATA as D4
from translations.cases_29_33 import DATA as D5

ALL_DATA = {}
for d in [D1, D2, D3, D4, D5]:
    ALL_DATA.update(d)

print(f"Loaded translations for {len(ALL_DATA)} cases.")

errors = []
total_options_processed = 0

for i in range(1, 34):
    num_str = f"{i:02d}"
    cid = f"case-{num_str}"
    en_file = f"src/data/cases/case-{num_str}.json"
    vi_file = f"src/data/cases/vi/case-{num_str}.json"

    if cid not in ALL_DATA:
        errors.append(f"Missing translation for {cid}")
        continue

    tr_case = ALL_DATA[cid]

    with open(en_file, "r", encoding="utf-8") as f:
        en = json.load(f)
    with open(vi_file, "r", encoding="utf-8") as f:
        vi = json.load(f)

    for sec in ["rootCause", "fix"]:
        if sec not in tr_case:
            errors.append(f"{cid}: Missing section {sec}")
            continue

        # Update question
        vi["diagnosis"][sec]["question"] = tr_case[sec]["question"]

        en_options = {o["id"]: o for o in en["diagnosis"][sec]["options"]}
        tr_options = tr_case[sec]["options"]

        for vo in vi["diagnosis"][sec]["options"]:
            oid = vo["id"]
            if oid not in en_options:
                errors.append(f"{cid} {sec}: unknown option {oid} in EN")
                continue
            if oid not in tr_options:
                errors.append(f"{cid} {sec}: missing translation for option {oid}")
                continue

            eo = en_options[oid]
            tro = tr_options[oid]

            vo["text"] = tro["text"]
            vo["feedback"] = tro["feedback"]
            vo["correct"] = eo["correct"]

            # Consistency checks
            if eo["correct"]:
                if not tro["feedback"].startswith("Chính xác! "):
                    errors.append(f"{cid} {sec} {oid} is TRUE, but feedback does not start with 'Chính xác! ': {tro['feedback'][:30]}")
            else:
                if tro["feedback"].startswith("Chính xác! "):
                    errors.append(f"{cid} {sec} {oid} is FALSE, but feedback starts with 'Chính xác! ': {tro['feedback'][:30]}")

            total_options_processed += 1

    with open(vi_file, "w", encoding="utf-8") as f:
        json.dump(vi, f, ensure_ascii=False, indent=2)

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print(f"SUCCESS: Processed {total_options_processed} options across all 33 cases with 100% correct answer alignment!")
