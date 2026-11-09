#!/usr/bin/env python3
"""
Build or top up queue.json from content/*.json.

queue.json is the single source of truth for the posting task. It lives in
this repo because every scheduled run starts in a fresh workspace with no
memory of the last one.

Posts already in the queue keep their state (approved / posted_at / media_id).
New content files are appended, interleaved by kind so the feed alternates
between crazy-stats, top5 and spotlight rather than running five of one type.

Usage:
    python3 make_queue.py                 # add new posts as approved=false
    python3 make_queue.py --approve-new   # add new posts already approved
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
CONTENT = ROOT / "content"
QUEUE = ROOT / "queue.json"

ACCOUNT_ID = "17841435841293051"
HANDLE = "earth_by_numbers"
BASE_URL = ("https://raw.githubusercontent.com/thepropertyaccountant/media/"
            "main/earth-by-numbers/img")

DEFAULT = {
    "account_id": ACCOUNT_ID,
    "handle": HANDLE,
    "base_url": BASE_URL,
    "slots_utc": ["11:31", "23:31"],
    "queue": [],
}


def full_caption(spec):
    tags = " ".join("#" + t for t in spec.get("tags", []))
    return spec["caption"].strip() + "\n\n" + tags


def interleave(items):
    """Round-robin by kind so the feed alternates formats."""
    buckets = {}
    for it in items:
        buckets.setdefault(it["kind"], []).append(it)
    order = ["crazy", "top5", "spotlight"]
    order += [k for k in buckets if k not in order]
    out, i = [], 0
    while any(buckets.get(k) for k in order):
        k = order[i % len(order)]
        if buckets.get(k):
            out.append(buckets[k].pop(0))
        i += 1
    return out


def main():
    approve_new = "--approve-new" in sys.argv
    state = json.loads(QUEUE.read_text()) if QUEUE.exists() else dict(DEFAULT)
    state.setdefault("queue", [])
    # keep config current
    for k, v in DEFAULT.items():
        if k != "queue":
            state[k] = v

    known = {e["slug"] for e in state["queue"]}
    fresh = []
    for f in sorted(CONTENT.glob("*.json")):
        spec = json.loads(f.read_text())
        if spec["slug"] in known:
            continue
        n = len(spec["slides"])
        fresh.append({
            "slug": spec["slug"],
            "kind": spec.get("kind", "carousel"),
            "images": [f"{BASE_URL}/{spec['slug']}-{i:02d}.jpg" for i in range(1, n + 1)],
            "caption": full_caption(spec),
            "approved": bool(approve_new),
            "posted_at": None,
            "media_id": None,
        })

    state["queue"].extend(interleave(fresh))
    QUEUE.write_text(json.dumps(state, indent=2, ensure_ascii=False))

    pending = [e for e in state["queue"] if not e["posted_at"]]
    appr = [e for e in pending if e["approved"]]
    print(f"queue.json: {len(state['queue'])} total, {len(pending)} unposted, "
          f"{len(appr)} approved and ready ({len(appr)/2:.1f} days at 2/day)")
    print(f"added {len(fresh)} new")
    for e in state["queue"][:6]:
        flag = "posted" if e["posted_at"] else ("ready" if e["approved"] else "NEEDS APPROVAL")
        print(f"  {e['slug']:22s} {e['kind']:9s} {len(e['images'])} imgs  {flag}")


if __name__ == "__main__":
    main()
