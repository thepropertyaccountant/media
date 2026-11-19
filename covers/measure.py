#!/usr/bin/env python3
"""
measure.py — assert in the browser what looking cannot tell you.

    python3 covers/measure.py <page.html>       # any page of .slide.cover divs

For every cover on the page it asserts:
  * the type band does not overflow its 450px — content clipped at the
    bottom edge is invisible in a thumbnail and obvious in the feed;
  * no stat value is ellipsised (scrollWidth > clientWidth on the .v);
  * the headline is at most TWO lines, measured as rendered height over
    line-height, not guessed from character counts;
  * the kicker row does not collide with the headline;
  * every slide is exactly 1080x1350.

A contact sheet catches a broken illustration. It does not catch any of
these, which is why both steps exist.
"""

import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

JS = """
() => Array.from(document.querySelectorAll('.slide.cover')).map(s => {
  const band = s.querySelector('.band');
  const disp = s.querySelector('.disp');
  const kick = s.querySelector('.kick');
  const stats = Array.from(s.querySelectorAll('.stat .v'));
  const lh = parseFloat(getComputedStyle(disp).lineHeight)
          || parseFloat(getComputedStyle(disp).fontSize) * 0.92;
  const br = band.getBoundingClientRect();
  const dr = disp.getBoundingClientRect();
  const kr = kick.getBoundingClientRect();
  let inner = 0;
  for (const c of band.children) {
    const r = c.getBoundingClientRect();
    inner = Math.max(inner, r.bottom - br.top);
  }
  return {
    id: s.id,
    w: s.getBoundingClientRect().width,
    h: s.getBoundingClientRect().height,
    bandH: br.height,
    contentBottom: Math.round(inner),
    lines: Math.round(dr.height / lh),
    fontSize: Math.round(parseFloat(getComputedStyle(disp).fontSize)),
    kickCollide: kr.bottom > dr.top + 1,
    clipped: stats.filter(v => v.scrollWidth > v.clientWidth + 1)
                  .map(v => v.textContent.trim()),
    nstats: stats.length
  };
})
"""


def measure(page_url):
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1350},
                        device_scale_factor=1)
        pg.goto(page_url)
        pg.wait_for_timeout(2500)
        rows = pg.evaluate(JS)
        b.close()
    return rows


def check(rows, labels=None):
    bad = []
    for i, r in enumerate(rows):
        name = (labels or {}).get(i, r["id"])
        if round(r["w"]) != 1080 or round(r["h"]) != 1350:
            bad.append((name, f"slide is {r['w']}x{r['h']}, not 1080x1350"))
        if r["contentBottom"] > r["bandH"] - 2:
            bad.append((name, f"band overflows: content reaches "
                              f"{r['contentBottom']} of {round(r['bandH'])}px"))
        if r["lines"] > 2:
            bad.append((name, f"headline is {r['lines']} lines at "
                              f"{r['fontSize']}px — the rule is two"))
        if r["kickCollide"]:
            bad.append((name, "kicker row collides with the headline"))
        for v in r["clipped"]:
            bad.append((name, f"stat value ellipsised: {v!r}"))
    return bad


if __name__ == "__main__":
    src = pathlib.Path(sys.argv[1]).resolve()
    labels = None
    lf = src.parent / "labels.json"
    if lf.exists():
        labels = {i: s for i, s in enumerate(json.loads(lf.read_text()))}
    rows = measure(f"file://{src}")
    bad = check(rows, labels)
    print(f"measured {len(rows)} covers")
    if not bad:
        print("PASS — no overflow, no ellipsis, no headline over two lines")
    else:
        print(f"FAIL — {len(bad)} problems")
        for name, msg in bad:
            print(f"  {name}: {msg}")
    sys.exit(1 if bad else 0)
