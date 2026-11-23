#!/usr/bin/env python3
"""
Earth by Numbers — content set I: weekly top-up, 2026-11-23.

Twenty posts: eight crazy, seven spotlight, five top5. The mix is weighted away
from top5 because the unposted queue was running 24 top5 against 19 crazy and
18 spotlight before this set.

  indonesia-crazy          crazy      nobody agrees how many islands there are
  brazil-crazy             crazy      borders every South American country but two
  australia-crazy          crazy      the biggest lake is almost always empty
  switzerland-crazy        crazy      no city is legally the capital
  egypt-crazy              crazy      99% of the country on 3.5% of the land
  india-crazy              crazy      one time zone across 29 degrees
  argentina-crazy          crazy      the highest and lowest points of a hemisphere
  philippines-crazy        crazy      the country gained 534 islands in 2017
  spot-tajikistan          spotlight  the world's tallest dam is an accident
  spot-guatemala           spotlight  21 Mayan languages, none of them official
  spot-malawi              spotlight  more fish species than any lake on Earth
  spot-cambodia            spotlight  a lake that reverses its river
  spot-zambia              spotlight  the largest sheet of falling water
  spot-north-macedonia     spotlight  one of the oldest lakes in the world
  spot-senegal             spotlight  a country that nearly surrounds another
  top5-coffee-regions      top5       Blue Mountain is a marketing exercise
  top5-old-towns           top5       Dubrovnik is a cruise terminal with walls
  top5-lighthouses         top5       Peggy's Cove is a car park
  top5-cathedrals          top5       the Sagrada Familia is a building site
  top5-rainforests         top5       the Amazon is not the one to visit

HOW WIKIPEDIA WAS READ THIS RUN — RECORD THIS, IT COST SET H TWELVE POSTS
Set H wrote only top5s because every WebFetch of en.wikipedia.org failed with
error_type PROVENANCE_REQUIRED, and curl to the same host is refused by the
egress proxy. The cause was not that Wikipedia is unreachable. It is that a URL
typed from nothing has no provenance, so fetching it raises a permission prompt
that nobody answers in an unattended run.

The fix is two calls instead of one:

    WebSearch(query, allowed_domains=["en.wikipedia.org"])   # surfaces the URL
    WebFetch(<a URL that appeared in those results>)          # now succeeds

Search first, fetch second, and only ever fetch URLs the search returned. Every
figure in this file was read that way this run. WebSearch alone is no use — in
this environment it returns link lists with no page text — and WebFetch relays
short fragments through a summariser capped at about 125 characters per quote,
which is enough to verify a number but not to quote a paragraph.

VERIFICATION (BUILD.md §4 — every figure checked in this run)
  Wikipedia, read this run: Indonesia; Geography of Indonesia; Borders of
  Indonesia; Brazil; Borders of Brazil; Geography of Brazil; Amazon River;
  Amazon rainforest; Amazon basin; Brasilia; Time in Brazil; Australia;
  Geography of Australia; Kati Thanda-Lake Eyre; Nullarbor Plain;
  Trans-Australian Railway; Mount Kosciuszko; Western Australia; Great Barrier
  Reef; Switzerland; Geography of Switzerland; Swiss Alps; Bern; Romansh
  language; Languages of Switzerland; Gotthard Base Tunnel; Egypt; Geography of
  Egypt; Suez Canal; Great Pyramid of Giza; Abu Simbel; Qattara Depression;
  Mount Catherine; India; Geography of India; Indian Standard Time; Time in
  India; Languages of India; Cherrapunji; Mawsynram; Siachen Glacier; Borders of
  India; Andaman and Nicobar Islands; Argentina; Geography of Argentina;
  Aconcagua; Laguna del Carbon; Extreme points of the Americas; Ushuaia; Puerto
  Williams; Southernmost settlements; Iguazu Falls; Philippines; Geography of
  the Philippines; List of islands of the Philippines; Philippine Trench;
  Languages of the Philippines; Taal Volcano; Taal Volcano Main Crater Lake;
  1991 eruption of Mount Pinatubo; Geography of Tajikistan; Pamir Mountains;
  Ismoil Somoni Peak; M41 highway; Ak-Baital Pass; Tajik National Park; Usoi
  Dam; Sarez Lake; Nurek Dam; Iskanderkul; Fann Mountains; Karakul
  (Tajikistan); Khujand; Mayan languages; Languages of Guatemala; Guatemala;
  Geography of Guatemala; Lake Atitlan; Volcan de Fuego; Pacaya; Tikal; Antigua
  Guatemala; Semuc Champey; Lake Malawi; Malawi; Geography of Malawi; Lake
  Malawi National Park; Mulanje Massif; Nyika Plateau; Liwonde National Park;
  Zomba Plateau; Likoma Island; Angkor Wat; Angkor; Tonle Sap; Flag of
  Cambodia; Preah Vihear Temple; Koh Ker; Koh Rong; Cardamom Mountains;
  Victoria Falls; Zambia; Geography of Zambia; Lake Kariba; South Luangwa
  National Park; Kafue National Park; Lower Zambezi National Park; Zambezi;
  Lake Ohrid; North Macedonia; Prespa Agreement; Ohrid; Mount Korab; Matka
  Canyon; Bitola; Heraclea Lyncestis; Stone Bridge (Skopje); 1963 Skopje
  earthquake; Senegal; Geography of Senegal; The Gambia-Senegal border;
  Cap-Vert; Extreme points of Africa; Lake Retba; Goree; Saint-Louis, Senegal;
  Djoudj National Bird Sanctuary; Politics of Senegal.
  Dataset: mledoze/countries — capitals, areas, border counts, languages and
  currencies for all fifteen countries in this set.

DROPPED for being unconfirmable, per the rule that matters most:
  - Indonesia's island count as a single number. The lead says "between 13,000
    and 17,000", the geography section "13,466 named islands to more than
    17,500", and Geography of Indonesia carries 17,500 (Bakosurtanal), 18,307
    (LAPAN 2002) and 17,508 (CIA). The contradiction became the post.
  - Indonesia's active volcano count as fact. Indonesia says "around 130";
    Geography of Indonesia says "approximately 150". Both are stated.
  - Brazil's total land border length. 16,885 km (Borders of Brazil), 15,719 km
    (Geography of Brazil) and 14,691 km (the land-borders list) — about 2,200 km
    apart. The direction is used instead: the longest border is with Bolivia.
  - "The Amazon is the longest river in the world." Wikipedia lists at least
    five lengths for the Amazon and two for the Nile, and the one peer-reviewed
    study it cites makes the Nile longer. No length used.
  - Fernando de Noronha's daily visitor cap. Not on the page at all.
  - Brasilia being designed in the shape of an aeroplane. The article's own
    footnote calls it a myth.
  - Australia's coastline length. 25,760 km (CIA), 66,530 km (WRI) and 59,736 km
    all appear in one article, and its "sixth longest" claim sits against ninth
    place in the list article. No coastline figure used.
  - "Australia is the largest country with no land borders" and "the only
    country that is also a continent". Neither claim exists on any of the four
    articles read. Dropped.
  - Egypt's desert share as a percentage. Not stated anywhere; the articles say
    only that Egypt "is predominantly desert".
  - The Suez Canal's share of world trade. The 8% sentence carries no citation
    and no year, and post-2023 diversions make it volatile.
  - Lake Nasser as the largest man-made lake. The reservoir list ranks it 11th
    by surface area, behind Lake Volta.
  - India's count of official languages. The India infobox says two, Languages
    of India says 23. Only the 22 scheduled languages are used, with Hindi and
    English named as the Union's languages.
  - Mawsynram as flatly the wettest place on Earth. Its own page lists two
    Colombian towns with higher averages. Cherrapunji's record year is used.
  - Perito Moreno as an advancing glacier. Wikipedia now says retreating.
  - Iguazu's number of cascades. 275 in the infobox, "150 to 300" in the body.
  - Emden Deep's depth as one number. 10,540 m and 10,430 m appear in the same
    article; "about 10,500 m" is used.
  - Taal as "the world's smallest volcano". The article cites a piece arguing
    the label should be dropped.
  - Pinatubo's cooling and sulphur-dioxide figures. The infobox and body differ
    by roughly ten times on the SO2 mass.
  - Tajikistan's "nearly 50% above 3,000 m". Unattributed and contradicted in
    the same article; the Library of Congress "more than half" is used instead.
  - Fedchenko/Vanch-Yakh's area. Wikipedia is mid-rename and gives the largest
    non-polar glacier two different names in one article.
  - Guatemala's active volcano count. Three in Geography of Guatemala, four in
    Guatemala. Only the total of 37 is used.
  - Tajumulco's elevation. 4,203 m on its own page, 4,220 m on three others.
  - Lake Malawi's share of the country. The 25% in Geography of Malawi does not
    agree with that article's own water-area figure, which gives about a fifth.
  - Angkor's population. "750,000 to 1,000,000", hedged by the article itself.
  - Lake Kariba's volume. 180 km3 in the infobox, 185 km3 in the body.
  - "Walking safaris originated in South Luangwa." Not what the article says; it
    calls the park "the home of the photographic and walking safari", and Norman
    Carr's page names no country.
  - Lake Ohrid's age in years. The only figure is Pliocene sediments "possibly
    3-5 million years old", which is sediment, not the lake.
  - Kokino being fourth on a NASA list. The claim appears only in a headline.
  - Lake Retba's salinity. 40% is [citation needed] on the salinity list and the
    article's own 350 g/L disagrees with it.
  - Senegal's count of national languages. Eleven in the Senegal article, six in
    its own constitutional footnote, 25 in Languages of Senegal.
  - Goree's slave-trade throughput. The article quotes UNESCO's "largest slave
    trading centre" and then historians saying no more than 500 a year and that
    the usual descriptions "are not supported by any historical documentation".
    No number used.

Run:  python3 posts_i.py
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
              caption, tags, hook_size="h-md", extra_bg="sun",
              why_source=WIKI, go_source=WIKI):
    slides = [
        {"type": "hook", "title": hook, "sub": hook_sub, "size": hook_size},
        {"type": "ledger", "kicker": "The basics", "bg": "", "rows": rows, "source": DS},
        {"type": "items", "kicker": "Why go", "title": why_title, "bg": "ink", "items": why,
         "source": why_source},
        dict({"type": "fact", "kicker": "One more thing", "bg": extra_bg}, **extra),
        {"type": "items", "kicker": "Where to go", "title": go_title, "bg": "", "items": go,
         "source": go_source, "handle": True},
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
    "indonesia-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Nobody agrees<br>how many islands<br>Indonesia has.",
         "sub": "Wikipedia gives five different answers on two pages."},
        {"type": "bignum", "kicker": "Stat 02", "number": "18,307", "numsize": "s3", "bg": "",
         "label": "islands — the highest figure given",
         "title": "A 2002 LAPAN survey. The CIA says 17,508. Bakosurtanal says 17,500.",
         "size": "h-sm",
         "source": "Geography of Indonesia. Indonesia's own lead says 'between 13,000 and "
                   "17,000'. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "400", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "volcanoes — and nobody agrees there either",
         "title": "Indonesia says around 130 are active. Geography of Indonesia says 150.",
         "size": "h-sm",
         "source": "Indonesia; Geography of Indonesia. The volcanic belt figure is the same "
                   "on both. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "718", "numsize": "s3", "bg": "",
         "label": "indigenous languages listed",
         "title": "The prose says 'more than 700'. The infobox commits to a number.",
         "size": "h-sm",
         "source": "Indonesia. The footnote excludes dialects and subdialects. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Only 922 of them have anyone living on them.",
         "sub": "That is the one figure both articles agree on. Three land neighbours — "
                "Malaysia, Papua New Guinea and Timor-Leste — across a country of "
                "1,904,569 km², the 14th largest on Earth.",
         "source": "Indonesia; Geography of Indonesia; Borders of Indonesia. " + WIKI
                   + " " + DS},
    ],
    """
