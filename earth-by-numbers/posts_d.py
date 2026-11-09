#!/usr/bin/env python3
"""
Earth by Numbers — content set D: weekly top-up, 2026-11-09.

Three posts, written to take the approved-and-unposted queue from 25 to 28.
Mix chosen to even out the grid: `crazy` was running 6 against 10 top5 and
10 spotlight, so this set is two crazy and one top5.

  france-crazy    crazy  5 slides  longest border is with Brazil
  bolivia-crazy   crazy  5 slides  a navy with no coastline
  top5-treks      top5   6 slides  Everest Base Camp is a queue

VERIFICATION (BUILD.md §4 — every figure checked in this run)
  Wikipedia, read this run: Borders of France, Time in France, French Guiana,
  Guiana Space Centre, Bolivian Naval Force, Bolivia, War of the Pacific,
  Lake Titicaca, Snowman Trek, Kungsleden, Alta Via 1, Overland Track,
  Torres del Paine National Park.
  Dataset: mledoze/countries — Austria 83,871 km², Bolivia 1,098,581 km² and
  5 land neighbours, France 551,695 km² metropolitan.

DROPPED for being unconfirmable, per the rule that matters most:
  - France's EEZ rank. The Wikipedia article contradicts itself on whether
    France or the US has the largest EEZ, and its body figure (10,186,624 km²)
    disagrees with its own table (11,691,000 km²). No number used.
  - "La Paz is the highest capital city." The altitude table would not load,
    so the claim could not be checked. Replaced with the two-capitals fact,
    which is in Bolivia's lead verbatim.
  - "Most trekkers do not finish the Snowman Trek." Tagged [citation needed]
    on Wikipedia. Only the cited 347 km / eleven passes / 5,230 m are used.
  - Length of the coastline Bolivia lost in 1879. Not stated on any page read.

Run:  python3 posts_d.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "content"

DS = "Dataset: mledoze/countries (CC-BY-SA)."
WIKI = "Source: Wikipedia."

POSTS = []


def post(slug, kind, slides, caption, tags):
    slides[-1]["handle"] = True
    POSTS.append({"slug": slug, "kind": kind, "slides": slides,
                  "caption": caption.strip(), "tags": tags})


def top5(slug, hook_title, hook_sub, entries, caption, tags, hook_size="h-md"):
    """entries: list of 5 (place, where, note, source)."""
    slides = [{"type": "hook", "title": hook_title, "sub": hook_sub, "size": hook_size}]
    for i, (place, where, note, src) in enumerate(entries, start=1):
        slides.append({
            "type": "rank", "kicker": f"No. {i}", "rank": f"{i:02d}",
            "place": place, "where": where, "note": note, "source": src,
            "bg": "" if i % 2 else "ink",
        })
    slides[-1]["handle"] = True
    POSTS.append({"slug": slug, "kind": "top5", "slides": slides,
                  "caption": caption.strip(), "tags": tags})


# ══════════════════════════════════════════════════════ FRANCE ════

post(
    "france-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "France's<br>longest border<br>is with Brazil.",
         "sub": "Five stats about a country that is not where you think it is."},
        {"type": "bignum", "kicker": "Stat 02", "number": "730", "numsize": "s3", "bg": "",
         "label": "km — the France–Brazil border",
         "title": "Spain comes second, at 646 km.", "size": "h-sm",
         "source": "Borders of France. The border runs along French Guiana. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "83,534", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "km² of France in South America",
         "title": "French Guiana is a department, not a colony. That makes it EU territory.",
         "size": "h-sm",
         "source": "French Guiana: 83,534 km², slightly smaller than Austria at 83,871 km². "
                   + WIKI + " " + DS},
        {"type": "bignum", "kicker": "Stat 04", "number": "12", "numsize": "s2", "bg": "",
         "label": "time zones — more than any other country",
         "title": "UTC−10 to UTC+12. Thirteen if you count the Antarctic claim.",
         "size": "h-sm",
         "source": "Time in France. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Europe launches its rockets from South America.",
         "sub": "The Guiana Space Centre sits about 5° north of the equator, which takes "
                "substantially less energy to reach geostationary orbit. ESA owns the launch "
                "infrastructure; CNES manages the land.",
         "source": "Guiana Space Centre, also called Europe's Spaceport. " + WIKI},
    ],
    """
