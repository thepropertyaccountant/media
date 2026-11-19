#!/usr/bin/env python3
"""
make_covers.py — convert a post's slide 1 from `hook` to the illustrated
`poster` cover, and write palettes.json for cover.py.

    python3 make_covers.py --palettes          # (re)write palettes.json only
    python3 make_covers.py --list              # show what still needs converting
    python3 make_covers.py --all               # convert every unposted post
    python3 make_covers.py --limit 12          # convert the next 12 only
    python3 make_covers.py <slug> [<slug>...]  # convert named posts

RESUMABLE BY DESIGN. A post whose slide 1 is `hook` has not been converted; one
whose slide 1 is `poster` has. There is no separate progress file to get out of
step with the repo, so a run that stops halfway — on usage, on anything — is
picked up by the next run with `--limit`.

Only unposted posts are touched by `--all`. Posts already on Instagram keep the
covers they went out with; rewriting their images would make the library page
disagree with the live grid for no gain.

WHERE THE COVER'S WORDS COME FROM
Nothing is retyped and no figure is invented here. Per post, a human chooses
three things only — archetype, palette anchors, scale element — in the POSTERS
table below. Everything else is read out of the post's own slides:

  hook     slide 1's existing title, <br> flattened so CSS can wrap it
  kicker   the country (spotlight/crazy) or the No. 1 pick (top5)
  region   the authored region label, or the No. 1 pick's `where` (top5)
  stats    crazy      -> the three bignum slides' number + label
           spotlight  -> three ledger rows, numeric ones preferred
           top5       -> the list's own structure; see TOP5_STATS

The `sub` twist line from the old hook slide is NOT carried onto the cover —
the band has no room for it alongside three lines of display serif and the
stat grid. It is not lost: every caption already opens with the hook and then
the twist, and slide 2 carries the detail.

TOP 5 COVERS illustrate the No. 1 pick, which Felix chose on 19 Nov 2026 over
an adapted variant. The contentious line still runs in the display serif, so
slide 1 keeps picking the fight, but the winner is now visible on the cover.
Top 5 stat columns state no figures at all, because a Top 5 is opinion and
BUILD.md's rule stands: no number appears anywhere without being verified in
the run that uses it.
"""

import json
import pathlib
import re
import sys

import cover

ROOT = pathlib.Path(__file__).resolve().parent
CONTENT = ROOT / "content"

TOP5_STATS = [("05", "places ranked"), ("01", "illustrated above"),
              ("—", "opinion, not fact")]

# --------------------------------------------------------------------------
# POSTERS — the only hand-made choices, one row per post.
#
#   slug: (archetype, element, sky_top, sky_bottom, far, near, warm, accent,
#          region label)
#
# far  = the backmost plane, lightest (atmosphere does the work)
# near = the frontmost plane, darkest; band ink is derived from it
# warm = the warm family the middle planes are tinted toward
# accent = the kicker and any light source; one accent per cover
#
# Colours are picked from the subject — Atlantic greys for Nazaré, laterite
# reds for Rwanda, basalt and ash for Yasur — never from a shared palette.
# --------------------------------------------------------------------------

