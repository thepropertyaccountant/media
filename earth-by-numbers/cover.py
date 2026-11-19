#!/usr/bin/env python3
"""
cover.py — layered-plane place-poster covers for Earth by Numbers.

Slide 1 of every post. Replaces the old plain `hook` slide with an illustrated
poster: a flat-vector landscape built from stacked planes, over a dark type band
carrying the contentious hook line and three stats.

Anatomy (fixed — every cover in the set is identical in structure):

    0 .. 920     illustration, full bleed, inline SVG, flat vector only
    920 .. 1350  type band, 430px, solid dark ink, padding 54 / 72 / 56
                   kicker (accent)            region label (muted, 2 lines, right)
                   hook line — Instrument Serif, 52-80px, line-height .9
                   ------------------------------- hairline
                   stat   stat   stat          numeral over uppercase label

    "01" + a 40px hairline sit at the illustration's top-left, inset 72 / 56.
    The brand mark sits top-right, same inset.

WHY THE BAND IS 430px AND NOT THE BRIEF'S 340px
The brief sized its band for a one- or two-word place name. These covers carry
a full hook sentence in the display serif — that is the whole point of the
cover — so the band grew by 90px to fit three lines of it plus the stat grid.
Illustration height came down to match. Everything else follows the brief.

TYPE SIZES ARE SCALED UP FROM THE BRIEF
The brief's 11-12px labels were written for a poster viewed large. A 1080px
slide is seen about 400px wide in the Instagram feed, where 12px renders at
roughly 4px and disappears. Labels are therefore 20-26px here, which is the
same relationship to the frame that the brief's sizes had to a poster.

DEPTH RULES (from the brief, do not relax them)
  * 4-6 stacked planes, back to front, each one flat-filled.
  * Lightness steps monotonically plane to plane, so depth reads with no
    outlines anywhere.
  * One low-opacity haze band at each major plane junction.
  * Gradients only for sky, haze and light sources. Never as decoration.
  * Every major form gets a lit face and a shadow face as two separate paths.
  * Exactly one human-scale element per cover, small, off-centre, silhouetted.

PALETTES
5-7 flats derived from the subject itself — never a house palette. One ground,
one warm family, one cool family, one accent, chroma consistent across accents.
Band ink is the darkest plane colour pushed darker still.

Add a post by adding a POSTERS entry: archetype, palette, scale element. The
hook, kicker, region label and stats are derived from the post's own slides by
poster_from_spec(), so no figure is ever retyped or invented here.
"""

import json
import math
import pathlib
import re

W, H = 1080, 1350
ART_H = 920
BAND_H = H - ART_H          # 430

ROOT = pathlib.Path(__file__).resolve().parent


# --------------------------------------------------------------------------
# deterministic jitter — same slug always draws the same cover
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


def seed_of(slug):
    n = 7
    for ch in slug:
        n = (n * 131 + ord(ch)) & 0x7FFFFFFF
    return n


# --------------------------------------------------------------------------
# colour
# --------------------------------------------------------------------------

def _rgb(c):
    c = c.lstrip("#")
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
    """Band ink = darkest colour in the illustration, pushed darker."""
    darkest = min(pal["planes"] + list(pal["sky"]), key=lum)
    ink = shade(darkest, 0.42)
    # keep it a true ink, never a muddy mid-tone
    while lum(ink) > 34:
        ink = shade(ink, 0.8)
    return ink


# --------------------------------------------------------------------------
# geometry
# --------------------------------------------------------------------------

def fill_below(pts, base=ART_H):
    """Polyline across the frame, filled down to `base`. One flat plane."""
    d = "M %.1f %.1f" % (pts[0][0], pts[0][1])
    for x, y in pts[1:]:
        d += " L %.1f %.1f" % (x, y)
    d += " L %.1f %.1f L %.1f %.1f Z" % (pts[-1][0], base, pts[0][0], base)
    return d


def smooth_below(pts, base=ART_H):
    """Same, but a gentle curve through the points instead of hard angles."""
    d = "M %.1f %.1f" % (pts[0][0], pts[0][1])
    for i in range(1, len(pts)):
        x0, y0 = pts[i - 1]
        x1, y1 = pts[i]
        mx = (x0 + x1) / 2
        d += " Q %.1f %.1f %.1f %.1f" % (mx, y0, mx, (y0 + y1) / 2)
        d += " Q %.1f %.1f %.1f %.1f" % (mx, y1, x1, y1)
    d += " L %.1f %.1f L %.1f %.1f Z" % (pts[-1][0], base, pts[0][0], base)
    return d


def ridge(rnd, y, amp, n=7, x0=-40, x1=W + 40):
    """A jagged ridge line: n points, vertical jitter of `amp`."""
    out = []
    for k in range(n + 1):
        x = x0 + (x1 - x0) * k / n
        out.append((x, y + rnd.f(-amp, amp)))
    return out


def peaks(rnd, base_y, count, lo, hi, profile="alpine"):
    """A far-plane skyline. Returns (polyline, apex list).

    `profile` is what stops the set looking templated. Six archetypes use this
    function for their backmost plane, and when they all drew the same sharp
    triangles, 32 of 70 covers shared a silhouette — invisible post by post in
    the feed, obvious the moment you see the profile grid. Each archetype now
    picks the landform its subject actually has:

        alpine   sharp asymmetric peaks         mountains
        rounded  soft domes, worn down          forest valleys
        plateau  flat tops, steep sides         steppe, terraces
        tabular  ice shelf: vertical and flat   ice
        ridge    one long undulating crest      lakeshores

    Widths vary and apexes sit off-centre in their own segment whatever the
    profile, so no two peaks are the same shape either.
    """
    pts = [(-40, base_y)]
    apex = []
    shares = [rnd.f(0.55, 1.7) for _ in range(count)]
    total = (W + 80) / sum(shares)
    x = -40
    biggest = max(shares)
    for sh in shares:
        wd = total * sh
        h = rnd.f(lo, hi) * (0.68 + 0.42 * sh / biggest)
        ax = x + wd * rnd.f(0.3, 0.7)
        ay = base_y - h

        if profile == "rounded":
            for k in range(1, 13):
                tt = k / 13.0
                pts.append((x + wd * tt,
                            base_y - h * math.sin(math.pi * tt) ** 0.72))
            ax, ay = x + wd * 0.5, base_y - h
        elif profile == "plateau":
            cap = wd * rnd.f(0.2, 0.4)
            pts.append((ax - cap, ay + rnd.f(2, 14)))
            pts.append((ax + cap, ay))
        elif profile == "tabular":
            cap = wd * rnd.f(0.28, 0.46)
            pts.append((ax - cap, base_y))
            pts.append((ax - cap, ay))
            pts.append((ax + cap, ay + rnd.f(-7, 7)))
            pts.append((ax + cap, base_y))
        elif profile == "ridge":
            for k in range(1, 8):
                tt = k / 8.0
                pts.append((x + wd * tt,
                            base_y - h * (0.42 + 0.58 * math.sin(math.pi * tt))
                            * rnd.f(0.82, 1.08)))
            ax, ay = x + wd * 0.5, base_y - h * 0.82
        else:                                        # alpine
            pts.append((ax, ay))

        apex.append((ax, ay))
        x += wd
        if profile != "tabular":
            pts.append((x, base_y - rnd.f(0, 34)))
    pts.append((W + 40, base_y))
    return pts, apex