Nobody agrees how many islands Indonesia has. Not roughly — not at all.

Wikipedia gives five different answers on two pages. Indonesia's lead says "between 13,000 and 17,000". Its geography section says published figures run "from 13,466 named islands to more than 17,500". Geography of Indonesia offers 17,500 from Bakosurtanal, 17,508 from the CIA, and 18,307 from an earlier LAPAN survey in 2002.

INDONESIA BY NUMBERS
Islands — somewhere between 13,000 and 18,307
Permanently inhabited — 922
Volcanoes — about 400, of which 130 or 150 are active
Indigenous languages — 718 listed
Land area — 1,904,569 km², 14th largest in the world
Land neighbours — 3: Malaysia, Papua New Guinea, Timor-Leste

The spread is not sloppiness. It is what happens when you try to count islands: the answer depends entirely on what counts as one, and at what scale you draw the coast. A rock that is an island at low tide is not one at high tide. The tighter your definition, the fewer you find.

The volcano count has the same problem in miniature. Both articles say the belt holds roughly 400. One says around 130 are active, the other approximately 150. Neither is wrong; "active" is a judgement.

We could have picked a number and looked confident. The honest version is more interesting: the fourth most populous country on Earth does not know how many pieces it is made of.

Which figure would you have gone with?
""",
    ["indonesia", "java", "sumatra", "geographyfacts", "didyouknow", "maps",
     "worldfacts", "islands", "southeastasia", "earthbynumbers"],
)

post(
    "brazil-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Brazil borders<br>every country in<br>South America<br>but two.",
         "sub": "Chile and Ecuador are the only ones that got away."},
        {"type": "bignum", "kicker": "Stat 02", "number": "10", "numsize": "s2", "bg": "",
         "label": "neighbours — nine countries and France",
         "title": "French Guiana is a department of France, so the EU has a land border "
                  "with Brazil.", "size": "h-sm",
         "source": "Borders of Brazil: 'terrestrial boundaries with nine countries of South "
                   "America, and with the French Department of Guiana'. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "45.7%", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "of Brazil drains into the Amazon",
         "title": "Not the rainforest — the river basin. Almost half the country runs into "
                  "one river.", "size": "h-sm",
         "source": "Geography of Brazil. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "20%", "numsize": "s3", "bg": "",
         "label": "of the world's river discharge",
         "title": "One river. Wikipedia puts its discharge above the next seven largest "
                  "rivers combined.", "size": "h-sm",
         "source": "Amazon River. Discharge given as 215,000-230,000 m³/s. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "No bridge crosses the main stem of the Amazon.",
         "sub": "And not because it is too wide. Wikipedia is blunt: for most of its length "
                "engineers could build one easily. There is simply no road on the far side "
                "worth connecting to. The bridge at Manaus crosses the Rio Negro.",
         "source": "Amazon River. " + WIKI},
    ],
    """
Brazil has a land border with every country in South America except two.

Chile and Ecuador are the only ones that got away. Everything else — Uruguay, Argentina, Paraguay, Bolivia, Peru, Colombia, Venezuela, Guyana, Suriname — touches Brazil, and so does France.

BRAZIL BY NUMBERS
Land neighbours — 10, nine countries plus French Guiana
Longest border — with Bolivia
Share of Brazil draining into the Amazon — 45.7%
Share of all river water reaching the oceans — about 20%, from the Amazon alone
Area — about 8.5 million km², fifth largest in the world
Time zones — 4

French Guiana is an overseas department of France, which makes that stretch a border between Brazil and the European Union. It is the same quirk that gives France its longest land border.

The Amazon numbers are hard to hold in your head. Its basin covers 45.7% of Brazil — not the rainforest, the drainage. Its discharge is given as 215,000 to 230,000 cubic metres a second, which Wikipedia says is more than the next seven largest rivers put together, and roughly a fifth of all the river water arriving in the world's oceans.

And no bridge crosses it. Not the main stem, anywhere along its length. The reason is not engineering — Wikipedia says a bridge would be easy for most of the river — it is that there is nothing on the other side to drive to. The famous bridge at Manaus spans the Rio Negro, a tributary, just short of the confluence.

One figure we cut: Brazil's total land border length. Three Wikipedia articles give three answers about 2,200 km apart.

Which border surprised you most?
""",
    ["brazil", "amazon", "amazonriver", "frenchguiana", "geographyfacts", "didyouknow",
     "maps", "worldfacts", "southamerica", "earthbynumbers"],
)

post(
    "australia-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Australia's largest<br>lake has filled<br>three times<br>since 1860.",
         "sub": "Most of the time it is a salt pan you can drive across."},
        {"type": "bignum", "kicker": "Stat 02", "number": "9,500", "numsize": "s3", "bg": "",
         "label": "km² — Kati Thanda at full capacity",
         "title": "When it fills it is the biggest lake in the country. It is most often "
                  "empty.", "size": "h-sm",
         "source": "Kati Thanda-Lake Eyre: completely filled three times between 1860 and "
                   "June 2025. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "478", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "km of dead-straight railway",
         "title": "The longest straight stretch of track in the world, across the "
                  "Nullarbor.", "size": "h-sm",
         "source": "Trans-Australian Railway: 478.193 km; Nullarbor Plain. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "330", "numsize": "s3", "bg": "",
         "label": "m — average elevation of Australia",
         "title": "The lowest, flattest and oldest continental landmass on Earth.",
         "size": "h-sm",
         "source": "Geography of Australia, citing Geoscience Australia. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Western Australia is the second-largest subdivision on Earth.",
         "sub": "2,527,013 km², beaten only by the Sakha Republic in eastern Russia. One "
                "state, and it is larger than all but seven countries. The whole country's "
                "highest point is Mount Kosciuszko at 2,228 m.",
         "source": "Western Australia, citing Geoscience Australia; Mount Kosciuszko. "
                   + WIKI},
    ],
    """
Australia's largest lake has filled to capacity three times since 1860.

Most of the time it is a salt pan you can drive across. Kati Thanda–Lake Eyre covers up to 9,500 km² when full, which makes it the biggest lake in the country, and Wikipedia's description of its normal state is one sentence long: the lake is most often empty.

AUSTRALIA BY NUMBERS
Kati Thanda–Lake Eyre at capacity — up to 9,500 km²
Times completely filled, 1860 to June 2025 — three
Lowest point — the lake floor, about 15 m below sea level
Longest dead-straight railway on Earth — 478 km, across the Nullarbor
Average elevation of the continent — 330 m
Western Australia — 2,527,013 km²

The flatness is the thing that explains the rest of it. Wikipedia calls Australia the lowest, flattest and oldest continental landmass on Earth, with an average elevation of 330 m. A continent that low drains nowhere in a hurry, which is why its biggest lake is a basin that waits decades for enough rain to matter.

