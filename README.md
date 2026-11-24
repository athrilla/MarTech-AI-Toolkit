# MarTech AI Toolkit

Open-source AI skills, reusable QA tools, and practical examples for marketing automation professionals and MarTech developers.

## Start here

| Skill | What it checks | Instructions |
| --- | --- | --- |
| HTML Email Technical QA | HTML email compatibility, accessibility, links, personalization and code quality | [Open SKILL.md](skills/html-email-technical-qa/SKILL.md) |
| Email Creative QA | Subject, preheader, message hierarchy, CTA and audience fit | [Open SKILL.md](skills/email-creative-qa/SKILL.md) |

**Workflow:** Load a skill in your AI assistant, provide an email sample, and request a QA report. The skill reports issues and recommendations first; it asks before applying edits. See [sample fixtures](tests/README.md) and the [evaluation guide](evaluation/README.md).

### Using with Claude, ChatGPT, or Gemini

These are portable Markdown instructions using a `SKILL.md` structure. Platform support and installation steps vary; when native skill installation is unavailable, supply the file as context with your input. No platform-specific installation or automatic integration is guaranteed by this repository.

### Evaluate the skills

Four synthetic fixtures in `tests/` contain known issues or clearer comparison examples. Compare findings with `tests/expected-findings.json`. Score trials using `evaluation/scorecard.csv` and run `python evaluation/score.py` after entering human assessments. Blank entries are **not** evaluation results. See the [rubric](evaluation/rubric.json).

### Roadmap

- Add secure Salesforce Marketing Cloud CloudPage examples, SSJS, AMPscript and SQL patterns
- Add platform-specific setup guides and more test fixtures
- Improve reproducibility and eventually automate evaluation

### Safety and limitations

These are review aids, not guaranteed email-client rendering tests, live link checks, accessibility certification, deliverability validation, or legal advice. Review output before using in production. All samples are synthetic; do not publish private customer or employer information.

### License

MIT. See [LICENSE](LICENSE).
