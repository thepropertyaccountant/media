#!/usr/bin/env python3
"""
Earth by Numbers — content set E: the 100-buffer batch, 2026-11-09.

Fifteen posts. Felix removed the per-post approval gate and raised the standing
queue target from 28 to 100, so these land approved (make_queue.py --approve-new)
and the twice-daily posting task picks them up without a review step.

  crazy (6)      oman, suriname, finland, djibouti, kyrgyzstan, madagascar
  spotlight (5)  bhutan, albania, colombia, uzbekistan, ethiopia
  top5 (4)       markets, hot springs, ancient cities, ferries

Mix is weighted to crazy and spotlight because top5 was running ahead.

VERIFICATION (BUILD.md §4 — every figure checked in this run)
Wikipedia pages read this run: Madha; Musandam Governorate; Oman; Suriname;
List of countries by forest area; Finland; Lakes of Finland; Lake Assal
(Djibouti); Djibouti; Kyrgyzstan; Issyk-Kul; Madagascar; Wildlife of
Madagascar; Bhutan; Thimphu; Gangkhar Puensum; Albania; Colombia; Andes;
Landlocked country; Uzbekistan; Aral Sea; Ethiopian calendar; Ethiopia;
Danakil Depression; Addis Ababa; Grand Bazaar Istanbul; Chatuchak Weekend
Market; Blue Lagoon; Pamukkale; Onsen; Pompeii; Petra; Leptis Magna;
Hierapolis; Hurtigruten.
Ledger rows come from the mledoze/countries dataset, so they are checkable
against one file; Wikipedia's own totals differ slightly for some countries
(it quotes total area, the dataset quotes a land figure) and the two are
never mixed inside one source line.

DROPPED, per the rule that matters most:
  - Thimphu "has no traffic lights". The fetch never returned that sentence
    verbatim, only a summary of it. Classic travel trivia, so it needed the
    real text. Cut.
  - Bhutan "carbon negative" and the constitutional 60% forest minimum.
    Summary-only, and the constitution link was explicitly not supported.
  - Albania's concrete bunker count. The Bunkerisation of Albania article
    404s and no figure appears in the Albania article. No number used, so
    Albania leans on its borders and coast instead.
  - Colombia as "the only South American country with two coasts". The word
    "only" is not on the page. Reduced to the two coasts it does state.
  - Colombia bird-species counts. Summary-only.
  - Ethiopia "never colonised". The page says "the only African country to
    never be FULLY colonised", alongside Liberia, and describes the 1936–41
    Italian occupation. Wording follows the page exactly.
  - Lake Assal's salinity RANK. The article says fifth most saline in the
    lead and second in the body. The g/L figures are not in dispute, so the
    post uses those and makes the contradiction its own slide.
  - Suriname's forest RANK as a flat claim, for the same reason: lead says
    second-highest, body says highest at 90.2%, FAO table says 94.5%.
  - Aral Sea's "third largest" / "fourth largest" rank. Same contradiction.
  - Hurtigruten route length and round-trip duration. Not stated.
  - Petra's founding date and unexcavated share; Pompeii's exact excavated
    percentage (only "two-thirds"); Chatuchak's area. Not stated.

Run:  python3 posts_e.py
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


def spotlight(slug, hook, hook_sub, rows, why_title, why, extra, go_title, go,
              caption, tags, hook_size="h-md", extra_bg="sun"):
    slides = [
        {"type": "hook", "title": hook, "sub": hook_sub, "size": hook_size},
        {"type": "ledger", "kicker": "The basics", "bg": "", "rows": rows, "source": DS},
        {"type": "items", "kicker": "Why go", "title": why_title, "bg": "ink", "items": why},
        dict({"type": "fact", "kicker": "One more thing", "bg": extra_bg}, **extra),
        {"type": "items", "kicker": "Where to go", "title": go_title, "bg": "", "items": go,
         "handle": True},
    ]
    POSTS.append({"slug": slug, "kind": "spotlight", "slides": slides,
                  "caption": caption.strip(), "tags": tags})


def top5(slug, hook_title, hook_sub, entries, caption, tags, hook_size="h-md"):
    """entries: list of 5 (place, where, note, source). source may be ""."""
    slides = [{"type": "hook", "title": hook_title, "sub": hook_sub, "size": hook_size}]
    for i, (place, where, note, src) in enumerate(entries, start=1):
        s = {"type": "rank", "kicker": f"No. {i}", "rank": f"{i:02d}",
             "place": place, "where": where, "note": note,
             "bg": "" if i % 2 else "ink"}
        if src:
            s["source"] = src
        slides.append(s)
    slides[-1]["handle"] = True
    POSTS.append({"slug": slug, "kind": "top5", "slides": slides,
                  "caption": caption.strip(), "tags": tags})


# ══════════════════════════════════════════════ CRAZY STATS ════════

post(
    "oman-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Oman has a town<br>inside the UAE.<br>Inside it sits<br>a UAE village.",
         "sub": "Five stats from the most confusing border on Earth."},
        {"type": "bignum", "kicker": "Stat 02", "number": "93.34", "numsize": "s3", "bg": "",
         "label": "km² — Madha, an exclave of Oman",
         "title": "Entirely surrounded by the United Arab Emirates.", "size": "h-sm",
         "source": "Madha. " + WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink", "size": "h-sm",
         "title": "Inside Madha is Nahwa, which belongs to Sharjah.",
         "sub": "A counter-enclave: UAE territory, inside Omani territory, inside the UAE. "
                "Wikipedia calls it a second-order enclave.",
         "source": "Madha. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "1,800", "numsize": "s3", "bg": "",
         "label": "km² — Musandam, Oman's other exclave",
         "title": "Also cut off from Oman by the UAE.", "size": "h-sm",
         "source": "Musandam Governorate. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "That detached corner controls the Strait of Hormuz.",
         "sub": "Musandam juts into the narrow entry to the Persian Gulf. Wikipedia: its "
                "location gives Oman partial control of the strait, shared with Iran.",
         "source": "Musandam Governorate. " + WIKI},
    ],
    """