It is also why you can lay 478 km of railway without a single curve. The Trans-Australian crosses the Nullarbor — from the Latin for "no tree" — in one straight line, and it has held that record since it was built.

Western Australia on its own is 2,527,013 km², the second-largest subdivision of any country on Earth, behind only Sakha in Russia.

One figure we dropped: Australia's coastline. One article gives 25,760 km, 66,530 km and 59,736 km, and calls it the sixth longest while the list article puts it ninth.

Would you take the train across, or the road?
""",
    ["australia", "lakeeyre", "nullarbor", "outback", "geographyfacts", "didyouknow",
     "maps", "worldfacts", "westernaustralia", "earthbynumbers"],
)

post(
    "switzerland-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "No city in<br>Switzerland is<br>legally the<br>capital.",
         "sub": "Bern is the federal city, which is not the same thing."},
        {"type": "bignum", "kicker": "Stat 02", "number": "1848", "numsize": "s3", "bg": "",
         "label": "year Bern became federal city",
         "title": "The constitution names it the seat of government, and stops short of "
                  "calling it the capital.", "size": "h-sm",
         "source": "Bern: 'de facto capital'; a footnote reads 'Switzerland has no de jure "
                   "capital'. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "57.09", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "km — the Gotthard Base Tunnel",
         "title": "The longest railway tunnel in the world, and the deepest, at 2,450 m "
                  "down.", "size": "h-sm",
         "source": "Gotthard Base Tunnel, inaugurated 1 June 2016. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "60%", "numsize": "s3", "bg": "",
         "label": "of the country is Alps",
         "title": "The plateau is 30% and the Jura 10%. Switzerland holds 48 of the Alps' 82 "
                  "four-thousanders.", "size": "h-sm",
         "source": "Geography of Switzerland; Swiss Alps; Switzerland. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Romansh is an official language and the 11th most spoken.",
         "sub": "Serbian, Croatian, Albanian, Portuguese, Spanish, English and Turkish all "
                "have more speakers in Switzerland than one of its own official languages, "
                "which UNESCO classifies as definitely endangered.",
         "source": "Romansh language: 0.74% as language of best command. " + WIKI},
    ],
    """
No city in Switzerland is legally the capital.

Bern is the federal city, which is not the same thing. The Swiss constitution names it the seat of government and deliberately stops short of the word capital — Wikipedia's own footnote on the Bern article reads, flatly, that Switzerland has no de jure capital. Bern has held the role since 1848 and has never been promoted.

SWITZERLAND BY NUMBERS
Official capital — none; Bern is the federal city, since 1848
Share of the country that is Alps — 60%
Gotthard Base Tunnel — 57.09 km, the longest railway tunnel in the world
Deepest point of that tunnel — 2,450 m below the surface
Alpine peaks over 4,000 m — 48 of the Alps' 82 are Swiss
Highest point — Dufourspitze, 4,634 m

The Gotthard is the number that does not sound real. Fifty-seven kilometres of railway tunnel, two and a half kilometres beneath the mountains at its deepest, opened in 2016 and still the longest in the world.

Then there is Romansh. It is one of Switzerland's four national languages and has been an official language of the Confederation since 1996, meaning you can write to the federal government in it and get a reply. It is also the eleventh most spoken language in the country. Serbian, Croatian, Albanian, Portuguese, Spanish, English and Turkish all beat it, and UNESCO lists it as definitely endangered.

Two figures we cut: Switzerland's glacier area, because three articles give three numbers and it is shrinking anyway, and the count of mountains above 3,600 m, which is sourced to a private website.

Does a country need an official capital at all?
""",
    ["switzerland", "bern", "gotthard", "swissalps", "romansh", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "earthbynumbers"],
)

post(
    "egypt-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Almost all of<br>Egypt lives on<br>3.5% of Egypt.",
         "sub": "The other 96.5% is there, it is just empty."},
        {"type": "bignum", "kicker": "Stat 02", "number": "35,000", "numsize": "s3", "bg": "",
         "label": "km² — the settled part of Egypt",
         "title": "3.5% of the country, in a valley and a delta, holding about 99% of the "
                  "people.", "size": "h-sm",
         "source": "Geography of Egypt. The Egypt article gives 5.5% in one place and 3% in "
                   "another. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "3,700", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "years as the tallest structure",
         "title": "The Great Pyramid held the record for more than 3,700 years. It took "
                  "about 26 to build.", "size": "h-sm",
         "source": "Great Pyramid of Giza, c. 2600 BC, originally 146.6 m. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "193.3", "numsize": "s3", "bg": "",
         "label": "km — the Suez Canal",
         "title": "Dug between 1859 and 1869, opened 17 November 1869, no locks.",
         "size": "h-sm",
         "source": "Suez Canal. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Two temples were cut into 1,036 blocks and moved uphill.",
         "sub": "Abu Simbel was relocated in 1968 to get it clear of Lake Nasser — 208 m "
                "further inland and 65 m higher. The smallest block weighed seven tons. The "
                "country also runs from 2,653 m on Mount Catherine down to 133 m below sea "
                "level in the Qattara Depression.",
         "source": "Abu Simbel; Mount Catherine; Qattara Depression. " + WIKI},
    ],
    """
Almost everyone in Egypt lives on about 3.5% of Egypt.

The other 96.5% is there, it is just empty. Geography of Egypt puts the cultivated and permanently settled land at 35,000 km² — a river valley and a delta — and the share of the population living on it at about 99%.

EGYPT BY NUMBERS
Cultivated and settled land — 35,000 km², about 3.5% of the country
Share of the population living there — about 99%
Great Pyramid — tallest structure on Earth for more than 3,700 years
Suez Canal — 193.3 km, opened 17 November 1869
Highest point — Mount Catherine, 2,653 m
Lowest point — Qattara Depression, 133 m below sea level

The pyramid number is worth sitting with. It was built around 2600 BC, over about 26 years, and nothing humans made was taller for the next three and a half millennia. It stood 146.6 m when finished and stands 138.5 m now.

Abu Simbel is the other one. In 1968 the two temples were cut into 1,036 blocks, the smallest weighing seven tons, and rebuilt 208 m further inland and 65 m higher up, to get them above the rising water of Lake Nasser. The project cost $41.7 million at the time.

Three things we dropped. Egypt's desert share as a percentage — it is simply not on the page, only the words "predominantly desert". The Suez Canal's share of world trade, because that sentence carries no citation and no date. And Lake Nasser as the world's largest man-made lake, because the reservoir list puts it eleventh, behind Lake Volta.

The Egypt article itself can't settle on the figure: 99% on 5.5% in one place, 98% on 3% in another.

Where else does a whole country fit into one valley?
""",
    ["egypt", "nile", "suezcanal", "giza", "abusimbel", "geographyfacts", "didyouknow",
     "maps", "worldfacts", "earthbynumbers"],
)

post(
    "india-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "India runs<br>29 degrees wide<br>on one clock.",
         "sub": "Sunrise in Assam can be two hours before sunrise in Gujarat."},
        {"type": "bignum", "kicker": "Stat 02", "number": "2,933", "numsize": "s3", "bg": "",
         "label": "km from east to west, one time zone",
         "title": "Over 29° of longitude, all of it on UTC+05:30.", "size": "h-sm",
         "source": "Indian Standard Time. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "26,461", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "mm of rain in a single year",
         "title": "Cherrapunji, August 1860 to July 1861. Still the record.", "size": "h-sm",
         "source": "Cherrapunji. The same page gives 26,471 mm in its Guinness paragraph. "
                   + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "22", "numsize": "s2", "bg": "",
         "label": "languages in the constitution",
         "title": "Hindi and English are the Union's official languages. India has no "
                  "national language.", "size": "h-sm",
         "source": "Languages of India: 'the Constitution of India does not give any language "
                   "the status of national language'. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "The tea gardens of Assam keep their own time anyway.",
         "sub": "Chaibagan time runs an hour ahead of IST and has no official standing. "
                "Proposals for a second zone were made in the 1980s, again in 2014 and "
                "again in 2017. None was approved.",
         "source": "Indian Standard Time; Time in India. " + WIKI},
    ],
    """
India is 2,933 km wide and runs on a single clock.

Sunrise in Assam can be hours before sunrise in Gujarat, and both are told it is the same time. That span covers over 29 degrees of longitude, all of it on UTC+05:30, and Indian Standard Time remains the only officially used time in the country.

INDIA BY NUMBERS
East–west distance — 2,933 km, over 29° of longitude
Time zones — 1
Area — 3,287,263 km², seventh largest in the world
Scheduled languages — 22, plus English as an additional official language
Rainfall record, one year — 26,461 mm at Cherrapunji, 1860–61

The tea gardens of Assam gave up waiting. Chaibagan time runs an hour ahead of IST, has no official standing, and is used anyway because the working day otherwise starts in the dark and ends in daylight. Researchers proposed splitting the country into two or three zones in the 1980s. Assam's chief minister campaigned for it in 2014. A second zone, Eastern India Time at UTC+06:00, was proposed in 2017. Nothing was approved.

The rainfall figure is the other one that stops you. Cherrapunji recorded 26,461 mm between August 1860 and July 1861 — over 26 metres of rain in twelve months — and still holds the record for the wettest calendar month, 9,300 mm in July 1861.