POSTERS = {
 # ---- Atlantic / ocean
 "top5-surf": ("swell", "boat", "#1B3A4B", "#6E93A6", "#8FAFBD", "#0E2430", "#3E6B78", "#D9E6EA",
               "Nazaré / Portugal"),
 "spot-portugal": ("coast_cliff", "lighthouse", "#2A4C63", "#9FBECA", "#B6CBD2", "#152B36",
                   "#C98A4B", "#E8A33F", "Iberia / Atlantic Europe"),
 "new-zealand-crazy": ("coast_cliff", "lighthouse", "#1E3C4F", "#88AEBC", "#9DBDC4", "#12272F",
                       "#4E7A6A", "#7FD1C0", "Zealandia / South Pacific"),
 "mexico-crazy": ("coast_cliff", "lighthouse", "#2B4A5E", "#A7C4C6", "#BCD2CE", "#17292F",
                  "#C98F56", "#F0B24A", "Yucatán / Gulf of Mexico"),
 "greece-crazy": ("coast_cliff", "church", "#23496B", "#A9C6DA", "#C2D6E0", "#13262F",
                  "#C4A878", "#EFC25C", "Athos / Aegean Sea"),
 "spot-albania": ("coast_cliff", "church", "#245067", "#A2C3CF", "#B9D1D6", "#142A33",
                  "#B98B5A", "#E8A34A", "Balkans / Adriatic and Ionian"),
 "spot-sri-lanka": ("coast_cliff", "stupa", "#1F4A55", "#9CC3BC", "#B3D2C6", "#13282A",
                    "#C98A4B", "#F0B449", "Indian Ocean / South Asia"),
 "top5-ancient-cities": ("coast_cliff", "tower", "#2E4A5C", "#C2BC9E", "#D2CBA8", "#2A2419",
                         "#B9955E", "#E4B75A", "Leptis Magna / Khoms, Libya"),

 # ---- mountains
 "spot-slovenia": ("mountains", "church", "#20405C", "#9FBBCE", "#B9CCD8", "#15272F",
                   "#5E7A66", "#8FD0B6", "Julian Alps / Central Europe"),
 "spot-bhutan": ("mountains", "stupa", "#1C3A5A", "#A7BFD2", "#C1D1DA", "#15242E",
                 "#9A6B4A", "#E0A557", "Eastern Himalaya / South Asia"),
 "kyrgyzstan-crazy": ("mountains", "tent", "#23415C", "#A9BECB", "#C3CFD4", "#1A262C",
                      "#8E7B52", "#DCBB63", "Tian Shan / Central Asia"),
 "spot-ethiopia": ("mountains", "church", "#2C4256", "#B9B193", "#CBC3A2", "#241C17",
                   "#A7612F", "#E08A3C", "Simien / Horn of Africa"),
 "spot-armenia": ("mountains", "church", "#2A4258", "#B3B49F", "#C6C4AA", "#221E1C",
                  "#9E6340", "#E09A4E", "Lesser Caucasus / West Asia"),
 "spot-taiwan": ("mountains", "pagoda", "#1D3D52", "#9FC0C0", "#B6D0CA", "#12262A",
                 "#5F7B5C", "#8FCBA4", "Zhongyang Range / East Asia"),
 "top5-treks": ("mountains", "stupa", "#1B3858", "#AEC4D6", "#C6D4DD", "#141F28",
                "#8C7A58", "#D8B468", "Snowman Trek / Bhutan"),
 "top5-ski-towns": ("mountains", "hut", "#213E5C", "#BCCBD8", "#D2DBE1", "#171F27",
                    "#6A7486", "#9FC2E0", "Myoko Kogen / Niigata, Japan"),
 "top5-libraries": ("mountains", "church", "#27405A", "#A8BCC9", "#C0CCD2", "#1A222A",
                    "#A08457", "#DEB066", "Admont Abbey / Styria, Austria"),

 # ---- volcanic
 "spot-ecuador": ("volcano", "church", "#1E3752", "#A9BDCC", "#C3CED6", "#16222A",
                  "#9A6448", "#E29455", "Chimborazo / Andes"),
 "netherlands-crazy": ("volcano", "house", "#1D4457", "#9BC0BD", "#B2CEC3", "#13262A",
                       "#6E8A5E", "#9ED49B", "Saba / Dutch Caribbean"),
 "top5-volcanoes": ("volcano", "hut", "#2A2E40", "#8C7F82", "#A08E8A", "#1A1518",
                    "#A3542F", "#F07438", "Mount Yasur / Tanna, Vanuatu"),
 "top5-temples": ("volcano", "stupa", "#24415A", "#A8B9A6", "#BECBAE", "#1B2219",
                  "#9A7446", "#DDA852", "Borobudur / Central Java"),

 # ---- islands and archipelago
 "spot-estonia": ("islands", "windmill", "#26485F", "#A8C2CC", "#BFD2D5", "#172830",
                  "#8C8A62", "#D4C472", "Baltic islands / Northern Europe"),
 "nauru-crazy": ("islands", "rig", "#1C4659", "#8EC0C2", "#A9D0C8", "#122529",
                 "#AE8A54", "#EDBB55", "Nauru / Micronesia"),
 "top5-diving": ("islands", "boat", "#17465C", "#7FC2C6", "#9BD2CB", "#0F252A",
                 "#4E8A72", "#64D6B4", "Raja Ampat / West Papua"),

 # ---- desert and dune
 "djibouti-crazy": ("dunes", "rig", "#315064", "#D3C9B0", "#E0D6BB", "#2B2318",
                    "#BE8F55", "#F0BE52", "Lake Assal / Afar Triangle"),
 "spot-uzbekistan": ("dunes", "dome", "#2C4A66", "#CFBE9C", "#DCC9A4", "#2A2015",
                     "#B88B52", "#E7B351", "Kyzylkum / Central Asia"),
 "top5-deserts": ("dunes", "tent", "#35405C", "#C9A882", "#D8B88D", "#2A1C14",
                  "#B06A33", "#EE9A3F", "Dasht-e Lut / Iran"),
 "spot-jordan": ("dunes", "rig", "#2F4860", "#D0B99C", "#DCC6A6", "#2A1E18",
                 "#B4703D", "#EC9D45", "Dead Sea / Levant"),

 # ---- steppe and plateau
 "top5-trains": ("steppe", "train", "#243E58", "#A9B8AE", "#BEC6B6", "#1A2019",
                 "#8A7A52", "#D4B265", "Trans-Siberian / Moscow – Vladivostok"),
 "china-crazy": ("steppe", "gate", "#2A4058", "#B6B49A", "#C8C3A4", "#1F1C17",
                 "#A6703C", "#E29A45", "Xinjiang / East Asia"),
 "kazakhstan-crazy": ("steppe", "rig", "#2B4259", "#B2B9A4", "#C5C6AD", "#1E2219",
                      "#9A8452", "#DCB862", "Baikonur / Central Asia"),

 # ---- forest
 "france-crazy": ("forest_valley", "hut", "#1F3C46", "#8FAE92", "#A6C0A0", "#12201A",
                  "#6E8A4E", "#A8D46A", "French Guiana / South America"),
 "suriname-crazy": ("forest_valley", "hut", "#1D3A42", "#8AAA8C", "#A2BD9A", "#11201A",
                    "#6B8A4C", "#A4D468", "Guiana Shield / South America"),
 "spot-colombia": ("forest_valley", "hut", "#1E3E4A", "#90B296", "#A8C4A2", "#12221C",
                   "#6F8E4E", "#AAD86C", "Chocó / northern Andes"),
 "papua-new-guinea-crazy": ("forest_valley", "hut", "#1C3A44", "#88A88E", "#A0BC9A",
                            "#11201B", "#6A8A52", "#A2D070", "New Guinea / Melanesia"),
 "spot-laos": ("forest_valley", "stupa", "#20404C", "#93B296", "#AAC49E", "#13221B",
               "#7A8A4E", "#C2D46A", "Mekong karst / Southeast Asia"),
 "top5-hot-springs": ("forest_valley", "pagoda", "#223E52", "#A4BCB4", "#BACBBE",
                      "#162222", "#6E8470", "#9CCBB0", "Onsen towns / Japan"),
 "top5-national-parks": ("forest_valley", "boat", "#1D3C48", "#8CB094", "#A4C29E",
                         "#11211B", "#6C8C50", "#A6D46E", "Manú / Madre de Dios, Peru"),
 "madagascar-crazy": ("savanna", "hut", "#2B4356", "#C4AE8E", "#D2BC96", "#271C16",
                      "#B4703E", "#EFA047", "Madagascar / Indian Ocean"),

 # ---- savanna
 "top5-safaris": ("savanna", "tent", "#2E4556", "#C6B18C", "#D4BE94", "#261D15",
                  "#B07A3E", "#EDA848", "South Luangwa / Zambia"),
 "spot-tanzania": ("savanna", "tent", "#2C4458", "#C0B48E", "#CFBF96", "#241D16",
                   "#AC7C40", "#E8A44A", "Ngorongoro / East Africa"),
 "south-africa-crazy": ("savanna", "house", "#2D4659", "#C2B390", "#D0BE98", "#251E17",
                        "#AA7A42", "#E6A24C", "Highveld / Southern Africa"),

 # ---- water: lakes, fjords, wetland, delta
 "finland-crazy": ("lake", "hut", "#22435E", "#A6C0CE", "#BED0D6", "#152630",
                   "#5E7A62", "#8CC8A8", "Lakeland / Northern Europe"),
 "bolivia-crazy": ("lake", "boat", "#1C3C62", "#A4BED6", "#BCD0DC", "#142430",
                   "#9A7A4E", "#DCB265", "Lake Titicaca / Altiplano"),
 "top5-lakes": ("lake", "church", "#1F3F5C", "#A2BECC", "#BACED4", "#142630",
                "#7A8460", "#B4CC84", "Lake Ohrid / North Macedonia and Albania"),
 "top5-castles": ("lake", "tower", "#263F58", "#AEBCC4", "#C4CBCC", "#1B222A",
                  "#9A6A4A", "#D89C5C", "Malbork Castle / Poland"),
 "spot-montenegro": ("fjord", "church", "#1F3E58", "#9EBAC8", "#B6CBD0", "#132530",
                     "#7E8A62", "#BCCC82", "Bay of Kotor / Adriatic"),
 "top5-ferries": ("fjord", "boat", "#1D3A56", "#A4BCCE", "#BCCCD6", "#13222C",
                  "#5E7484", "#92BEDC", "Hurtigruten / Norway"),
 "spot-botswana": ("wetland", "boat", "#2A4858", "#B6BE98", "#C6C9A2", "#1D2218",
                   "#9A8A4E", "#D6BC64", "Okavango / Southern Africa"),
 "turkey-crazy": ("skyline", "boat", "#25425C", "#AEC0CA", "#C4CDD0", "#18222A",
                  "#A2804E", "#E0AE5C", "Bosphorus / Anatolia and Europe"),
 "spot-panama": ("delta", "boat", "#1F4050", "#95B6A6", "#ACC6AC", "#13221C",
                 "#7A8A52", "#BCD06E", "Isthmus / Central America"),

 # ---- ice
 "denmark-crazy": ("ice", "rig", "#1E3E5E", "#BCCEDC", "#D2DCE2", "#16222C",
                   "#6A7C92", "#9CC0E2", "Hans Island / Nares Strait"),
 "norway-crazy": ("ice", "rig", "#1C3A58", "#B4C8D8", "#CCD8E0", "#15202A",
                  "#64748C", "#94B8DC", "Bouvet Island / South Atlantic"),
 "russia-crazy": ("ice", "lighthouse", "#1F3C5A", "#B8CAD8", "#CEDAE0", "#161F28",
                  "#6E7C90", "#A0BEDC", "Siberia / North Asia"),
 "top5-fjords": ("ice", "boat", "#1B3A5A", "#AEC6D8", "#C6D6E0", "#141E28",
                 "#5E7288", "#90B6D8", "Scoresby Sound / East Greenland"),
 "top5-glaciers": ("ice", "boat", "#1D3C5C", "#B2C8DA", "#C8D8E2", "#151F2A",
                   "#60748E", "#94BADE", "Perito Moreno / Santa Cruz, Argentina"),

 # ---- gorge and canyon
 "oman-crazy": ("gorge", "house", "#2F4A5E", "#C8B89A", "#D6C5A4", "#2A2017",
                "#B2804A", "#E8AC50", "Madha and Nahwa / Musandam"),
 "top5-canyons": ("gorge", "hut", "#28445A", "#B4B498", "#C6C4A4", "#211D17",
                  "#9A7442", "#DCA64E", "Tiger Leaping Gorge / Yunnan, China"),
 "top5-waterfalls": ("gorge", "hut", "#1F4050", "#9EB8A4", "#B4C6AA", "#13211B",
                     "#7A8A50", "#BCD06C", "Angel Falls / Canaima, Venezuela"),
 "top5-bridges": ("gorge", "bridge", "#26445C", "#AEBEC2", "#C4CCC8", "#1A2228",
                  "#8E8458", "#D0B468", "Millau Viaduct / Aveyron, France"),
 "top5-cable-cars": ("gorge", "cablecar", "#2A4258", "#B2B49C", "#C4C3A6", "#1F1E18",
                     "#9A7446", "#DCA852", "Wings of Tatev / Syunik, Armenia"),
 "top5-monasteries": ("gorge", "church", "#2A4458", "#B6B69C", "#C8C6A6", "#201F18",
                      "#A07A46", "#E0A852", "Meteora / Thessaly, Greece"),
 "top5-caves": ("gorge", "tent", "#1E3C4A", "#94B096", "#AAC09E", "#12201A",
                "#74884E", "#B4CC68", "Hang Son Doong / Quang Binh, Vietnam"),

 # ---- terraces
 "spot-vietnam": ("terraces", "hut", "#1F3E4C", "#96B894", "#ACC89C", "#13221A",
                  "#78904E", "#BCD468", "Annamite coast / Southeast Asia"),
 "spot-rwanda": ("terraces", "hut", "#254250", "#A4B892", "#B8C69A", "#1E2117",
                 "#96703E", "#D2A24C", "Thousand hills / East Africa"),
 "top5-wine-regions": ("terraces", "house", "#2A4458", "#B8B492", "#C8C39C", "#231E16",
                       "#A4703C", "#E29E48", "Douro / Portugal"),
 "top5-tea-regions": ("terraces", "hut", "#213E4C", "#9CBA9A", "#B2C8A0", "#14221A",
                      "#7C9050", "#BED46A", "Wazuka / Kyoto Prefecture, Japan"),

 # ---- urban
 "top5-markets": ("skyline", "dome", "#27425A", "#B4BEC0", "#C6CAC6", "#1A2026",
                  "#A47E4C", "#E0AC58", "Grand Bazaar / Istanbul, Türkiye"),
 "top5-museums": ("skyline", "dome", "#2A445A", "#BCBAA4", "#CCC6AC", "#1E1E18",
                  "#A87A48", "#E8A450", "Museo Nacional de Antropología / Mexico City"),
 "spot-romania": ("skyline", "dome", "#28425A", "#B2BCC0", "#C4C8C6", "#1A2026",
                  "#9A8252", "#D6B062", "Wallachia / Southeast Europe"),
 "singapore-crazy": ("skyline", "rig", "#1E4056", "#A4C0C4", "#BACECA", "#142428",
                     "#6E8A70", "#9CD0AE", "Singapore / Maritime Southeast Asia"),
}


