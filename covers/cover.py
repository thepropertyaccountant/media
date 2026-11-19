#!/usr/bin/env python3
"""
cover.py — illustrated covers for The Property Accountant.

Slide 1 of every carousel. Replaces the plain hook slide with an illustrated
cover: a flat-vector object scene drawn from the post's subject, over a dark
type band carrying the post's own headline and, where the post has them, two
or three figures lifted from its own verified slides.

    0 .. 900     illustration, full bleed, inline SVG, flat vector only
    900 .. 1350  type band, 450px, solid dark ink, padding 54 / 72 / 56
                   kicker (accent)                        index, muted, right
                   headline — Instrument Serif, 48-76px, line-height .92
                   --------------------------------------- hairline
                   stat   stat   stat    value over uppercase mono label

    The brand mark sits at the illustration's top-left, inset 72 / 56.

WHY THIS DIVERGES FROM @earth_by_numbers
That account draws landscapes, because its posts are about places. Stacked
landscape planes say nothing about the GST registration threshold. The
vocabulary here is flat-vector OBJECTS from the subject instead — a rental
house, a set of keys, a calendar page, a car, a ledger, a sale sign. The
construction rules are the same, and they are what keeps it looking designed
rather than like clip-art.

WHERE THE WORDS COME FROM — THE RULE THAT MATTERS MOST
Nothing on a cover is typed here. `apply_cover.py` derives the headline and
the stat row out of the finished carousel's own HTML, AFTER the run has
verified every figure against Inland Revenue. The cover is a view of
validated content; it is never a new source of it. If a value cannot be
derived the build stops and names the slug — it never guesses and never
falls back to something plausible.

This is why this account derives at RENDER time and not, as @earth_by_numbers
does, at conversion time. That account's content files hold finished slides.
This account's queue holds DRAFTS whose figures are explicitly unverified:
queue/README.md calls a drafted figure "a starting point and a pointer to its
source, never a number to copy onto a slide unchecked". On 19 Nov 2026 a
draft had petrol and diesel both at $1.20/$0.37 when Inland Revenue quotes
diesel at $1.30/$0.38. A cover built from that draft would now be arguing
with slide 3 of its own post. Deriving after verification makes that
impossible by construction.

BAND IS 450px, NOT THE BRIEF'S 340px
The brief sized a band for a one- or two-word title. These carry a full
headline sentence in the display serif plus a stat grid whose labels can run
to two lines, so the band grew and the illustration came down to match.

TYPE SIZES ARE SCALED UP FROM THE BRIEF
A 1080px slide is seen about 400px wide in the feed, where the brief's 12px
label renders at roughly 4px and disappears. Labels are 20-26px here — the
same relationship to the frame that the brief's sizes had to a poster.

DEPTH RULES (do not relax them)
  * 4-6 stacked flat-filled shapes, lightness stepping monotonically front
    to back, so depth reads with NO outlines anywhere.
  * Every major form gets a lit face and a shadow face as two separate paths.
  * Gradients ONLY for the background wash and light sources. Never as
    decoration. A flat shape that wants to be a gradient gets removed instead.
  * Exactly one human-scale element per cover, small and off-centre.
  * 5-7 colours per cover, derived from the subject, never a house palette.

TWO TRAPS ALREADY PAID FOR ON THE OTHER ACCOUNT
  * `backdrop()` takes a STYLE and has no default. When six archetypes shared
    one backdrop helper over there, 32 of 70 covers came out with the same
    silhouette — invisible post by post, obviously a template in the 3-wide
    profile grid.
  * `lightsource()` takes a chance, so roughly a third of covers have no light
    source at all. A sun on all 70 is its own kind of template.
"""

import math
import re

W, H = 1080, 1350
ART_H = 900
BAND_H = H - ART_H          # 450


# --------------------------------------------------------------------------
# deterministic jitter — the same slug always draws the same cover
# --------------------------------------------------------------------------

class Rnd:
    """Tiny LCG. Reproducible across machines and Python versions."""

    def __init__(self, seed):
        self.s = seed & 0x7FFFFFFF or 1

    def next(self):
        self.s = (self.s * 1103515245 + 12345) & 0x7FFFFFFF
        return self.s / 0x7FFFFFFF

    def f(self, a, b):
        return a + (b - a) * self.next()

    def i(self, a, b):
        return int(self.f(a, b + 1))

    def pick(self, seq):
        return seq[self.i(0, len(seq) - 1)]

    def chance(self, p):
        return self.next() < p


def seed_of(slug):
    n = 7
    for ch in str(slug):
        n = (n * 131 + ord(ch)) & 0x7FFFFFFF
    return n


# --------------------------------------------------------------------------
# colour
# --------------------------------------------------------------------------

def _rgb(c):
    c = str(c).lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _hex(t):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(v)))) for v in t)


def shade(c, k):
    """k < 1 darkens, k > 1 lightens toward white."""
    r, g, b = _rgb(c)
    if k <= 1:
        return _hex((r * k, g * k, b * k))
    t = min(1.0, k - 1.0)
    return _hex((r + (255 - r) * t, g + (255 - g) * t, b + (255 - b) * t))


def mix(a, b, t):
    ra, ga, ba = _rgb(a)
    rb, gb, bb = _rgb(b)
    return _hex((ra + (rb - ra) * t, ga + (gb - ga) * t, ba + (bb - ba) * t))


