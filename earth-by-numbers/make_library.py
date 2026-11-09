#!/usr/bin/env python3
"""Build the content-library page: every post, every slide, every caption."""
import base64
import io
import json
import pathlib
import html as H
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
Q = json.loads((ROOT / "queue.json").read_text())
OUT = ROOT / ".work" / "library.html"

KIND_LABEL = {"crazy": "Country crazy stats", "top5": "Top 5",
              "spotlight": "Country spotlight"}

IMG = ROOT / "img"
_cache = {}


def thumb(url):
    """Inline a small thumbnail as a data URI.

    The artifact viewer's content security policy blocks images from other
    hosts, so remote URLs render blank. Thumbnails are embedded; the full-size
    image stays on GitHub behind the link, which opens outside the viewer.
    """
    name = url.rsplit("/", 1)[-1]
    if name in _cache:
        return _cache[name]
    f = IMG / name
    if not f.exists():
        _cache[name] = url
        return url
    im = Image.open(f).convert("RGB")
    im.thumbnail((190, 238), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=72, optimize=True)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    _cache[name] = uri
    return uri

posted = [e for e in Q["queue"] if e["posted_at"]]
pending = [e for e in Q["queue"] if not e["posted_at"]]

cards = []
for i, e in enumerate(Q["queue"], start=1):
    slides = "".join(
        f'<a class="sl" href="{u}" target="_blank" rel="noopener">'
        f'<img loading="lazy" src="{thumb(u)}" alt="slide {j}"><span>{j}</span></a>'
        for j, u in enumerate(e["images"], start=1))
    if e["posted_at"]:
        state = f'<span class="pill done">Posted {e["posted_at"][:10]}</span>'
    elif e["approved"]:
        state = '<span class="pill ready">Queued</span>'
    else:
        state = '<span class="pill wait">Awaiting approval</span>'
    cap = H.escape(e["caption"])
    cards.append(f"""
<article class="card" id="{e['slug']}">
  <header>
    <div class="hl">
      <span class="num">{i:02d}</span>
      <h2>{H.escape(e['slug'])}</h2>
    </div>
    <div class="meta">
      <span class="kind">{KIND_LABEL.get(e['kind'], e['kind'])}</span>
      <span class="kind">{len(e['images'])} slides</span>
      {state}
    </div>
  </header>
  <div class="slides">{slides}</div>
  <div class="caphead">
    <h3>Caption</h3>
    <button class="copy" data-for="c{i}">Copy caption</button>
  </div>
  <pre class="cap" id="c{i}">{cap}</pre>
</article>""")

html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Earth by Numbers — content library</title>
<style>
:root{{--ink:#0C1B2A;--ink2:#061220;--paper:#F3EEE4;--sun:#F5A524;--sea:#2DD4BF;
      --soft:#5B6C79;--soft-d:#90A4B1;--rule:#1E3346;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--ink2);color:var(--paper);
     font:16px/1.55 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
     padding:40px 20px 80px}}
.wrap{{max-width:1080px;margin:0 auto}}
h1{{font-size:clamp(34px,6vw,60px);letter-spacing:-.035em;line-height:1}}
.lede{{color:var(--soft-d);margin-top:14px;max-width:62ch}}
.stats{{display:flex;flex-wrap:wrap;gap:12px;margin:28px 0 8px}}
.stat{{background:var(--ink);border:1px solid var(--rule);border-radius:10px;
      padding:14px 18px;min-width:132px}}
.stat b{{display:block;font-size:30px;letter-spacing:-.03em;color:var(--sun)}}
.stat span{{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--soft-d)}}
.note{{background:var(--ink);border:1px solid var(--rule);border-left:4px solid var(--sea);
      border-radius:8px;padding:16px 20px;margin:26px 0 40px;color:var(--soft-d);font-size:14.5px}}
.note b{{color:var(--paper)}}
.card{{background:var(--ink);border:1px solid var(--rule);border-radius:14px;
      padding:24px;margin-bottom:26px}}
.card header{{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;
             align-items:center;margin-bottom:18px}}