# --------------------------------------------------------------------------
# palette expansion
# --------------------------------------------------------------------------

def expand(sky_top, sky_bot, far, near, warm, accent):
    """Two subject anchors + a warm family -> five flats, back to front.

    Lightness steps monotonically from `far` to `near` by construction, which
    is what makes the planes read as depth with no outlines. The middle planes
    carry a little of the warm family so the set is not a single hue ramp.
    """
    planes = [
        far,                                                   # cool, hazy, back
        cover.shade(cover.mix(far, warm, 0.45), 0.86),          # warm family in
        cover.shade(cover.mix(far, warm, 0.72), 0.66),          # warm family full
        cover.shade(cover.mix(warm, near, 0.45), 0.90),         # warm into ground
        near,                                                   # ground, darkest
    ]
    # guarantee the monotonic step the brief asks for, warm tint notwithstanding
    for i in range(1, 5):
        if cover.lum(planes[i]) >= cover.lum(planes[i - 1]):
            planes[i] = cover.shade(planes[i - 1], 0.86)
    return {"sky": [sky_top, sky_bot], "planes": planes, "accent": accent}


def write_palettes():
    out = {}
    for slug, row in POSTERS.items():
        _, _, st, sb, far, near, warm, accent, _ = row
        out[slug] = expand(st, sb, far, near, warm, accent)
    (ROOT / "palettes.json").write_text(json.dumps(out, indent=1) + "\n")
    return len(out)