Oman has a town inside the United Arab Emirates. Inside that town is a village that belongs to the UAE.

The town is Madha, 93.34 km², an exclave of Oman entirely surrounded by the UAE. Inside Madha sits Nahwa, which belongs to the Emirate of Sharjah. Wikipedia's term for it is a second-order enclave: UAE land, inside Omani land, inside the UAE.

OMAN BY NUMBERS
Capital — Muscat
Land area — 309,500 km²
Land borders — 3: Saudi Arabia, UAE, Yemen
Official language — Arabic
Currency — Omani rial

Madha is not even Oman's only detached piece. Musandam, 1,800 km², sits at the tip of the peninsula, also separated from the rest of the country by the UAE.

And Musandam is the one that matters. It juts into the Strait of Hormuz, the narrow entry to the Persian Gulf. Wikipedia puts it plainly: that location gives Oman partial control of the strait, shared with Iran. A piece of land most people have never heard of sits on one of the most important shipping routes in the world.

Borders are not tidy. They are the leftovers of old agreements between tribes who grazed where they grazed.

What's the strangest border you've crossed?
""",
    ["oman", "madha", "nahwa", "musandam", "geographyfacts", "borders", "enclave",
     "didyouknow", "worldfacts", "earthbynumbers"],
)

post(
    "suriname-crazy", "crazy",
    [
        {"type": "hook", "size": "h-lg",
         "title": "Suriname is<br>94% forest.",
         "sub": "The smallest country in South America, and nearly all of it is trees."},
        {"type": "bignum", "kicker": "Stat 02", "number": "94.5%", "numsize": "s3", "bg": "",
         "label": "of the land is forest",
         "title": "More than any other sovereign country.", "size": "h-sm",
         "source": "List of countries by forest area, FAO data for 2022. French Guiana is "
                   "higher at 96.6%, but it is a department of France. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "163,820", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "km² — the smallest country in South America",
         "title": "Smallest by population too.", "size": "h-sm",
         "source": DS + " " + WIKI},
        {"type": "fact", "kicker": "Stat 04", "bg": "", "size": "h-sm",
         "title": "The official language is Dutch.",
         "sub": "Its neighbours are French Guiana, Brazil and Guyana. Four languages meet "
                "at three borders, and none of them is Spanish.",
         "source": DS + " " + WIKI},
        {"type": "fact", "kicker": "Stat 05 — the catch", "bg": "sun", "size": "h-sm",
         "title": "Suriname's own Wikipedia page cannot agree with itself.",
         "sub": "Its opening says second-highest forest cover in the world. Its body says "
                "highest, at 90.2%. The FAO table says 94.5%. We used the FAO figure and "
                "are telling you so.",
         "source": WIKI},
    ],
    """
Suriname is 94.5% forest. It is also the smallest country in South America, by area and by population.

That forest figure is the highest of any sovereign country on the FAO's 2022 numbers. Only French Guiana beats it, at 96.6%, and French Guiana is a department of France rather than a country.

SURINAME BY NUMBERS
Capital — Paramaribo
Land area — 163,820 km²
Land borders — 3: French Guiana, Brazil, Guyana
Official language — Dutch
Currency — Surinamese dollar

Dutch. In South America. Suriname was a Dutch colony until 1975 and the language stayed, which makes it the odd one out on a continent of Spanish and Portuguese speakers. Its three neighbours speak French, Portuguese and English respectively.

One honest note, because this account would rather tell you than be caught: Wikipedia's Suriname article contradicts itself on the forest number. The opening paragraph says over 90% and calls it the second-highest in the world. The ecoregions section says 90.2% and calls it the highest in the world. The FAO table on a different page says 94.5% for 2022. We went with the FAO figure because it is dated and sourced, but all three are on Wikipedia right now.

A number with three versions is still a good number. It just needs a footnote.

Which country surprised you most with its official language?
""",
    ["suriname", "paramaribo", "rainforest", "southamerica", "geographyfacts",
     "didyouknow", "worldfacts", "amazon", "travelinspo", "earthbynumbers"],
)

post(
    "finland-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Finland has<br>187,888 lakes.<br>Or 5,600.<br>Or 309.",
         "sub": "All three are correct. It depends where you draw the line."},
        {"type": "bignum", "kicker": "Stat 02", "number": "187,888", "numsize": "s3", "bg": "",
         "label": "lakes larger than 500 m²",
         "title": "Five ares. The smallest threshold anyone counts to.", "size": "h-sm",
         "source": "Lakes of Finland. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "5,600", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "lakes larger than 0.1 km²",
         "title": "Raise the bar once and 97% of them vanish.", "size": "h-sm",
         "source": "Lakes of Finland. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "309", "numsize": "s3", "bg": "",
         "label": "lakes larger than 10 km²",
         "title": "Raise it again and you are down to 309.", "size": "h-sm",
         "source": "Lakes of Finland. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "There is no agreed definition of a lake.",
         "sub": "That is Wikipedia's own caveat on the page: no standard unambiguous "
                "definition of the size a body of water needs to be one. Every lake count "
                "you have ever read is a choice of threshold.",
         "source": "Lakes of Finland. " + WIKI},
    ],
    """
Finland has 187,888 lakes. It also has 5,600 lakes. It also has 309 lakes. All three numbers are correct.

