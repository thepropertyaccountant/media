#!/usr/bin/env python3
"""
Earth by Numbers — slide generator.

Takes a post spec (dict, normally loaded from content/<slug>.json), writes an
HTML file of 1080x1350 slides, renders each to PNG with Playwright, converts to
JPEG for the Instagram API.

Usage:
    python3 build.py content/<slug>.json          # one post
    python3 build.py --all                        # every json in content/

See BUILD.md for the content schema and the design rules.
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
IMG = ROOT / "img"
WORK = ROOT / ".work"

CSS = """
:root{
  --ink:#0C1B2A; --ink2:#061220; --paper:#F3EEE4; --paper2:#E7DFD0;
  --sun:#F5A524; --sea:#2DD4BF; --coral:#E4572E;
  --soft:#5B6C79; --soft-d:#90A4B1;
  --rule:#CFC6B4; --rule-d:#23394A;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#444}
.slide{
  width:1080px;height:1350px;position:relative;overflow:hidden;
  padding:88px 84px;display:flex;flex-direction:column;
  font-family:"Space Grotesk",sans-serif;
  background:var(--paper);color:var(--ink);
}
.slide.ink{background:var(--ink);color:var(--paper)}
.slide.ink2{background:var(--ink2);color:var(--paper)}
.slide.sun{background:var(--sun);color:var(--ink)}

h1,h2{font-family:"Archivo Black",sans-serif;font-weight:400;
      letter-spacing:-.035em;line-height:.98}
.mono{font-family:"Space Mono",monospace;font-variant-numeric:tabular-nums}

.top{display:flex;align-items:center;justify-content:space-between;gap:24px}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0}
.mark{font-family:"Archivo Black",sans-serif;font-size:25px;letter-spacing:-.01em;
      text-transform:uppercase}
.kicker{font-family:"Space Mono",monospace;font-size:25px;letter-spacing:.06em;
        text-transform:uppercase;color:var(--soft)}