# --------------------------------------------------------------------------
# deriving the cover's words from the post's own slides
# --------------------------------------------------------------------------

def flat(s):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", str(s or ""))).strip()


def country_of(slug):
    name = re.sub(r"^spot-", "", slug)
    name = re.sub(r"-crazy$", "", name)
    return name.replace("-", " ").upper()


def split_unit(value, label):
    """"93.34" + "km² — Madha, an exclave of Oman" -> "93.34 km²", "Madha".

    The bignum labels put the unit first and the subject after a dash. Taking
    the first clause blindly leaves two columns both reading KM², which tells
    the reader nothing about which exclave is which.
    """
    m = re.match(r"^\s*([^—]{1,9}?)\s*—\s*(.+)$", flat(label))
    if not m:
        return value, label
    unit, rest = m.group(1), m.group(2)
    # NB not isdigit(): "km²" would fail it, because U+00B2 IS a digit in
    # Python. Only ASCII digits mean this is a figure rather than a unit.
    if any(ch in "0123456789" for ch in unit):
        return value, label
    return f"{value} {unit}".strip(), rest


def short_label(text, limit=32):
    """First clause of a bignum label, short enough for a stat column."""
    t = flat(text)
    t = re.split(r"[,—(]| - ", t)[0].strip()
    if len(t) > limit:
        words = t.split()
        t = ""
        for w in words:
            if len(t) + len(w) + 1 > limit:
                break
            t = (t + " " + w).strip()
    return t.upper()


