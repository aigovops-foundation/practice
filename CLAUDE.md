# AiGovOps Practice: notes for Claude

The Fall 2026 practice release: worksheets at four levels, the manifesto, the catalogue and the
site at practice.aigovops-foundation.com. The GitHub repo is `aigovops-foundation/practice`; the
local folder may be named `Open-Source-Unified-Sept-2026`. Public repo, Apache-2.0.

## Layout

- `levels/`: the worksheets (100 Begin, 200 Retrofit, 300 Hold, 400 Prove).
- `MANIFESTO.md`, `docs/`: the manifesto, Thursday, Wren, the flow, and Spanish translations
  under `docs/es/`.
- `catalog/`, `scripts/`, `_layouts/`, `_config.yml`: the catalogue, the tests and the Jekyll site.
- GitHub Pages serves `main` from the repo root at the custom domain in `CNAME`. A merge to
  `main` is a publish. Do not edit or remove `CNAME`.

## Checks to run before a pull request

```bash
python3 scripts/test_door_landing.py
python3 scripts/test_thursday_fallback.py
```

CI also runs a link check on every push and pull request.

## Things that are easy to get wrong

- `docs/FLOW.md` says which file owns which object. Change a thing in the file that owns it, not
  in a copy.
- A worksheet follows the shape in `docs/reference/MEMBER-ACTIVITIES.md`: one real case from the corpus
  (cite its `VH-` number), all four gates, one signed artifact, one return.
- A policy change is a governed event and needs a 400-level reviewer. Spec questions go to the
  OVERT steward first: see `docs/reference/GLACIS-ALIGNMENT.md`.
- Where a document has a Spanish version, a change to the English needs the Spanish updated or
  the gap stated in the pull request.
- `CONTRIBUTING.md` asks for a DCO sign-off (`git commit -s`). That sign-off is a human's
  certification. An agent does not add it for them.
- Versions and the release checklist live in `RELEASE.md` and `VERSION`.

## Rules for an agent

- Agents propose, humans approve. Open a pull request; do not merge it, and do not push to `main`.
- Never sign, approve or rule on anything in a human's name.
- Secrets live in 1Password. Never print, paste or commit a key, token or private key.
- A check that was not run is reported as not run. Do not write "passes" from memory.
- Read `CONTRIBUTING.md` where there is one. It wins over this file where they differ.
