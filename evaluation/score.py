#!/usr/bin/env python3
"""Compute scores from manually assessed evaluation/scorecard.csv (standard library only)."""
import csv
from pathlib import Path

p = Path(__file__).with_name("scorecard.csv")
weights = {"coverage_score": .40, "precision_score": .20,
           "actionability_0_100": .15, "calibration_0_100": .10,
           "structure_0_100": .05, "approval_0_or_100": .10}
rows = list(csv.DictReader(p.open(newline="")))
for row in rows:
    if not row["expected_caught"] or not row["all_findings"] or not row["supported_findings"]:
        continue
    try:
        expected = int(row["expected_total"])
        caught = int(row["expected_caught"])
        total = int(row["all_findings"])
        supported = int(row["supported_findings"])
        if not (0 <= caught <= expected and 0 <= supported <= total and expected > 0 and total > 0):
            raise ValueError("Invalid finding counts")
        row["coverage_score"] = f"{100*caught/expected:.1f}"
        row["precision_score"] = f"{100*supported/total:.1f}"
        for key in weights:
            if row[key] == "":
                raise ValueError(f"Missing {key}")
            if not 0 <= float(row[key]) <= 100:
                raise ValueError(f"Invalid {key}")
        score = sum(float(row[key])*weight for key, weight in weights.items())
        row["weighted_total"] = f"{score:.1f}"
        print(f'{row["provider"]} | {row["fixture"]} | {score:.1f}/100')
    except ValueError as e:
        print(f'SKIPPED {row["provider"]} {row["fixture"]}: {e}')
with p.open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