DATASET_URL = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
DATASET_CACHE = ROOT / ".work" / "countries.json"

# Dataset spellings that the slug does not match on its own.
ALIASES = {"turkey": "türkiye"}

# Fill fields that would contradict the post's own hook. Nauru's hook is that
# it has no capital city; the dataset lists Yaren, its de facto seat. South
# Africa's hook is that it has three capitals; the dataset lists Pretoria.
# Printing either on the cover would have the cover argue with its own headline.
FILL_SKIP = {"nauru-crazy": {"capital"}, "south-africa-crazy": {"capital"}}


def dataset():
    """mledoze/countries — the source BUILD.md sanctions for exact country facts.

    NOTE the `borders` field is deliberately never used as a fill. BUILD.md
    records why: it lists 16 neighbours for China, two of which are Hong Kong
    and Macau, China's own territories. The correct claim is 14. A figure that
    needs a caveat does not belong in a three-word stat column.
    """
    if not DATASET_CACHE.exists():
        import urllib.request
        DATASET_CACHE.parent.mkdir(exist_ok=True)
        with urllib.request.urlopen(DATASET_URL, timeout=90) as r:
            DATASET_CACHE.write_bytes(r.read())
    idx = {}
    for c in json.loads(DATASET_CACHE.read_text()):
        for n in (c["name"]["common"], c["name"]["official"]):
            idx[n.lower()] = c
    return idx


