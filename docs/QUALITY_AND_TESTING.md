# Development, Resume-Quality, and Privacy Guide

This project supports resume-oriented workflows. Confirm current editing, templates, import, and export capabilities in source before describing them as implemented.

## Setup

```bash
git clone https://github.com/kandisaikishore/resume-building.git
cd resume-building
```

Use the runtime, package manager, and scripts defined by the current manifests. Keep credentials and real resume files out of version control and test fixtures.

## Resume validation

For implemented resume forms, test:
- Required sections and missing/empty fields
- Invalid dates, reversed employment/education ranges, and inconsistent date formats
- Long names, long bullets, Unicode characters, and special characters
- Duplicate entries and repeated submissions
- Save/reload and draft recovery behavior
- Import of malformed or unsupported files, if import exists

## Document export

If PDF or other document export is implemented, verify page breaks, margins, font rendering, long sections, hyperlinks, and multi-page resumes. A successful export must not silently omit user content. Test oversized or malformed uploads with safe synthetic fixtures and enforce size/type limits where applicable.

## Privacy

Resume data can contain contact details and employment history. Do not log full resume text by default. Explain where data is stored and what deletion removes based on the actual implementation. Avoid sending personal resume content to external AI services without clear disclosure and user consent.

## Pull-request checklist

- [ ] Add regression tests for validation or export changes.
- [ ] Run declared test/build commands.
- [ ] Verify long-content and Unicode behavior where applicable.
- [ ] State any export or integration checks that could not be run.
- [ ] Keep planned features distinct from implemented features.