France's longest land border is not with Spain or Germany. It is with Brazil.

730 km of it, along French Guiana. The Spanish border is 646 km. Nothing in metropolitan France comes close.

FRANCE BY NUMBERS
Longest land border — 730 km, with Brazil
Second — 646 km, with Spain
French Guiana — 83,534 km², slightly smaller than Austria
Time zones — 12, more than any other country on Earth
Range — UTC−10 to UTC+12

French Guiana is not a colony or a territory. It is an overseas department and region of France, which means it is part of the European Union. The euro is legal tender in South America. The European Union has a land border with Brazil.

It is also why Europe launches its rockets from the Amazon. The Guiana Space Centre at Kourou sits about 5 degrees north of the equator, and the closer you are to the equator the less energy it takes to put something into geostationary orbit. ESA owns the launch infrastructure. Europe's spaceport is in South America, and that is a deliberate choice about physics, not history.

Twelve time zones is the part people argue about. It runs from UTC−10 in French Polynesia to UTC+12 in Wallis and Futuna — thirteen if you count the Antarctic claim.

Which country did you think had the most time zones?
""",
    ["france", "frenchguiana", "kourou", "geographyfacts", "didyouknow", "maps",
     "worldfacts", "southamerica", "europeanunion", "earthbynumbers"],
)

# ═════════════════════════════════════════════════════ BOLIVIA ════

post(
    "bolivia-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Bolivia has<br>a navy and<br>no coastline.",
         "sub": "Five stats from a country that has never accepted the loss."},
        {"type": "bignum", "kicker": "Stat 02", "number": "5,000", "numsize": "s3", "bg": "",
         "label": "naval personnel, in a landlocked country",
         "title": "They patrol a lake and the rivers that feed the Amazon.", "size": "h-sm",
         "source": "Bolivian Navy, figure as of 2018, citing the CIA World Factbook. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "1879", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "the year the coast was occupied",
         "title": "Chile took Antofagasta in February. Bolivia accepted it in the 1884 truce.",
         "size": "h-sm",
         "source": "War of the Pacific, 1879–1884. The lost province was the Litoral. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "3,812", "numsize": "s3", "bg": "",
         "label": "metres above sea level — Lake Titicaca",
         "title": "8,372 km², the largest lake in South America. This is where the navy sails.",
         "size": "h-sm",
         "source": "Lake Titicaca: largest in South America by surface area and by volume. " + WIKI},
        {"type": "fact", "kicker": "Stat 05 — the myth", "bg": "sun", "size": "h-sm",
         "title": "Titicaca is not the highest lake in the world.",
         "sub": "It is the highest NAVIGABLE lake, and that claim is generally taken to mean "
                "commercial craft. The crater lake on Ojos del Salado sits above 6,400 m.",
         "source": "Lake Titicaca. " + WIKI},
    ],
    """
Bolivia maintains a navy of roughly 5,000 personnel. Bolivia has no coastline.

It lost the coast in 1879, when Chile occupied the port of Antofagasta without resistance and took the Litoral province with it. Bolivia signed a truce in 1884 and has been landlocked ever since. The navy was not disbanded. It was reorganised, and it is still there.

BOLIVIA BY NUMBERS
Naval personnel — about 5,000 (2018)
Coastline — 0 km
Land area — 1,098,581 km²
Land neighbours — 5: Brazil, Paraguay, Argentina, Chile, Peru
Lake Titicaca — 3,812 m above sea level, 8,372 km²

The fleet patrols Lake Titicaca and thousands of miles of navigable river running into the Amazon basin. Wikipedia puts the purpose plainly: the navy exists to keep alive the hope of recovering the coast.