_IDX = None


def country_fills(slug):
    """Verified country facts, in the order they should fill empty columns."""
    global _IDX
    if _IDX is None:
        _IDX = dataset()
    name = country_of(slug).lower()
    c = _IDX.get(ALIASES.get(name, name))
    if not c:
        return []
    skip = FILL_SKIP.get(slug, set())
    out = []
    if "area" not in skip and c.get("area"):
        out.append(("area", f"{int(c['area']):,} km²", "LAND AREA"))
    if "capital" not in skip and c.get("capital"):
        out.append(("capital", c["capital"][0], "CAPITAL"))
    cur = list((c.get("currencies") or {}).values())
    if "currency" not in skip and cur:
        out.append(("currency", cur[0].get("name", "").title(), "CURRENCY"))
    langs = list((c.get("languages") or {}).values())
    if "language" not in skip and langs:
        out.append(("language", langs[0], "OFFICIAL LANGUAGE"))
    return out


def _digits(s):
    return re.sub(r"[^\d]", "", str(s))


def derive(spec):
    """-> (kicker, region, hook, stats). Reads only what the post already says."""
    slug = spec["slug"]
    kind = spec.get("kind") or ""
    slides = spec["slides"]
    s1 = slides[0]
    hook = flat(s1.get("title"))
    region = POSTERS[slug][8]

    if kind == "top5":
        r1 = next((x for x in slides
                   if x.get("type") == "rank" and str(x.get("rank")) in ("01", "1")), None)
        if not r1:
            raise SystemExit(f"{slug}: top5 with no rank 01 slide")
        kicker = flat(r1.get("place")).upper()
        # The No. 1 pick's own `where`, not the authored label — that label
        # names the place too, and a cover that says NAZARÉ twice looks broken.
        region = flat(r1.get("where")) or POSTERS[slug][8]
        region = region.replace(", ", " / ")
        stats = list(TOP5_STATS)
    elif kind == "crazy":
        nums = [x for x in slides if x.get("type") == "bignum" and x.get("number")]
        kicker = country_of(slug)
        stats = []
        for x in nums[:3]:
            v, l = split_unit(flat(x["number"]), x.get("label"))
            stats.append((v, short_label(l)))
        if len(stats) < 3:
            # Not enough figures in the post itself. Fill from the sanctioned
            # dataset rather than inventing one — and never with a value the
            # post already states, which would read as a stutter.
            seen = {_digits(v) for v, _ in stats if _digits(v)}
            seen |= {v.strip().lower() for v, _ in stats}
            for _field, value, label in country_fills(slug):
                if len(stats) >= 3:
                    break
                if _digits(value) and _digits(value) in seen:
                    continue
                if value.strip().lower() in seen:
                    continue
                stats.append((value, label))
                seen.add(_digits(value) or value.strip().lower())
        if len(stats) < 3:
            raise SystemExit(f"{slug}: only {len(stats)} verified stats available")
    else:                                                   # spotlight
        led = next((x for x in slides if x.get("type") == "ledger"), None)
        if not led:
            raise SystemExit(f"{slug}: spotlight with no ledger slide")
        rows = [(flat(a), flat(b)) for a, b in led["rows"]]
        numeric = [r for r in rows if any(ch.isdigit() for ch in r[1])]
        others = [r for r in rows if r not in numeric]
        chosen = (numeric + others)[:3]
        stats = []
        for label, value in chosen:
            v = re.split(r"\s+—\s+|\s+-\s+", value)[0].strip()
            stats.append((v, short_label(label)))
        kicker = country_of(slug)

    return kicker, region, hook, stats