187,888 counts everything larger than 500 square metres — five ares, roughly a large garden. Move the threshold to 0.1 km² and 97% of them disappear, leaving about 5,600. Move it to 10 km² and you are left with 309.

FINLAND BY NUMBERS
Capital — Helsinki
Land area — 338,424 km²
Land borders — 3: Sweden, Norway, Russia
Official languages — Finnish and Swedish
Currency — euro

None of those numbers is wrong and none of them is the truth. They are three answers to three different questions, and the only reason 187,888 is the famous one is that it is the biggest.

Wikipedia says so itself, in a line most people scroll past: there is no standard unambiguous definition of the size requirements for a body of water to be classified as a lake. Every lake count you have ever seen — for Canada, for Minnesota, for anywhere — is a threshold someone picked.

The largest of them, Saimaa, is the fourth-largest natural freshwater lake in Europe.

This is the thing about superlatives. Somebody chose the units.

What other "fact" do you think is really just a measuring decision?
""",
    ["finland", "lakes", "saimaa", "helsinki", "geographyfacts", "didyouknow",
     "worldfacts", "maps", "nordic", "earthbynumbers"],
)

post(
    "djibouti-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Africa's lowest<br>point is a lake<br>saltier than<br>the Dead Sea.",
         "sub": "Five stats from the bottom of a continent."},
        {"type": "bignum", "kicker": "Stat 02", "number": "155", "numsize": "s3", "bg": "",
         "label": "metres below sea level — Lake Assal",
         "title": "The lowest point on land in Africa.", "size": "h-sm",
         "source": "Lake Assal. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "276.5", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "grams of salt per litre at the surface",
         "title": "The Dead Sea measures 268.8.", "size": "h-sm",
         "source": "Lake Assal. Average salt concentration 34.8%. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "54", "numsize": "s3", "bg": "",
         "label": "km² of liquid brine",
         "title": "The salt flat around it is bigger, at 68 km².", "size": "h-sm",
         "source": "Lake Assal. " + WIKI},
        {"type": "fact", "kicker": "Stat 05 — the catch", "bg": "sun", "size": "h-sm",
         "title": "Nobody can agree how salty it actually ranks.",
         "sub": "Wikipedia's own article calls Lake Assal the fifth most saline body of "
                "water in the world in one paragraph, and the second in another. The "
                "grams per litre are not in dispute. The league table is.",
         "source": "Lake Assal. " + WIKI},
    ],
    """
The lowest point on land in Africa is a lake, and it is saltier than the Dead Sea.

Lake Assal sits 155 metres below sea level in Djibouti. At the surface it measures 276.5 grams of salt per litre. The Dead Sea measures 268.8.

DJIBOUTI BY NUMBERS
Capital — Djibouti
Land area — 23,200 km²
Land borders — 3: Eritrea, Ethiopia, Somalia
Official languages — Arabic and French
Lake Assal — 155 m below sea level, 54 km²

The lake itself is small, 54 km² of liquid brine, with a crystallised salt flat of 68 km² around it. Average salt concentration is 34.8%, about ten times seawater. Salt has been cut and carried out of there by caravan for centuries.

Djibouti is a small country in an enormous position. It sits at the mouth of the Red Sea, and Wikipedia describes it as lying near some of the world's busiest shipping lanes, controlling access to the Red Sea and the Indian Ocean. Which is why so many countries pay rent for a base there.

One honest note. We cannot tell you where Lake Assal ranks for salinity, because Wikipedia's own article says fifth in its opening and second in its body. The concentration figures are consistent. The ranking is not, so we have left it out rather than pick the more impressive one.

Would you float in it, or is 34.8% salt too much?
""",
    ["djibouti", "lakeassal", "deadsea", "africa", "geographyfacts", "didyouknow",
     "worldfacts", "redsea", "travelinspo", "earthbynumbers"],
)

post(
    "kyrgyzstan-crazy", "crazy",
    [
        {"type": "hook", "size": "h-lg",
         "title": "Nowhere is<br>further from<br>the sea.",
         "sub": "Wikipedia's claim, not ours. Five stats from a country that is 80% mountain."},
        {"type": "bignum", "kicker": "Stat 02", "number": "80%", "numsize": "s2", "bg": "",
         "label": "of the country is the Tian Shan range",
         "title": "Over 80%, in fact. Less than 8% of the land is cultivated.", "size": "h-sm",
         "source": "Kyrgyzstan. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "7,439", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "metres — Jengish Chokusu, the high point",
         "title": "The country's LOWEST point is still 132 m above sea level.", "size": "h-sm",
         "source": "Kyrgyzstan. The low point is the Kara Darya river. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "668", "numsize": "s3", "bg": "",
         "label": "metres deep — Issyk-Kul",
         "title": "The second-largest mountain lake on Earth, after Titicaca.", "size": "h-sm",
         "source": "Issyk-Kul: 1,607 m elevation, 6,236 km². " + WIKI},
        {"type": "fact", "kicker": "Stat 05 — the catch", "bg": "sun", "size": "h-sm",
         "title": "Issyk-Kul rarely freezes, and the stated reason does not add up.",
         "sub": "Wikipedia says it is down to the lake's high salinity. The same page "
                "gives that salinity as about 0.6%. Seawater is 3.5%. Both sentences are "
                "on the same page.",
         "source": "Issyk-Kul. " + WIKI},
    ],
    """
Kyrgyzstan is further from the sea than any other country on Earth. That is Wikipedia's wording, not ours.

It is also mostly vertical. The Tian Shan range covers over 80% of the country, and less than 8% of the land is cultivated.

