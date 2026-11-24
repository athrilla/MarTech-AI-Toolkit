# QA skill test fixtures

These are **synthetic examples**, not real customer campaigns. Run each file through the matching skill and compare the response to `expected-findings.json`.

## Manual evaluation
1. Load the matching `SKILL.md` into your AI tool.
2. Supply the fixture and ask for a QA report.
3. Check whether expected findings are covered, false positives are limited, and confidence is calibrated.
4. Verify the assistant **does not modify the original before explicit approval**.
5. Record model, date, skill revision, findings caught, false positives, and whether the approval gate was respected.

The cleaner examples are comparison fixtures, **not certified production-ready templates**. Email rendering, live links, and deliverability require separate testing.