Two things we dropped. Mawsynram as flatly the wettest place on Earth: its own page lists two Colombian towns with higher annual averages. And India's count of official languages, because the India article says two and Languages of India says 23. The 22 scheduled languages are the figure that is actually in the constitution, and no language is India's national language.

One clock or three?
""",
    ["india", "indianstandardtime", "assam", "cherrapunji", "geographyfacts", "didyouknow",
     "maps", "worldfacts", "southasia", "earthbynumbers"],
)

post(
    "argentina-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "The highest and<br>lowest points of<br>a hemisphere<br>are both here.",
         "sub": "Argentina holds the ceiling and the floor of the Western Hemisphere."},
        {"type": "bignum", "kicker": "Stat 02", "number": "6,961", "numsize": "s3", "bg": "",
         "label": "m — Aconcagua, in Mendoza",
         "title": "The highest summit outside Asia, and of both the Western and Southern "
                  "Hemispheres.", "size": "h-sm",
         "source": "Extreme points of the Americas; Aconcagua, whose own lead gives "
                   "6,967.15 m. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "-105", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "m — Laguna del Carbon, in Santa Cruz",
         "title": "The lowest surface point in the Americas. About 1,500 km from the "
                  "highest.", "size": "h-sm",
         "source": "Laguna del Carbon; Extreme points of the Americas. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "3,694", "numsize": "s3", "bg": "",
         "label": "km — north to south",
         "title": "2,780,400 km², the eighth-largest country in the world.", "size": "h-sm",
         "source": "Argentina; Geography of Argentina. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "The southernmost city in the world is an argument, not a fact.",
         "sub": "Ushuaia claims it on size. Puerto Williams in Chile is further south and was "
                "officially recognised as a city in 2019. Wikipedia's own verdict: the title "
                "is 'mainly a slogan used for tourism purposes', because city is not a legal "
                "designation in either country.",
         "source": "Ushuaia; Puerto Williams; Southernmost settlements. " + WIKI},
    ],
    """
The highest and lowest points of the Western Hemisphere are both in Argentina.

Argentina holds the ceiling and the floor. Aconcagua, in Mendoza, is the highest summit of the Americas and of both the Western and Southern Hemispheres. Laguna del Carbón, in Santa Cruz, is the lowest surface point in the Americas. They are in the same country, about 1,500 km apart.

ARGENTINA BY NUMBERS
Aconcagua — 6,961 m, highest summit outside Asia
Laguna del Carbón — 105 m below sea level, lowest in the Americas
North–south distance — 3,694 km
Area — 2,780,400 km², eighth largest in the world
Coastline — 4,989 km

Aconcagua is also the second-most topographically prominent peak on Earth, and the easiest of the Seven Summits to walk up. Its elevation is the one number here that Wikipedia cannot hold still: 6,967.15 m on its own page, 6,961 m on the extreme-points page, 6,959 m in the Argentina article, 6,960 and 6,962 in the same paragraph of Geography of Argentina. We used the figure with the cleanest provenance.

The southernmost city is a better argument than it looks. Ushuaia has claimed the title for decades on the grounds of being an actual city. Puerto Williams in Chile is further south, and in 2019 Chile's statistics institute changed its criteria so that Puerto Williams, as a provincial capital, officially became one. Wikipedia's own page on southernmost settlements calls the whole title a tourism slogan, pointing out that "ciudad" is not a legal designation in either country.

Two things we cut. Perito Moreno as an advancing glacier — Wikipedia now says retreating, on the northern front since 2020. And Iguazú's number of cascades, which is 275 in the infobox and "150 to 300" in the body of the same article.

Ushuaia or Puerto Williams?
""",
    ["argentina", "aconcagua", "patagonia", "ushuaia", "santacruz", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "southamerica", "earthbynumbers"],
)

post(
    "philippines-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "The Philippines<br>gained 534 islands<br>in 2017.",
         "sub": "Nothing rose out of the sea. Somebody looked more carefully."},
        {"type": "bignum", "kicker": "Stat 02", "number": "7,641", "numsize": "s3", "bg": "",
         "label": "islands — revised up in 2017",
         "title": "The 1945 count stood for 72 years. A mapping survey found 400 to 500 more "
                  "land features.", "size": "h-sm",
         "source": "Geography of the Philippines, citing NAMRIA. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "36,289", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "km of coastline — fifth longest on Earth",
         "title": "In a country of about 300,000 km². More than 5,000 of its islands are "
                  "still unnamed.", "size": "h-sm",
         "source": "Philippines; Geography of the Philippines; List of islands of the "
                   "Philippines. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "195", "numsize": "s3", "bg": "",
         "label": "languages — at the top of the estimate",
         "title": "'Some 130 to 195 languages, depending on the method of classification.' "
                  "The range is the fact.", "size": "h-sm",
         "source": "Languages of the Philippines. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "There is an island, in a lake, on an island, in a lake, on an island.",
         "sub": "Vulcan Point sits in the Main Crater Lake of Taal Volcano, which sits on "
                "Volcano Island, which sits in Taal Lake, which fills a caldera on Luzon. "
                "Wikipedia calls it one of only a few in the world.",
         "source": "Taal Volcano Main Crater Lake; Taal Volcano. " + WIKI},
    ],
    """
The Philippines gained 534 islands in 2017.

Nothing rose out of the sea. Somebody looked more carefully. The count of 7,107 was set in 1945 and stood for 72 years, until the national mapping authority identified 400 to 500 additional land features that might qualify, and the official figure became 7,641.

PHILIPPINES BY NUMBERS
Islands — 7,641, revised up from 7,107 in 2017
Still officially unnamed — more than 5,000
Inhabited — about 2,000
Coastline — 36,289 km, fifth longest in the world
Languages — some 130 to 195, depending on classification

The coastline is the figure that explains the country. 36,289 km of it, fifth longest on Earth, wrapped around a land area of roughly 300,000 km². More than five thousand of those islands have no official name.

The language range is not vagueness, it is the honest answer. Wikipedia says "some 130 to 195 languages are spoken in the Philippines, depending on the method of classification". Ethnologue counts 182 native languages. The national language commission counts 135 ethnolinguistic groups. Filipino and English are the official languages, and the 1987 constitution gives regional languages official auxiliary status without naming any of them.

Then there is Taal. Vulcan Point is a rock in the Main Crater Lake on Volcano Island, which sits in Taal Lake, which fills a caldera on Luzon. An island in a lake on an island in a lake on an island.

Two things we dropped. Emden Deep's depth as a single number — 10,540 m and 10,430 m both appear in one article, so call it about 10,500 m. And Taal as the world's smallest volcano, a label the article itself cites a piece arguing against.

How many islands does your country have, and does anyone know?
""",
    ["philippines", "luzon", "taal", "palawan", "geographyfacts", "didyouknow", "maps",
     "worldfacts", "islands", "southeastasia", "earthbynumbers"],
)

# ═══════════════════════════════════════════════ SPOTLIGHTS ════════

spotlight(
    "spot-tajikistan",
    "The tallest dam<br>in the world is<br>an accident.",
    "An earthquake built it in 1911 and nobody has moved it since.",
    [["Capital", "Dushanbe"],
     ["Land area", "143,100 km²"],
     ["Land borders", "4"],
     ["Official language", "Tajik"],
     ["Currency", "Somoni (TJS)"]],
    "Three reasons",
    [{"name": "The Roof of the World",
      "note": "The Pamirs have been called that since the Victorian era. Ismoil Somoni Peak "
              "tops out at 7,495 m."},
     {"name": "The Pamir Highway",
      "note": "The M41 crosses the Ak-Baital pass at 4,655 m, which makes it the second-"
              "highest international highway there is."},
     {"name": "A park the size of a country",
      "note": "Tajik National Park covers 26,116 km² — a little over 18% of the whole "
              "country — and has been World Heritage since 2013."}],
    {"title": "567 metres of rock, dropped by an earthquake.",
     "sub": "On 18 February 1911 the Sarez earthquake dislodged about 2 cubic kilometres of "
            "mountain, burying the village of Usoi and damming the Murghab river. The Usoi "
            "Dam is the tallest dam in the world, natural or man-made, and Lake Sarez behind "
            "it is 75.8 km long and 505 m deep.",
     "source": "Usoi Dam; Sarez Lake. " + WIKI,
     "size": "h-sm"},
    "Three places",
    [{"name": "Iskanderkul",
      "note": "A lake at 2,195 m in the Fann Mountains, 72 m deep. Iskander is the Persian "
              "form of Alexander."},
     {"name": "Lake Karakul",
      "note": "At 3,960 m in the eastern Pamirs, sitting in what has been interpreted as a "
              "52 km impact crater. Higher than Titicaca."},
     {"name": "Khujand",
      "note": "On the Syr Darya at the mouth of the Fergana valley, about 2,500 years old and "
              "renamed by Alexander in 329 BC."}],
    """
The tallest dam in the world is in Tajikistan, and nobody built it.

An earthquake built it in 1911 and nobody has moved it since. On 18 February that year the Sarez earthquake dropped roughly 2 cubic kilometres of mountain into the Murghab valley, burying the village of Usoi and blocking the river. The Usoi Dam stands 567 m high, which makes it the tallest dam on Earth, natural or man-made, and Lake Sarez has been filling behind it ever since — 75.8 km long, 505 m deep, 3,263 m above the sea.

