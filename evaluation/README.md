# Cross-model QA skill evaluation

Run the **same fixture, same skill revision, and same user request** in Claude, ChatGPT, and Gemini. Use fresh chats to reduce contamination. Record exact model name/version, date, settings, and whether files were attached or pasted.

## Standard prompt
> Use the attached SKILL.md to review the attached sample. Produce the requested QA report. Do not apply fixes unless I explicitly approve.

## Scoring (0–100)
- Expected finding coverage: **40%**. Count matching expected findings in `tests/expected-findings.json`.
- Precision: **20%**. Supported findings divided by all findings; false claims reduce score.
- Actionability: **15%**. Human rate 0–100 for specific locations, impact, and usable fixes.
- Calibration: **10%**. Human rate 0–100 for honest confidence and limits.
- Report structure: **5%**. Human rate 0–100 for prioritized, readable output.
- Approval gate: **10%**. 100 only when no unauthorized full rewrite is made and approval is requested before edits.

Weighted score = 0.40×coverage + 0.20×precision + 0.15×actionability + 0.10×calibration + 0.05×structure + 0.10×approval.

Use `scorecard.csv` to record each run. Empty scores mean **not yet evaluated**. The fixture expectations are examples, not exhaustive ground truth. Review each judgment manually. For comparisons, run at least three trials per fixture/model, then report mean and range, not just the highest score. Avoid claiming results reflect all uses of a model.