def haze(y, h, colour, op=0.22, tag="h"):
    """One low-opacity band where two planes meet, to push the back one back."""
    gid = "hz%s%d" % (tag, int(y))
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{colour}" stop-opacity="0"/>'
        f'<stop offset="0.45" stop-color="{colour}" stop-opacity="{op}"/>'
        f'<stop offset="1" stop-color="{colour}" stop-opacity="0"/>'
        f'</linearGradient>',
        f'<rect x="0" y="{y - h / 2:.0f}" width="{W}" height="{h:.0f}" fill="url(#{gid})"/>',
    )


def sky(pal, rnd, light=None, chance=0.64):
    """Sky gradient plus, optionally, one light source. The only decoration."""
    top, bot = pal["sky"]
    defs = (
        '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{top}"/>'
        f'<stop offset="1" stop-color="{bot}"/>'
        "</linearGradient>"
    )
    body = f'<rect x="0" y="0" width="{W}" height="{ART_H}" fill="url(#sky)"/>'
    # Not every scene gets a sun. One on all 70 covers is itself a template,
    # and an overcast fjord or a forest under flat light is a better picture.
    if light and rnd.next() < chance:
        cx, cy, r = light
        # The disc carries only a hint of the accent. Straight accent gives a
        # mint-green or teal sun whenever the palette's accent is a cool one,
        # which reads as a mistake rather than a light source.
        disc = mix(pal["accent"], "#FFF4E2", 0.55)
        defs += (
            '<radialGradient id="glow">'
            f'<stop offset="0" stop-color="{disc}" stop-opacity="0.8"/>'
            f'<stop offset="0.5" stop-color="{pal["accent"]}" stop-opacity="0.2"/>'
            f'<stop offset="1" stop-color="{pal["accent"]}" stop-opacity="0"/>'
            "</radialGradient>"
        )
        body += f'<circle cx="{cx}" cy="{cy}" r="{r * 3.4:.0f}" fill="url(#glow)"/>'
        body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{disc}"/>'
    return defs, body


# --------------------------------------------------------------------------
# the one human-scale element
# --------------------------------------------------------------------------

def scale_el(kind, x, y, s, colour):
    """A small silhouette for scale and narrative. y is its ground line."""
    def P(d):
        return (f'<g transform="translate({x:.0f},{y:.0f}) scale({s:.3f})">'
                f'<path d="{d}" fill="{colour}"/></g>')

    if kind == "house":
        return P("M-26 0 L-26 -30 L0 -52 L26 -30 L26 0 Z")
    if kind == "church":
        return P("M-30 0 L-30 -34 L0 -56 L30 -34 L30 0 Z M-4 -56 L-4 -86 L4 -86 L4 -56 Z"
                 " M-12 -86 L12 -86 L12 -80 L-12 -80 Z")
    if kind == "lighthouse":
        return P("M-16 0 L-11 -62 L11 -62 L16 0 Z M-16 -62 L16 -62 L16 -72 L-16 -72 Z"
                 " M-9 -72 L9 -72 L9 -92 L-9 -92 Z M-14 -92 L14 -92 L0 -106 Z")
    if kind == "boat":
        return P("M-40 0 Q0 16 40 0 Z M-2 0 L-2 -54 L2 -54 L2 0 Z"
                 " M2 -50 L34 -14 L2 -14 Z")
    if kind == "tower":
        return P("M-18 0 L-10 -78 L10 -78 L18 0 Z M-14 -78 L14 -78 L0 -104 Z")
    if kind == "pagoda":
        return P("M-8 0 L-8 -58 L8 -58 L8 0 Z M-34 -54 L34 -54 L24 -66 L-24 -66 Z"
                 " M-26 -66 L26 -66 L18 -78 L-18 -78 Z M-18 -78 L18 -78 L0 -96 Z")
    if kind == "stupa":
        return P("M-30 0 L-30 -12 L30 -12 L30 0 Z M-22 -12 Q0 -70 22 -12 Z"
                 " M-3 -66 L-3 -92 L3 -92 L3 -66 Z")
    if kind == "dome":
        return P("M-34 0 L-34 -16 L34 -16 L34 0 Z M-24 -16 Q0 -74 24 -16 Z"
                 " M-2 -70 L-2 -88 L2 -88 L2 -70 Z")
    if kind == "tent":
        return P("M-30 0 L0 -44 L30 0 Z")
    if kind == "fence":
        return P("M-56 0 L-56 -26 L-50 -26 L-50 0 Z M-26 0 L-26 -30 L-20 -30 L-20 0 Z"
                 " M4 0 L4 -30 L10 -30 L10 0 Z M34 0 L34 -26 L40 -26 L40 0 Z"
                 " M-58 -22 L42 -26 L42 -20 L-58 -16 Z")
    if kind == "bridge":
        return P("M-70 0 L-70 -8 L70 -8 L70 0 Z M-70 -8 Q0 -62 70 -8 Z"
                 " M-40 -8 L-40 -34 L-34 -34 L-34 -8 Z M34 -8 L34 -34 L40 -34 L40 -8 Z")
    if kind == "train":
        return P("M-62 0 L-62 -26 L18 -26 L18 0 Z M20 0 L20 -34 L62 -34 L62 0 Z"
                 " M44 -34 L52 -34 L52 -48 L44 -48 Z")
    if kind == "cablecar":
        return P("M-70 -96 L70 -70 L70 -66 L-70 -92 Z M-10 -80 L-10 -62 L-6 -62 L-6 -80 Z"
                 " M-34 -62 L22 -52 L22 -16 L-34 -26 Z")
    if kind == "windmill":
        return P("M-18 0 L-12 -58 L12 -58 L18 0 Z M-2 -58 L2 -58 L2 -74 L-2 -74 Z"
                 " M0 -74 L52 -92 L54 -84 L2 -66 Z M0 -74 L-52 -56 L-54 -64 L-2 -82 Z")
    if kind == "hut":
        return P("M-24 0 L-24 -18 L24 -18 L24 0 Z M-32 -18 L32 -18 L0 -50 Z")
    if kind == "gate":          # torii
        return P("M-40 0 L-32 -62 L-24 -62 L-30 0 Z M24 0 L30 -62 L38 -62 L40 0 Z"
                 " M-44 -62 L44 -62 L44 -54 L-44 -54 Z M-38 -74 L38 -74 L38 -66 L-38 -66 Z")
    if kind == "rig":           # small jetty / platform
        return P("M-56 0 L-56 -6 L56 -6 L56 0 Z M-44 -6 L-38 -40 L-32 -40 L-36 -6 Z"
                 " M34 -6 L30 -40 L36 -40 L42 -6 Z M-50 -40 L50 -40 L50 -32 L-50 -32 Z")
    return P("M-26 0 L-26 -30 L0 -52 L26 -30 L26 0 Z")