def lum(c):
    r, g, b = _rgb(c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def band_ink(pal):
    """The darkest plane pushed darker still, so the band sits under the art."""
    darkest = min(pal["planes"], key=lum)
    ink = shade(darkest, 0.34)
    while lum(ink) > 26:
        ink = shade(ink, 0.8)
    return ink


def expand(far, near, warm, accent):
    """Two anchors plus a warm family -> a 5-step ramp with monotonic lightness.

    The practical method from the brief: interpolate the middle shades between
    two subject-derived anchors and bend them toward one warm family. That
    guarantees the monotonic step the depth rules need while keeping the colour
    specific to the post rather than drawn from a house palette.

    planes[0] is the BACKMOST (lightest) and planes[4] the FRONTMOST (darkest).
    The result is asserted monotonic — a ramp that is not is a bug in the
    anchors, not something to paper over at draw time.
    """
    # The warm bend is deliberately light. At 0.30/0.22/0.10 every ramp
    # collapsed toward the same beige-olive and sixty covers read as one house
    # palette in the contact sheet — the exact fault the per-post anchors
    # exist to avoid. It bends the middle shades; it does not set them.
    ramp = [far,
            mix(mix(far, near, 0.28), warm, 0.17),
            mix(mix(far, near, 0.54), warm, 0.11),
            mix(mix(far, near, 0.78), warm, 0.05),
            near]
    # enforce the monotonic step: each plane well below the last, so depth
    # reads with no outlines. 12, not 7 — at 7 adjacent planes were too close
    # in value for the step to carry the depth on its own.
    out = [ramp[0]]
    for c in ramp[1:]:
        limit = lum(out[-1]) - 12
        while lum(c) > limit:
            c = shade(c, 0.93)
        out.append(c)
    sky_top = shade(far, 1.34)
    sky_bot = mix(shade(far, 1.04), warm, 0.16)
    return {"sky": (sky_top, sky_bot), "planes": out, "accent": accent}


# --------------------------------------------------------------------------
# geometry helpers
# --------------------------------------------------------------------------

def pts(seq):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in seq)


def poly(points, fill, op=None):
    o = f' opacity="{op}"' if op is not None else ""
    return f'<polygon points="{pts(points)}" fill="{fill}"{o}/>'


def rect(x, y, w, h, fill, rx=0, op=None):
    o = f' opacity="{op}"' if op is not None else ""
    r = f' rx="{rx}"' if rx else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"'
            f' fill="{fill}"{r}{o}/>')


def circ(cx, cy, r, fill, op=None):
    o = f' opacity="{op}"' if op is not None else ""
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{o}/>'


def path(d, fill, op=None):
    o = f' opacity="{op}"' if op is not None else ""
    return f'<path d="{d}" fill="{fill}"{o}/>'


# --------------------------------------------------------------------------
# background wash, backdrop silhouettes and light
# --------------------------------------------------------------------------

def wash(pal):
    """The one gradient every cover gets. Background only — never decoration."""
    top, bot = pal["sky"]
    return (f'<defs><linearGradient id="wash" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{top}"/>'
            f'<stop offset="1" stop-color="{bot}"/></linearGradient></defs>'
            f'{rect(0, 0, W, ART_H, "url(#wash)")}')