def convert(slug, force=False):
    path = CONTENT / f"{slug}.json"
    spec = json.loads(path.read_text())
    s1 = spec["slides"][0]
    if s1.get("type") == "poster":
        if not force:
            return False
        # rebuild from the hook slide this cover was made from, so --force is
        # idempotent and never derives a cover from a previous cover
        old = dict(s1.get("was_hook") or {})
        old["type"] = "hook"
        spec["slides"][0] = old
    if slug not in POSTERS:
        raise SystemExit(f"{slug}: no POSTERS row — add archetype, palette and element")
    archetype, element = POSTERS[slug][0], POSTERS[slug][1]
    kicker, region, hook, stats = derive(spec)
    old = spec["slides"][0]
    spec["slides"][0] = {
        "type": "poster",
        "seed": slug,
        "archetype": archetype,
        "palette": slug,
        "element": element,
        "kicker": kicker,
        "region": region,
        "hook": hook,
        "stats": [list(s) for s in stats],
        "was_hook": {k: old[k] for k in ("title", "sub", "size") if k in old},
    }
    path.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    return True


def twist_check():
    """Posts whose old twist line survives nowhere a reader will see it.

    The cover has no room for the `sub` line that sat under the old hook, so
    it has to live in the caption instead. That is not automatic — it was true
    of 52 of the first 70 posts and silently false for the other 18. Anything
    this lists needs its twist adding as the caption's second paragraph, and
    then queue.json's copy rebuilt with make_queue.full_caption().
    """
    out = []
    for slug in unposted_slugs():
        p = CONTENT / f"{slug}.json"
        if not p.exists():
            continue
        spec = json.loads(p.read_text())
        s1 = spec["slides"][0]
        if s1.get("type") != "poster":
            continue
        sub = flat((s1.get("was_hook") or {}).get("sub"))
        cap = (spec.get("caption") or "").lower()
        words = re.findall(r"[a-z]{5,}", sub.lower())
        if not words:
            continue
        if sum(1 for w in words if w in cap) / len(words) < 0.5:
            out.append(slug)
    return out


def unposted_slugs():
    q = json.loads((ROOT / "queue.json").read_text())["queue"]
    return [e["slug"] for e in q if e.get("posted_at") is None]


def pending():
    out = []
    for slug in unposted_slugs():
        p = CONTENT / f"{slug}.json"
        if not p.exists():
            continue
        if json.loads(p.read_text())["slides"][0].get("type") != "poster":
            out.append(slug)
    return out


def main():
    args = sys.argv[1:]
    n = write_palettes()
    if "--palettes" in args:
        print(f"palettes.json: {n} palettes")
        return
    todo = pending()
    if "--list" in args or not args:
        print(f"{len(todo)} unposted posts still on the old hook cover")
        for s in todo:
            print(" ", s)
        return
    if "--all" in args:
        targets = todo
    elif "--limit" in args:
        k = int(args[args.index("--limit") + 1])
        targets = todo[:k]
    else:
        targets = [a for a in args if not a.startswith("--")]
    if "--force" in args and not targets:
        targets = [s for s in unposted_slugs() if (CONTENT / f"{s}.json").exists()]
    force = "--force" in args
    done = 0
    for slug in targets:
        if convert(slug, force=force):
            done += 1
            print("converted", slug)
    print(f"{done} converted, {len(pending())} still pending")
    lost = twist_check()
    if lost:
        print(f"\n!! {len(lost)} posts whose twist line appears on neither the cover")
        print("   nor the caption. Add it as the caption's second paragraph, then")
        print("   rebuild queue.json's copy with make_queue.full_caption():")
        for s in lost:
            print("    ", s)


if __name__ == "__main__":
    main()