# --------------------------------------------------------------------------
# archetypes — each returns inner SVG markup for the illustration
# --------------------------------------------------------------------------

def _wrap(defs, body):
    return (f'<svg class="art" viewBox="0 0 {W} {ART_H}" width="{W}" height="{ART_H}" '
            f'xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">'
            f'<defs>{defs}</defs>{body}</svg>')


def a_mountains(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(140, 940), rnd.f(140, 250), 30))
    far, fapex = peaks(rnd, 560, 5, 150, 250)
    b += f'<path d="{fill_below(far)}" fill="{p[0]}"/>'
    for ax, ay in fapex:                                  # shadow faces
        b += (f'<path d="{fill_below([(ax, ay), (ax + 90, 560)], 560)}" '
              f'fill="{shade(p[0], 0.88)}"/>')
    hd, hb = haze(560, 150, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    mid, mapex = peaks(rnd, 700, 4, 170, 280)
    b += f'<path d="{fill_below(mid)}" fill="{p[1]}"/>'
    for ax, ay in mapex:
        b += (f'<path d="{fill_below([(ax, ay), (ax + 120, 700)], 700)}" '
              f'fill="{shade(p[1], 0.84)}"/>')
    hd, hb = haze(700, 110, pal["sky"][1], 0.2, "b")
    d += hd
    b += hb
    b += f'<path d="{smooth_below(ridge(rnd, 790, 22, 6))}" fill="{p[2]}"/>'
    b += f'<path d="{smooth_below(ridge(rnd, 862, 16, 5))}" fill="{p[3]}"/>'
    b += scale_el(el, rnd.f(200, 330), 852, rnd.f(0.62, 0.8), shade(p[4], 0.6))
    b += f'<path d="{smooth_below(ridge(rnd, 902, 10, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_coast_cliff(pal, rnd, el):
    """Headlands standing in the sea, seen along the coast.

    The sea is derived from the sky rather than taken from the plane ramp. The
    ramp's middle planes carry the warm family, so using one of them as water
    gives a sand-coloured sea and the headlands read as boxes floating on a
    desert. Water has to be explicitly cool and explicitly darker than the sky
    it reflects.
    """
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(150, 930), rnd.f(150, 250), 26))
    b += f'<path d="{smooth_below(ridge(rnd, 512, 12, 5))}" fill="{p[0]}"/>'
    hd, hb = haze(518, 120, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    sea = mix(pal["sky"][1], p[4], 0.58)
    sea_y = 596
    b += f'<rect x="0" y="{sea_y}" width="{W}" height="{ART_H - sea_y}" fill="{sea}"/>'

    # promontories, back to front. Each runs well below the waterline and is
    # cut off by the nearer water plane, which is what puts it *in* the sea.
    for i, (cx, top, wd, col) in enumerate([
            (rnd.f(40, 260), rnd.f(548, 586), rnd.f(300, 420), p[1]),
            (rnd.f(600, 880), rnd.f(590, 640), rnd.f(340, 460), p[2]),
            (rnd.f(180, 520), rnd.f(650, 700), rnd.f(380, 520), p[3])]):
        foot = sea_y + 150 + i * 70
        b += (f'<path d="M{cx - wd / 2:.0f} {foot} L{cx - wd / 2 + 26:.0f} {top + 30:.0f} '
              f'Q{cx - wd * 0.18:.0f} {top - 20:.0f} {cx + wd * 0.1:.0f} {top:.0f} '
              f'Q{cx + wd * 0.38:.0f} {top + 22:.0f} {cx + wd / 2:.0f} {foot} Z" '
              f'fill="{col}"/>')
        b += (f'<path d="M{cx + wd * 0.1:.0f} {top:.0f} '
              f'Q{cx + wd * 0.38:.0f} {top + 22:.0f} {cx + wd / 2:.0f} {foot} '
              f'L{cx + wd * 0.1:.0f} {foot} Z" fill="{shade(col, 0.78)}"/>')
        b += (f'<rect x="0" y="{sea_y + 92 + i * 74:.0f}" width="{W}" '
              f'height="{ART_H:.0f}" fill="{shade(sea, 0.9 - i * 0.07)}"/>')

    # the near cliff the viewer is standing on, bottom-left, holding the mark
    cliff_y = 820
    b += (f'<path d="M-40 {ART_H} L-40 {cliff_y:.0f} '
          f'Q{rnd.f(180, 320):.0f} {cliff_y - 36:.0f} {rnd.f(430, 560):.0f} '
          f'{cliff_y + 40:.0f} L{rnd.f(430, 560):.0f} {ART_H} Z" fill="{p[4]}"/>')
    b += scale_el(el, rnd.f(150, 330), cliff_y - 4, rnd.f(0.5, 0.64),
                  shade(p[4], 0.58))
    return _wrap(d, b)


def a_volcano(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(130, 950), rnd.f(150, 260), 28))
    b += f'<path d="{smooth_below(ridge(rnd, 600, 18, 5))}" fill="{p[0]}"/>'
    # A cone that fills the frame reads as a pyramid, not a mountain. Keep it
    # set back, with ridges either side and ground in front of it.
    cx = rnd.f(380, 700)
    apex, base = rnd.f(352, 418), 726
    hw = rnd.f(190, 260)
    # Concave flanks. Straight ones give a pyramid; the inward sweep from base
    # to crater is what makes a cone read as a volcano at a glance.
    rim, sweep = 46, (base - apex) * 0.38
    b += (f'<path d="M{cx - hw:.0f} {base} '
          f'Q{cx - hw * 0.42:.0f} {apex + sweep:.0f} {cx - rim:.0f} {apex:.0f} '
          f'L{cx + rim:.0f} {apex:.0f} '
          f'Q{cx + hw * 0.42:.0f} {apex + sweep:.0f} {cx + hw:.0f} {base} Z" '
          f'fill="{p[1]}"/>')
    b += (f'<path d="M{cx + 8:.0f} {apex + 2:.0f} L{cx + rim:.0f} {apex:.0f} '
          f'Q{cx + hw * 0.42:.0f} {apex + sweep:.0f} {cx + hw:.0f} {base} '
          f'L{cx + 24:.0f} {base} Z" fill="{shade(p[1], 0.8)}"/>')
    b += (f'<path d="M{cx - rim:.0f} {apex:.0f} L{cx + rim:.0f} {apex:.0f} '
          f'L{cx + 22:.0f} {apex + 18:.0f} L{cx - 22:.0f} {apex + 18:.0f} Z" '
          f'fill="{shade(p[1], 0.62)}"/>')
    # No ash plume. It only works as a soft gradient, and the brief allows
    # gradients for sky, haze and light sources — not as decoration. Drawn as
    # a flat shape it reads as a chimney stack sitting on the summit.
    hd, hb = haze(740, 120, pal["sky"][1], 0.24, "a")
    d += hd
    b += hb
    b += f'<path d="{smooth_below(ridge(rnd, 800, 14, 5))}" fill="{p[2]}"/>'
    b += scale_el(el, rnd.f(170, 300), 846, rnd.f(0.56, 0.7), shade(p[4], 0.58))
    b += f'<path d="{smooth_below(ridge(rnd, 860, 12, 5))}" fill="{p[3]}"/>'
    b += f'<path d="{smooth_below(ridge(rnd, 904, 8, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_islands(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(160, 300), rnd.f(160, 220), 24))
    b += f'<rect x="0" y="540" width="{W}" height="{ART_H - 540}" fill="{p[0]}"/>'
    hd, hb = haze(540, 130, pal["sky"][1], 0.28, "a")
    d += hd
    b += hb
    rows = [(560, 0.42, p[1]), (650, 0.62, p[2]), (760, 0.9, p[3])]
    for k, (y, sc, col) in enumerate(rows):
        n = 4 - k
        for j in range(n):
            cx = rnd.f(-40, W + 40)
            hw = rnd.f(130, 260) * sc
            ht = rnd.f(60, 130) * sc
            b += (f'<path d="M{cx - hw:.0f} {y} Q{cx - hw * 0.35:.0f} {y - ht:.0f} '
                  f'{cx:.0f} {y - ht:.0f} Q{cx + hw * 0.5:.0f} {y - ht * 0.9:.0f} '
                  f'{cx + hw:.0f} {y} Z" fill="{col}"/>')
            b += (f'<path d="M{cx:.0f} {y - ht:.0f} Q{cx + hw * 0.5:.0f} '
                  f'{y - ht * 0.9:.0f} {cx + hw:.0f} {y} L{cx:.0f} {y} Z" '
                  f'fill="{shade(col, 0.82)}"/>')
        b += f'<rect x="0" y="{y}" width="{W}" height="{ART_H - y}" fill="{p[k + 1]}"/>'
    b += scale_el(el, rnd.f(220, 400), 798, rnd.f(0.5, 0.62), shade(p[4], 0.6))
    b += f'<path d="{smooth_below(ridge(rnd, 856, 10, 5))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_dunes(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(680, 860), rnd.f(180, 260), 32))
    b += f'<path d="{smooth_below(ridge(rnd, 560, 10, 4))}" fill="{p[0]}"/>'
    hd, hb = haze(560, 140, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    for i, y in enumerate([620, 700, 790, 880]):
        crest = rnd.f(0.3, 0.7)
        pts = [(-40, y + 30), (W * crest, y - rnd.f(40, 80)), (W + 40, y + 40)]
        b += f'<path d="{smooth_below(pts)}" fill="{p[min(i + 1, 4)]}"/>'
        cx = W * crest
        b += (f'<path d="M{cx:.0f} {y - 60:.0f} Q{cx + 220:.0f} {y - 10:.0f} '
              f'{W + 40} {y + 40} L{W + 40} {ART_H} L{cx:.0f} {ART_H} Z" '
              f'fill="{shade(p[min(i + 1, 4)], 0.88)}"/>')
    b += scale_el(el, rnd.f(200, 340), 836, rnd.f(0.5, 0.62), shade(p[4], 0.56))
    return _wrap(d, b)


def a_steppe(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(200, 880), rnd.f(150, 220), 26))
    far, fapex = peaks(rnd, 560, 6, 70, 140, "plateau")
    b += f'<path d="{fill_below(far)}" fill="{p[0]}"/>'
    for ax, ay in fapex:
        b += (f'<path d="{fill_below([(ax, ay), (ax + 70, 560)], 560)}" '
              f'fill="{shade(p[0], 0.9)}"/>')
    hd, hb = haze(560, 130, pal["sky"][1], 0.26, "a")
    d += hd
    b += hb
    for i, y in enumerate([640, 730, 820, 890]):
        b += f'<path d="{smooth_below(ridge(rnd, y, 18, 5))}" fill="{p[min(i + 1, 4)]}"/>'
    b += scale_el(el, rnd.f(620, 820), 812, rnd.f(0.54, 0.68), shade(p[4], 0.56))
    return _wrap(d, b)