def lightsource(pal, rnd, chance=0.50):
    """A soft radial glow. Roughly a third of covers get none — see the
    module docstring: a light source on every cover is its own template."""
    if not rnd.chance(chance):
        return ""
    cx = rnd.f(140, W - 140)
    cy = rnd.f(120, 300)
    r = rnd.f(150, 260)
    c = shade(pal["sky"][0], 1.5)
    return (f'<defs><radialGradient id="ls"><stop offset="0" stop-color="{c}"'
            f' stop-opacity=".55"/><stop offset="1" stop-color="{c}"'
            f' stop-opacity="0"/></radialGradient></defs>'
            f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="url(#ls)"/>')


BACKDROP_STYLES = ("horizon", "arch", "grid", "bands", "corner", "rooftops",
                   "ground", "none")


def backdrop(pal, rnd, style):
    """The far plane behind the subject.

    `style` is REQUIRED and has no default. See the module docstring: a shared
    backdrop helper with one silhouette is how 32 of 70 covers on the other
    account ended up looking like a template in the profile grid. Every
    archetype names the style that suits its subject.
    """
    if style not in BACKDROP_STYLES:
        raise ValueError(f"unknown backdrop style {style!r}")
    p = pal["planes"]
    out = []
    if style == "none":
        return ""
    if style == "horizon":
        y = rnd.f(470, 540)
        out.append(poly([(0, y), (W, y - rnd.f(10, 40)), (W, ART_H), (0, ART_H)], p[0]))
        y2 = y + rnd.f(70, 120)
        out.append(poly([(0, y2 + rnd.f(0, 30)), (W, y2), (W, ART_H), (0, ART_H)], p[1]))
    elif style == "arch":
        cx, cy = rnd.f(420, 660), rnd.f(400, 470)
        out.append(circ(cx, cy, rnd.f(250, 310), p[0]))
        out.append(poly([(0, 620), (W, 600), (W, ART_H), (0, ART_H)], p[1]))
    elif style == "grid":
        out.append(rect(0, 0, W, ART_H, p[0], op=0.45))
        step = rnd.f(78, 104)
        y = 150.0
        while y < ART_H - 40:
            out.append(rect(0, y, W, 2, p[2], op=0.30))
            y += step
        out.append(poly([(0, 640), (W, 660), (W, ART_H), (0, ART_H)], p[1]))
    elif style == "bands":
        y = 180.0
        i = 0
        while y < ART_H:
            h = rnd.f(60, 130)
            out.append(rect(0, y, W, h, p[0] if i % 2 else p[1], op=0.55))
            y += h
            i += 1
    elif style == "corner":
        if rnd.chance(0.5):
            out.append(poly([(0, 0), (W, 0), (0, ART_H)], p[0], op=0.75))
        else:
            out.append(poly([(W, 0), (W, ART_H), (0, 0)], p[0], op=0.75))
        out.append(poly([(0, 650), (W, 620), (W, ART_H), (0, ART_H)], p[1]))
    elif style == "rooftops":
        x = -60.0
        base = rnd.f(520, 580)
        while x < W + 60:
            w = rnd.f(90, 160)
            h = rnd.f(60, 150)
            out.append(poly([(x, base), (x + w / 2, base - h), (x + w, base)], p[0]))
            x += w * rnd.f(0.62, 0.9)
        out.append(poly([(0, base), (W, base), (W, ART_H), (0, ART_H)], p[1]))
    elif style == "ground":
        y = rnd.f(600, 660)
        out.append(poly([(0, y), (W, y), (W, ART_H), (0, ART_H)], p[1]))
    return "".join(out)


def ground(pal, y):
    """The frontmost plane the subject stands on."""
    return poly([(0, y), (W, y), (W, ART_H), (0, ART_H)], pal["planes"][3])


# --------------------------------------------------------------------------
# the one human-scale element
# --------------------------------------------------------------------------

def scale_el(kind, x, y, s, colour):
    """Exactly one per cover, small and off-centre. Silhouette only."""
    g = []
    if kind == "figure":
        g.append(circ(x, y - 30 * s, 9 * s, colour))
        g.append(path(f"M{x - 10 * s:.1f},{y - 18 * s:.1f} h{20 * s:.1f} "
                      f"v{24 * s:.1f} h{-20 * s:.1f} z", colour))
        g.append(rect(x - 9 * s, y + 6 * s, 7 * s, 22 * s, colour))
        g.append(rect(x + 2 * s, y + 6 * s, 7 * s, 22 * s, colour))
    elif kind == "figure_bag":
        g.append(scale_el("figure", x, y, s, colour))
        g.append(rect(x + 10 * s, y - 12 * s, 11 * s, 14 * s, colour))
    elif kind == "figure_board":
        g.append(scale_el("figure", x, y, s, colour))
        g.append(rect(x - 24 * s, y - 14 * s, 14 * s, 18 * s, colour))
    elif kind == "two_figures":
        g.append(scale_el("figure", x, y, s, colour))
        g.append(scale_el("figure", x + 26 * s, y + 2 * s, s * 0.92, colour))
    elif kind == "dog":
        g.append(path(f"M{x:.1f},{y:.1f} h{26 * s:.1f} v{-13 * s:.1f} "
                      f"h{-26 * s:.1f} z", colour))
        g.append(circ(x + 28 * s, y - 16 * s, 7 * s, colour))
        for dx in (2, 10, 18, 24):
            g.append(rect(x + dx * s, y, 3.4 * s, 12 * s, colour))
    else:
        raise ValueError(f"unknown scale element {kind!r}")
    return "".join(g)


# --------------------------------------------------------------------------
# archetypes — flat-vector objects from the subject
#
# Each returns the SVG body. Each names its own backdrop style, places its
# forms with a lit face and a shadow face, and places exactly one human-scale
# element. No outlines anywhere; depth comes from the lightness step alone.
# --------------------------------------------------------------------------

def a_rental_house(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "horizon")]
    gy = 700
    g.append(ground(pal, gy))
    cx = rnd.f(470, 560)
    bw, bh = 300, 230
    x0, y0 = cx - bw / 2, gy - bh
    g.append(poly([(x0 - 36, y0), (cx, y0 - 132), (cx + bw / 2 + 36, y0)], p[2]))      # roof lit
    g.append(poly([(cx, y0 - 132), (cx + bw / 2 + 36, y0), (cx, y0)], shade(p[2], 0.8)))
    g.append(rect(x0, y0, bw, bh, p[1]))                                              # wall lit
    g.append(rect(cx, y0, bw / 2, bh, shade(p[1], 0.82)))                             # wall shadow
    g.append(rect(x0 + 40, y0 + 62, 66, 60, pal["accent"]))                           # window
    g.append(rect(cx + 44, y0 + 62, 66, 60, shade(pal["accent"], 0.74)))
    g.append(rect(cx - 26, gy - 104, 52, 104, shade(p[4], 1.1)))                      # door
    # letterbox, on its own post, front plane
    lx = x0 - 128
    g.append(rect(lx, gy - 92, 13, 92, p[4]))
    g.append(rect(lx - 29, gy - 128, 71, 42, p[3]))
    g.append(rect(lx - 29, gy - 128, 71, 20, shade(p[3], 1.14)))
    g.append(scale_el(el, cx + 236, gy - 6, 1.05, shade(p[4], 0.72)))
    return "".join(g)


def a_keys(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "arch")]
    g.append(ground(pal, 712))
    cx, cy = rnd.f(470, 560), 430
    g.append(circ(cx, cy, 104, p[1]))
    g.append(circ(cx, cy, 104, shade(p[1], 0.82), op=1.0) if False else "")
    g.append(path(f"M{cx:.1f},{cy - 104:.1f} a104,104 0 0 1 0,208 z", shade(p[1], 0.82)))
    g.append(circ(cx, cy, 52, pal["sky"][1]))
    for i, ang in enumerate((-14, 26)):
        a = math.radians(ang)
        ln = 250 + i * 34
        ex, ey = cx + math.cos(a) * ln, cy + math.sin(a) * ln
        shaft = p[2] if i == 0 else p[3]
        g.append(path(f"M{cx + math.cos(a) * 96:.1f},{cy + math.sin(a) * 96 - 13:.1f} "
                      f"L{ex:.1f},{ey - 13:.1f} L{ex:.1f},{ey + 13:.1f} "
                      f"L{cx + math.cos(a) * 96:.1f},{cy + math.sin(a) * 96 + 13:.1f} z", shaft))
        g.append(path(f"M{cx + math.cos(a) * 96:.1f},{cy + math.sin(a) * 96 + 2:.1f} "
                      f"L{ex:.1f},{ey + 2:.1f} L{ex:.1f},{ey + 13:.1f} "
                      f"L{cx + math.cos(a) * 96:.1f},{cy + math.sin(a) * 96 + 13:.1f} z",
                      shade(shaft, 0.8)))
        g.append(rect(ex - 44, ey + 11, 17, 28, shade(shaft, 0.84)))
        g.append(rect(ex - 16, ey + 11, 14, 20, shade(shaft, 0.84)))
    g.append(scale_el(el, 196, 706, 0.98, shade(p[4], 0.74)))
    return "".join(g)