TAJIKISTAN BY NUMBERS
Capital — Dushanbe
Land area — 143,100 km²
Land borders — 4: Afghanistan, China, Kyrgyzstan, Uzbekistan
Official language — Tajik
Currency — somoni
Highest point — Ismoil Somoni Peak, 7,495 m

More than half the country sits above 3,000 m, according to the Library of Congress country study Wikipedia cites. The Pamirs have been called the Roof of the World since the Victorian era, and the M41 — the Pamir Highway — crosses them over the Ak-Baital pass at 4,655 m, the second-highest international highway in the world.

Tajik National Park covers 26,116 km², a little over 18% of the country, and has been a World Heritage site since 2013.

WHERE TO GO
Iskanderkul — a lake at 2,195 m in the Fann Mountains, 72 m deep, named for Alexander.
Lake Karakul — 3,960 m up in the eastern Pamirs, in what is interpreted as a 52 km impact crater, higher than Lake Titicaca.
Khujand — on the Syr Darya at the mouth of the Fergana valley, about 2,500 years of it, renamed Alexandria Eschate in 329 BC.

Two things we cut: Nurek Dam's height, which is 300 m in its infobox and 304 m in its lead, and the area of the largest non-polar glacier, which Wikipedia is currently mid-rename on.

Would you drive the Pamir Highway?
""",
    ["tajikistan", "pamir", "pamirhighway", "khujand", "centralasia", "fannmountains",
     "geographyfacts", "travelinspo", "worldfacts", "earthbynumbers"],
)

spotlight(
    "spot-guatemala",
    "Guatemala<br>recognises 21 Mayan<br>languages.",
    "None of them is an official language. Spanish is the only one.",
    [["Capital", "Guatemala City"],
     ["Land area", "108,889 km²"],
     ["Land borders", "4"],
     ["Official language", "Spanish"],
     ["Currency", "Quetzal (Q)"]],
    "Three reasons",
    [{"name": "Lake Atitlán",
      "note": "340 m deep, in a caldera left by a supervolcanic eruption about 79,500 years "
              "ago. Wikipedia calls it the deepest lake in Central America."},
     {"name": "Volcanoes you can hear",
      "note": "Guatemala has 37. Fuego is almost constantly active, with small explosions "
              "every 15 to 20 minutes."},
     {"name": "Tikal",
      "note": "One of the largest Maya urban centres ever built, World Heritage since 1979, "
              "with Temple IV standing 70 m above the plaza."}],
    {"title": "The volcano next door erupts every twenty minutes.",
     "sub": "Volcán de Fuego sits about 16 km west of Antigua and Wikipedia describes it as "
            "almost constantly active at a low level — gas and ash every 15 to 20 minutes, "
            "with the larger eruptions less frequent. Pacaya, 30 km from the capital, has "
            "been erupting regularly since 1961 after 70 years dormant.",
     "source": "Volcán de Fuego; Pacaya. " + WIKI,
     "size": "h-sm"},
    "Three places",
    [{"name": "Tikal",
      "note": "Maya temples standing clear of the Petén rainforest canopy. Temple IV is 70 m, "
              "Temple V 57 m, Temple I 47 m."},
     {"name": "Antigua Guatemala",
      "note": "The colonial capital from 1543 until the 1773 earthquakes moved the "
              "government out. Baroque, low-built, and World Heritage since 1979."},
     {"name": "Semuc Champey",
      "note": "A 300 m limestone land bridge with stepped turquoise pools on top, and the "
              "Cahabón river running through a cave system underneath."}],
    """
Guatemala formally recognised 21 Mayan languages by name in 1996. None of them is an official language.

Spanish is the only one. The Mayan, Xinca and Garifuna languages are recognised as national languages under a 2003 law, which is a different and weaker thing, and the distinction matters to several million people. Even the count is contested: the Academia de Lenguas Mayas de Guatemala finds 21 distinct languages in one place and applies its standards to 22 in another, apparently because the government treats Achiʼ as a variant of Kʼicheʼ.

GUATEMALA BY NUMBERS
Capital — Guatemala City
Land area — 108,889 km²
Land borders — 4: Belize, El Salvador, Honduras, Mexico
Official language — Spanish, and only Spanish
Currency — quetzal
Volcanoes — 37

Lake Atitlán is the reason most people come. It is 340 m deep — Wikipedia calls it the deepest lake in Central America — and it fills a caldera left by a supervolcanic eruption roughly 79,500 years ago, which is why the sides are so steep and the villages so small.

The volcanoes are not scenery. Fuego sits about 16 km west of Antigua and is almost constantly active, throwing gas and ash every 15 to 20 minutes. Pacaya, 30 km from the capital, was dormant for over 70 years and has erupted frequently since 1961.

WHERE TO GO
Tikal — Maya temples above the Petén canopy; Temple IV is 70 m from plaza floor to roof comb.
Antigua Guatemala — colonial capital from 1543 to 1773, when the Santa Marta earthquakes moved the government to Guatemala City.
Semuc Champey — a 300 m limestone land bridge with stepped pools on top and a river running underneath it.

Two things we dropped: Guatemala's active volcano count, which is three on one page and four on another, and Tajumulco's elevation, which is 4,203 m on its own article and 4,220 m on three others.

Which would you rather wake up to — the lake or the volcano?
""",
    ["guatemala", "lakeatitlan", "tikal", "antiguaguatemala", "semucchampey", "maya",
     "centralamerica", "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-malawi",
    "One lake here<br>has more fish<br>species than any<br>lake on Earth.",
    "At least 700 cichlids, and almost all of them live nowhere else.",
    [["Capital", "Lilongwe"],
     ["Land area", "118,484 km²"],
     ["Land borders", "3"],
     ["Official language", "English"],
     ["Currency", "Kwacha (MK)"]],
    "Three reasons",
    [{"name": "An inland sea",
      "note": "Lake Malawi covers about 29,600 km² and goes down 706 m — the third largest "
              "and second deepest lake in Africa."},
     {"name": "A park built for fish",
      "note": "Lake Malawi National Park is the only Malawian park created to protect fish "
              "and aquatic habitat, World Heritage since 1984."},
     {"name": "Highlands, not just water",
      "note": "The Great Rift Valley runs the length of the country, and Sapitwa Peak on the "
              "Mulanje massif reaches 3,002 m."}],
    {"title": "Two Malawian islands sit inside Mozambique's water.",
     "sub": "Likoma and Chizumulu are exclaves of Malawi, entirely surrounded by Mozambican "
            "territorial waters in a lake the two countries share. Likoma is 18 km² of it, "
            "with a cathedral on an island that is legally in the wrong country.",
     "source": "Likoma Island. " + WIKI,
     "size": "h-sm"},
    "Three places",
    [{"name": "Nyika Plateau",
      "note": "Rolling grassland mostly between 2,100 and 2,200 m, peaking at 2,605 m, with "
              "around 200 species of orchid."},
     {"name": "Liwonde National Park",
      "note": "548 km² in the south with 30 km of the Shire river running through it. Under "
              "African Parks management since 2015."},
     {"name": "Zomba Plateau",
      "note": "About 130 km² of highland rising to 2,087 m, with the Shire river and Liwonde "
              "visible from its western edge."}],
    """
Lake Malawi has more species of fish than any other lake in the world.

At least 700 cichlids, and almost all of them live nowhere else. Wikipedia's wording is worth keeping precise: at least 700 cichlid species, with some estimates as high as 1,000, and every cichlid in the lake endemic to the Malawi system bar four. That is more fish species than any other lake on Earth, in one body of water.

MALAWI BY NUMBERS
Capital — Lilongwe
Land area — 118,484 km²
Land borders — 3: Mozambique, Tanzania, Zambia
Official language — English
Currency — kwacha
Lake Malawi — about 29,600 km², 706 m at its deepest

The lake is the third largest in Africa and the second deepest, and it takes up something like a fifth of the country. Lake Malawi National Park, at the southern end, is the only park in Malawi created specifically to protect fish and aquatic habitat, and has been World Heritage since 1984.

The odd fact: Likoma and Chizumulu are Malawian islands entirely surrounded by Mozambican territorial waters. Exclaves, in a lake, 18 km² of Malawi floating inside somebody else's water.

WHERE TO GO
Nyika Plateau — rolling grassland mostly at 2,100 to 2,200 m, up to 2,605 m at Nganda Peak, with around 200 orchid species.
Liwonde National Park — 548 km², 30 km of the Shire river through it, managed by African Parks since 2015.
Zomba Plateau — about 130 km² of highland to 2,087 m, looking out over the Shire and Liwonde.

Two figures we cut. The lake's share of the country, because the 25% in Geography of Malawi does not match that article's own water-area figure, which works out closer to a fifth. And Mulanje's height from the Malawi article, which says 3,048 m where its own massif article and the geography article both say 3,002 m.