def a_forest_valley(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(220, 860), rnd.f(150, 210), 24))
    far, fapex = peaks(rnd, 540, 4, 130, 220, "rounded")
    b += f'<path d="{fill_below(far)}" fill="{p[0]}"/>'
    for ax, ay in fapex:
        b += (f'<path d="{fill_below([(ax, ay), (ax + 100, 540)], 540)}" '
              f'fill="{shade(p[0], 0.88)}"/>')
    hd, hb = haze(545, 140, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb

    def trees(y, step, ht, col):
        s = f'<path d="{smooth_below(ridge(rnd, y, 12, 5))}" fill="{col}"/>'
        x = -30
        while x < W + 30:
            h = ht * rnd.f(0.7, 1.25)
            w = h * 0.3
            s += (f'<path d="M{x - w:.0f} {y + 6:.0f} L{x:.0f} {y - h:.0f} '
                  f'L{x + w:.0f} {y + 6:.0f} Z" fill="{col}"/>')
            x += step * rnd.f(0.7, 1.3)
        return s

    b += trees(660, 34, 60, p[1])
    b += trees(760, 44, 84, p[2])
    b += scale_el(el, rnd.f(170, 330), 826, rnd.f(0.56, 0.7), shade(p[4], 0.54))
    b += trees(862, 58, 110, p[3])
    b += f'<path d="{smooth_below(ridge(rnd, 908, 8, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_fjord(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(400, 700), rnd.f(140, 200), 22))
    b += f'<path d="{smooth_below(ridge(rnd, 500, 14, 5))}" fill="{p[0]}"/>'
    hd, hb = haze(505, 120, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    # the inlet: water first, then walls stepping in from each side over it.
    # Drawing the walls as two triangles meeting in the middle left a seam
    # down the centre that read as a crack, not a channel.
    water = mix(pal["sky"][1], p[4], 0.52)
    b += f'<rect x="0" y="560" width="{W}" height="{ART_H - 560}" fill="{water}"/>'
    far_gap = rnd.f(150, 240)
    for i, (side, col) in enumerate(((-1, p[1]), (1, p[2]), (-1, p[3]))):
        reach = far_gap + rnd.f(120, 260) + i * 150
        x_edge = -40 if side < 0 else W + 40
        inner = x_edge + side * -1 * reach if side < 0 else x_edge - reach
        top = 470 + i * 60 + rnd.f(-30, 30)
        foot = 700 + i * 80
        b += (f'<path d="M{x_edge} {ART_H} L{x_edge} {top:.0f} '
              f'Q{(x_edge + inner) / 2:.0f} {top + 30:.0f} {inner:.0f} {foot:.0f} '
              f'L{inner:.0f} {ART_H} Z" fill="{col}"/>')
        # shadow face: the wall's water side, where the light does not reach
        b += (f'<path d="M{inner - side * 70:.0f} {foot - 60:.0f} '
              f'Q{inner - side * 20:.0f} {foot - 20:.0f} {inner:.0f} {foot:.0f} '
              f'L{inner:.0f} {ART_H} L{inner - side * 70:.0f} {ART_H} Z" '
              f'fill="{shade(col, 0.76)}"/>')
    b += scale_el(el, W / 2 + rnd.f(-60, 90), 848, rnd.f(0.4, 0.5), shade(p[4], 0.62))
    b += f'<path d="{smooth_below(ridge(rnd, 886, 8, 5))}" fill="{shade(water, 0.82)}"/>'
    return _wrap(d, b)


def a_ice(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(200, 900), rnd.f(140, 200), 26))
    far, fapex = peaks(rnd, 530, 5, 90, 180, "tabular")
    b += f'<path d="{fill_below(far)}" fill="{p[0]}"/>'
    for ax, ay in fapex:
        b += (f'<path d="{fill_below([(ax, ay), (ax + 80, 530)], 530)}" '
              f'fill="{shade(p[0], 0.9)}"/>')
    hd, hb = haze(535, 140, pal["sky"][1], 0.32, "a")
    d += hd
    b += hb
    b += f'<rect x="0" y="640" width="{W}" height="{ART_H - 640}" fill="{p[1]}"/>'
    for i in range(5):                                    # tabular bergs
        cx = rnd.f(-30, W + 30)
        wd = rnd.f(110, 230)
        ht = rnd.f(50, 120)
        y = rnd.f(660, 780)
        b += (f'<path d="M{cx - wd / 2:.0f} {y} L{cx - wd / 2 + 16:.0f} {y - ht:.0f} '
              f'L{cx + wd / 2 - 24:.0f} {y - ht * 0.82:.0f} L{cx + wd / 2:.0f} {y} Z" '
              f'fill="{p[2]}"/>')
        b += (f'<path d="M{cx + 6:.0f} {y - ht * 0.9:.0f} '
              f'L{cx + wd / 2 - 24:.0f} {y - ht * 0.82:.0f} '
              f'L{cx + wd / 2:.0f} {y} L{cx + 6:.0f} {y} Z" fill="{shade(p[2], 0.82)}"/>')
    b += f'<path d="{smooth_below(ridge(rnd, 824, 10, 5))}" fill="{p[3]}"/>'
    b += scale_el(el, rnd.f(240, 420), 868, rnd.f(0.46, 0.58), shade(p[4], 0.62))
    b += f'<path d="{smooth_below(ridge(rnd, 894, 8, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_delta(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(640, 880), rnd.f(170, 240), 30))
    b += f'<path d="{smooth_below(ridge(rnd, 560, 12, 5))}" fill="{p[0]}"/>'
    hd, hb = haze(565, 130, pal["sky"][1], 0.28, "a")
    d += hd
    b += hb
    b += f'<rect x="0" y="620" width="{W}" height="{ART_H - 620}" fill="{p[1]}"/>'
    # braided water channels widening toward the viewer
    for i in range(3):
        x = rnd.f(120, 900)
        wtop = rnd.f(16, 34)
        wbot = wtop * rnd.f(3.0, 5.0)
        b += (f'<path d="M{x - wtop / 2:.0f} 620 L{x + wtop / 2:.0f} 620 '
              f'L{x + wbot / 2 + rnd.f(-70, 70):.0f} {ART_H} '
              f'L{x - wbot / 2 + rnd.f(-70, 70):.0f} {ART_H} Z" fill="{p[2]}"/>')
    for i, y in enumerate([720, 800, 876]):
        b += (f'<path d="{smooth_below(ridge(rnd, y, 14, 6))}" fill="{p[3] if i < 2 else p[4]}" '
              f'opacity="{0.9 if i < 2 else 1}"/>')
    b += scale_el(el, rnd.f(640, 840), 790, rnd.f(0.5, 0.62), shade(p[4], 0.56))
    return _wrap(d, b)


def a_skyline(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(200, 880), rnd.f(150, 230), 28))
    b += f'<path d="{smooth_below(ridge(rnd, 560, 16, 5))}" fill="{p[0]}"/>'
    hd, hb = haze(565, 130, pal["sky"][1], 0.26, "a")
    d += hd
    b += hb

    def blocks(y, col, lo, hi, wlo, whi):
        s = ""
        x = -30
        while x < W + 30:
            wd = rnd.f(wlo, whi)
            ht = rnd.f(lo, hi)
            s += f'<rect x="{x:.0f}" y="{y - ht:.0f}" width="{wd:.0f}" height="{ht:.0f}" fill="{col}"/>'
            s += (f'<rect x="{x + wd * 0.64:.0f}" y="{y - ht:.0f}" '
                  f'width="{wd * 0.36:.0f}" height="{ht:.0f}" fill="{shade(col, 0.84)}"/>')
            x += wd + rnd.f(4, 16)
        return s + f'<rect x="0" y="{y}" width="{W}" height="{ART_H - y}" fill="{col}"/>'

    b += blocks(700, p[1], 90, 230, 40, 86)
    b += blocks(800, p[2], 80, 190, 50, 100)
    b += scale_el(el, rnd.f(170, 330), 846, rnd.f(0.5, 0.62), shade(p[4], 0.58))
    b += blocks(880, p[3], 50, 120, 60, 120)
    b += f'<rect x="0" y="902" width="{W}" height="{ART_H - 902}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_swell(pal, rnd, el):
    """Open ocean: ranks of swell receding to the horizon, one breaking near.

    Built as swell lines rather than a single hero wave. A lone wave drawn in
    flat planes reads as a hill; a rank of crests with foam along each top edge
    reads unmistakably as sea.
    """
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(180, 320), rnd.f(150, 220), 26))
    b += f'<path d="{smooth_below(ridge(rnd, 500, 8, 4))}" fill="{p[0]}"/>'
    hd, hb = haze(506, 110, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    b += f'<rect x="0" y="548" width="{W}" height="{ART_H - 548}" fill="{p[1]}"/>'

    def swell(y, amp, col, foam_h, phase):
        """One rank: a shallow arc filled below, with a foam lip on its edge."""
        top = (f"M-40 {y + amp:.0f} "
               f"Q{W * 0.22:.0f} {y - amp:.0f} {W * 0.48 + phase:.0f} {y:.0f} "
               f"Q{W * 0.78:.0f} {y + amp * 1.6:.0f} {W + 40} {y - amp * 0.4:.0f}")
        s = f'<path d="{top} L{W + 40} {ART_H} L-40 {ART_H} Z" fill="{col}"/>'
        s += (f'<path d="{top} L{W + 40} {y - amp * 0.4 + foam_h:.0f} '
              f'Q{W * 0.78:.0f} {y + amp * 1.6 + foam_h:.0f} '
              f'{W * 0.48 + phase:.0f} {y + foam_h:.0f} '
              f'Q{W * 0.22:.0f} {y - amp + foam_h:.0f} -40 {y + amp + foam_h:.0f} Z" '
              f'fill="{shade(col, 1.45)}"/>')
        return s

    b += swell(606, 14, p[1], 7, rnd.f(-150, 150))
    b += swell(672, 20, p[2], 10, rnd.f(-150, 150))
    b += scale_el(el, rnd.f(150, 330), 700, rnd.f(0.34, 0.44), shade(p[4], 0.66))

    # the near breaker: body, curling lip, and the shadowed hollow beneath it
    cx = rnd.f(400, 700)
    crest = 790
    body = (f"M-40 {crest + 130:.0f} Q{cx - 280:.0f} {crest + 20:.0f} "
            f"{cx:.0f} {crest:.0f} Q{cx + 190:.0f} {crest - 8:.0f} "
            f"{W + 40} {crest + 120:.0f}")
    b += f'<path d="{body} L{W + 40} {ART_H} L-40 {ART_H} Z" fill="{p[3]}"/>'
    # shadow face: everything right of the crest, down to the frame edge
    b += (f'<path d="M{cx:.0f} {crest:.0f} Q{cx + 190:.0f} {crest - 8:.0f} '
          f'{W + 40} {crest + 120:.0f} L{W + 40} {ART_H} L{cx:.0f} {ART_H} Z" '
          f'fill="{shade(p[3], 0.8)}"/>')
    b += (f'<path d="{body} L{W + 40} {crest + 134:.0f} '
          f'Q{cx + 190:.0f} {crest + 6:.0f} {cx:.0f} {crest + 15:.0f} '
          f'Q{cx - 280:.0f} {crest + 35:.0f} -40 {crest + 146:.0f} Z" '
          f'fill="{shade(p[3], 1.5)}"/>')
    b += f'<path d="{smooth_below(ridge(rnd, 900, 10, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_savanna(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(700, 900), rnd.f(180, 260), 34))
    b += f'<path d="{smooth_below(ridge(rnd, 560, 10, 4))}" fill="{p[0]}"/>'
    hd, hb = haze(565, 140, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    # flat-topped escarpment, lit face and shadow face
    ex, ew, et = rnd.f(560, 800), rnd.f(300, 440), rnd.f(590, 640)
    b += (f'<path d="M{ex - ew / 2:.0f} 700 L{ex - ew / 2 + 50:.0f} {et:.0f} '
          f'L{ex + ew / 2 - 30:.0f} {et - 12:.0f} L{ex + ew / 2:.0f} 700 Z" fill="{p[1]}"/>')
    b += (f'<path d="M{ex + ew / 2 - 110:.0f} {et - 8:.0f} L{ex + ew / 2 - 30:.0f} '
          f'{et - 12:.0f} L{ex + ew / 2:.0f} 700 L{ex + ew / 2 - 110:.0f} 700 Z" '
          f'fill="{shade(p[1], 0.8)}"/>')
    b += f'<path d="{smooth_below(ridge(rnd, 712, 14, 5))}" fill="{p[2]}"/>'

    def acacia(x, y, s, col):
        return (f'<g transform="translate({x:.0f},{y:.0f}) scale({s:.2f})">'
                f'<path d="M-4 0 L-7 -70 L7 -70 L4 0 Z" fill="{col}"/>'
                f'<path d="M-78 -74 Q0 -112 78 -74 Q0 -92 -78 -74 Z" fill="{col}"/></g>')

    b += acacia(rnd.f(120, 300), 792, rnd.f(0.8, 1.05), p[3])
    b += f'<path d="{smooth_below(ridge(rnd, 800, 12, 5))}" fill="{p[3]}"/>'
    b += acacia(rnd.f(700, 940), 884, rnd.f(1.0, 1.3), shade(p[4], 0.7))
    b += scale_el(el, rnd.f(260, 420), 880, rnd.f(0.5, 0.62), shade(p[4], 0.56))
    b += f'<path d="{smooth_below(ridge(rnd, 892, 10, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_terraces(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(220, 860), rnd.f(150, 220), 24))
    far, fapex = peaks(rnd, 520, 4, 110, 190, "plateau")
    b += f'<path d="{fill_below(far)}" fill="{p[0]}"/>'
    for ax, ay in fapex:
        b += (f'<path d="{fill_below([(ax, ay), (ax + 90, 520)], 520)}" '
              f'fill="{shade(p[0], 0.88)}"/>')
    hd, hb = haze(525, 130, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    y = 600
    for i in range(6):                                    # stepped paddies
        col = p[1 + min(i // 2, 3)]
        h = 44 + i * 9
        bow = rnd.f(26, 54)
        b += (f'<path d="M-40 {y + bow:.0f} Q{W / 2:.0f} {y - bow:.0f} {W + 40} {y + bow:.0f} '
              f'L{W + 40} {y + h + bow:.0f} Q{W / 2:.0f} {y + h - bow:.0f} -40 '
              f'{y + h + bow:.0f} Z" fill="{col}"/>')
        b += (f'<path d="M-40 {y + h + bow - 10:.0f} Q{W / 2:.0f} {y + h - bow - 10:.0f} '
              f'{W + 40} {y + h + bow - 10:.0f} L{W + 40} {y + h + bow:.0f} '
              f'Q{W / 2:.0f} {y + h - bow:.0f} -40 {y + h + bow:.0f} Z" '
              f'fill="{shade(col, 0.82)}"/>')
        y += h
    b += scale_el(el, rnd.f(170, 330), 700, rnd.f(0.42, 0.52), shade(p[4], 0.58))
    return _wrap(d, b)


def a_gorge(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(300, 780), rnd.f(150, 210), 24))
    b += f'<path d="{smooth_below(ridge(rnd, 470, 12, 5))}" fill="{p[0]}"/>'
    hd, hb = haze(475, 120, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    # stepped canyon walls, each step a lit top and a shadowed face
    for i, (col, inset, top) in enumerate([
            (p[1], 0, 500), (p[2], 150, 580), (p[3], 300, 670)]):
        lw = inset + rnd.f(60, 130)
        rw = inset + rnd.f(60, 130)
        b += (f'<path d="M0 {ART_H} L0 {top:.0f} L{lw:.0f} {top + 70:.0f} '
              f'L{lw:.0f} {ART_H} Z" fill="{col}"/>')
        b += (f'<path d="M{lw - 54:.0f} {top + 62:.0f} L{lw:.0f} {top + 70:.0f} '
              f'L{lw:.0f} {ART_H} L{lw - 54:.0f} {ART_H} Z" fill="{shade(col, 0.78)}"/>')
        b += (f'<path d="M{W} {ART_H} L{W} {top + 30:.0f} L{W - rw:.0f} {top + 100:.0f} '
              f'L{W - rw:.0f} {ART_H} Z" fill="{shade(col, 0.9)}"/>')
    b += f'<rect x="0" y="880" width="{W}" height="{ART_H - 880}" fill="{p[4]}"/>'
    b += scale_el(el, W / 2 + rnd.f(-90, 90), 878, rnd.f(0.4, 0.5), shade(p[4], 0.5))
    return _wrap(d, b)


def a_lake(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(220, 860), rnd.f(150, 220), 26))
    far, fapex = peaks(rnd, 560, 5, 120, 210, "ridge")
    b += f'<path d="{fill_below(far)}" fill="{p[0]}"/>'
    for ax, ay in fapex:
        b += (f'<path d="{fill_below([(ax, ay), (ax + 90, 560)], 560)}" '
              f'fill="{shade(p[0], 0.88)}"/>')
    hd, hb = haze(565, 140, pal["sky"][1], 0.3, "a")
    d += hd
    b += hb
    b += f'<path d="{smooth_below(ridge(rnd, 660, 16, 5))}" fill="{p[1]}"/>'
    b += f'<rect x="0" y="720" width="{W}" height="{ART_H - 720}" fill="{p[2]}"/>'
    # reflection: the far range inverted, lighter, as a flat plane
    inv = [(x, 720 + (720 - y) * 0.42) for x, y in reversed(fapex)]
    if len(inv) > 1:
        b += (f'<path d="{fill_below([(-40, 720)] + inv + [(W + 40, 720)], 820)}" '
              f'fill="{shade(p[2], 1.1)}" opacity="0.5"/>')
    b += scale_el(el, rnd.f(180, 340), 714, rnd.f(0.46, 0.58), shade(p[4], 0.58))
    b += f'<path d="{smooth_below(ridge(rnd, 862, 10, 5))}" fill="{p[3]}"/>'
    b += f'<path d="{smooth_below(ridge(rnd, 904, 8, 4))}" fill="{p[4]}"/>'
    return _wrap(d, b)


def a_wetland(pal, rnd, el):
    p = pal["planes"]
    d, b = sky(pal, rnd, (rnd.f(660, 880), rnd.f(170, 250), 30))
    b += f'<path d="{smooth_below(ridge(rnd, 580, 10, 4))}" fill="{p[0]}"/>'
    hd, hb = haze(585, 130, pal["sky"][1], 0.28, "a")
    d += hd
    b += hb
    b += f'<rect x="0" y="640" width="{W}" height="{ART_H - 640}" fill="{p[1]}"/>'
    for i in range(7):                                    # flat islands of reed
        cx = rnd.f(-40, W + 40)
        wd = rnd.f(130, 300)
        y = rnd.f(680, 870)
        b += (f'<path d="M{cx - wd / 2:.0f} {y} Q{cx:.0f} {y - rnd.f(18, 40):.0f} '
              f'{cx + wd / 2:.0f} {y} Q{cx:.0f} {y + 14:.0f} {cx - wd / 2:.0f} {y} Z" '
              f'fill="{p[2 + i % 2]}"/>')
    b += scale_el(el, rnd.f(600, 820), 804, rnd.f(0.46, 0.58), shade(p[4], 0.58))
    b += f'<path d="{smooth_below(ridge(rnd, 884, 10, 5))}" fill="{p[4]}"/>'
    return _wrap(d, b)


ARCHETYPES = {
    "mountains": a_mountains,
    "coast_cliff": a_coast_cliff,
    "volcano": a_volcano,
    "islands": a_islands,
    "dunes": a_dunes,
    "steppe": a_steppe,
    "forest_valley": a_forest_valley,
    "fjord": a_fjord,
    "ice": a_ice,
    "delta": a_delta,
    "skyline": a_skyline,
    "swell": a_swell,
    "savanna": a_savanna,
    "terraces": a_terraces,
    "gorge": a_gorge,
    "lake": a_lake,
    "wetland": a_wetland,
}


# --------------------------------------------------------------------------
# palettes — 5 flats + accent, derived from the subject, never a house palette
# --------------------------------------------------------------------------

def pal(sky_top, sky_bot, p1, p2, p3, p4, p5, accent):
    return {"sky": (sky_top, sky_bot), "planes": [p1, p2, p3, p4, p5],
            "accent": accent}


PALETTES = json.loads((ROOT / "palettes.json").read_text()) \
    if (ROOT / "palettes.json").exists() else {}


# --------------------------------------------------------------------------
# the type band
# --------------------------------------------------------------------------

POSTER_CSS = """
.slide.poster{padding:0;display:block;background:#000}
.poster .art{position:absolute;left:0;top:0;display:block}
.poster .idx{position:absolute;left:72px;top:56px;
  font-family:"Instrument Serif",serif;font-size:40px;line-height:1;
  color:rgba(243,238,228,.92)}
.poster .idx i{display:block;width:40px;height:1px;margin-top:14px;
  background:rgba(243,238,228,.6)}
.poster .brand{position:absolute;right:72px;top:62px;
  font-family:"Archivo",sans-serif;font-weight:600;font-size:20px;
  letter-spacing:.18em;text-transform:uppercase;color:rgba(243,238,228,.72)}
.poster .band{position:absolute;left:0;right:0;bottom:0;height:430px;
  padding:54px 72px 56px;display:flex;flex-direction:column}
.poster .brow{display:flex;align-items:flex-start;justify-content:space-between;gap:30px}
.poster .kick{font-family:"Archivo",sans-serif;font-weight:600;font-size:26px;
  letter-spacing:.22em;text-transform:uppercase}
.poster .region{font-family:"Archivo",sans-serif;font-weight:500;font-size:21px;
  letter-spacing:.14em;text-transform:uppercase;text-align:right;line-height:1.45;
  white-space:pre-line;flex:0 0 auto;max-width:34%}
.poster .disp{font-family:"Instrument Serif",serif;font-weight:400;
  line-height:.9;letter-spacing:-.01em;margin-top:18px}
.poster .rule{height:1px;margin-top:auto}
.poster .stats{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;
  padding-top:26px}
.poster .stat .v{font-family:"Instrument Serif",serif;font-size:40px;line-height:1;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.poster .stat .l{font-family:"Archivo",sans-serif;font-weight:600;font-size:19px;
  letter-spacing:.18em;text-transform:uppercase;margin-top:12px;line-height:1.3}
"""


def _esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def disp_size(text):
    """Largest size from the ladder that keeps the hook to TWO lines.

    Two, not three. The band's 320px of content has to hold the kicker row,
    the hook, the hairline and a stat grid whose labels can run to two lines
    themselves; three lines of display serif only fits when every label is
    short, and a cover that clips its own headline on the one post with long
    labels is not a system. Two lines always fits, so two lines it is.
    """
    n = len(text)
    for size, per_line in ((76, 27), (64, 32), (56, 37), (48, 43)):
        if n <= per_line * 2:
            return size
    return 42


def slide_poster(s, n, total):
    """Builder for slide type `poster`. Registered into build.py's BUILDERS.

    The spec carries only the choices a human made — archetype, palette name,
    scale element — plus the strings derived from the post's other slides. The
    illustration itself is regenerated here, so content/*.json stays small and
    the art is reproducible from the slug.
    """
    p = PALETTES[s["palette"]]
    palette = {"sky": tuple(p["sky"]), "planes": list(p["planes"]),
               "accent": p["accent"]}
    rnd = Rnd(seed_of(s.get("seed") or s.get("kicker", "x")))
    art = ARCHETYPES[s["archetype"]](palette, rnd, s.get("element", "house"))
    ink = band_ink(palette)
    paper = s.get("paper", "#F3EEE4")
    accent = palette["accent"]
    if lum(accent) < 90:                      # keep the kicker legible on ink
        accent = shade(accent, 1.35)
    muted = mix(paper, ink, 0.45)
    rule = mix(paper, ink, 0.72)
    hook = s["hook"]
    size = s.get("size") or disp_size(re.sub("<[^>]+>", "", hook))
    stats = "".join(
        f'<div class="stat"><div class="v">{_esc(v)}</div>'
        f'<div class="l" style="color:{muted}">{_esc(l)}</div></div>'
        for v, l in s["stats"])
    region = _esc(s.get("region", "")).replace(" / ", "\n")
    return f"""<div class="slide poster" id="s{n}">
  {art}
  <div class="idx">{n:02d}<i></i></div>
  <div class="brand">Earth by Numbers</div>
  <div class="band" style="background:{ink};color:{paper}">
    <div class="brow">
      <span class="kick" style="color:{accent}">{_esc(s.get("kicker", ""))}</span>
      <span class="region" style="color:{muted}">{region}</span>
    </div>
    <div class="disp" style="font-size:{size}px">{hook}</div>
    <div class="rule" style="background:{rule}"></div>
    <div class="stats">{stats}</div>
  </div>
</div>"""