def a_calendar(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "grid")]
    g.append(ground(pal, 724))
    x0, y0, cw, ch = rnd.f(300, 356), 250, 440, 400
    g.append(rect(x0 + 22, y0 + 26, cw, ch, shade(p[3], 0.9), rx=10))     # cast shadow form
    g.append(rect(x0, y0, cw, ch, p[1], rx=10))                           # page lit
    g.append(rect(x0 + cw * 0.58, y0, cw * 0.42, ch, shade(p[1], 0.9), rx=0))
    g.append(rect(x0, y0, cw, 86, pal["accent"], rx=10))                  # header
    g.append(rect(x0, y0 + 56, cw, 30, shade(pal["accent"], 0.82)))
    for r in range(4):
        for c in range(5):
            cell = p[2] if (r + c) % 3 else shade(p[2], 0.86)
            g.append(rect(x0 + 34 + c * 76, y0 + 128 + r * 64, 54, 40, cell, rx=4))
    # the ring binding, front plane
    for i in range(4):
        g.append(rect(x0 + 60 + i * 104, y0 - 26, 14, 52, p[4], rx=7))
    g.append(scale_el(el, x0 + cw + 128, 718, 0.95, shade(p[4], 0.72)))
    return "".join(g)


def a_vehicle(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "horizon")]
    gy = 690
    g.append(ground(pal, gy))
    x0 = rnd.f(250, 300)
    bw = 540
    body_y = gy - 132
    g.append(path(f"M{x0:.1f},{body_y:.1f} L{x0 + 118:.1f},{body_y - 96:.1f} "
                  f"L{x0 + 352:.1f},{body_y - 96:.1f} L{x0 + 408:.1f},{body_y:.1f} z", p[1]))
    g.append(path(f"M{x0 + 240:.1f},{body_y:.1f} L{x0 + 352:.1f},{body_y - 96:.1f} "
                  f"L{x0 + 408:.1f},{body_y:.1f} z", shade(p[1], 0.84)))
    g.append(rect(x0, body_y, bw, 86, p[2], rx=16))
    g.append(rect(x0, body_y + 52, bw, 34, shade(p[2], 0.82), rx=8))
    g.append(rect(x0 + 140, body_y - 80, 92, 64, pal["accent"], rx=6))      # glass
    for wx in (x0 + 108, x0 + 420):
        g.append(circ(wx, gy, 52, p[4]))
        g.append(circ(wx, gy, 23, shade(p[3], 1.12)))
    g.append(rect(x0 + bw - 16, body_y + 14, 22, 22, shade(pal["accent"], 1.1), rx=5))
    g.append(scale_el(el, x0 + bw + 118, gy + 4, 1.0, shade(p[4], 0.74)))
    return "".join(g)


def a_ledger(pal, rnd, el):
    """An open ledger, seen from slightly above.

    Drawn flat and WIDE. The first version built it as two tall quads meeting
    at a high spine and it read as a pyramid in the contact sheet, which is
    not a thing an accountant keeps records in.
    """
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "bands")]
    gy = 716
    g.append(ground(pal, gy))
    cx = rnd.f(520, 560)
    hw, spine_y, edge_y = 372, 436, 506
    base_y = spine_y + 182
    # the block of closed pages under each half
    g.append(poly([(cx - hw, edge_y), (cx, spine_y), (cx, base_y),
                   (cx - hw, base_y + 26)], shade(p[3], 0.92)))
    g.append(poly([(cx + hw, edge_y), (cx, spine_y), (cx, base_y),
                   (cx + hw, base_y + 26)], p[3]))
    # the two open pages — lit on the left, shadow on the right
    g.append(poly([(cx - hw, edge_y), (cx, spine_y), (cx, spine_y + 126),
                   (cx - hw, edge_y + 126)], shade(p[1], 1.08)))
    g.append(poly([(cx + hw, edge_y), (cx, spine_y), (cx, spine_y + 126),
                   (cx + hw, edge_y + 126)], shade(p[1], 0.84)))
    # ruled lines, following each page's angle
    for i in range(5):
        t = 0.16 + i * 0.165
        ly = spine_y + 22 + i * 20
        g.append(poly([(cx - hw * 0.86, ly + 36 * t), (cx - 40, ly),
                       (cx - 40, ly + 7), (cx - hw * 0.86, ly + 7 + 36 * t)],
                      p[2], op=0.9))
        g.append(poly([(cx + hw * 0.86, ly + 36 * t), (cx + 40, ly),
                       (cx + 40, ly + 7), (cx + hw * 0.86, ly + 7 + 36 * t)],
                      shade(p[2], 0.86), op=0.9))
    g.append(rect(cx - 6, spine_y, 12, base_y - spine_y, p[4]))
    g.append(rect(cx + hw * 0.52, spine_y + 30, 96, 13, pal["accent"], rx=6))
    g.append(scale_el(el, cx - hw - 118, gy - 4, 0.95, shade(p[4], 0.74)))
    return "".join(g)


