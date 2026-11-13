#!/usr/bin/env python3
"""Write dashboard/queue.json: one row per post, posted and prepared.

Read by the "The Property Accountant Instagram Content" dashboard. Run from the
repo root after every post, and whenever queue/README.md changes:

    python3 dashboard/snapshot.py

It reads queue/README.md (run order, bank, held) and POSTED.md, then works out
the date each prepared post is expected to go out by walking the posting slots
forward under the rules in queue/README.md ("Which post a run takes").
"""
import json, re, sys, datetime as dt, pathlib
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent.parent
NZ = ZoneInfo("Pacific/Auckland")
DAILY_UNTIL = dt.date(2026, 12, 13)                  # daily cadence ends (inclusive)
SLOT_DAYS = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}  # after that: cron */3
MONTHS = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}

def category(aud):
    return "Rental" if "Property" in aud else "Contractor"

def table_rows(text, heading):
    """Rows of the first markdown table after a heading."""
    part = text.split(heading, 1)[1]
    rows, started = [], False
    for line in part.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                started = True
                continue
            if started:
                rows.append(cells)
        elif started:
            break
    return rows

def parse_window(w):
    """'open' -> None. Otherwise a list of ((m, d), (m, d)) inclusive ranges, recurring yearly."""
    w = w.replace("–", "-").replace("—", "-")
    if w.strip().lower() == "open":
        return None
    out = []
    for a_d, a_m, b_d, b_m in re.findall(r"(\d{1,2})\s*([A-Za-z]{3})?\s*-\s*(\d{1,2})\s*([A-Za-z]{3})", w):
        b = (MONTHS[b_m[:3].title()], int(b_d))
        a = (MONTHS[a_m[:3].title()] if a_m else b[0], int(a_d))
        out.append((a, b))
    if "last week of apr" in w.lower():
        out.append(((4, 24), (4, 30)))
    return out

def in_window(win, d):
    if win is None:
        return True
    md = (d.month, d.day)
    return any(a <= md <= b for a, b in win)

def is_slot(d):
    return d <= DAILY_UNTIL or d.day in SLOT_DAYS