KYRGYZSTAN BY NUMBERS
Capital — Bishkek
Land area — 199,951 km²
Land borders — 4: Kazakhstan, Uzbekistan, Tajikistan, China
Highest point — Jengish Chokusu, 7,439 m
Lowest point — the Kara Darya river, 132 m

Read those last two together. The lowest place in the entire country is still 132 metres above sea level. There is nowhere in Kyrgyzstan that counts as low ground.

Then there is Issyk-Kul: 6,236 km², 668 metres deep, sitting at 1,607 metres. The second-largest mountain lake in the world after Titicaca, and the eighth-deepest lake of any kind.

An honest note on that lake. Wikipedia says Issyk-Kul rarely freezes because of its high salinity, then gives the salinity as roughly 0.6% — against 3.5% for seawater. Those two sentences are on the same page and they do not sit well together. We are repeating what the source says and flagging that it looks thin.

Landlocked is one thing. This is landlocked twice over, at altitude, behind a wall.

Would you rather be a long way from the sea, or a long way from everyone?
""",
    ["kyrgyzstan", "issykkul", "tianshan", "centralasia", "geographyfacts", "mountains",
     "didyouknow", "worldfacts", "adventuretravel", "earthbynumbers"],
)

post(
    "madagascar-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "All 651 land<br>snail species<br>here live<br>nowhere else.",
         "sub": "Five stats from an island that has been on its own for 88 million years."},
        {"type": "bignum", "kicker": "Stat 02", "number": "651", "numsize": "s3", "bg": "",
         "label": "terrestrial snail species, every one endemic",
         "title": "Not most of them. All of them.", "size": "h-sm",
         "source": "Wildlife of Madagascar. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "90%", "numsize": "s2",
         "bg": "ink", "sea": True,
         "label": "of its plant and animal species are endemic",
         "title": "Plants run lower, at more than 80% of 14,883 species.", "size": "h-sm",
         "source": "Wildlife of Madagascar. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "88", "numsize": "s3", "bg": "",
         "label": "million years since it split from India",
         "title": "It left Africa around 180 million years ago. Everything since has "
                  "evolved in isolation.", "size": "h-sm",
         "source": "Wildlife of Madagascar gives 88 million; the Madagascar article says "
                   "about 90 million. " + WIKI},
        {"type": "fact", "kicker": "Stat 05 — the hard part", "bg": "sun", "size": "h-sm",
         "title": "103 species of lemur, and 90% of them are threatened.",
         "sub": "That was a 2012 assessment. At least 17 lemur species have already gone "
                "extinct since people arrived on the island.",
         "source": "Wildlife of Madagascar. " + WIKI},
    ],
    """
Every single one of Madagascar's 651 terrestrial snail species is found nowhere else on Earth. Not most. All of them.

That is what 88 million years alone does to a place. Madagascar separated from Africa around 180 million years ago and from India about 88 million years ago, and everything living on it has been evolving in a sealed room ever since.

MADAGASCAR BY NUMBERS
Capital — Antananarivo
Land area — 587,041 km²
Land borders — none. It is the world's fourth-largest island
Official languages — Malagasy and French
Currency — ariary

Roughly 90% of all plant and animal species on the island are endemic. Reptiles run above 90% across more than 260 species. Plants are lower but still extraordinary: more than 80% of 14,883 species grow nowhere else. Some ecologists call the island the eighth continent, and the label is not really an exaggeration.

Now the part that is less fun. As of 2012 there were 103 recognised species and subspecies of lemur, and a 2012 assessment found 90% of lemur species threatened with extinction. At least 17 species have already gone, since humans arrived.

An island that spent 88 million years building something unrepeatable can lose it in a couple of centuries. Those two numbers belong in the same post.

Which animal would you most want to see before it is gone?
""",
    ["madagascar", "lemurs", "endemic", "wildlife", "biodiversity", "geographyfacts",
     "didyouknow", "worldfacts", "conservation", "earthbynumbers"],
)

# ═══════════════════════════════════════════════ SPOTLIGHTS ════════

spotlight(
    "spot-bhutan",
    "Bhutan is<br>98.8% mountain.",
    "Which makes it, by that measure, the most mountainous country in the world.",
    [["Capital", "Thimphu"], ["Land area", "38,394 km²"],
     ["Land borders", "2 — China, India"], ["Official language", "Dzongkha"],
     ["Currency", "Ngultrum (Nu.)"]],
    "Three reasons",
    [{"name": "The scale", "note": "98.8% of the country is mountain, and around 71% of the land is still under forest cover."},
     {"name": "Thimphu", "note": "At 2,320 m, the fifth-highest capital in the world and the highest in Asia."},
     {"name": "Two neighbours", "note": "China to the north, India to the south, and a border with nobody else at all."}],
    {"title": "The highest unclimbed mountain on Earth is here, and it is staying that way.",
     "sub": "Gangkhar Puensum, 7,570 m. Bhutan banned climbing peaks above 6,000 m in 1994 "
            "and banned mountaineering entirely in 2003.",
     "source": "Gangkhar Puensum. " + WIKI, "size": "h-sm"},
    "Three valleys",
    [{"name": "Paro", "note": "The valley most people arrive into, and the one they wish they had given longer."},
     {"name": "Punakha", "note": "Lower, warmer and greener, at the meeting of two rivers."},
     {"name": "Bumthang", "note": "Further east, harder to reach, and the reason to keep going past the first week."}],
    """
98.8% of Bhutan is mountain. By that measure Wikipedia calls it the most mountainous country in the world.

BHUTAN BY NUMBERS
Capital — Thimphu, at 2,320 m
Land area — 38,394 km²
Land borders — 2: China and India
Official language — Dzongkha
Currency — ngultrum