def a_folder(pal, rnd, el):
    """A folder with papers standing proud of it, and a tab on the back panel.

    The front panel's top edge sits well below the back panel's, and the
    papers sit between them. Without that step the whole thing rendered as a
    featureless crate in the contact sheet.
    """
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "corner")]
    gy = 724
    g.append(ground(pal, gy))
    x0 = rnd.f(306, 352)
    fw, back_y, front_y = 470, 300, 418
    # back panel, with its tab
    g.append(rect(x0, back_y, fw, gy - back_y - 14, shade(p[2], 1.1), rx=8))
    g.append(path(f"M{x0 + fw - 196:.1f},{back_y:.1f} "
                  f"L{x0 + fw - 46:.1f},{back_y:.1f} "
                  f"L{x0 + fw - 46:.1f},{back_y - 44:.1f} "
                  f"L{x0 + fw - 168:.1f},{back_y - 44:.1f} z", pal["accent"]))
    # the papers, stepped so each one is visible
    for i, (dx, dy) in enumerate(((34, 34), (58, 58), (82, 82))):
        g.append(rect(x0 + dx, back_y + dy, fw - 118, gy - back_y - dy - 40,
                      shade(p[0], 1.0 + 0.1 * (2 - i)), rx=4))
        g.append(rect(x0 + dx + 26, back_y + dy + 30, fw - 210, 11, p[2], rx=5))
        g.append(rect(x0 + dx + 26, back_y + dy + 58, fw - 250, 11, p[2], rx=5))
    # front panel — lit face, then its shadow face
    g.append(rect(x0, front_y, fw, gy - front_y - 14, p[1], rx=8))
    g.append(rect(x0, front_y + (gy - front_y - 14) * 0.54, fw,
                  (gy - front_y - 14) * 0.46, shade(p[1], 0.82)))
    g.append(rect(x0 + 40, front_y + 46, 150, 14, shade(p[3], 1.06), rx=7))
    g.append(scale_el(el, x0 - 112, gy - 4, 0.96, shade(p[4], 0.74)))
    return "".join(g)


def a_odometer(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "arch")]
    g.append(ground(pal, 726))
    cx, cy, r = rnd.f(486, 556), 436, 206
    g.append(circ(cx, cy, r + 26, p[1]))
    g.append(path(f"M{cx:.1f},{cy - r - 26:.1f} a{r + 26},{r + 26} 0 0 1 0,{2 * (r + 26)} z",
                  shade(p[1], 0.84)))
    g.append(circ(cx, cy, r, p[2]))
    g.append(path(f"M{cx - r:.1f},{cy:.1f} a{r},{r} 0 0 1 {2 * r},0 z", shade(p[2], 1.1)))
    for i in range(11):
        a = math.radians(200 + i * 14)
        g.append(rect(cx + math.cos(a) * (r - 44) - 5, cy + math.sin(a) * (r - 44) - 5,
                      10, 10, p[4] if i < 8 else pal["accent"], rx=5))
    a = math.radians(rnd.f(214, 322))
    g.append(path(f"M{cx - 11:.1f},{cy:.1f} L{cx + math.cos(a) * (r - 58):.1f},"
                  f"{cy + math.sin(a) * (r - 58):.1f} L{cx + 11:.1f},{cy + 10:.1f} z",
                  pal["accent"]))
    g.append(circ(cx, cy, 24, p[4]))
    g.append(scale_el(el, cx + r + 132, 720, 0.92, shade(p[4], 0.74)))
    return "".join(g)


def a_sale_sign(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "rooftops")]
    gy = 706
    g.append(ground(pal, gy))
    cx = rnd.f(470, 566)
    g.append(rect(cx - 13, 356, 26, gy - 356, p[4]))                      # post
    bw, bh = 384, 236
    g.append(rect(cx - bw / 2, 300, bw, bh, p[1], rx=8))
    g.append(rect(cx - bw / 2, 300 + bh * 0.58, bw, bh * 0.42, shade(p[1], 0.86)))
    g.append(rect(cx - bw / 2, 300, bw, 62, pal["accent"], rx=8))
    for i in range(3):
        g.append(rect(cx - bw / 2 + 36, 392 + i * 44, bw - 150 - i * 52, 20,
                      shade(p[2], 0.92), rx=10))
    g.append(scale_el(el, cx - 236, gy - 4, 1.02, shade(p[4], 0.74)))
    return "".join(g)