def main():
    readme = (ROOT / "queue" / "README.md").read_text()
    posted_md = (ROOT / "POSTED.md").read_text()
    posts = {}

    for f, slot, topic, aud, status in table_rows(readme, "## Run order"):
        posts[f] = dict(file=f, topic=topic, category=category(aud), status=status, window="", hold="")
    for f, window, topic, aud, status in table_rows(readme, "## The bank"):
        posts[f] = dict(file=f, topic=topic, category=category(aud), status=status,
                        window="" if window.lower() == "open" else window, hold="", _win=parse_window(window))
    for f, until, topic, why in table_rows(readme, "### Held back"):
        m = re.fullmatch(r"\d{4}-\d{2}-\d{2}", until)
        # audience of a held post comes from its draft header
        draft = next((ROOT / "queue").glob(f"{f}-*.md")).read_text()
        aud = "Property" if re.search(r"\*\*Audience:\*\*[^\n]*(rental|homeowner|property owner)", draft, re.I) else "Agent"
        posts[f] = dict(file=f, topic=topic, category=category(aud), status="held", window="",
                        hold=("Held until " + until) if m else ("Held: " + until),
                        _until=dt.date.fromisoformat(until) if m else None,
                        _posted=until.lower().startswith("posted"))

    # what has gone out, from the log
    log = []
    for date, topic, source in table_rows(posted_md, "# Posted carousels"):
        m = re.match(r"queue/(\d\d)-", source)
        f = m.group(1) if m else ""
        cat = posts[f]["category"] if f in posts else (
            "Rental" if re.search(r"bright-line|rental", source) else "Contractor")
        log.append(dict(date=date, topic=topic, file=f, category=cat))
        if f in posts:
            posts[f]["status"] = "posted"
            posts[f]["posted_on"] = date

    rows = []
    for i, p in enumerate(log, 1):
        title = posts[p["file"]]["topic"] if p["file"] in posts else p["topic"]
        rows.append(dict(key=p["file"] or f"p{i}", file=p["file"], title=title, category=p["category"],
                         status="posted", stage="Posted", posted_on=p["date"], expected_on="",
                         order=None, in_run=False, window="", note=""))
    logged = {p["file"] for p in log}
    for p in posts.values():                       # marked posted in the queue but missing from the log
        if p["status"] == "posted" and p["file"] not in logged:
            rows.append(dict(key=p["file"], file=p["file"], title=p["topic"], category=p["category"],
                             status="posted", stage="Posted", posted_on="", expected_on="",
                             order=None, in_run=False, window="", note="Marked posted in the queue, not in POSTED.md"))

    # walk the slots forward
    today = dt.datetime.now(NZ).date()
    last_dates = [dt.date.fromisoformat(p["date"]) for p in log]
    start = today + dt.timedelta(days=1) if today in last_dates else today
    recent = [p["category"] for p in log]
    todo = [p for p in posts.values() if p["status"] in ("queued", "bank")
            or (p["status"] == "held" and p.get("_until"))]
    order_rank = {id(p): i for i, p in enumerate(posts.values())}
    stage = {"queued": "Queued", "bank": "Bank", "held": "Dated hold"}
    blocked = [p for p in posts.values() if p["status"] == "held" and not p.get("_until") and not p.get("_posted")]

    def eligible(d):
        held = [p for p in todo if p["status"] == "held" and p["_until"] <= d]
        queued = [p for p in todo if p["status"] == "queued"]
        bank = [p for p in todo if p["status"] == "bank" and in_window(p.get("_win"), d)]
        return held + queued + bank

    d, n, first_gap, planned = start, 0, None, []
    horizon = start + dt.timedelta(days=500)
    while todo and d <= horizon:
        if is_slot(d):
            el = eligible(d)
            pick = el[0] if el else None
            if pick:
                if pick["category"] == "Contractor" and recent[-2:] == ["Contractor"] * 2:
                    pick = next((p for p in el if p["category"] == "Rental"), pick)
                elif pick["category"] == "Rental" and recent[-4:] == ["Rental"] * 4:
                    pick = next((p for p in el if p["category"] == "Contractor"), pick)
                n += 1
                planned.append((pick, d, n, first_gap is None))
                todo.remove(pick)
                recent.append(pick["category"])
            elif first_gap is None:
                first_gap = d
        d += dt.timedelta(days=1)

    for p, when, seq, in_run in planned:
        note = p["hold"] or (("Window: " + p["window"]) if p["window"] else "")
        rows.append(dict(key=p["file"], file=p["file"], title=p["topic"], category=p["category"],
                         status=p["status"], stage=stage[p["status"]], posted_on="",
                         expected_on=when.isoformat(), order=seq, in_run=in_run, window=p["window"], note=note))
    for p in todo:                                  # never reached inside the horizon
        rows.append(dict(key=p["file"], file=p["file"], title=p["topic"], category=p["category"],
                         status=p["status"], stage=stage[p["status"]], posted_on="", expected_on="",
                         order=None, in_run=False, window=p["window"], note="No slot found"))
    for p in blocked:
        rows.append(dict(key=p["file"], file=p["file"], title=p["topic"], category=p["category"],
                         status="held", stage="Needs you", posted_on="", expected_on="",
                         order=None, in_run=False, window="", note=p["hold"]))

    out = dict(
        rows=rows,
        meta=[
            dict(label="Made by", value="dashboard/snapshot.py in thepropertyaccountant/media"),
            dict(label="Made at", value=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
            dict(label="Read from", value="queue/README.md and POSTED.md"),
            dict(label="Cadence used for expected dates",
                 value=f"Every day to {DAILY_UNTIL.isoformat()}, then days 1, 4, 7 ... 31 of each month"),
            dict(label="First slot with nothing to post", value=first_gap.isoformat() if first_gap else "none inside 500 days"),
        ],
    )
    dest = ROOT / "dashboard" / "queue.json"
    dest.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    c = lambda s: sum(r["status"] == s for r in rows)
    print(f"wrote {dest.relative_to(ROOT)}: {len(rows)} posts - {c('posted')} posted, {c('queued')} queued, "
          f"{c('bank')} bank, {c('held')} held; first empty slot {first_gap}")

if __name__ == "__main__":
    main()