Thimphu is the fifth-highest capital city in the world and the highest in Asia. Around 71% of the country is under forest cover. Two neighbours, both enormous, and nobody else.

The detail that says the most about the place: Gangkhar Puensum, 7,570 m, is the highest unclimbed mountain on Earth. Not unclimbed because nobody has tried. Bhutan banned climbing peaks over 6,000 metres in 1994 and banned mountaineering altogether in 2003. There is a summit up there that no person has ever stood on, and that is a decision rather than an accident.

WHERE TO GO
Paro, the valley most people fly into and wish they had given longer. Punakha, lower and warmer, where two rivers meet. Bumthang, further east and harder to reach, which is the reason to keep going past the first week.

A country that decided some things are worth more unclimbed than climbed.

Is there anywhere you think should be left alone?
""",
    ["bhutan", "thimphu", "himalaya", "gangkharpuensum", "mountains", "geographyfacts",
     "travelbhutan", "offthebeatenpath", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-albania",
    "Albania has<br>two seas and<br>four borders.",
    "In a country slightly smaller than Belgium.",
    [["Capital", "Tirana"], ["Land area", "28,748 km²"],
     ["Land borders", "4"],
     ["Official language", "Albanian"], ["Currency", "Lek (L)"]],
    "Three reasons",
    [{"name": "Two coastlines", "note": "The Adriatic in the north, the Ionian in the south, and a different sea temperature on each."},
     {"name": "Still cheap", "note": "One of the last stretches of Mediterranean coast where a week does not cost a fortune."},
     {"name": "The mountains", "note": "The north is alpine, roadless in places, and crossed on foot between villages."}],
    {"title": "Four neighbours, and no two of them alike.",
     "sub": "Montenegro, Kosovo, North Macedonia and Greece, packed around a country "
            "smaller than Belgium's 30,528 km².",
     "source": DS, "size": "h-sm"},
    "Three past the beach",
    [{"name": "Berat", "note": "Ottoman-era houses stacked up a hillside, window above window."},
     {"name": "Theth to Valbona", "note": "A day's walk over a pass between two valleys in the northern alps."},
     {"name": "Gjirokastër", "note": "A stone town in the south, built grey and steep on the side of a hill."}],
    """
Albania has coastline on two seas. The Adriatic in the north, the Ionian in the south, in a country of 28,748 km² — slightly smaller than Belgium.

ALBANIA BY NUMBERS
Capital — Tirana
Land area — 28,748 km²
Land borders — 4: Montenegro, Kosovo, North Macedonia, Greece
Official language — Albanian
Currency — lek

Four neighbours packed around something smaller than Belgium, and no two of them alike. That is the whole character of the place: it has been the edge of somebody else's map for most of its history, and it shows in the architecture, the food and the language, which is its own branch of Indo-European with no close living relative.

It is also the last stretch of Mediterranean coast in Europe where a week does not cost a fortune, and that is not going to be true for much longer.

WHERE TO GO, past the beach:
Berat — Ottoman-era houses stacked up a hillside, window above window above window.
Theth to Valbona — a day's walk over a pass between two valleys in the northern alps, the best single day of walking in the Balkans.
Gjirokastër — a stone town in the south, grey and steep, built into the hill.

Go before the Riviera finishes turning into everybody else's Riviera.

Where did you go just before it got popular?
""",
    ["albania", "tirana", "berat", "gjirokaster", "theth", "balkans", "traveleurope",
     "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-colombia",
    "Nowhere has<br>more life per<br>square mile.",
    "Colombia is first in the world for biodiversity by area, and second overall.",
    [["Capital", "Bogotá"], ["Land area", "1,141,748 km²"],
     ["Land borders", "5"],
     ["Official language", "Spanish"], ["Currency", "Colombian peso ($)"]],
    "Three reasons",
    [{"name": "Two coasts", "note": "Caribbean to the north, Pacific to the west, and they feel like different countries."},
     {"name": "Altitude", "note": "You pick your climate by driving uphill. Bogotá is cold, the coast is not."},
     {"name": "Biodiversity", "note": "One of seventeen megadiverse countries, and the densest of the lot."}],
    {"title": "First in the world per square mile. Second overall.",
     "sub": "Wikipedia's wording: Colombia has the highest level of biodiversity per square "
            "mile in the world, and the second-highest level overall.",
     "source": "Colombia. " + WIKI, "size": "h-sm"},
    "Three past Cartagena",
    [{"name": "Medellín", "note": "A city in a narrow valley that rebuilt itself around cable cars and public libraries."},
     {"name": "Salento", "note": "Coffee country and the wax palm valley, where the palms are absurdly tall."},
     {"name": "Tayrona", "note": "Caribbean coast where the jungle runs down to the sand and nobody has built on it."}],
    """
Colombia has more biodiversity per square mile than any country on Earth, and the second-highest amount overall. That is Wikipedia's wording, and it is the single most useful fact about the place.

COLOMBIA BY NUMBERS
Capital — Bogotá
Land area — 1,141,748 km²
Land borders — 5: Panama, Venezuela, Brazil, Peru, Ecuador
Official language — Spanish
Currency — Colombian peso

Here is why. Colombia has a Caribbean coast to the north and a Pacific coast to the west, the Andes running up the middle, and Amazon lowland in the south. Altitude does the rest: you choose your climate by driving uphill, from hot coast to cold capital in a morning. Stack that many habitats into one country and you get one of the seventeen megadiverse countries, and the densest of them.

The two coasts genuinely feel like different countries. The Caribbean side is loud, hot and built for it. The Pacific side is wet, forested and barely visited.