def a_apartment(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "corner")]
    gy = 716
    g.append(ground(pal, gy))
    x0 = rnd.f(330, 392)
    for i, (w, h, c) in enumerate(((176, 404, p[1]), (150, 318, p[2]))):
        bx = x0 + i * 192
        g.append(rect(bx, gy - h, w, h, c))
        g.append(rect(bx + w * 0.62, gy - h, w * 0.38, h, shade(c, 0.84)))
        rows = int(h // 74)
        for r in range(rows):
            for cc in range(3):
                lit = pal["accent"] if ((r * 3 + cc + i) % 4 == 0) else shade(c, 1.16)
                g.append(rect(bx + 20 + cc * 48, gy - h + 34 + r * 74, 30, 38, lit, rx=3))
    g.append(scale_el(el, x0 - 112, gy - 2, 1.0, shade(p[4], 0.74)))
    return "".join(g)


def a_desk(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "grid")]
    gy = 742
    g.append(ground(pal, gy))
    x0 = rnd.f(230, 276)
    dw = 616
    ty = 560
    g.append(rect(x0, ty, dw, 26, p[2], rx=5))                            # desk top lit
    g.append(rect(x0, ty + 16, dw, 14, shade(p[2], 0.8), rx=3))
    g.append(rect(x0 + 34, ty + 26, 22, gy - ty - 26, p[3]))
    g.append(rect(x0 + dw - 56, ty + 26, 22, gy - ty - 26, p[3]))
    # screen
    g.append(rect(x0 + 150, ty - 212, 268, 190, p[1], rx=8))
    g.append(rect(x0 + 150 + 268 * 0.6, ty - 212, 268 * 0.4, 190, shade(p[1], 0.86)))
    g.append(rect(x0 + 170, ty - 192, 228, 150, pal["accent"], rx=4))
    g.append(rect(x0 + 262, ty - 22, 44, 22, p[4]))
    # lamp
    lx = x0 + dw - 120
    g.append(rect(lx, ty - 150, 11, 150, p[4]))
    g.append(path(f"M{lx - 46:.1f},{ty - 150:.1f} L{lx + 58:.1f},{ty - 150:.1f} "
                  f"L{lx + 30:.1f},{ty - 198:.1f} L{lx - 18:.1f},{ty - 198:.1f} z", p[3]))
    g.append(scale_el(el, x0 + 76, gy - 4, 0.9, shade(p[4], 0.74)))
    return "".join(g)


def a_envelope(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "bands")]
    g.append(ground(pal, 724))
    x0, y0, ew, eh = rnd.f(256, 310), 300, 560, 352
    g.append(rect(x0 + 26, y0 + 86, ew - 72, eh - 40, shade(p[1], 1.12), rx=6))   # letter
    g.append(rect(x0, y0 + 56, ew, eh, p[2], rx=10))
    g.append(rect(x0, y0 + 56 + eh * 0.6, ew, eh * 0.4, shade(p[2], 0.85)))
    g.append(path(f"M{x0:.1f},{y0 + 56:.1f} L{x0 + ew / 2:.1f},{y0 + 232:.1f} "
                  f"L{x0 + ew:.1f},{y0 + 56:.1f} z", p[1]))                       # flap lit
    g.append(path(f"M{x0 + ew / 2:.1f},{y0 + 232:.1f} L{x0 + ew:.1f},{y0 + 56:.1f} "
                  f"L{x0 + ew / 2:.1f},{y0 + 56:.1f} z", shade(p[1], 0.86)))
    g.append(rect(x0 + ew - 128, y0 + 86, 86, 70, pal["accent"], rx=4))           # stamp
    g.append(scale_el(el, x0 + ew + 100, 718, 0.9, shade(p[4], 0.74)))
    return "".join(g)


def a_clock(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "horizon")]
    g.append(ground(pal, 728))
    cx, cy, r = rnd.f(480, 556), 428, 196
    g.append(circ(cx, cy, r + 24, p[2]))
    g.append(path(f"M{cx:.1f},{cy - r - 24:.1f} a{r + 24},{r + 24} 0 0 1 0,{2 * (r + 24)} z",
                  shade(p[2], 0.82)))
    g.append(circ(cx, cy, r, shade(p[1], 1.12)))
    for i in range(12):
        a = math.radians(i * 30)
        big = 14 if i % 3 == 0 else 8
        g.append(rect(cx + math.cos(a) * (r - 34) - big / 2,
                      cy + math.sin(a) * (r - 34) - big / 2, big, big, p[3], rx=big / 2))
    g.append(path(f"M{cx - 9:.1f},{cy:.1f} L{cx + 8:.1f},{cy - 128:.1f} "
                  f"L{cx + 17:.1f},{cy + 5:.1f} z", p[4]))
    g.append(path(f"M{cx:.1f},{cy - 9:.1f} L{cx + 118:.1f},{cy + 44:.1f} "
                  f"L{cx:.1f},{cy + 12:.1f} z", pal["accent"]))
    g.append(circ(cx, cy, 18, p[4]))
    g.append(scale_el(el, cx - r - 142, 722, 0.92, shade(p[4], 0.74)))
    return "".join(g)


def a_coins(pal, rnd, el):
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "arch")]
    gy = 718
    g.append(ground(pal, gy))
    x0 = rnd.f(360, 420)
    for col, (n, dx) in enumerate(((6, 0), (9, 186), (4, 356))):
        for i in range(n):
            yy = gy - 34 - i * 34
            g.append(path(f"M{x0 + dx - 76:.1f},{yy:.1f} "
                          f"a76,26 0 1 0 152,0 a76,26 0 1 0 -152,0 z",
                          p[2] if i % 2 else shade(p[2], 0.9)))
            g.append(path(f"M{x0 + dx - 76:.1f},{yy:.1f} "
                          f"a76,26 0 0 0 152,0 l0,-13 a76,26 0 0 1 -152,0 z",
                          shade(p[2], 0.74)))
        top = gy - 34 - (n - 1) * 34
        g.append(path(f"M{x0 + dx - 76:.1f},{top:.1f} a76,26 0 1 1 152,0 "
                      f"a76,26 0 1 1 -152,0 z", pal["accent"] if col == 1 else p[1]))
    g.append(scale_el(el, x0 + 510, gy - 2, 0.92, shade(p[4], 0.74)))
    return "".join(g)


