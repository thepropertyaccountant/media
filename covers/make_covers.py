#!/usr/bin/env python3
"""
make_covers.py — cover design choices, and applying a cover to a built carousel.

TWO LEVELS, BOTH RESUMABLE WITH NO PROGRESS FILE
-------------------------------------------------------------------------
1. DESIGN. `COVERS` below holds the three choices a human makes per post:
   archetype, palette anchors, and the one human-scale element. A draft with
   a COVERS row is designed; one without is not. `--list` prints what is
   still outstanding, so a run that stops part way is picked up by the next
   one with `--limit`, and nothing can drift out of step with the repo.

2. APPLICATION. `apply` swaps slide 1 of a BUILT carousel for its cover. A
   slide 1 with class `cover` has been applied; a plain one has not. The
   original slide is stored verbatim in a `<template class="was-hook">`
   inside the cover, so `--force` always re-derives from the ORIGINAL
   wording and never from a cover it already made, however many times it
   runs. It also means the change is reversible: `revert` puts the original
   slide 1 back.

WHY THE WORDS ARE DERIVED AT RENDER TIME AND NOT FROM THE DRAFT
-------------------------------------------------------------------------
queue/README.md: a drafted figure "is a starting point and a pointer to its
source, never a number to copy onto a slide unchecked". Drafts are not
verified and their figures move. On 19 Nov 2026 draft 08 had petrol and
diesel both at $1.20/$0.37; Inland Revenue quotes diesel at $1.30/$0.38, and
the run corrected it. A cover built from that draft would be contradicting
slide 3 of its own post on the grid.

So the headline and the stat row are read out of the finished carousel's own
HTML, after the run has verified every figure. NO FIGURE IS EVER TYPED HERE,
and none is ever carried over from a draft. If a value cannot be derived the
build stops and names the slug — it never guesses and never falls back to
something plausible.

THE KICKER is the post's own title, taken from the draft's H1 and uppercased.
A COVERS row may override it with a shorter label, which is a design choice
like the archetype — but an override carrying an ASCII digit is rejected,
because the kicker is the one line on the cover that is not read back out of
a verified slide and so is the one place a figure could sneak in.
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cover as C                                              # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "queue"

# --------------------------------------------------------------------------
# THE THREE HUMAN CHOICES, PER POST
#
#   slug: (archetype, far, near, warm, accent, element, kicker_override)
#
# Colours come from the subject, never from a house palette: kilometre rates
# get asphalt greys and an indicator amber, the bright-line test gets survey
# blues, GST gets ledger greens. `far` is the backmost/lightest anchor and
# `near` the frontmost/darkest; `warm` bends the interpolated middle shades;
# `accent` is the one saturated note. cover.expand() asserts the ramp steps
# monotonically, so a pair that does not is a bug in the anchors here.
#
# kicker_override is "" to use the draft's own title.
# --------------------------------------------------------------------------

COVERS = {}


def _c(slug, archetype, far, near, warm, accent, element, kicker=""):
    COVERS[slug] = (archetype, far, near, warm, accent, element, kicker)


# ---- run order ----------------------------------------------------------
_c("09-intention-test",            "sale_sign", "#A8B8C2", "#1D2F3B", "#C08A52", "#E6A552", "figure_board", "The intention test")
_c("11-mixed-use-holiday-home",    "rental_house", "#9FC0BE", "#15322F", "#C4894F", "#E5B257", "two_figures", "Mixed-use assets")
_c("12-schedular-payments",        "receipt",   "#B4B2C4", "#262036", "#B98A5C", "#D79A5B", "figure",       "Withholding")

# ---- the bank, in run order --------------------------------------------
_c("47-the-two-gst-dates-that-are-not-the-28th", "calendar", "#A9C0B2", "#1B3128", "#BE8A50", "#DFA14E", "figure",      "GST due dates")
_c("48-the-seventh-of-february",   "calendar",  "#B6BCC8", "#232B3A", "#C08B54", "#E0A355", "figure",       "Terminal tax")
_c("69-the-seventh-of-july",       "calendar",  "#AEC3C6", "#1C3034", "#C28E55", "#E2A74F", "figure_bag",   "The rental return")
_c("23-short-stay-standard-cost",  "rental_house", "#BCC7B4", "#24301F", "#C79154", "#E4AC52", "figure_bag", "Short-stay standard cost")
_c("24-principal-is-not-deductible", "coins",   "#AFB9C6", "#1F2936", "#BC8750", "#DC9E51", "figure",       "Principal and interest")
_c("14-entertainment-and-your-own-lunch", "receipt", "#C5B6AE", "#322520", "#C28A55", "#DFA055", "two_figures", "Entertainment")
_c("25-gst-on-short-stay-marketplaces", "apartment", "#A6BCC4", "#182C34", "#BE8A52", "#DDA253", "figure",   "Marketplace GST")
_c("26-repairs-versus-improvements", "front_door", "#B8C0AE", "#262E1F", "#C68E51", "#E3A84F", "figure_board", "Repairs or improvements")
_c("27-settlement-gifts",          "coins",     "#C3B4C0", "#2C2332", "#C08C58", "#DFA059", "two_figures",  "Settlement gifts")
_c("28-legal-fees-on-purchase",    "folder",    "#AEB7C8", "#1E2636", "#BB8853", "#DB9E54", "figure",       "Legal fees")
_c("29-gst-registered-short-stay-sale", "apartment", "#A9C2B6", "#18312A", "#C18C52", "#E0A450", "figure",  "GST on the sale")
_c("30-clothing-and-grooming",     "folder",   "#C6BAB2", "#302722", "#C28D57", "#E0A356", "figure",       "Clothing and grooming")
_c("31-gross-rent-not-net",        "ledger",    "#B2C0B6", "#1F2E25", "#C28E52", "#E1A651", "figure",       "Gross rent")
_c("32-interest-follows-purpose",  "coins",     "#A7B6C6", "#1B2634", "#BA8751", "#DA9D52", "figure_board", "Interest follows purpose")
_c("33-gst-from-the-invoice-not-the-deposit", "receipt", "#B0BEC8", "#1E2B34", "#BD8A54", "#DDA054", "figure", "Your commission")
_c("34-vacant-between-tenants",    "front_door", "#BAC2C6", "#272F34", "#C38F54", "#E0A552", "figure",    "Vacant periods")
_c("35-inherited-property-bright-line", "keys",  "#B9BCB2", "#2A2C22", "#C38E50", "#E2A74E", "figure",      "Inherited property")
_c("36-first-year-on-commission",  "clock",     "#AEBAC6", "#1E2834", "#BC8852", "#DC9E53", "figure_bag",   "Year one on commission")
_c("37-your-own-labour",           "desk",      "#BEB6AC", "#2C2620", "#C48F53", "#E2A550", "figure",       "Your own labour")
_c("38-low-value-assets-and-the-invoice", "folder", "#AFC0B8", "#1D2E27", "#C08C52", "#DFA350", "figure",    "Low-value assets")
_c("22-smoothing-provisional-tax", "clock",     "#B4BAC8", "#222838", "#BE8A55", "#DEA156", "figure",       "Provisional tax")
_c("39-body-corporate-levies",     "apartment", "#A8BCC8", "#1A2A34", "#BC8852", "#DB9F53", "figure",       "Body corporate levies")
_c("40-off-the-plans-bright-line", "site_plan", "#B6C2BA", "#243028", "#C28E52", "#E1A550", "figure_board", "Off the plans")
_c("41-home-to-work-travel",       "vehicle",   "#B8BCC0", "#282C30", "#C08C52", "#E0A451", "figure",       "Home to work")
_c("42-mates-rates",               "rental_house", "#BFC0AE", "#2E2F1F", "#C69051", "#E4A94E", "two_figures", "Mates' rates")
_c("43-flatmates-in-your-own-home", "rental_house", "#B4C4BC", "#22322A", "#C18D53", "#E0A451", "two_figures", "Flatmates")
_c("44-the-ninety-day-logbook",    "odometer",  "#AFB6BE", "#1F262E", "#BE8A52", "#DEA052", "figure",       "The logbook")
_c("45-boarders-standard-cost",    "rental_house", "#BDC6B6", "#2A3222", "#C59052", "#E3A750", "two_figures", "Boarders")
_c("46-the-tenants-bond",          "envelope",  "#AEC0C6", "#1C2C32", "#BD8A53", "#DCA052", "figure",       "The bond")
_c("19-marketing-you-fund-yourself", "sale_sign", "#B6B8C8", "#262838", "#C08C56", "#DFA257", "figure_board", "Marketing you fund")
_c("49-relationship-property-transfers", "keys", "#BCBAC2", "#2C2A32", "#C28E54", "#E0A454", "two_figures", "Relationship property")
_c("50-when-your-home-becomes-a-rental", "keys", "#B0C2BE", "#1E302C", "#C18D52", "#E0A550", "figure_bag", "Home becomes a rental")
_c("51-writing-off-what-you-throw-out", "ledger", "#B8BEB4", "#282E22", "#C38F52", "#E2A650", "figure",     "Writing off what you remove")
_c("52-leaky-building-repairs",    "rental_house", "#A8BAC4", "#182A32", "#BC8A52", "#DCA151", "figure_board", "Leaky building repairs")
_c("16-interest-and-penalties",    "clock",     "#C0B4B2", "#302422", "#C28B54", "#DF9E55", "figure",       "Interest and penalties")
_c("53-bright-line-losses",        "sale_sign", "#B2BCC8", "#202a36", "#BD8952", "#DCA052", "figure",       "Bright-line losses")
_c("55-what-comes-off-a-bright-line-gain", "ledger", "#AEBCC2", "#1C2A30", "#BC8952", "#DB9F51", "figure",  "The bright-line gain")
_c("54-paying-your-partner",       "desk",      "#BEB8C4", "#2C2834", "#C18D56", "#DFA157", "two_figures",  "Paying your partner")
_c("56-residential-rent-is-outside-gst", "front_door", "#AEC2B8", "#1C3028", "#C08C52", "#DFA450", "figure", "Residential rent and GST")
_c("13-depreciation-recovery",     "ledger",    "#B6BAB0", "#262A20", "#C28E51", "#E1A64F", "figure",       "Depreciation recovery")
_c("57-income-protection-premiums", "folder",   "#B0BAC8", "#1E2634", "#BC8954", "#DBA054", "figure",       "Income protection")
_c("58-mortgage-break-fees",       "coins",     "#B4BEC4", "#222C32", "#BE8B52", "#DDA151", "figure",       "Break fees")
_c("59-rental-in-a-trust",         "folder",    "#BCB6C0", "#2A2432", "#C08D56", "#DEA156", "figure",       "Rentals in a trust")
_c("20-fees-taken-out-of-commission", "receipt", "#B2B6C6", "#202436", "#BD8A55", "#DCA055", "figure",      "Deductions from commission")
_c("60-into-the-family-trust",     "keys",      "#B8BAC0", "#282A30", "#C18D53", "#E0A452", "two_figures",  "Into the family trust")
_c("62-portfolio-or-property-by-property", "apartment", "#AAC0C2", "#1A2E30", "#BE8B52", "#DDA151", "figure", "Two rentals, one loss")
_c("61-the-real-estate-fact-sheet", "folder",   "#B6BCC2", "#262C32", "#C08D54", "#DFA254", "figure_board", "Inland Revenue's fact sheet")
_c("63-the-rental-overseas",       "envelope",  "#A8BEC8", "#182C34", "#BC8A52", "#DCA052", "figure_bag",   "The rental overseas")
_c("65-the-drive-to-your-rental",  "vehicle",   "#B4BCB6", "#242C26", "#C18D52", "#E0A550", "figure",       "The drive to your rental")
_c("64-sponsorship-or-donation",   "sale_sign", "#BEB8B0", "#2C2620", "#C38F54", "#E2A652", "two_figures",  "Sponsorship")
_c("66-when-the-insurer-pays",     "rental_house", "#AEBCC6", "#1C2A34", "#BC8952", "#DBA051", "figure",    "When the insurer pays")
_c("67-subdividing-and-the-bright-line-clock", "site_plan", "#B6C0B4", "#242E22", "#C28E51", "#E1A64F", "figure_board", "Subdividing")
_c("15-gst-payments-or-invoice-basis", "ledger", "#AEC0B6", "#1C2E26", "#BF8B52", "#DEA250", "figure",      "GST basis")
_c("68-moved-overseas-kept-the-rental", "envelope", "#AAC0C8", "#1A2E34", "#BD8A53", "#DCA052", "figure_bag", "Moved overseas")

# ---- held back (designed now so a hold that comes round is not blocked) --
_c("06-provisional-tax-15-january", "calendar", "#B2BAC8", "#202838", "#BE8A55", "#DDA056", "figure",       "Provisional tax")
_c("10-healthy-homes-deductibility", "front_door", "#B6C4B8", "#243224", "#C38F52", "#E2A750", "figure_board", "Healthy Homes")


# --------------------------------------------------------------------------
# reading the built carousel
# --------------------------------------------------------------------------

SLIDE_START = re.compile(r'<div class="slide([^"]*)" id="s(\d+)">')


def _text(html):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", html or "")).strip()


def has_digit(s):
    """ASCII digits only.

    NOT str.isdigit(): '²'.isdigit() is True in Python, which is how two
    different stat columns on the other account both ended up labelled KM².
    Only an ASCII digit means a string is carrying a figure.
    """
    return any(ch in "0123456789" for ch in str(s))


def slides_of(html):
    """(class, number, whole block) per slide.

    Split on slide starts rather than matching to the first `</div>`: a cover
    nests several divs, so a non-greedy match truncated the block before the
    stored original and broke --force and revert. Slides are top-level
    siblings, so the boundaries are unambiguous.
    """
    starts = [m for m in SLIDE_START.finditer(html)]
    out = []
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else html.find("\n</body>")
        if end == -1:
            end = len(html)
        out.append((m.group(1).strip(), int(m.group(2)), html[m.start():end].rstrip()))
    return out


def short_label(text, limit=22):
    t = _text(text)
    t = re.split(r"[,—(]| - ", t)[0].strip()
    if len(t) > limit:
        out = ""
        for w in t.split():
            if len(out) + len(w) + 1 > limit:
                break
            out = (out + " " + w).strip()
        t = out or t[:limit]
    return t.upper()


# Serif value widths, measured at 46px. Used only to decide HOW MANY columns
# a cover gets — never to shorten a value. A value that will not fit is
# dropped whole; it is never truncated, because half a figure is a wrong one.
_COL_W = {1: 936, 2: 453, 3: 292}


def _fits(value, cols):
    return len(str(value)) * 23.0 <= _COL_W[cols]


def fit_stats(stats):
    """Most columns (up to 3) in which every value fits without ellipsis.

    Trap #7: where there is no honest figure, use fewer columns. Never invent
    one and never shrink one to fit.
    """
    for cols in (3, 2, 1):
        use = stats[:cols]
        if len(use) == cols and all(_fits(v, cols) for v, _ in use):
            return use
    return []


def derive_stats(html):
    """Figures read back out of the post's own verified slides.

    Ledger rows first, because those are the figures the post has committed
    to on a slide of its own. `.big` numbers next. Nothing else: a `.tag` is
    a qualifier, not a figure, and a headline number belongs to its sentence.
    """
    found, seen = [], set()
    for cls, n, body in slides_of(html):
        if n == 1:
            continue
        for m in re.finditer(r'<span class="lab"[^>]*>(.*?)</span>\s*'
                             r'<span class="fig([^"]*)">(.*?)</span>', body, re.S):
            lab, val = _text(m.group(1)), _text(m.group(3))
            if not has_digit(val) or val.lower() in seen:
                continue
            seen.add(val.lower())
            found.append((val, short_label(lab)))
        for m in re.finditer(r'<div class="big">(.*?)</div>', body, re.S):
            val = _text(m.group(1))
            if not has_digit(val) or val.lower() in seen:
                continue
            k = re.search(r'<span class="kicker mono">(.*?)</span>', body, re.S)
            seen.add(val.lower())
            found.append((val, short_label(k.group(1) if k else "")))
    return fit_stats([(v, l) for v, l in found if l])


def kicker_for(slug, override):
    if override:
        if has_digit(override):
            raise SystemExit(
                f"{slug}: kicker override {override!r} carries a figure. The "
                f"kicker is the one cover line not read back out of a verified "
                f"slide, so it may not hold one.")
        return override.upper()
    draft = QUEUE / f"{slug}.md"
    if not draft.exists():
        raise SystemExit(f"{slug}: no draft at {draft} and no kicker override — "
                         f"cannot derive a kicker. Add one to the COVERS row.")
    m = re.match(r"#\s*\d+\s*[—-]\s*(.+)", draft.read_text().splitlines()[0])
    if not m:
        raise SystemExit(f"{slug}: draft H1 is not '# NN — Title'; cannot derive a kicker.")
    title = re.split(r"[:.]", m.group(1))[0].strip()
    return title.upper()


# --------------------------------------------------------------------------
# apply / revert
# --------------------------------------------------------------------------

def apply_cover(html_path, slug, force=False):
    p = pathlib.Path(html_path)
    html = p.read_text()
    slides = slides_of(html)
    if not slides:
        raise SystemExit(f"{slug}: no slides found in {p}")
    cls1, n1, body1 = slides[0]
    total = len(slides)

    if "cover" in cls1.split():
        if not force:
            return False
        m = re.search(r'<template class="was-hook">(.*?)</template>', body1, re.S)
        if not m:
            raise SystemExit(f"{slug}: slide 1 is a cover with no stored was-hook; "
                             f"cannot re-derive from the original wording.")
        original = unescape(m.group(1))
        html = html.replace(body1, original, 1)
        slides = slides_of(html)
        cls1, n1, body1 = slides[0]

    if slug not in COVERS:
        raise SystemExit(f"{slug}: no COVERS row — add archetype, palette anchors "
                         f"and element before building.")
    archetype, far, near, warm, accent, element, kov = COVERS[slug]

    hm = re.search(r'<h[12] class="h-(?:xl|lg|md)">(.*?)</h[12]>', body1, re.S)
    if not hm:
        raise SystemExit(f"{slug}: slide 1 has no h-xl/h-lg/h-md headline to derive from.")
    headline = hm.group(1).strip()

    spec = {
        "slug": slug, "archetype": archetype, "far": far, "near": near,
        "warm": warm, "accent": accent, "element": element,
        "kicker": kicker_for(slug, kov),
        "headline": headline,
        "stats": derive_stats(html),
        "was_hook": C._esc(body1),
    }
    new = C.slide_cover(spec, 1, total)
    html = html.replace(body1, new, 1)
    if "/* ---- cover slide (covers/cover.py)" not in html:
        html = html.replace("</style>", C.COVER_CSS + "</style>", 1)
    p.write_text(html)
    return True


def revert_cover(html_path):
    p = pathlib.Path(html_path)
    html = p.read_text()
    cls1, n1, body1 = slides_of(html)[0]
    if "cover" not in cls1.split():
        return False
    m = re.search(r'<template class="was-hook">(.*?)</template>', body1, re.S)
    if not m:
        raise SystemExit(f"{p}: cover has no stored was-hook to revert to.")
    p.write_text(html.replace(body1, unescape(m.group(1)), 1))
    return True


def unescape(s):
    return (s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&"))


# --------------------------------------------------------------------------
# the outstanding-design list, and the twist report
# --------------------------------------------------------------------------

def unposted_slugs():
    readme = (QUEUE / "README.md").read_text()
    posted = set(re.findall(r"^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|[^|]*\|\s*posted\s*\|",
                            readme, re.M))
    out = []
    for f in sorted(QUEUE.glob("*.md")):
        if f.name == "README.md":
            continue
        if f.name.split("-")[0] in posted:
            continue
        out.append(f.stem)
    return out


def pending():
    return [s for s in unposted_slugs() if s not in COVERS]


SUB_RE = re.compile(r"^1\.\s+\*\*.*?sub:\s*`([^`]+)`", re.M | re.S)


def twist_report():
    """Unposted drafts whose slide-1 sub line is not carried in the caption.

    The cover has no room for the sub that sat under the old headline. Unlike
    @earth_by_numbers, this repo stores no published caption — each run writes
    the caption fresh from the draft's `## Caption` sketch — so the fix is not
    to edit drafts but for the RUN to carry the sub into the caption it
    writes. BUILD.md section 9 says so and the task prompt repeats it. This
    list is what that instruction applies to; it is not a warning to scroll
    past.
    """
    out = []
    for slug in unposted_slugs():
        f = QUEUE / f"{slug}.md"
        t = f.read_text()
        m = SUB_RE.search(t)
        if not m:
            continue
        sub = m.group(1)
        cap = t.split("## Caption")[-1].lower() if "## Caption" in t else ""
        words = re.findall(r"[a-z]{5,}", sub.lower())
        if not words:
            continue
        if sum(1 for w in words if w in cap) / len(words) < 0.5:
            out.append((slug, sub))
    return out


def main():
    args = sys.argv[1:]
    if args and args[0] == "apply":
        force = "--force" in args
        rest = [a for a in args[1:] if not a.startswith("--")]
        if len(rest) != 2:
            raise SystemExit("usage: make_covers.py apply <carousel.html> <slug> [--force]")
        ok = apply_cover(rest[0], rest[1], force=force)
        print(("applied" if ok else "already a cover (use --force to re-derive)"), rest[1])
        return
    if args and args[0] == "revert":
        print("reverted" if revert_cover(args[1]) else "not a cover", args[1])
        return
    if args and args[0] == "--twist":
        rows = twist_report()
        print(f"{len(rows)} unposted drafts whose slide-1 sub is not in the caption sketch.")
        print("The RUN must carry the sub into the caption it writes (BUILD.md s9).")
        for slug, sub in rows:
            print(f"  {slug}\n      {sub}")
        return
    todo = pending()
    print(f"{len(todo)} unposted drafts with no COVERS row")
    for s in todo:
        print(" ", s)
    if not todo:
        print("every unposted draft is designed.")


if __name__ == "__main__":
    main()