.ink .kicker,.ink2 .kicker{color:var(--sea)}
.sun .kicker{color:#7A4F08}
.page{font-family:"Space Mono",monospace;font-size:25px;color:var(--soft)}
.ink .page,.ink2 .page{color:var(--soft-d)}
.sun .page{color:#7A4F08}

.h-xl{font-size:126px}
.h-lg{font-size:100px}
.h-md{font-size:80px}
.h-sm{font-size:62px}
.sub{font-size:42px;line-height:1.3;color:var(--soft);margin-top:36px;max-width:22ch}
.ink .sub,.ink2 .sub{color:var(--soft-d)}
.sun .sub{color:#7A4F08}

.big{font-family:"Archivo Black",sans-serif;font-size:300px;line-height:.82;
     letter-spacing:-.06em;color:var(--sun)}
.ink .big,.ink2 .big{color:var(--sun)}
.big.sea{color:var(--sea)}
.big.s2{font-size:220px}
.big.s3{font-size:170px}
.biglab{font-family:"Space Mono",monospace;font-size:34px;letter-spacing:.06em;
        text-transform:uppercase;color:var(--soft);margin-top:26px}
.ink .biglab,.ink2 .biglab{color:var(--soft-d)}

.rows{margin-top:8px;border-top:5px solid var(--sea)}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:36px;
     padding:30px 0;border-bottom:2px solid var(--rule)}
.ink .row,.ink2 .row{border-bottom-color:var(--rule-d)}
.row .lab{font-size:34px;line-height:1.2;max-width:15ch;color:var(--soft)}
.ink .row .lab,.ink2 .row .lab{color:var(--soft-d)}
.row .fig{font-family:"Space Mono",monospace;font-variant-numeric:tabular-nums;
          font-size:44px;font-weight:700;white-space:nowrap;letter-spacing:-.03em;
          text-align:right}

.rank{display:flex;align-items:flex-start;gap:40px}
.rank .num{font-family:"Archivo Black",sans-serif;font-size:170px;line-height:.8;
           letter-spacing:-.06em;color:var(--sun);flex:0 0 auto}
.rank .rbody{flex:1;min-width:0;padding-top:12px}
.rank .place{font-family:"Archivo Black",sans-serif;font-size:84px;line-height:.98;
             letter-spacing:-.035em}
.rank .where{font-family:"Space Mono",monospace;font-size:32px;letter-spacing:.04em;
             text-transform:uppercase;color:var(--sea);margin-top:22px}

.items{margin-top:40px;display:flex;flex-direction:column;gap:38px}
.item{display:flex;gap:28px;align-items:flex-start}
.item .dot{font-family:"Space Mono",monospace;font-size:34px;color:var(--sun);
           flex:0 0 auto;line-height:1.25}
.item .itext{flex:1;min-width:0}
.item .iname{font-family:"Archivo Black",sans-serif;font-size:50px;line-height:1.02;
             letter-spacing:-.03em}
.item .inote{font-size:32px;line-height:1.3;color:var(--soft);margin-top:12px;max-width:26ch}
.ink .item .inote,.ink2 .item .inote{color:var(--soft-d)}

.swipe{position:absolute;right:84px;bottom:88px;font-family:"Space Mono",monospace;
       font-size:27px;letter-spacing:.08em;color:var(--sea)}

.foot{margin-top:auto}
.src{font-family:"Space Mono",monospace;font-size:22px;line-height:1.4;color:var(--soft);
     max-width:40ch}
.ink .src,.ink2 .src{color:var(--soft-d)}
.sun .src{color:#7A4F08}

.cta-name{font-family:"Archivo Black",sans-serif;font-size:104px;letter-spacing:-.04em;
          line-height:.96}
.cta-line{font-size:40px;line-height:1.35;color:var(--soft-d);margin-top:34px;max-width:24ch}
.handle{font-family:"Space Mono",monospace;font-size:36px;letter-spacing:.02em;color:var(--sea)}
.hr{border-top:5px solid var(--sea);margin-top:64px;padding-top:44px}
"""

BRAND = "Earth by Numbers"
HANDLE = "@earth_by_numbers"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _top(left_html, n, total, cls=""):
    page = f'<span class="page mono">{n}/{total}</span>' if total > 1 else '<span class="page mono"></span>'
    return f'<div class="top">{left_html}{page}</div>'


def _foot(s):
    """Source line, plus the handle when the slide asks for it."""
    bits = []
    if s.get("source"):
        bits.append(f'<p class="src">{esc(s["source"])}</p>')
    if s.get("handle"):
        bits.append(f'<p class="handle mono" style="margin-top:20px">{esc(HANDLE)}</p>')
    if not bits:
        return ""
    return f'<div class="foot">{"".join(bits)}</div>'


def _mark():
    return f'<span class="mark">{esc(BRAND)}</span>'


def _kick(text):
    return f'<span class="kicker mono">{esc(text)}</span>'


def slide_hook(s, n, total):
    size = s.get("size", "h-xl")
    sub = f'<p class="sub">{esc(s["sub"])}</p>' if s.get("sub") else ""
    return f"""<div class="slide ink" id="s{n}">
  {_top(_mark(), n, total)}
  <div class="body">
    <h1 class="{size}">{s["title"]}</h1>
    {sub}
  </div>
  <div class="swipe mono">SWIPE</div>
</div>"""


def slide_ledger(s, n, total):
    rows = "".join(
        f'<div class="row"><span class="lab">{esc(r[0])}</span>'
        f'<span class="fig">{esc(r[1])}</span></div>'
        for r in s["rows"]
    )
    head = f'<h2 class="h-sm" style="margin-bottom:46px">{s["title"]}</h2>' if s.get("title") else ""
    src = _foot(s)
    cls = s.get("bg", "")
    return f"""<div class="slide {cls}" id="s{n}">
  {_top(_kick(s.get("kicker", "")), n, total)}
  <div class="body">
    {head}
    <div class="rows">{rows}</div>
  </div>
  {src}
</div>"""


def slide_bignum(s, n, total):
    size = s.get("numsize", "")
    sea = " sea" if s.get("sea") else ""
    lab = f'<div class="biglab">{esc(s["label"])}</div>' if s.get("label") else ""
    head = f'<h2 class="{s.get("size","h-md")}" style="margin-top:70px">{s["title"]}</h2>' if s.get("title") else ""
    src = _foot(s)
    return f"""<div class="slide {s.get("bg","ink")}" id="s{n}">
  {_top(_kick(s.get("kicker", "")), n, total)}
  <div class="body">
    <div class="big {size}{sea}">{s["number"]}</div>
    {lab}
    {head}
  </div>
  {src}
</div>"""


def slide_rank(s, n, total):
    note = f'<p class="sub" style="margin-top:44px;max-width:24ch">{esc(s["note"])}</p>' if s.get("note") else ""
    where = f'<div class="where">{esc(s["where"])}</div>' if s.get("where") else ""
    return f"""<div class="slide {s.get("bg","")}" id="s{n}">
  {_top(_kick(s.get("kicker", "")), n, total)}
  <div class="body">
    <div class="rank">
      <div class="num">{esc(s["rank"])}</div>
      <div class="rbody">
        <div class="place">{s["place"]}</div>
        {where}
      </div>
    </div>
    {note}
  </div>
  {_foot(s)}
</div>"""


def slide_items(s, n, total):
    items = "".join(
        f'<div class="item"><span class="dot mono">{i+1:02d}</span><div class="itext">'
        f'<div class="iname">{it["name"]}</div>'
        + (f'<div class="inote">{esc(it["note"])}</div>' if it.get("note") else "")
        + "</div></div>"
        for i, it in enumerate(s["items"])
    )
    head = f'<h2 class="{s.get("size","h-sm")}">{s["title"]}</h2>' if s.get("title") else ""
    return f"""<div class="slide {s.get("bg","")}" id="s{n}">
  {_top(_kick(s.get("kicker", "")), n, total)}
  <div class="body">
    {head}
    <div class="items">{items}</div>
  </div>
  {_foot(s)}
</div>"""


def slide_fact(s, n, total):
    sub = f'<p class="sub">{esc(s["sub"])}</p>' if s.get("sub") else ""
    src = _foot(s)
    return f"""<div class="slide {s.get("bg","")}" id="s{n}">
  {_top(_kick(s.get("kicker", "")), n, total)}
  <div class="body">
    <h2 class="{s.get("size","h-md")}">{s["title"]}</h2>
    {sub}
  </div>
  {src}
</div>"""


def slide_signoff(s, n, total):
    line = s.get("line", "Geography, ranked and counted.")
    cta = s.get("cta", "Follow for a new country by the numbers, twice a day.")
    return f"""<div class="slide ink2" id="s{n}">
  {_top('<span class="kicker mono"></span>', n, total)}
  <div class="body" style="flex:0 0 auto;margin-top:30px">
    <div class="cta-name">Earth<br>by Numbers</div>
    <p class="cta-line">{esc(line)}</p>
    <div class="hr">
      <h2 class="h-sm" style="max-width:17ch">{esc(cta)}</h2>
      <p class="handle mono" style="margin-top:40px">{esc(HANDLE)}</p>
    </div>
  </div>
  <p class="src" style="margin-top:auto">{esc(s.get("source", ""))}</p>
</div>"""


def slide_card(s, n, total):
    """Standalone single-image stat card."""
    sub = f'<p class="sub" style="max-width:24ch">{esc(s["sub"])}</p>' if s.get("sub") else ""
    num = ""
    if s.get("number"):
        sea = " sea" if s.get("sea") else ""
        num = f'<div class="big {s.get("numsize","s2")}{sea}">{s["number"]}</div>'
    lab = f'<div class="biglab">{esc(s["label"])}</div>' if s.get("label") else ""
    head = f'<h2 class="{s.get("size","h-md")}" style="margin-top:56px">{s["title"]}</h2>' if s.get("title") else ""
    return f"""<div class="slide {s.get("bg","ink")}" id="s{n}">
  {_top(_mark(), 1, 1)}
  <div class="body">
    {num}{lab}{head}{sub}
  </div>
  <div class="foot">
    <p class="src">{esc(s.get("source",""))}</p>
    <p class="handle mono" style="margin-top:22px">{esc(HANDLE)}</p>
  </div>
</div>"""


BUILDERS = {
    "hook": slide_hook,
    "ledger": slide_ledger,
    "bignum": slide_bignum,
    "rank": slide_rank,
    "items": slide_items,
    "fact": slide_fact,
    "signoff": slide_signoff,
    "card": slide_card,
}


def build_html(spec):
    slides = spec["slides"]
    total = len(slides)
    parts = []
    for i, s in enumerate(slides, start=1):
        fn = BUILDERS[s["type"]]
        parts.append(fn(s, i, total))
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n" + "\n".join(parts) + "\n</body>\n</html>\n"
    )


SHOOT = r"""
from playwright.sync_api import sync_playwright
import sys, pathlib
src = pathlib.Path(sys.argv[1]).resolve()
prefix = sys.argv[2]
n = int(sys.argv[3])
with sync_playwright() as p:
    b = p.chromium.launch(args=["--font-render-hinting=none"])
    pg = b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=1)
    pg.goto(f"file://{src}")
    pg.wait_for_timeout(1200)
    for i in range(1, n+1):
        el = pg.query_selector(f"#s{i}")
        el.screenshot(path=f"{prefix}-{i:02d}.png")
    b.close()
print("rendered", n)
"""


def render(spec, slug):
    from PIL import Image

    WORK.mkdir(exist_ok=True)
    IMG.mkdir(exist_ok=True)
    html = build_html(spec)
    hp = WORK / f"{slug}.html"
    hp.write_text(html)
    sp = WORK / "_shoot.py"
    sp.write_text(SHOOT)
    n = len(spec["slides"])
    subprocess.run(
        [sys.executable, "-I", str(sp), str(hp), str(WORK / slug), str(n)],
        check=True, capture_output=True,
    )
    out = []
    for i in range(1, n + 1):
        png = WORK / f"{slug}-{i:02d}.png"
        jpg = IMG / f"{slug}-{i:02d}.jpg"
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=90, optimize=True)
        out.append(jpg.name)
    return out


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == "--all":
        files = sorted((ROOT / "content").glob("*.json"))
    else:
        files = [pathlib.Path(a) for a in args]
    for f in files:
        spec = json.loads(f.read_text())
        slug = spec["slug"]
        names = render(spec, slug)
        print(f"{slug}: {len(names)} images -> {names[0]} .. {names[-1]}")


if __name__ == "__main__":
    main()