def a_receipt(pal, rnd, el):
    """A till roll, torn at both ends and tilted off square.

    Narrow, tilted, torn top AND bottom, and curling at the foot. Drawn
    upright with a flat top it read as a tower block with lit windows on six
    different covers in the contact sheet.
    """
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "corner")]
    gy = 730
    g.append(ground(pal, gy))
    x0, y0, rw, rh = rnd.f(430, 472), 196, 252, 396
    rot = rnd.f(-7, -3)
    body = []
    steps = 7
    top = [(x0 + i * (rw / steps), y0 + (0 if i % 2 else 15)) for i in range(steps + 1)]
    bot = [(x0 + rw - i * (rw / steps), y0 + rh + (17 if i % 2 else 0))
           for i in range(steps + 1)]
    body = top + [(x0 + rw, y0 + rh)] + bot
    inner = f'<g transform="rotate({rot:.1f} {x0 + rw / 2:.0f} {y0 + rh / 2:.0f})">'
    inner += poly(body, shade(p[1], 1.12))
    inner += poly([(x0 + rw * 0.66, y0 + 8), (x0 + rw, y0 + 8),
                   (x0 + rw, y0 + rh + 8), (x0 + rw * 0.66, y0 + rh + 8)],
                  shade(p[1], 0.9))
    for i in range(8):
        w = rw - 74 - (i % 3) * 42
        inner += rect(x0 + 30, y0 + 58 + i * 38, w, 13, p[2], rx=6)
    inner += rect(x0 + 30, y0 + 58 + 8 * 38 + 10, rw - 60, 20, pal["accent"], rx=9)
    # the curl at the foot, as a flat form — never a gradient
    inner += path(f"M{x0:.1f},{y0 + rh + 8:.1f} "
                  f"q{rw / 2:.1f},{54:.1f} {rw:.1f},{4:.1f} "
                  f"l0,{30:.1f} q{-rw / 2:.1f},{34:.1f} {-rw:.1f},{-6:.1f} z",
                  shade(p[2], 0.82))
    inner += "</g>"
    g.append(inner)
    g.append(scale_el(el, x0 - 142, gy - 4, 0.94, shade(p[4], 0.74)))
    return "".join(g)



def a_front_door(pal, rnd, el):
    """A front door and its step. Close-in where a_rental_house is wide.

    Added because thirteen of sixty covers were whole houses, and in the
    three-wide profile grid thirteen of one silhouette is a template however
    different the colours are.
    """
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "grid")]
    gy = 742
    g.append(ground(pal, gy))
    cx = rnd.f(500, 568)
    fw, fh = 300, 470
    x0, y0 = cx - fw / 2, gy - fh
    g.append(rect(x0 - 54, y0 - 46, fw + 108, fh + 46, shade(p[2], 1.06)))   # wall lit
    g.append(rect(cx + 42, y0 - 46, fw / 2 + 12, fh + 46, p[2]))             # wall shadow
    g.append(rect(x0 - 70, y0 - 70, fw + 140, 30, p[3], rx=4))               # lintel
    g.append(rect(x0, y0, fw, fh, p[1]))                                     # door lit
    g.append(rect(x0 + fw * 0.62, y0, fw * 0.38, fh, shade(p[1], 0.84)))     # door shadow
    for r in range(2):
        for c in range(2):
            g.append(rect(x0 + 32 + c * 124, y0 + 40 + r * 180, 92, 140,
                          shade(p[1], 1.12 if r == 0 else 0.92), rx=4))
    g.append(rect(x0 + fw - 48, y0 + fh / 2 - 12, 26, 26, pal["accent"], rx=13))
    g.append(rect(x0 + 24, y0 - 112, 60, 42, pal["accent"], rx=4))           # number plate
    g.append(rect(x0 - 40, gy - 22, fw + 80, 22, p[4]))                      # step
    g.append(scale_el(el, x0 - 148, gy - 4, 0.98, shade(p[4], 0.74)))
    return "".join(g)


def a_site_plan(pal, rnd, el):
    """A survey plan: lots divided by boundary lines, one of them pegged out.

    The first version filled the middle lot with a solid accent block and the
    whole sheet read as a television in the contact sheet. The lots are drawn
    as outlines now, the way a plan actually looks, and the accent is spent on
    the one new boundary rather than on a face.
    """
    p = pal["planes"]
    g = [wash(pal), lightsource(pal, rnd), backdrop(pal, rnd, "corner")]
    g.append(ground(pal, 736))
    x0, y0, pw, ph = rnd.f(230, 268), 232, 620, 412
    g.append(rect(x0 + 22, y0 + 24, pw, ph, shade(p[3], 0.9), rx=6))          # under-sheet
    g.append(rect(x0, y0, pw, ph, shade(p[0], 1.16), rx=6))                   # sheet lit
    g.append(rect(x0 + pw * 0.70, y0, pw * 0.30, ph, shade(p[0], 1.0), rx=0)) # sheet shadow
    ix, iy, iw, ih = x0 + 46, y0 + 48, pw - 92, ph - 150
    g.append(rect(ix, iy, iw, ih, shade(p[1], 1.06)))                         # the block
    g.append(rect(ix, iy + ih * 0.62, iw, ih * 0.38, shade(p[1], 0.9)))
    t = 2.0
    for fx in (0.34, 0.64):                                                   # boundaries
        g.append(rect(ix + iw * fx - t, iy, t * 2, ih, p[3]))
    g.append(rect(ix, iy + ih * 0.58 - t, iw * 0.34, t * 2, p[3]))
    g.append(rect(ix + iw * 0.64 - t, iy, t * 2, ih, pal["accent"]))          # the new one
    for fx, fy in ((0.14, 0.26), (0.46, 0.3), (0.46, 0.74), (0.8, 0.34)):
        g.append(rect(ix + iw * fx, iy + ih * fy, 46, 34, p[2]))              # footprints
    g.append(circ(ix + iw * 0.64, iy + ih * 0.5, 13, p[4]))                   # the peg
    g.append(path(f"M{x0 + pw - 70:.1f},{y0 + ph - 60:.1f} "                  # north arrow
                  f"l14,-34 l14,34 l-14,-12 z", p[4]))
    for i in range(2):
        g.append(rect(x0 + 46, y0 + ph - 62 + i * 18, pw - 230 - i * 120, 7, p[2], rx=4))
    g.append(scale_el(el, x0 + pw + 92, 730, 0.92, shade(p[4], 0.74)))
    return "".join(g)