WHERE TO GO, past Cartagena:
Medellín — a city in a narrow valley that rebuilt itself around cable cars and public libraries.
Salento — coffee country, and a valley of wax palms that are an unreasonable height.
Tayrona — Caribbean coast where the jungle runs down to the sand and nobody built on it.

Two oceans, three mountain ranges and the Amazon, in one country.

Caribbean coast or Pacific coast — which one are you picking?
""",
    ["colombia", "medellin", "cartagena", "salento", "tayrona", "biodiversity",
     "southamerica", "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-uzbekistan",
    "Uzbekistan is<br>doubly<br>landlocked.",
    "To reach any sea you cross two borders. Only one other country on Earth qualifies.",
    [["Capital", "Tashkent"], ["Land area", "447,400 km²"],
     ["Land borders", "5"],
     ["Official language", "Uzbek"], ["Currency", "Soʻm"]],
    "Three reasons",
    [{"name": "The Silk Road cities", "note": "Samarkand, Bukhara and Khiva, which grew rich on the trade and still look it."},
     {"name": "Tilework", "note": "Whole facades in blue glazed tile, at a scale that does not photograph properly."},
     {"name": "Still quiet", "note": "The infrastructure improved faster than the visitor numbers did."}],
    {"title": "Even that claim comes with an argument attached.",
     "sub": "Wikipedia notes Uzbekistan's doubly landlocked status depends on whether the "
            "Caspian Sea counts as a lake or a sea. Liechtenstein has no such asterisk.",
     "source": "Landlocked country. " + WIKI, "size": "h-sm"},
    "Three cities",
    [{"name": "Samarkand", "note": "The Registan, three tiled facades around one square. Go at opening and again at dusk."},
     {"name": "Bukhara", "note": "Smaller, older-feeling, and the one people end up liking most."},
     {"name": "Khiva", "note": "A walled town you can cross in twenty minutes, best stayed in overnight once the buses go."}],
    """
Uzbekistan is one of only two doubly landlocked countries in the world. To reach any sea from inside it you cross at least two national borders. The other one is Liechtenstein.

UZBEKISTAN BY NUMBERS
Capital — Tashkent
Land area — 447,400 km²
Land borders — 5: Kazakhstan, Kyrgyzstan, Tajikistan, Afghanistan, Turkmenistan
Official language — Uzbek
Currency — so'm

It is also the only Central Asian state that borders all four of the others, which tells you most of what you need to know about where it sits.

Even the headline fact has an argument inside it. Wikipedia notes that Uzbekistan's doubly landlocked status depends on whether the Caspian Sea is counted as a lake or a sea. If the Caspian is a sea, the claim fails. Liechtenstein has no such asterisk. We are telling you because you will meet someone who brings it up.

Being that far inland is the reason the place exists in the form it does. Bukhara and Samarkand became extremely wealthy on overland trade along what became the Silk Road, and the money went into tilework.

WHERE TO GO
Samarkand — the Registan, three tiled facades around one square. Go at opening, then again at dusk.
Bukhara — smaller, older-feeling, and the one most people end up preferring.
Khiva — a walled town you cross in twenty minutes. Stay the night and have it to yourself.

One more thing worth knowing: the Aral Sea, on the northern border, has shrunk to about 10% of its former area since the 1960s.

Two borders from the sea. Could you live that far inland?
""",
    ["uzbekistan", "samarkand", "bukhara", "khiva", "silkroad", "centralasia",
     "geographyfacts", "doublylandlocked", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-ethiopia",
    "Ethiopia has<br>thirteen months<br>in its year.",
    "And right now it is not the year you think it is.",
    [["Capital", "Addis Ababa"], ["Land area", "1,104,300 km²"],
     ["Land borders", "6"],
     ["Official language", "Amharic"], ["Currency", "Birr (Br)"]],
    "Three reasons",
    [{"name": "The highlands", "note": "Addis Ababa sits at 2,355 m, the fourth-highest capital in the world and the highest in Africa."},
     {"name": "The Danakil", "note": "Wikipedia calls it the hottest place on Earth by year-round average temperature."},
     {"name": "Its own thread", "note": "Own calendar, own script, own clock. Very little of it borrowed."}],
    {"title": "Twelve months of thirty days, then a thirteenth month of five.",
     "sub": "Six in a leap year. The new year falls on 11 September, or the 12th in the "
            "year before a leap year. The year number runs eight behind the Gregorian "
            "until September, then seven.",
     "source": "Ethiopian calendar. " + WIKI, "size": "h-sm"},
    "Three to build a trip around",
    [{"name": "Lalibela", "note": "Churches cut downwards into solid rock rather than built up out of it."},
     {"name": "Simien Mountains", "note": "Escarpment walking at altitude, with gelada troops that ignore you completely."},
     {"name": "Danakil", "note": "Sulphur fields and salt flats. Go with people who know it, and go in winter."}],
    """
Ethiopia's calendar has thirteen months. Twelve of thirty days each, then a thirteenth month called Pagumen with five days in it — six in a leap year.

The year number runs eight behind the Gregorian calendar until 10 or 11 September, then seven behind for the rest of the year. New year falls on 11 September, or the 12th in the year before a leap year.

ETHIOPIA BY NUMBERS
Capital — Addis Ababa, at 2,355 m
Land area — 1,104,300 km²
Land borders — 6: Eritrea, Djibouti, Somalia, Kenya, South Sudan, Sudan
Official language — Amharic
Currency — birr

Addis Ababa is the fourth-highest capital city in the world and the highest in Africa. Ethiopia is also the most populous landlocked country on Earth.

Its own calendar, its own script, its own way of counting the hours. Wikipedia describes Ethiopia, alongside Liberia, as the only African country never to have been fully colonised — and is careful about that wording, because Italy did occupy the country from 1936 to 1941.