.hl{{display:flex;align-items:baseline;gap:12px}}
.num{{font-variant-numeric:tabular-nums;color:var(--sun);font-weight:700}}
.card h2{{font-size:21px;letter-spacing:-.02em;font-family:ui-monospace,monospace;font-weight:600}}
.meta{{display:flex;gap:8px;flex-wrap:wrap}}
.kind,.pill{{font-size:11.5px;letter-spacing:.07em;text-transform:uppercase;
            padding:5px 11px;border-radius:999px;border:1px solid var(--rule);color:var(--soft-d)}}
.pill.done{{border-color:#2c6e52;color:#6fdca8}}
.pill.ready{{border-color:#8a5c12;color:var(--sun)}}
.pill.wait{{border-color:#7a3326;color:#ff9b82}}
.slides{{display:grid;grid-template-columns:repeat(auto-fill,minmax(132px,1fr));gap:10px}}
.sl{{position:relative;display:block;border-radius:8px;overflow:hidden;background:#09151f;
    border:1px solid var(--rule)}}
.sl img{{width:100%;display:block;aspect-ratio:4/5;object-fit:cover}}
.sl span{{position:absolute;left:7px;top:7px;background:rgba(6,18,32,.86);color:var(--sea);
         font-size:11px;padding:2px 7px;border-radius:5px;font-variant-numeric:tabular-nums}}
.caphead{{display:flex;justify-content:space-between;align-items:center;margin:22px 0 10px}}
.caphead h3{{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--soft-d)}}
.copy{{background:transparent;border:1px solid var(--sea);color:var(--sea);border-radius:7px;
      padding:7px 14px;font-size:12.5px;cursor:pointer;font-family:inherit}}
.copy:hover{{background:var(--sea);color:var(--ink2)}}
.copy.ok{{background:var(--sea);color:var(--ink2);border-color:var(--sea)}}
.cap{{white-space:pre-wrap;font:13.5px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;
     background:#09151f;border:1px solid var(--rule);border-radius:9px;padding:16px;
     color:#d9e2e8;overflow-x:auto}}
footer{{margin-top:50px;color:var(--soft);font-size:13px;border-top:1px solid var(--rule);
       padding-top:22px}}
a{{color:var(--sea)}}
</style></head><body><div class="wrap">
<h1>Earth by Numbers</h1>
<p class="lede">Every post in the pipeline: all slides, the full caption and hashtags.
Click any slide to open it full size and save it. Use this to post by hand if the
automation ever stops.</p>

<div class="stats">
  <div class="stat"><b>{len(Q['queue'])}</b><span>Posts built</span></div>
  <div class="stat"><b>{sum(len(e['images']) for e in Q['queue'])}</b><span>Slides</span></div>
  <div class="stat"><b>{len(posted)}</b><span>Posted</span></div>
  <div class="stat"><b>{len(pending)}</b><span>Queued</span></div>
  <div class="stat"><b>{len(pending)/2:.1f}</b><span>Days of buffer</span></div>
</div>

<div class="note">
  <b>Posting automatically</b> at 11:31 and 23:31 UTC, to @{Q['handle']}.
  Order runs top to bottom. Images are served from the
  <a href="https://github.com/thepropertyaccountant/media/tree/main/earth-by-numbers"
     target="_blank" rel="noopener">media repo</a>, so these links keep working
  whether or not anything else is running.
</div>

{''.join(cards)}

<footer>Generated from queue.json. Figures verified against Wikipedia, Statistics Canada,
the Geospatial Information Authority of Japan and the mledoze/countries dataset.
Top 5 lists are opinion and labelled as such.</footer>
</div>
<script>
document.querySelectorAll('.copy').forEach(function(b){{
  b.addEventListener('click', function(){{
    var el = document.getElementById(b.dataset.for);
    var t = el ? el.textContent : '';
    var done = function(){{ var o=b.textContent; b.textContent='Copied'; b.classList.add('ok');
      setTimeout(function(){{ b.textContent=o; b.classList.remove('ok'); }}, 1400); }};
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(t).then(done, function(){{ b.textContent='Select manually'; }});
    }} else {{
      var ta=document.createElement('textarea'); ta.value=t; document.body.appendChild(ta);
      ta.select(); try {{ document.execCommand('copy'); done(); }} catch(e) {{}}
      document.body.removeChild(ta);
    }}
  }});
}});
</script>
</body></html>
"""

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(html)
print("wrote", OUT, f"({len(html)//1024} KB), {len(Q['queue'])} posts")