ARCHETYPES = {
    "rental_house": a_rental_house,
    "keys": a_keys,
    "calendar": a_calendar,
    "vehicle": a_vehicle,
    "ledger": a_ledger,
    "folder": a_folder,
    "odometer": a_odometer,
    "sale_sign": a_sale_sign,
    "apartment": a_apartment,
    "desk": a_desk,
    "envelope": a_envelope,
    "clock": a_clock,
    "coins": a_coins,
    "receipt": a_receipt,
    "front_door": a_front_door,
    "site_plan": a_site_plan,
}


# --------------------------------------------------------------------------
# the type band
# --------------------------------------------------------------------------

COVER_CSS = """
/* ---- cover slide (covers/cover.py) — appended, never edit the rules above */
.slide.cover{padding:0;display:block;background:#000;overflow:hidden}
.cover .art{position:absolute;left:0;top:0;display:block}
.cover .brand{position:absolute;left:72px;top:56px;
  font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:28px;
  letter-spacing:-.03em}
.cover .band{position:absolute;left:0;right:0;bottom:0;height:450px;
  padding:54px 72px 56px;display:flex;flex-direction:column}
.cover .brow{display:flex;align-items:flex-start;justify-content:space-between;gap:30px}
.cover .kick{font-family:"IBM Plex Mono",monospace;font-size:25px;
  letter-spacing:.2em;text-transform:uppercase}
.cover .idx{font-family:"IBM Plex Mono",monospace;font-size:24px;
  letter-spacing:.14em;flex:0 0 auto}
.cover .disp{font-family:"Instrument Serif",serif;font-weight:400;
  line-height:.92;letter-spacing:-.005em;margin-top:22px}
.cover .rule{height:1px;margin-top:auto}
.cover .stats{display:grid;gap:30px;padding-top:28px}
.cover .stats.n1{grid-template-columns:1fr}
.cover .stats.n2{grid-template-columns:repeat(2,1fr)}
.cover .stats.n3{grid-template-columns:repeat(3,1fr)}
.cover .stat .v{font-family:"Instrument Serif",serif;font-size:46px;line-height:1;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cover .stat .l{font-family:"IBM Plex Mono",monospace;font-size:20px;
  letter-spacing:.15em;text-transform:uppercase;margin-top:14px;line-height:1.3}
"""


def _esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def disp_size(text):
    """Largest size from the ladder that keeps the headline to TWO lines.

    Two, not three. The band's content has to hold the kicker row, the
    headline, the hairline and a stat grid whose labels can run to two lines
    themselves. Three lines of display serif only fits when every stat label
    is short, and a cover that clips its own headline on the one post with
    long labels is not a system. Two lines always fits, so two lines it is.
    """
    n = len(text)
    for size, per_line in ((76, 26), (66, 31), (58, 36), (50, 42)):
        if n <= per_line * 2:
            return size
    return 44


def slide_cover(s, n, total):
    """Render the cover slide. `s` carries only derived words plus the three
    human choices; the illustration is regenerated from the slug every time."""
    if s["archetype"] not in ARCHETYPES:
        raise SystemExit(f"{s.get('slug')}: unknown archetype {s['archetype']!r}")
    palette = expand(s["far"], s["near"], s["warm"], s["accent"])
    rnd = Rnd(seed_of(s["slug"]))
    art = ARCHETYPES[s["archetype"]](palette, rnd, s["element"])
    ink = band_ink(palette)
    paper = "#F4F7F3"
    accent = palette["accent"]
    while lum(accent) < 110:                  # keep the kicker legible on ink
        accent = shade(accent, 1.2)
    muted = mix(paper, ink, 0.46)
    rule_c = mix(paper, ink, 0.70)
    # The draft's <br> breaks were measured for the ORIGINAL slide at h-xl.
    # At the cover's size they force three, four and five line headlines and
    # blow straight through the two-line rule, so they are dropped and the
    # line is left to wrap. Only the line breaking changes; not one word does.
    headline = re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " ", s["headline"])).strip()
    size = s.get("size") or disp_size(re.sub("<[^>]+>", " ", headline))
    stats = s.get("stats") or []
    stat_html = "".join(
        f'<div class="stat"><div class="v">{_esc(v)}</div>'
        f'<div class="l" style="color:{muted}">{_esc(l)}</div></div>'
        for v, l in stats)
    stat_block = (f'<div class="stats n{len(stats)}">{stat_html}</div>'
                  if stats else '<div class="stats n1"></div>')
    was = s.get("was_hook", "")
    return f"""<div class="slide cover" id="s{n}">
  <svg class="art" width="{W}" height="{ART_H}" viewBox="0 0 {W} {ART_H}">{art}</svg>
  <div class="brand" style="color:{paper}">The Property Accountant</div>
  <div class="band" style="background:{ink};color:{paper}">
    <div class="brow">
      <span class="kick" style="color:{accent}">{_esc(s.get("kicker", ""))}</span>
      <span class="idx mono" style="color:{muted}">{n}/{total}</span>
    </div>
    <div class="disp" style="font-size:{size}px">{headline}</div>
    <div class="rule" style="background:{rule_c}"></div>
    {stat_block}
  </div>
  <template class="was-hook">{was}</template>
</div>"""