WHERE TO GO
Lalibela — churches cut downwards into solid rock instead of built up out of it.
Simien Mountains — escarpment walking at altitude, with gelada troops that ignore you entirely.
Danakil Depression — sulphur fields and salt flats, and what Wikipedia calls the hottest place on Earth by year-round average temperature. Go with people who know it, and go in winter.

A country that kept its own thread while the continent around it was cut up.

Would you rather lose six years or gain a month?
""",
    ["ethiopia", "addisababa", "lalibela", "simienmountains", "danakil", "africa",
     "geographyfacts", "ethiopiancalendar", "travelinspo", "earthbynumbers"],
)

# ═══════════════════════════════════════════════════ TOP 5s ════════

top5(
    "top5-markets",
    "Camden Market<br>is a gift shop<br>with a roof.",
    "Five markets where people actually buy their dinner. Opinion.",
    [
        ("Grand Bazaar", "Istanbul, Türkiye",
         "61 covered streets, and somewhere between 250,000 and 400,000 people walking "
         "them every day. Running since the winter of 1455.",
         "Grand Bazaar, Istanbul. The page says 4,000 shops in one place and 3,000 in "
         "another. " + WIKI),
        ("Chatuchak", "Bangkok, Thailand",
         "More than 15,000 stalls across 27 sections, and over 200,000 visitors every "
         "weekend. Go at 8am or do not go.",
         "Chatuchak Weekend Market. " + WIKI),
        ("Jemaa el-Fnaa", "Marrakech, Morocco",
         "A square, not a hall. It sells carpets by day and turns into several hundred "
         "food stalls after dark.", ""),
        ("Khan el-Khalili", "Cairo, Egypt",
         "A bazaar quarter that has been trading on the same lanes since the 14th century, "
         "and still sells to Cairo rather than to visitors.", ""),
        ("Mercat Central", "Valencia, Spain",
         "A modernista iron and glass hall where the city genuinely does its shopping, "
         "which is rarer than it sounds.", ""),
    ],
    """
Camden Market is a gift shop with a roof. So is most of Borough on a Saturday. A market is where people buy their dinner, not where they buy a fridge magnet shaped like the place they are standing in.

Five that still work:

01 GRAND BAZAAR, Istanbul — 61 covered streets and between 250,000 and 400,000 people a day, trading since the winter of 1455. Yes, parts of it sell tat. Go deeper in and it is still a working wholesale district. Wikipedia itself cannot decide whether it holds 3,000 shops or 4,000.

02 CHATUCHAK, Bangkok — more than 15,000 stalls in 27 sections, over 200,000 visitors every weekend. Arrive at eight or do not bother.

03 JEMAA EL-FNAA, Marrakech — a square rather than a hall, carpets by day, several hundred food stalls after dark.

04 KHAN EL-KHALILI, Cairo — a bazaar quarter trading on the same lanes since the 14th century, still selling to Cairo rather than to visitors.

05 MERCAT CENTRAL, Valencia — a modernista iron and glass hall where the city actually does its shopping. Rarer than it sounds.

This is opinion. The visitor counts are not.

Which market would you defend, and which one is a tourist trap you fell for?
""",
    ["markets", "grandbazaar", "chatuchak", "jemaaelfnaa", "cairo", "streetfood",
     "traveltheworld", "foodtravel", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-hot-springs",
    "The Blue Lagoon<br>is power plant<br>run-off.",
    "Wikipedia's word, not ours: man-made. Five that are not. Opinion.",
    [
        ("Onsen towns", "Japan",
         "Roughly 25,000 hot spring sources nationwide and about 3,000 onsen using them. "
         "You are never far from one.",
         "Onsen. " + WIKI),
        ("Pamukkale", "Türkiye",
         "White travertine terraces built by 17 hot springs running from 35 °C to 100 °C. "
         "UNESCO-listed with Hierapolis since 1988.",
         "Pamukkale. More than two million visitors annually. " + WIKI),
        ("Hveravellir", "Iceland",
         "A geothermal field in the middle of the interior, reached on a rough track, with "
         "one small pool and no gift shop.", ""),
        ("Termas Geométricas", "Chile",
         "Seventeen slate pools on walkways up a forested gorge, fed by the stream running "
         "under them.", ""),
        ("Saturnia", "Italy",
         "Cascate del Mulino: free, open all night, and a stack of limestone bowls with "
         "37 °C water falling through them.", ""),
    ],
    """
The Blue Lagoon is not a natural hot spring. Wikipedia's own words: the lagoon is man-made, and the water is a byproduct of the Svartsengi geothermal power plant next door. It is lovely. It is also industrial run-off at 37 to 39 degrees, and 1.3 million people paid to sit in it in 2017.

Five that came out of the ground on their own:

01 ONSEN TOWNS, Japan — roughly 25,000 hot spring sources across the country feeding about 3,000 onsen. The whole culture is built around them, which is the difference between a bath and an attraction.

02 PAMUKKALE, Türkiye — white travertine terraces deposited by 17 springs running anywhere from 35 °C to 100 °C. UNESCO-listed alongside Hierapolis since 1988, and busy with it: more than two million visitors a year.

03 HVERAVELLIR, Iceland — a geothermal field in the middle of the interior, up a rough track, one small pool, no queue. The Blue Lagoon's exact opposite, in the same country.

04 TERMAS GEOMÉTRICAS, Chile — seventeen slate pools on red walkways up a forested gorge, fed by the stream beneath them.

05 SATURNIA, Italy — the Cascate del Mulino. Free, open all night, limestone bowls with 37 °C water pouring through.

Opinion, as always. The temperatures and the counts are Wikipedia's.

