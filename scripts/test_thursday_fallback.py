"""docs/THURSDAY.md's no-JavaScript join fallback must point somewhere that exists.

Café Walk run 5: the fallback href was community.aigovops-foundation.com/events.html, a page the
community platform does not serve (its Thursday card lives on the front page, portal.html). With
JavaScript on, assets/thursday.js rewrites the href to joinUrl, so only a no-JS reader (or an empty
joinUrl) ever met the dead link.

It also runs assets/thursday.js in Node at fixed clocks to check window.THURSDAY.skip: a listed date
is stepped past (also consecutive ones), an empty list changes nothing, and a Luma event on a skipped
day is ignored. Issue #47: 26 Nov 2026 (US Thanksgiving) was advertised with a live Join link.

Run:  python3 scripts/test_thursday_fallback.py
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = (ROOT / "docs" / "THURSDAY.md").read_text()
JS = (ROOT / "assets" / "thursday.js").read_text()
fails = 0


def check(c, label):
    global fails
    fails += 0 if c else 1
    print(f"  {'ok  ' if c else 'FAIL'} {label}")


m = re.search(r'data-thursday="join"\s+href="([^"]+)"', MD)
check(bool(m), "THURSDAY.md has a data-thursday=join link with a fallback href")
href = m.group(1) if m else ""
check("events.html" not in href, f"fallback is not the non-existent events.html ({href})")
check(href.startswith("https://community.aigovops-foundation.com/"), "fallback points at the community platform")

# Runs thursday.js with a frozen clock and an optional stubbed Luma answer; prints next.iso.
HARNESS = r"""
const vm = require("vm");
const [src, nowIso, luma] = JSON.parse(require("fs").readFileSync(0, "utf8"));
const Real = Date, now = new Real(nowIso).getTime();
class FakeDate extends Real {
  constructor(...a) { if (a.length) super(...a); else super(now); }
  static now() { return now; }
}
const window = {};
if (luma) window.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve(luma) });
const ctx = { window, Date: FakeDate, Intl, Event: class { constructor(t) { this.type = t; } },
  fetch: window.fetch,
  document: { readyState: "complete", querySelectorAll: () => [], addEventListener() {}, dispatchEvent() {} } };
vm.runInNewContext(src, ctx);
setTimeout(() => console.log(window.THURSDAY.next.iso), 20);
"""
NODE = shutil.which("node")
check(bool(NODE), "node is on PATH (needed to run assets/thursday.js)")
SKIP_RE = re.compile(r"skip:\s*\[[^\]]*\]")
check(bool(SKIP_RE.search(JS)), "window.THURSDAY has a skip: [...] list")


def next_iso(now, skip=None, luma=None, src=None):
    src = src or (JS if skip is None else SKIP_RE.sub("skip: " + json.dumps(skip), JS))
    if not NODE:
        return None
    r = subprocess.run([NODE, "-e", HARNESS], input=json.dumps([src, now, luma]),
                       capture_output=True, text=True, timeout=20)
    return r.stdout.strip() or r.stderr.strip()


m = SKIP_RE.search(JS)
shipped = json.loads(m.group(0).split(":", 1)[1]) if m else []
check("2026-11-26" in shipped, f"shipped skip list holds 2026-11-26 ({shipped})")

FRI = "2026-11-20T12:00:00-08:00"  # Friday before Thanksgiving week
cases = [
    ("empty list: next Thursday unchanged", next_iso(FRI, []), "2026-11-26"),
    ("empty list equals no skip key", next_iso(FRI, []), next_iso(FRI, src=SKIP_RE.sub("_noskip: []", JS))),
    ("skip one date steps to the following Thursday", next_iso(FRI, ["2026-11-26"]), "2026-12-03"),
    ("skip consecutive dates steps past both", next_iso(FRI, ["2026-11-26", "2026-12-03"]), "2026-12-10"),
    ("skip consecutive dates across the year end", next_iso("2026-12-20T12:00:00-08:00", ["2026-12-24", "2026-12-31"]), "2027-01-07"),
    ("a skipped non-Thursday changes nothing", next_iso(FRI, ["2026-11-25"]), "2026-11-26"),
    ("on the skipped Thursday itself, before the call", next_iso("2026-11-26T10:00:00-08:00", ["2026-11-26"]), "2026-12-03"),
    ("shipped file, Wednesday 25 Nov 2026", next_iso("2026-11-25T09:00:00-08:00"), "2026-12-03"),
    ("shipped file, Thursday 26 Nov 2026 14:00 Pacific", next_iso("2026-11-26T14:00:00-08:00"), "2026-12-03"),
    ("Luma event on a skipped day is ignored", next_iso(FRI, ["2026-11-26"], {"start": "2026-11-26T23:00:00Z"}), "2026-12-03"),
    ("Luma event on a call day still wins", next_iso(FRI, ["2026-11-26"], {"start": "2026-12-03T23:00:00Z"}), "2026-12-03"),
    ("Luma event with no skip still wins", next_iso(FRI, [], {"start": "2026-11-26T23:00:00Z"}), "2026-11-26"),
]
for label, got, want in cases:
    check(got == want, f"{label}: {got} (want {want})")

print(f"\nTHURSDAY FALLBACK: {'FAIL' if fails else 'ok'}")
sys.exit(1 if fails else 0)