Two other things worth knowing. Bolivia has two capitals — Sucre is the constitutional capital and holds the judiciary, La Paz is the seat of government. And since independence the country has lost more than half its territory to its neighbours.

One correction, because it gets repeated everywhere: Titicaca is not the highest lake on Earth. It is the highest navigable lake, and that claim is generally understood to mean commercial boats. The crater lake on Ojos del Salado sits above 6,400 m. Titicaca is still the largest lake in South America, by surface area and by volume, which is impressive enough without the upgrade.

Should a landlocked country keep a navy?
""",
    ["bolivia", "laketiticaca", "landlocked", "geographyfacts", "southamerica",
     "didyouknow", "worldfacts", "sucre", "lapaz", "earthbynumbers"],
)

# ═══════════════════════════════════════════════════════ TOP 5 ════

top5(
    "top5-treks",
    "Everest Base<br>Camp is a<br>queue.",
    "Not a trek. Five long walks with nobody standing in front of you. Opinion.",
    [
        ("Snowman Trek", "Bhutan",
         "347 km over eleven mountain passes, topping out at 5,230 m. Wikipedia rates the "
         "difficulty as hard and leaves it at that.",
         "Snowman Trek. " + WIKI),
        ("Kungsleden", "Sweden",
         "467 km from Abisko to Hemavan. Huts every 9 to 22 km, except for one stretch of "
         "about 130 km with none at all.",
         "Kungsleden. Huts operated by STF. " + WIKI),
        ("The full circuit", "Torres del Paine, Chile",
         "Everyone walks the W: 50 miles, three to five days, shoulder to shoulder. The full "
         "O is 81 miles over seven to nine days, and the back half is empty.",
         "Torres del Paine National Park. " + WIKI),
        ("Alta Via 1", "Dolomites, Italy",
         "125 km from Pragser Wildsee to Belluno, seven to twelve days, through limestone "
         "towers that look computer-generated.",
         "Alta Via 1. " + WIKI),
        ("Overland Track", "Tasmania, Australia",
         "Only 65 km and five or six days, but you book a start date and walk north to "
         "south. The rationing is what keeps it worth doing.",
         "Overland Track. Booking system since 2005. " + WIKI),
    ],
    """
Everest Base Camp is a queue. It is a famous walk to a car park of tents at the bottom of a mountain you are not climbing, and you will do it in single file.

Five long walks where that does not happen:

01 SNOWMAN TREK, Bhutan — 347 km over eleven mountain passes, high point 5,230 m. Wikipedia rates it hard. It is the one on this list that can genuinely beat you.

02 KUNGSLEDEN, Sweden — 467 km from Abisko to Hemavan through Lapland. Huts every 9 to 22 km, run by the Swedish Tourist Association, apart from one stretch of about 130 km with none.

03 THE FULL CIRCUIT, Torres del Paine, Chile — everybody does the W, 50 miles in three to five days, and it is busy. The full O route is 81 miles over seven to nine days. Same park, same towers, a fraction of the people on the far side.

04 ALTA VIA 1, Dolomites, Italy — 125 km from Pragser Wildsee down to Belluno, seven to twelve days, through the most improbable rock architecture in Europe.

05 OVERLAND TRACK, Tasmania — the short one, 65 km in five or six days. You book a start date and walk north to south, and the limit on numbers is exactly why it stays good.

This is opinion. The distances are not — those are Wikipedia's.

Tell us which one we got wrong, and which trek you would put at number one.
""",
    ["trekking", "hiking", "snowmantrek", "kungsleden", "torresdelpaine", "dolomites",
     "overlandtrack", "longdistancehiking", "adventuretravel", "travelinspo",
     "earthbynumbers"],
    hook_size="h-lg",
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        (OUT / f"{p['slug']}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False))
    print(f"wrote {len(POSTS)} posts")
    for p in POSTS:
        tags = len(p["tags"])
        print(f"  {p['slug']:16s} {p['kind']:9s} {len(p['slides'])} slides  "
              f"{len(p['caption'])} caption chars  {tags} tags")


if __name__ == "__main__":
    main()