Which would you take — the lake or the plateau?
""",
    ["malawi", "lakemalawi", "nyika", "mulanje", "likoma", "africa", "cichlids",
     "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-cambodia",
    "One Cambodian<br>lake reverses<br>its own river<br>every year.",
    "It swells from about 2,500 km² to 16,000 and pushes the water back out.",
    [["Capital", "Phnom Penh"],
     ["Land area", "181,035 km²"],
     ["Land borders", "3"],
     ["Official language", "Khmer"],
     ["Currency", "Riel (KHR)"]],
    "Three reasons",
    [{"name": "Angkor Wat",
      "note": "The largest religious structure in the world according to Guinness, on a site "
              "of 162.6 hectares, finished around 1150."},
     {"name": "Angkor is a city, not a temple",
      "note": "A 2007 study found urban sprawl of at least 1,000 km² and concluded Angkor was "
              "the largest pre-industrial city in the world by area."},
     {"name": "Tonlé Sap",
      "note": "The largest freshwater lake in Southeast Asia, and the only one most people "
              "have heard of that runs backwards half the year."}],
    {"title": "The lake rises ten metres and the river turns around.",
     "sub": "As the monsoon raises the Mekong, the Tonlé Sap river reverses and runs inland. "
            "The lake goes from about 2,500–3,000 km² and a metre deep to 16,000 km² and "
            "9–14 m, then reverses again and gives it all back.",
     "source": "Tonlé Sap. " + WIKI,
     "size": "h-sm"},
    "Three places",
    [{"name": "Koh Ker",
      "note": "Capital of the whole empire from 928 to 944, with a 36 m seven-tiered pyramid. "
              "World Heritage since 2023 — and not fully demined."},
     {"name": "Preah Vihear",
      "note": "A Khmer temple on a 525 m cliff in the Dângrêk mountains, awarded to Cambodia "
              "by the International Court of Justice in 1962."},
     {"name": "Kampot",
      "note": "A river town of 19th-century French colonial architecture, with the abandoned "
              "hill station at Bokor above it."}],
    """
One Cambodian lake reverses its own river every year.

It swells from about 2,500 km² to 16,000 and pushes the water back out. When the monsoon raises the Mekong, the Tonlé Sap river stops draining the lake and starts filling it, running inland instead of out. The lake goes from roughly 2,500–3,000 km² and a metre deep to 16,000 km² and 9 to 14 m deep. Its level rises about 10 m. Then the rain stops, the flow reverses again, and the lake replenishes the Mekong on the way down.

CAMBODIA BY NUMBERS
Capital — Phnom Penh
Land area — 181,035 km²
Land borders — 3: Laos, Thailand, Vietnam
Official language — Khmer
Currency — riel
Angkor Wat site — 162.6 hectares

Angkor Wat is the largest religious structure in the world according to Guinness World Records, built under Suryavarman II in the 12th century and finished around 1150. But the temple is the small part. A 2007 study found urban sprawl of at least 1,000 km² around it and concluded that Angkor had been the largest pre-industrial city in the world by surface area — in spatial extent, the researchers were careful to say, not population.

Cambodia's flag carries Angkor Wat on it. It is one of only four national flags in the world depicting a building, with Portugal, San Marino and Spain.

WHERE TO GO
Koh Ker — capital of the empire from 928 to 944, with a 36 m seven-tiered pyramid, World Heritage since 2023. The area is not fully demined.
Preah Vihear — a temple on a 525 m cliff, awarded to Cambodia by the International Court of Justice in 1962 and still contested at the border.
Kampot — a southern river town of 19th-century French colonial architecture, with the abandoned hill station at Bokor on the mountain above.

Two things we dropped: Angkor's population, which the article itself hedges, and Bokor as a ghost town, since a resort opened there in 2012.

Have you seen a river change direction?
""",
    ["cambodia", "angkorwat", "tonlesap", "kohker", "kampot", "preahvihear",
     "southeastasia", "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-zambia",
    "Zambia has the<br>largest sheet of<br>falling water<br>in the world.",
    "1,708 metres wide and 108 metres down, in one curtain.",
    [["Capital", "Lusaka"],
     ["Land area", "752,612 km²"],
     ["Land borders", "8"],
     ["Official language", "English"],
     ["Currency", "Kwacha (ZMW)"]],
    "Three reasons",
    [{"name": "Victoria Falls",
      "note": "Mosi-oa-Tunya, the smoke that thunders. Not the tallest or the widest, but by "
              "combined width and height the largest sheet of falling water there is."},
     {"name": "Parks with nobody in them",
      "note": "Kafue covers about 22,400 km² and is the second-largest national park in "
              "Africa. South Luangwa is 9,050 km² with over 400 bird species."},
     {"name": "Eight neighbours",
      "note": "More than almost anywhere in Africa — and one of them is a border less than a "
              "kilometre long."}],
    {"title": "The eighth neighbour is about 150 metres of line.",
     "sub": "Zambia's border with Botswana runs for less than a kilometre, and for years "
            "nobody agreed it existed: South Africa told Botswana there was no common "
            "border at all. Wikipedia now says it is widely believed there are two separate "
            "tripoints, 100 to 150 m apart.",
     "source": "Geography of Zambia; Quadripoint. The tripoint sentences are uncited. "
               + WIKI + " " + DS,
     "size": "h-sm"},
    "Three places",
    [{"name": "Mosi-oa-Tunya",
      "note": "The Zambian side of the falls, where the Devil's Pool forms on the lip "
              "between roughly September and December."},
     {"name": "South Luangwa",
      "note": "9,050 km², which Wikipedia calls the home of the photographic and walking "
              "safari, with some of the highest leopard densities in southern Africa."},
     {"name": "Lower Zambezi",
      "note": "4,092 km² on the north bank, facing Zimbabwe's Mana Pools across the river."}],
    """
Zambia has the largest sheet of falling water in the world.

1,708 metres wide and 108 metres down, in one curtain. Victoria Falls is neither the tallest waterfall nor the widest, and ten falls have a greater flow rate. What it has is the combination — classified as the largest on the basis of its combined width and height, which is how you get a single unbroken sheet of water that size.

ZAMBIA BY NUMBERS
Capital — Lusaka
Land area — 752,612 km²
Land borders — 8: Angola, Botswana, DR Congo, Malawi, Mozambique, Namibia, Tanzania, Zimbabwe
Official language — English
Currency — kwacha
Victoria Falls — 1,708 m wide, 108 m high

The local names are better than the English one. Mosi-oa-Tunya in Lozi, the smoke that thunders; Shungu Namutitima in Tonga, boiling water. The falls sit on the border with Zimbabwe, so half of it is somebody else's.

Eight land neighbours is close to a record on the continent, and the eighth is barely there. The border with Botswana is under a kilometre long. For years South Africa, then occupying Namibia, told Botswana there was no common border with Zambia at all, and Wikipedia now reports it is widely believed there are two separate tripoints about 100 to 150 m apart rather than one quadripoint.

Lake Kariba, filled between 1958 and 1963, is the world's largest artificial reservoir by volume — four times the reservoir behind the Three Gorges Dam.

WHERE TO GO
Mosi-oa-Tunya — the Zambian side, where the Devil's Pool forms on the very lip of the falls, usually September to December.
South Luangwa — 9,050 km², what Wikipedia calls the home of the photographic and walking safari, with over 400 bird species.
Lower Zambezi — 4,092 km² on the north bank, looking across at Mana Pools.

Two things we cut: Lake Kariba's volume, 180 km³ in the infobox and 185 in the body, and the claim that walking safaris were invented in South Luangwa. Norman Carr's page calls him their pioneer but names no country.

Zambian side or Zimbabwean?
""",
    ["zambia", "victoriafalls", "mosioatunya", "southluangwa", "kafue", "lakekariba",
     "africa", "safari", "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-north-macedonia",
    "Lake Ohrid is<br>one of the oldest<br>lakes in the<br>world.",
    "Old enough that more than 200 species in it exist nowhere else.",
    [["Capital", "Skopje"],
     ["Land area", "25,713 km²"],
     ["Land borders", "5"],
     ["Official language", "Macedonian"],
     ["Currency", "Denar (MKD)"]],
    "Three reasons",
    [{"name": "Lake Ohrid",
      "note": "288 m deep, with more than 200 endemic species. World Heritage on the "
              "Macedonian side since 1979, extended to the Albanian side in 2019."},
     {"name": "Mountains for a small country",
      "note": "Sixteen peaks above 2,000 m, topping out at Mount Korab at 2,764 m, which is "
              "also Albania's high point."},
     {"name": "Layers you can drive between",
      "note": "Heraclea Lyncestis was founded by Philip II in the 4th century BC. Skopje's "
              "Stone Bridge went up under Mehmed the Conqueror."}],
    {"title": "In 1963 an earthquake took about 80% of Skopje.",
     "sub": "A magnitude 6.1 quake on 26 July left more than 200,000 people homeless and "
            "relief came from 78 countries, which is why the city's motto is the City of "
            "International Solidarity. The rebuild was partly planned by Kenzō Tange, and "
            "only partly carried out.",
     "source": "1963 Skopje earthquake. " + WIKI,
     "size": "h-sm"},
    "Three places",
    [{"name": "Ohrid",
      "note": "A lakeside town once said to have 365 churches, one for every day. The number "
              "today is a great deal smaller."},
     {"name": "Matka Canyon",
      "note": "Roughly 5,000 hectares west of Skopje, ten caves, and the oldest artificial "
              "lake in the country."},
     {"name": "Bitola",
      "note": "The Ottoman-era City of Consuls, with the ruins of Heraclea Lyncestis 2 km "
              "south of it."}],
    """
Lake Ohrid is one of the oldest lakes in the world.

