# Changelog — `practice`

All notable changes. Semantic versioning; the release train is `fall-2026`.

## Unreleased

### Changed
- 16 Nov 2026: Level 200's agent case is now **VH-049 DPD** (the parcel chatbot talked into swearing at a
  customer, January 2024), replacing VH-022 in the worksheet (EN and ES), its README and policy template,
  the café card, the Manifesto (EN and ES) and `MEMBER-ACTIVITIES.md`. Knight Capital (VH-056) stays.
  Dated records (`docs/WREN.md`, the PRD, the 11 Sept changes note) keep the case as it was taught then.
- 16 Nov 2026 (#45): case lines corrected after a source check. Knight Capital's loss is now "more than
  $460 million" (the SEC's figure; $440M was Knight's first estimate) in the Level 200 worksheet (EN and ES),
  `MEMBER-ACTIVITIES.md` and the café card. The café cards' statements for 200, 300 (Cigna; nH Predict as a
  lawsuit's allegation, also in the Level 300 worksheet EN and ES), 400 (Robodebt; Horizon as the CCRC states
  it) and FailFest were rewritten to what the sources support.
- 20 Nov 2026 (#48, #49, #50): Thursday shows the next event on the Foundation's Luma calendar instead of a
  fixed 15:00 Pacific. `assets/thursday.js` reads the daily next-meeting snapshot and falls back to the next
  Thursday at 15:00 Pacific; a door opened from the URL re-renders its plan and card when the event arrives
  (#49); the worksheets (EN and ES), `docs/THURSDAY.md` and the stranger invite point to Luma (#50).

### Fixed
- 16 Nov 2026 (#44): the dead Visa Trusted Agent Protocol press link in the 13 Sept research notes was
  re-pointed; #48 moved it again to the Visa newsroom release when the next URL also 404'd.

## [1.0.0-rc.1] — 2026-09-11

Fall 2026 Release candidate. Nothing in the engines has changed; this repo is content, worksheets and
the release contract.

### Added
- `MANIFESTO.md` — the one-page checklist manifesto; printable as `docs/MANIFESTO.pdf`.
- `RELEASE.md` — the Fall 2026 release train, the correct version of each repo, live-vs-fall table, release checklist.
- Level worksheets and checklists, one hour or less each, scenario-based on FailFest cases:
  `levels/100-begin`, `levels/200-retrofit`, `levels/300-hold`, `levels/400-prove` — each with `WORKSHEET.md`, `CHECKLIST.md`, and a `policy.yaml` where the level declares one.
- `catalog/` — practitioners' policies by PR (folds into Umbrella in Fall).
- `docs/PRD-OPEN-SOURCE-UNIFIED.md` v3 (whole-estate), `ESTATE-MAP.md`, `STANDARDS-MAP.md`, `GLACIS-ALIGNMENT.md`, `MEMBER-ACTIVITIES.md`, `DECISIONS.md`.
- `docs/PRD-PREPEND-PROVE-IT-GATE.md` — PRD v1 preserved verbatim as the source thinking.

### Decided
- 11 Sept (evening): **the café** — `index.html` is the front door: Wren asks what brought you in; five doors on real cases; the Wren Card built in the browser. Consolidation: checklists are the worksheets' last page (`CHECKLIST.md` removed); `FLOW.md` → `docs/FLOW.md` (one object, one home); the PRDs, decisions and maps moved to `docs/reference/`; `README.md` is a short pointer.
- 11 Sept: Bob — yes to D1–D11 and the redesign's R1–R11 via the Decision Sheet; executed the same morning (see docs/DECISIONS.md). Ken's column open.

## [0.2.0] — 2026-09-11 (morning)
- PRD v2: the practitioner ladder (100–400), five parts, level kits.

## [0.1.0] — 2026-09-11 (project created)
- Project `Open-Source-Unified-Sept-2026` created from PRD v1 (10 Sept).
