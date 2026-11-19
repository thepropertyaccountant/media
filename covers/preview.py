#!/usr/bin/env python3
"""
preview.py — render every designed cover so they can be looked at together.

    python3 covers/preview.py            # all designed unposted drafts
    python3 covers/preview.py 23 44 65   # just these

!! PREVIEW OUTPUT IS NEVER PUBLISHED AND NEVER COMMITTED. !!

A real cover derives its stat row from a BUILT carousel, after the run has
verified every figure against Inland Revenue (see make_covers.py). A draft
has no verified figures — queue/README.md is explicit that a drafted figure
is a pointer to a source and not a number to put on a slide. So this harness
reads the draft's own headline and its drafted row figures purely to get
something of the right shape into the band, and writes everything to the
scratch directory outside the repo.

Its job is to check the ILLUSTRATIONS and the TYPOGRAPHY — a broken
archetype, a silhouette shared by half the set, a headline running to three
lines, a value that ellipsises. Nothing it renders is a publishable image
and no figure it shows has been verified.
"""

import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cover as C                                              # noqa: E402
import make_covers as M                                        # noqa: E402

OUT = pathlib.Path("/tmp/claude-0/-home-claude-media/"
                   "9c6ebcc1-dbdd-53c7-b3da-3a743b582441/scratchpad/covers")
PAIR = re.compile(r"`([^`]{2,40})`\s*/\s*`([^`]{1,24})`")


def draft_bits(slug):
    """(headline, [(value,label)]) from the DRAFT. Preview only — unverified."""
    t = (M.QUEUE / f"{slug}.md").read_text()
    m = re.search(r"^1\.\s+\*\*.*?h-(?:xl|lg|md):\s*`([^`]+)`", t, re.M | re.S)
    headline = m.group(1) if m else None
    if not headline:
        raise SystemExit(f"{slug}: no slide-1 headline in the draft")
    body = t.split("## Slides")[-1].split("## Caption")[0]
    stats = []
    seen = set()
    for lab, val in PAIR.findall(body):
        if not M.has_digit(val) or val.lower() in seen:
            continue
        seen.add(val.lower())
        stats.append((val.strip(), M.short_label(lab)))
    return headline, M.fit_stats(stats)


def build(slugs):
    OUT.mkdir(parents=True, exist_ok=True)
    parts = []
    for i, slug in enumerate(slugs, 1):
        archetype, far, near, warm, accent, element, kov = M.COVERS[slug]
        headline, stats = draft_bits(slug)
        spec = {"slug": slug, "archetype": archetype, "far": far, "near": near,
                "warm": warm, "accent": accent, "element": element,
                "kicker": M.kicker_for(slug, kov), "headline": headline,
                "stats": stats, "was_hook": ""}
        parts.append(C.slide_cover(spec, i, 8).replace(f'id="s{i}"', f'id="p{i}"', 1))
    css = (pathlib.Path(__file__).resolve().parent.parent
           / "template" / "carousel-template.html").read_text()
    css = css.split("<style>")[1].split("</style>")[0]
    doc = ("<!DOCTYPE html><html><head><meta charset=utf-8><style>"
           + css + C.COVER_CSS +
           "\n.slide.cover{position:relative}\n</style></head><body>"
           + "".join(parts) + "</body></html>")
    (OUT / "preview.html").write_text(doc)
    shot = OUT / "shoot_preview.py"
    shot.write_text(
        "from playwright.sync_api import sync_playwright\n"
        "import sys\n"
        "n=int(sys.argv[1]); out=sys.argv[2]\n"
        "with sync_playwright() as p:\n"
        "    b=p.chromium.launch(args=['--font-render-hinting=none'])\n"
        "    pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)\n"
        f"    pg.goto('file://{OUT}/preview.html')\n"
        "    pg.wait_for_timeout(2500)\n"
        "    for i in range(1,n+1):\n"
        "        pg.query_selector(f'#p{i}').screenshot(path=f'{out}/cov-{i:02d}.png')\n"
        "    b.close()\n")
    subprocess.run([sys.executable, str(shot), str(len(slugs)), str(OUT)], check=True)
    return [OUT / f"cov-{i:02d}.png" for i in range(1, len(slugs) + 1)]


def contact_sheet(files, slugs, path, cols=6, tile=252):
    from PIL import Image, ImageDraw
    rows = (len(files) + cols - 1) // cols
    th = int(tile * 1350 / 1080)
    sheet = Image.new("RGB", (cols * tile, rows * (th + 18)), "#202020")
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB").resize((tile, th), Image.LANCZOS)
        x, y = (i % cols) * tile, (i // cols) * (th + 18)
        sheet.paste(im, (x, y))
        d.text((x + 4, y + th + 4), slugs[i][:34], fill="#cfcfcf")
    sheet.save(path)
    return path


if __name__ == "__main__":
    pick = [a for a in sys.argv[1:] if not a.startswith("-")]
    slugs = [s for s in M.unposted_slugs() if s in M.COVERS]
    if pick:
        slugs = [s for s in slugs if s.split("-")[0] in pick]
    files = build(slugs)
    sheets = []
    per = 30
    for k in range(0, len(slugs), per):
        p = OUT / f"sheet-{k // per + 1}.png"
        contact_sheet(files[k:k + per], slugs[k:k + per], p)
        sheets.append(p)
    print(f"{len(slugs)} covers -> {OUT}")
    for s in sheets:
        print("  sheet:", s)