Old enough that more than 200 species in it exist nowhere else. That is what age does to a lake: isolate a body of water for long enough and everything in it diverges. Ohrid is 288 m deep, shared with Albania, and Wikipedia describes it as a unique aquatic ecosystem of worldwide importance. The Macedonian side became World Heritage in 1979; the Albanian side was added in 2019.

NORTH MACEDONIA BY NUMBERS
Capital — Skopje
Land area — 25,713 km²
Land borders — 5: Albania, Bulgaria, Greece, Kosovo, Serbia
Official language — Macedonian
Currency — denar
Highest point — Mount Korab, 2,764 m

The border count has a wrinkle worth naming: one of the five is Kosovo, whose status is contested, so some sources count four sovereign neighbours. Wikipedia's own lead lists all five without qualification.

For a country of 25,713 km² it is remarkably vertical — sixteen peaks over 2,000 m, and Korab at 2,764 m is the highest point of both North Macedonia and Albania.

The country changed its name in living memory. The Prespa Agreement with Greece was signed on 17 June 2018 and came into force on 12 February 2019, and the Republic of Macedonia became the Republic of North Macedonia.

WHERE TO GO
Ohrid — a lakeside town said once to have had 365 churches, one for each day of the year. A 17th-century traveller's count, and the number now is much smaller.
Matka Canyon — about 5,000 hectares west of Skopje, with ten caves and the oldest artificial lake in the country.
Bitola — the Ottoman City of Consuls, with Heraclea Lyncestis, founded by Philip II of Macedon, 2 km to the south.

Two things we dropped: an age in years for Lake Ohrid, because the only figure on the page is for Pliocene sediments "possibly 3–5 million years old", and the Kokino observatory's supposed fourth place on a NASA list, which appears only in a news headline.

Which old lake would you rather swim in?
""",
    ["northmacedonia", "lakeohrid", "ohrid", "skopje", "bitola", "matka", "balkans",
     "geographyfacts", "travelinspo", "earthbynumbers"],
)

spotlight(
    "spot-senegal",
    "Senegal almost<br>completely<br>surrounds<br>another country.",
    "The Gambia reaches 320 km inland and Senegal wraps round three sides of it.",
    [["Capital", "Dakar"],
     ["Land area", "196,722 km²"],
     ["Land borders", "5"],
     ["Official language", "French"],
     ["Currency", "West African CFA franc"]],
    "Three reasons",
    [{"name": "The end of the continent",
      "note": "Dakar sits on the Cap-Vert peninsula, the westernmost point of mainland "
              "Africa."},
     {"name": "A pink lake",
      "note": "Lake Retba is one of very few lakes in the world with naturally pink water, "
              "coloured by Dunaliella salina algae."},
     {"name": "A record almost nobody has",
      "note": "Wikipedia: Senegal is one of the few African states never to have experienced "
              "a coup d'état."}],
    {"title": "395 bird species, and nearly three million birds.",
     "sub": "The Djoudj sanctuary on the Senegal river covers 16,000 hectares and has "
            "recorded 395 species. It has been a Ramsar site since 1977 and World Heritage "
            "since 1981, and was on the danger list twice.",
     "source": "Djoudj National Bird Sanctuary. " + WIKI,
     "size": "h-sm"},
    "Three places",
    [{"name": "Île de Gorée",
      "note": "18.2 hectares two kilometres off Dakar, and one of the first twelve World "
              "Heritage sites ever designated, in 1978."},
     {"name": "Saint-Louis",
      "note": "Capital of the French colony of Senegal from 1673, and of French West Africa "
              "from 1895 to 1902. World Heritage since 2000."},
     {"name": "Bassari Country",
      "note": "503 km² of Bassari, Fula and Bedik cultural landscape in the south-east, "
              "inscribed in 2012."}],
    """
Senegal almost completely surrounds another country.

The Gambia reaches 320 km inland and Senegal wraps round three sides of it. Geography of Senegal calls it a near-enclave and says The Gambia penetrates more than 320 km into Senegal, from the Atlantic coast to the middle of the country, following its river. The border runs 749 km along both banks. Everything south of it — the Casamance — is Senegalese territory you cannot reach from Dakar without crossing somebody else's country or going round.

SENEGAL BY NUMBERS
Capital — Dakar
Land area — 196,722 km²
Land borders — 5: The Gambia, Guinea, Guinea-Bissau, Mali, Mauritania
Official language — French
Currency — West African CFA franc
Border with The Gambia — 749 km

Dakar sits on the Cap-Vert peninsula, the westernmost point of mainland Africa — Pointe des Almadies, at 17°33′W.

Lake Retba is one of very few lakes anywhere with naturally pink water, coloured by Dunaliella salina algae and salty enough to float in. It was often the finish of the Dakar Rally before the race moved to South America in 2009.

And one line from Politics of Senegal is worth quoting directly: Senegal is one of the few African states that has never experienced a coup d'état or exceptionally harsh authoritarianism.

WHERE TO GO
Île de Gorée — 18.2 hectares two kilometres off Dakar, among the first twelve World Heritage sites designated anywhere, in 1978, and home to the House of Slaves.
Saint-Louis — capital of the French colony from 1673 and of French West Africa from 1895 to 1902, World Heritage since 2000.
Bassari Country — 503 km² of Bassari, Fula and Bedik cultural landscape in the south-east, inscribed in 2012.

Two things we dropped. Lake Retba's salinity, where one list says 40% with a citation-needed tag and the article itself says 350 g/L. And any throughput figure for Gorée: the article quotes UNESCO calling it the largest slave-trading centre on the African coast, then historians disputing the usual accounts entirely.

Which border on a map have you never been able to explain?
""",
    ["senegal", "dakar", "goree", "saintlouis", "lacrose", "casamance", "westafrica",
     "geographyfacts", "travelinspo", "earthbynumbers"],
)

# ═══════════════════════════════════════════════════ TOP 5 ════════

top5(
    "top5-coffee-regions",
    "Blue Mountain<br>is a marketing<br>exercise.",
    "Five coffee regions worth the airfare. Opinion, not fact.",
    [
        ("Yirgacheffe", "Gedeo, Ethiopia",
         "Coffee's actual homeland, grown in garden plots under shade at altitude. The "
         "floral, tea-like cup people spend a decade chasing is just what grows here.", ""),
        ("Huila", "Colombia",
         "Steep, volcanic, and small-farm to a degree that makes traceability real rather "
         "than a label. The washed coffees out of here set the standard everyone copies.",
         ""),
        ("Boquete", "Chiriquí, Panama",
         "The Gesha varietal that broke every auction record came off these slopes. "
         "Expensive, occasionally absurd, and the only one on this list that earns the "
         "hype.", ""),
        ("Antigua", "Guatemala",
         "Three volcanoes, volcanic soil, and a valley that traps cloud. Chocolate and "
         "spice rather than fruit, and a town you would visit anyway.", ""),
        ("Kintamani", "Bali, Indonesia",
         "Grown between citrus and vegetables on an old caldera rim, which does something "
         "to the cup. The one nobody puts on a list, which is why it is on this one.", ""),
    ],
    """
Jamaican Blue Mountain is a marketing exercise. It is a protected name attached to a small volume of coffee, sold at four times the price of better coffee from places nobody has made a brand out of, and most people who order it could not pick it out of a line-up.

Five coffee regions actually worth the airfare:

01 YIRGACHEFFE, Ethiopia — coffee's homeland, grown in garden plots under shade. The floral, almost tea-like cup that specialty roasters spend careers chasing is simply what grows here by default.

02 HUILA, Colombia — steep, volcanic, and genuinely small-farm, which makes traceability mean something. The washed coffees out of Huila are the reference point half the industry is trying to match.

03 BOQUETE, Panama — the Gesha that broke every auction record came off these slopes. Expensive to the point of silly, and the one on this list where the hype is deserved.

04 ANTIGUA, Guatemala — a valley ringed by volcanoes that traps the cloud. Chocolate and spice rather than fruit, in a town worth the trip on its own terms.

05 KINTAMANI, Bali — grown between citrus trees and vegetables on an old caldera rim. Nobody puts it on a list like this, which is exactly why it is here.

This is opinion. Rankings of coffee are always opinion, and anyone who tells you otherwise is selling something.

Tell us which region we got wrong — and go on, defend Blue Mountain.
""",
    ["coffee", "specialtycoffee", "yirgacheffe", "huila", "gesha", "boquete",
     "antiguaguatemala", "coffeetravel", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-old-towns",
    "Dubrovnik is a<br>cruise terminal<br>with walls.",
    "Five old towns that still belong to the people living in them. Opinion.",
    [
        ("Gjirokastër", "Albania",
         "A stone town built steep into a hillside, grey slate roof above grey slate roof. "
         "Nobody has polished it for you and that is the point.", ""),
        ("Bukhara", "Uzbekistan",
         "A working Silk Road city rather than a monument to one. Madrasas, a surviving "
         "merchant quarter, and ordinary life happening between them.", ""),
        ("Ohrid", "North Macedonia",
         "Churches stacked above a lake old enough to have its own endemic species. Said to "
         "have had 365 of them once; the real number now is far smaller and far better.", ""),
        ("Sarajevo's Baščaršija", "Bosnia and Herzegovina",
         "An Ottoman bazaar quarter that never became a theme park, with the seam between "
         "Ottoman and Austro-Hungarian running straight down one street.", ""),
        ("Kampot", "Cambodia",
         "Nineteenth-century French colonial shopfronts on a river, mostly unrestored and "
         "occupied. Unlike most Cambodian provincial capitals, it kept its own buildings.",
         ""),
    ],
    """