Is the Blue Lagoon still worth it, knowing what the water is?
""",
    ["hotsprings", "bluelagoon", "onsen", "pamukkale", "iceland", "saturnia",
     "traveltheworld", "geothermal", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-ancient-cities",
    "Pompeii is a<br>building site.",
    "Two-thirds excavated, 2.5 million visitors a year, and still a letdown. Five that are not. Opinion.",
    [
        ("Leptis Magna", "Khoms, Libya",
         "A Roman city of about 100,000 people at its height, 130 km east of Tripoli, "
         "UNESCO-listed since 1982, and visited by almost nobody.",
         "Leptis Magna. " + WIKI),
        ("Petra", "Jordan",
         "Nabataean capital from the second century BC, carved into rock across a 264 km² "
         "site. 1,135,300 visitors in 2019, and most of them see one facade.",
         "Petra. " + WIKI),
        ("Hierapolis", "Pamukkale, Türkiye",
         "A Hellenistic Greek city with a main street 1,500 m long and a theatre seating "
         "15,000, above the travertine terraces.",
         "Hierapolis. UNESCO-listed 1988. " + WIKI),
        ("Ani", "Kars, Türkiye",
         "A medieval Armenian capital abandoned on a gorge that is now an international "
         "border. Churches standing alone in grassland.", ""),
        ("Tikal", "Petén, Guatemala",
         "Maya temples pushing up through rainforest canopy. Stay inside the park and be "
         "at the top of one at dawn.", ""),
    ],
    """
Pompeii is a building site. Two-thirds of it has been excavated, roughly 2.5 million people a year walk through it, and most of them leave wondering what they missed. It is important. It is not enjoyable.

Five ancient cities that are:

01 LEPTIS MAGNA, Libya — a Roman city of around 100,000 people at its height, on the coast 130 km east of Tripoli, UNESCO-listed since 1982. One of the best-preserved Roman sites anywhere and almost nobody goes.

02 PETRA, Jordan — Nabataean capital from the second century BC, carved into rock across a site of 264 km². 1,135,300 visitors in 2019, and nearly all of them photograph one facade and leave. Walk further.

03 HIERAPOLIS, Türkiye — a Hellenistic Greek city sitting directly above the Pamukkale terraces, with a main street 1,500 m long and a theatre that seated 15,000. People come for the white pools and walk past a whole city.

04 ANI, Türkiye — a medieval Armenian capital abandoned on a gorge that is now an international border. Churches standing by themselves in open grassland.

05 TIKAL, Guatemala — Maya temples coming up through the rainforest canopy. Stay inside the park so you can be on top of one at dawn.

Ranking ruins is opinion. The visitor numbers and the dates are Wikipedia's.

Go on, defend Pompeii.
""",
    ["ruins", "ancienthistory", "leptismagna", "petra", "hierapolis", "ani", "tikal",
     "archaeology", "traveltheworld", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-ferries",
    "A cruise ship<br>is the worst<br>way to see<br>a coast.",
    "Five working ferries that beat it, and cost a fraction. Opinion.",
    [
        ("Hurtigruten", "Norway",
         "34 ports of call northbound and 33 southbound, worked by eleven ships. It is a "
         "mail and freight run that happens to be spectacular.",
         "Hurtigruten. " + WIKI),
        ("Belém to Manaus", "Brazil",
         "Several days up the Amazon in a hammock you buy at the dock, on a boat that is "
         "carrying people and cargo rather than passengers.", ""),
        ("Alaska Marine Highway", "United States",
         "A state ferry system serving towns with no road in. Sleep on deck in a tent "
         "taped down against the wind.", ""),
        ("Jadrolinija coastal", "Croatia",
         "Island to island down the Dalmatian coast on the boats the islanders use, for "
         "the price of a sandwich.", ""),
        ("Piraeus to the Dodecanese", "Greece",
         "An overnight run that stops at islands at three in the morning and puts six "
         "people and a crate of oranges ashore.", ""),
    ],
    """
A cruise ship is the worst way to see a coast. You arrive with four thousand people, you get six hours, and the port has rebuilt itself around exactly that. The ferry leaving from the next berth is going to the same places, costs a fraction, and is full of people who live there.

Five worth planning a trip around:

01 HURTIGRUTEN, Norway — 34 ports of call northbound and 33 southbound, worked by eleven ships. It is a mail and freight route that happens to run up one of the great coastlines. It calls in the middle of the night at places no cruise would bother with.

02 BELÉM TO MANAUS, Brazil — several days up the Amazon in a hammock you buy at the dock. Cargo below, families above, and nobody performing anything for you.

03 ALASKA MARINE HIGHWAY — a state ferry system serving towns with no road in. People sleep on the solarium deck in tents taped down against the wind.

04 JADROLINIJA COASTAL, Croatia — island to island down the Dalmatian coast on the boats the islanders actually use.

05 PIRAEUS TO THE DODECANESE, Greece — an overnight run that stops at an island at three in the morning to put six people and a crate of oranges ashore. That is the whole appeal.

Opinion. The Hurtigruten numbers are Wikipedia's.

What is the best boat you have ever been on that was not trying to entertain you?
""",
    ["ferries", "hurtigruten", "amazon", "alaska", "croatia", "greece", "slowtravel",
     "traveltheworld", "travelinspo", "earthbynumbers"],
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        (OUT / f"{p['slug']}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False))
    print(f"wrote {len(POSTS)} posts")
    for p in POSTS:
        print(f"  {p['slug']:22s} {p['kind']:9s} {len(p['slides'])} slides  "
              f"{len(p['caption'])} caption chars  {len(p['tags'])} tags")


if __name__ == "__main__":
    main()