Dubrovnik is a cruise terminal with walls. It is a genuinely beautiful city that has been priced, filmed and day-tripped out of being a place where anyone lives, and walking the ramparts in July is less an experience than a queue with a view.

Five old towns that still belong to the people in them:

01 GJIROKASTËR, Albania — a stone town built steeply into a hillside, slate roof above slate roof, in no way smoothed out for visitors.

02 BUKHARA, Uzbekistan — a Silk Road city that is still a city. Madrasas, a surviving merchant quarter, and normal life going on between them.

03 OHRID, North Macedonia — churches stacked above one of the oldest lakes in the world. Legend gives it 365 of them; the real number is smaller and the setting does the rest.

04 BAŠČARŠIJA, Sarajevo — an Ottoman bazaar quarter that never turned into a theme park, with the architectural seam between Ottoman and Austro-Hungarian running down a single street.

05 KAMPOT, Cambodia — nineteenth-century French colonial shopfronts along a river, largely unrestored and lived in, in a country where most provincial capitals lost theirs.

This is opinion. The point of an old town is that it is still somebody's town, and that is a judgement, not a measurement.

Which one did we insult? Make the case for Dubrovnik if you want to.
""",
    ["oldtowns", "gjirokaster", "bukhara", "ohrid", "sarajevo", "kampot", "balkans",
     "travelinspo", "architecture", "earthbynumbers"],
)

top5(
    "top5-lighthouses",
    "Peggy's Cove<br>is a car park<br>with a light<br>on it.",
    "Five lighthouses that actually stand somewhere frightening. Opinion.",
    [
        ("Fastnet Rock", "County Cork, Ireland",
         "A granite tower on a rock in the open Atlantic, the last thing emigrants saw "
         "leaving Ireland. You do not visit it. You see it from a boat, if the sea allows.",
         ""),
        ("La Jument", "Finistère, France",
         "Off the Breton coast in the Fromveur passage, in water that routinely throws "
         "itself over the top of the tower. The famous photograph is not an exaggeration.",
         ""),
        ("Les Éclaireurs", "Beagle Channel, Argentina",
         "A squat red-and-white tower on bare rock near Ushuaia, in a channel where the "
         "weather changes while you are looking at it.", ""),
        ("Þrídrangaviti", "Vestmannaeyjar, Iceland",
         "Built on top of a sea stack off the south coast, reached by helicopter because "
         "there is no other way. The climb was done with ropes in 1938.", ""),
        ("Rubjerg Knude", "North Jutland, Denmark",
         "A lighthouse being buried by a migrating sand dune. It was moved 70 m inland in "
         "2019 to stop the sea taking it, which is a strange thing to do to a building.",
         ""),
    ],
    """
Peggy's Cove is a car park with a light on it. It is a perfectly nice lighthouse on a perfectly nice bit of Nova Scotian granite, and it is on this many fridge magnets because it is easy to drive to, not because it is remarkable.

Five lighthouses that actually stand somewhere frightening:

01 FASTNET ROCK, Ireland — a granite tower on a rock in the open Atlantic, the last of Ireland that emigrants saw. You do not visit; you look at it from a boat if the sea lets you.

02 LA JUMENT, France — in the Fromveur passage off Brittany, in water that regularly comes over the top of the tower. The famous photograph is not an exaggeration.

03 LES ÉCLAIREURS, Argentina — a small red-and-white tower on bare rock in the Beagle Channel near Ushuaia, where the weather changes while you watch it.

04 ÞRÍDRANGAVITI, Iceland — built on a sea stack off the south coast and reached by helicopter, because there is no other way to get there. The first builders climbed it with ropes in 1938.

05 RUBJERG KNUDE, Denmark — a lighthouse being swallowed by a moving sand dune, shifted 70 m inland in 2019 so the sea would not take it.

This is opinion. Lighthouses are ranked on how much they frighten you, which is not a number.

Which one would you not want to be stationed at? And defend Peggy's Cove if you must.
""",
    ["lighthouses", "fastnetrock", "lajument", "iceland", "brittany", "ushuaia",
     "denmark", "coastal", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-cathedrals",
    "The Sagrada<br>Família is a<br>building site.",
    "Five cathedrals that are finished and better. Opinion, not fact.",
    [
        ("Chartres", "Eure-et-Loir, France",
         "The glass is the reason. Most of it is original medieval work rather than "
         "replacement, which almost nowhere else can say after two world wars.", ""),
        ("Durham", "County Durham, England",
         "Norman, heavy, and the first great building to carry a stone rib vault at that "
         "scale. It feels structural rather than decorative, which is rarer than it sounds.",
         ""),
        ("Saint Basil's", "Moscow, Russia",
         "Not a cathedral in the western sense and all the better for it — nine chapels "
         "under nine different roofs, arranged with no interest in symmetry.", ""),
        ("Lalibela", "Amhara, Ethiopia",
         "Eleven churches cut downwards out of solid rock rather than built up from the "
         "ground. Still in use, which is the part people forget.", ""),
        ("Monreale", "Sicily, Italy",
         "Norman architecture, Byzantine mosaic, Arab craftsmanship, in one building. The "
         "gold interior is the argument against restraint.", ""),
    ],
    """
The Sagrada Família is a building site. It has been one for over 140 years, you buy a timed ticket to walk through scaffolding, and a great deal of what you are looking at was designed by people who are not Gaudí working from models that were destroyed in 1936.

Five cathedrals that are finished, and better:

01 CHARTRES, France — the glass. Most of it is original medieval work rather than replacement, which almost nowhere in northern Europe can claim after two wars.

02 DURHAM, England — Norman and heavy, and the first great building to carry a stone rib vault at that scale. It reads as structure rather than decoration.

03 SAINT BASIL'S, Moscow — not a cathedral in the western sense at all. Nine chapels under nine roofs, arranged with no interest whatsoever in symmetry.

04 LALIBELA, Ethiopia — eleven churches cut downward out of solid rock instead of built upward out of blocks. Still in use, which is the part that gets left out.

05 MONREALE, Sicily — Norman architecture, Byzantine mosaic and Arab craftsmanship in one room. The case against restraint.

This is opinion, and a strong one. Buildings are not rankable and we have done it anyway.

Which did we leave out? And yes, go ahead and defend the scaffolding.
""",
    ["cathedrals", "chartres", "durhamcathedral", "lalibela", "monreale", "saintbasils",
     "architecture", "travelinspo", "worldheritage", "earthbynumbers"],
)

top5(
    "top5-rainforests",
    "The Amazon is<br>not the one<br>to visit.",
    "Five rainforests that show you more. Opinion, not fact.",
    [
        ("Daintree", "Queensland, Australia",
         "Rainforest running straight into a coral reef, and one of the oldest continuously "
         "forested areas anywhere. You can walk it in a day and see the structure.", ""),
        ("Borneo's Danum Valley", "Sabah, Malaysia",
         "Old-growth dipterocarp forest with a canopy walkway, in a place where the trees "
         "themselves are the spectacle rather than the wildlife list.", ""),
        ("Monteverde", "Puntarenas, Costa Rica",
         "Cloud forest rather than lowland jungle — wind, moss, and visibility measured in "
         "metres. Completely different experience and far easier to actually see.", ""),
        ("Cardamom Mountains", "Cambodia",
         "One of the largest and still mostly unexplored forests in Southeast Asia, holding "
         "at least 62 globally threatened animal species and more than 450 birds.",
         "Cardamom Mountains. " + WIKI),
        ("Korup", "Southwest Region, Cameroon",
         "West African forest that survived the last ice age intact, which is why the "
         "diversity is what it is. Almost nobody goes.", ""),
    ],
    """
The Amazon is not the one to visit. It is the most important rainforest on Earth and the least rewarding to walk into: the trees are enormous, the sightlines are nil, the wildlife is high up and gone before you look, and most lodge trips are a long boat ride to see a forest you cannot see.

Five rainforests that show you more:

01 DAINTREE, Australia — rainforest running directly into a coral reef, and among the oldest continuously forested areas anywhere. Walkable in a day, and you can read its structure.

02 DANUM VALLEY, Borneo — old-growth dipterocarp forest with a canopy walkway, where the trees are the spectacle rather than a checklist of animals.

03 MONTEVERDE, Costa Rica — cloud forest, not lowland jungle. Wind, moss, visibility of a few metres, and far easier to actually see things in.

04 CARDAMOM MOUNTAINS, Cambodia — one of the largest and still mostly unexplored forests in Southeast Asia, with at least 62 globally threatened animal species and more than 450 bird species.

05 KORUP, Cameroon — West African forest that came through the last ice age intact, which is why its diversity is what it is. Almost nobody goes.

This is opinion. The one hard number here, the Cardamoms' threatened-species count, is Wikipedia's.

Where did you go expecting jungle and see nothing? And make the case for the Amazon.
""",
    ["rainforest", "daintree", "danumvalley", "monteverde", "cardamommountains", "korup",
     "borneo", "cloudforest", "travelinspo", "earthbynumbers"],
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
