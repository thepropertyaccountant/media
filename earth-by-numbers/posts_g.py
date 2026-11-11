#!/usr/bin/env python3
"""
Earth by Numbers — content set G: the 100-buffer batch, run 3, 2026-11-11.

Twenty posts, the per-run maximum. The queue stood at 57 unposted against a
standing target of 100, and the posting task had cleared four entries since the
last build, so the buffer is working. These land approved.

  crazy (7)      nauru, new-zealand, mexico, turkey, south-africa, singapore,
                 greece
  spotlight (6)  armenia, rwanda, panama, taiwan, romania, botswana
  top5 (7)       caves, glaciers, national-parks, bridges, monasteries,
                 libraries, cable-cars

Mix is weighted to crazy and top5: crazy was furthest behind at 18 against 19
top5 and 20 spotlight.

VERIFICATION (BUILD.md §4 — every figure checked in this run)
Wikipedia pages read this run: Nauru; Yaren District; Zealandia; New Zealand;
Baldwin Street; Antipodes; Chicxulub crater; Mexico; Mexico City; Cenote;
Istanbul; Bosporus; Lake Van; Turkey; South Africa; Pretoria; Cape Floristic
Region; Vredefort impact structure; Singapore; Land reclamation in Singapore;
City-state; Water supply and sanitation in Singapore; Mount Athos; Monastic
community of Mount Athos; Greece; Armenia; Lake Sevan; Wings of Tatev;
Armenian alphabet; Rwanda; Volcanoes National Park; Nyungwe Forest; Mountain
gorilla; Panama Canal; Darién Gap; Panama; Pan-American Highway; Taiwan;
Yushan; Taroko National Park; Geography of Taiwan; Danube Delta; Palace of the
Parliament; Romania; Transfăgărășan; Okavango Delta; Botswana; Makgadikgadi
Pan; Chobe National Park; Hang Sơn Đoòng; Mammoth Cave National Park;
Veryovkina Cave; Eisriesenwelt; Waitomo Glowworm Caves; Perito Moreno Glacier;
Aletsch Glacier; Vatnajökull; Baltoro Glacier; Jostedalsbreen; Plitvice Lakes
National Park; Jiuzhaigou; Manú National Park; Kakadu National Park; Gran
Paradiso National Park; Millau Viaduct; Akashi Kaikyō Bridge; Danyang–Kunshan
Grand Bridge; Øresund Bridge; Si-o-se-pol; Meteora; Rila Monastery; Saint
Catherine's Monastery; Sumela Monastery; Hanging Temple; Trinity College
Library Dublin; Strahov Monastery; Admont Abbey; Bibliotheca Alexandrina;
George Peabody Library; Tianmen Mountain; Peak 2 Peak Gondola; Zugspitze;
Ngong Ping 360.

Ledger rows come from the mledoze/countries dataset. Wikipedia's own totals
differ for several countries in this batch (New Zealand 263,310 or 268,000 vs
270,467; Mexico 1,972,550 vs 1,964,375; Taiwan 36,197 or 35,808 vs 36,193;
Romania 238,397 vs 238,391; Botswana 581,730 vs 582,000). The two are never
mixed inside one source line.

The Nauru post is this run's dataset catch, in the same class as the China
border count. The dataset lists Yaren as Nauru's capital. Wikipedia's Yaren
article says plainly that the republic does not have cities nor an official
capital, and that the UN accepts Yaren as the "main district". The post uses
the contradiction rather than either claim on its own.

DROPPED, per the rule that matters most:
  - "Istanbul is the only city on two continents." Its own article says only
    "a city on two continents", and the Bosporus article says "one of very few
    intercontinental cities in the world". The hedge is the post.
  - Istanbul's European-side share as 64.4%, and its rank among European
    cities. Summary-only, and the infobox and lead disagree on the rank.
  - Türkiye's Europe/Asia split as 97%/3%, its UNESCO site count (the summary
    gives both 22 and 21), its coastline length, and Mount Ararat's height.
    All summary-only; the Türkiye page had to be read at /wiki/Turkey after the
    /wiki/Türkiye URL returned url_not_found, and only its first 40k characters
    came back as page text.
  - "Akashi Kaikyō has the longest suspension span in the world." Its page
    still says so in the present tense, which is exactly the shape of the
    Iceland mosquito claim. The span length and opening date are used; the
    superlative is not.
  - Millau's successor as tallest bridge. The page says it held the title
    "until late 2025" and never names what took it, so neither do we.
  - Vredefort as the largest verified impact structure. Its page hedges to
    "one of the largest", so South Africa leans on its plants instead — and
    one impact crater a batch is enough with Chicxulub in the Mexico post.
  - South Africa's megadiverse rank, UNESCO site count and highest point. All
    three are summary-only.
  - Wellington as the southernmost capital, and any New Zealand sheep-to-people
    ratio. Neither is on the page at all.
  - English's statutory status in New Zealand. The body lists three official
    languages; a note in the same article says "De facto official until 2026".
    Māori from 1987 and NZ Sign Language from 2006 are used instead.
  - Zealandia's area as a single number: the lead says 4,900,000 km², a later
    line gives 286,660.25 km² of land, and a stray reference says 3.5 million.
    The lead figure is used and labelled as continental crust.
  - Nauru's road length and the time to drive round the island (summary only),
    and "the only republic without an official capital" (not stated anywhere).
  - Rwanda's share of women in parliament and its plastic-bag ban. Neither
    appears in the page text, despite both being famous.
  - The mountain gorilla population's date: the lead says 2019 and the body
    says 2025 for the same 1,063. The figure is used with that noted.
  - Panama having more species than the US and Canada combined, the sun rising
    over the Pacific, and the country running east–west. None are stated.
  - The Darién Gap's length and width. The page gives only 106 km between the
    two road ends, which is not a width.
  - Gatun Lake's lift as one figure: 26 m in the lead and 27 m in the body.
  - Taiwan's peak count as 268. No page says it. "More than two hundred" is
    the Geography of Taiwan wording; Yushan's page says 165.
  - Yushan as the highest point in East Asia. The page says western Pacific
    outside Kamchatka. The Mount Fuji comparison is historical only.
  - Taroko's gorge depth and the Qingshui Cliffs' height. Not stated.
  - Romania's brown bear share, Carpathian share, Moldoveanu's height and its
    old-growth forest. All summary-only.
  - Transfăgărășan's length: the infobox says 151 km and the body 90 km.
  - Botswana's share of land set aside for parks and reserves. Read the whole
    page; the figure is not there.
  - Chobe's elephant estimate as a dated figure, and "the largest elephant
    population of any country". The 50,000 has no date on the page and the
    "largest herds" claim is about herds in the region.
  - The Okavango's area as one number: 6,000–15,000 km², 37,500 km² (tagged
    citation needed) and 15,000 km² all appear.
  - Mukumbarí, the Mérida cable car. Its article returned url_not_found, so the
    cable-car list uses the Wings of Tatev instead — which pushed Tatev out of
    the Armenia post, where Mount Aragats took its place.
  - The Zugspitze cable car's three 2017 world records. Its own page never
    mentions them; only the Peak 2 Peak article's span record is verifiable,
    so that is all the entry claims.
  - Tianmen's "longest cable car of its kind" as fact. Its page attributes the
    claim to tourist publications, and the post says so.
  - Hang Son Doong's annual visitor cap, Mammoth Cave's permit and tour cost,
    and admission prices for every library in that list. Not stated.
  - Trinity's Long Room being emptied for the restoration. Only a citation
    title says books were moved, so the post gives the restoration and not the
    state of the shelves.
  - Admont as flatly the largest monastery library. The page says the abbey
    says so, and the post keeps that attribution.

Run:  python3 posts_g.py
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
    """Set F's shape: the two items slides carry their own source line."""
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
    "nauru-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Nauru does not<br>have a capital<br>city.",
         "sub": "Five stats from the third-smallest country on Earth."},
        {"type": "bignum", "kicker": "Stat 02", "number": "21", "numsize": "s2", "bg": "",
         "label": "km² — the whole country",
         "title": "An oval island in the Pacific, divided into fourteen districts.",
         "size": "h-sm",
         "source": "Nauru, the third-smallest country in the world. " + WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink", "size": "h-sm",
         "title": "Yaren is not the capital. It is the main district.",
         "sub": "Nauru's own article calls Yaren the de facto capital. The Yaren article says "
                "the republic does not have cities nor an official capital, and that the UN "
                "accepts it as the main district. The countries dataset just lists it.",
         "source": "Nauru; Yaren District. " + WIKI + " " + DS},
        {"type": "bignum", "kicker": "Stat 04", "number": "80%", "numsize": "s3", "bg": "",
         "label": "of the land stripped by mining",
         "title": "Phosphate, strip-mined for about a century from 1900. The viable reserves "
                  "ran out in the 1990s.", "size": "h-sm",
         "source": "Nauru. The article says the mined land was left uninhabitable. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "No armed forces, and 71 metres of elevation.",
         "sub": "Australia is responsible for Nauru's defence under an informal agreement "
                "between the two countries. The high point of the plateau, Command Ridge, is "
                "71 m above the sea.",
         "source": "Nauru. " + WIKI},
    ],
    """
Nauru has no capital city. Not a small one, not a disputed one. None.

Yaren is what every list puts in the box, and the countries dataset we check against lists it too. But Wikipedia's own Yaren article is blunt about it: the republic does not have cities nor an official capital, and Yaren is accepted by the United Nations as the "main district". Nauru's own page hedges to "de facto capital". The island is divided into fourteen administrative districts and that is the whole of it.

NAURU BY NUMBERS
Area — 21 km², the third-smallest country in the world
Administrative districts — 14
Official capital — none
Land stripped by phosphate mining — about 80%
Highest point — Command Ridge, 71 m

The mining is the part that stops being funny. Most of the interior was strip-mined for phosphate for about a century starting in 1900, profitably and destructively, and the article says it left roughly 80% of the land uninhabitable. Income from the mines made Nauruans among the richest people in the world. The viable reserves were exhausted in the 1990s.

There is no army. Australia is responsible for Nauru's defence under an informal agreement, and a small police force operates under civilian control.

This is the kind of fact a dataset gets wrong quietly, and then everyone repeats. We nearly did.

Which country did you think was the smallest?
""",
    ["nauru", "pacific", "micronesia", "geographyfacts", "didyouknow", "maps",
     "worldfacts", "islands", "phosphate", "earthbynumbers"],
)

post(
    "new-zealand-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "New Zealand is the<br>dry part of a<br>sunken continent.",
         "sub": "Five stats from the top of Zealandia."},
        {"type": "bignum", "kicker": "Stat 02", "number": "94%", "numsize": "s3", "bg": "",
         "label": "of Zealandia is underwater",
         "title": "About 4,900,000 km² of continental crust. New Zealand is the largest piece "
                  "above the sea.", "size": "h-sm",
         "source": "Zealandia. New Caledonia is the next largest part above water. " + WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink", "size": "h-sm",
         "title": "In 2017 eleven geologists said it qualifies as a continent.",
         "sub": "Zealandia has been described as a submerged continent, a continental "
                "fragment and a microcontinent. If it counts as a microcontinent, it is the "
                "largest one there is.",
         "source": "Zealandia. The name was proposed by Bruce Luyendyk in 1995. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "1,487", "numsize": "s3", "bg": "",
         "label": "km to the nearest continent",
         "title": "Australia, across the Tasman. Zealandia broke off Gondwana 83 to 79 "
                  "million years ago.", "size": "h-sm",
         "source": "New Zealand; Zealandia. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "The world's steepest street lost its title and won it back.",
         "sub": "Baldwin Street in Dunedin was recognised in 1987, lost to Ffordd Pen Llech "
                "in Wales on 16 July 2019, and got it back on 8 April 2020 when Guinness "
                "decided steepness must be measured along the central axis.",
         "source": "Baldwin Street, maximum slope about 1:2.86, or 19°. " + WIKI},
    ],
    """
New Zealand is not an island group. It is the part of a continent that is still above water.

Zealandia is about 4,900,000 km² of continental crust, and 94% of it is under the Pacific. New Zealand is the largest piece showing, followed by New Caledonia. In 2017 a team of eleven geologists from New Zealand, New Caledonia and Australia concluded that it meets every requirement to be called a submerged continent rather than a microcontinent or a continental fragment.

NEW ZEALAND BY NUMBERS
Zealandia — about 4,900,000 km² of continental crust
Share of it underwater — 94%
Broke off Gondwana — 83 to 79 million years ago
Distance to Australia — about 1,487 km across the Tasman Sea
Official languages — three, including Māori since 1987 and NZ Sign Language since 2006

The isolation is the reason for everything else about the place. Eighty million years of it, which is long enough to produce birds that forgot how to fly.

Then there is Baldwin Street in Dunedin, which has had the strangest record history of anything on this account. Guinness recognised it as the world's steepest street in 1987. On 16 July 2019 it lost the title to Ffordd Pen Llech in Wales, measured at 37.45% against Baldwin's 35%. On 8 April 2020 Guinness decided steepness had to be measured along a street's central axis, which put the Welsh street at 28.6% and Baldwin at 34.8%, and the title went back to Dunedin.

We cut one figure: Zealandia's own article gives three different areas, and we used the one in its lead.

Is Zealandia a continent, or are we all just being generous?
""",
    ["newzealand", "zealandia", "geology", "continents", "dunedin", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "earthbynumbers"],
)

post(
    "mexico-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "The crater that<br>killed the dinosaurs<br>is in Mexico.",
         "sub": "Five stats from a country with a very bad day on its record."},
        {"type": "bignum", "kicker": "Stat 02", "number": "66", "numsize": "s2", "bg": "",
         "label": "million years ago — the Chicxulub impact",
         "title": "Dated to 66,043,000 years ago, give or take 11,000.", "size": "h-sm",
         "source": "Chicxulub crater, buried under the Yucatán Peninsula. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "10", "bg": "ink", "sea": True,
         "label": "km — the width of the asteroid",
         "title": "The crater is 180, or 200, or 300 km across, depending which part of the "
                  "article you read.", "size": "h-sm",
         "source": "Chicxulub crater. The 300 km figure is described as more recent "
                   "evidence. " + WIKI},
        {"type": "fact", "kicker": "Stat 04", "bg": "", "size": "h-sm",
         "title": "You can see the rim from the ground. It is a ring of sinkholes.",
         "sub": "A circular alignment of cenotes overlies the measured rim of the crater. "
                "The crater itself sits about a kilometre down, and was found by oil company "
                "geophysicists in 1978.",
         "source": "Cenote; Chicxulub crater. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Mexico City is sinking almost 50 cm a year.",
         "sub": "It has gone down as much as nine metres in places since the start of the "
                "20th century. The city sits on a drained lake bed and the groundwater is "
                "being pumped out from under it.",
         "source": "Mexico City, at an altitude of 2,240 m. " + WIKI},
    ],
    """
The asteroid that ended the dinosaurs landed in Mexico, and you can still trace the edge of the hole it made.

Chicxulub is buried under the Yucatán Peninsula, about a kilometre down. It was formed 66,043,000 years ago, give or take 11,000, by an impactor around 10 km across. Wikipedia's wording on the consequence is careful and worth copying: it is now widely accepted that the devastation and climate disruption resulting from the impact was the primary cause of the Cretaceous–Paleogene extinction event, which killed about 75% of plant and animal species, including every non-avian dinosaur.

MEXICO BY NUMBERS
Chicxulub impact — 66,043,000 years ago
The asteroid — about 10 km across
The crater — 180 km, or 200, or 300, depending on the paragraph
Indigenous languages with co-official status — 68
Mexico City — sinking almost 50 cm a year

The crater's width is a genuine mess on the page: the infobox says 180 to 200 km, the body says 200, and a later line says more recent evidence suggests 300 km with the 180 km ring being an inner wall.

The part that is easy to miss is that you can see it. A higher-density circular alignment of cenotes — the sinkholes the Yucatán is famous for — sits directly over the measured rim. People have been swimming in the edge of an extinction event for a very long time. The crater was found in 1978 by geophysicists working for the state oil company, and identified in a paper in 1991.

And Spanish is not constitutionally the official language. The article calls it the de facto official language of the federal government, legally equal with 68 indigenous languages.

Did you know you could see the crater from the ground?
""",
    ["mexico", "chicxulub", "yucatan", "cenotes", "dinosaurs", "geology",
     "geographyfacts", "didyouknow", "worldfacts", "earthbynumbers"],
)

post(
    "turkey-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Istanbul's best<br>known fact comes<br>with an asterisk.",
         "sub": "Five stats from a country that also changed its name."},
        {"type": "fact", "kicker": "Stat 02", "bg": "", "size": "h-sm",
         "title": "Nobody will call it the only city on two continents.",
         "sub": "Istanbul's article says just that it is a city on two continents, with about "
                "two-thirds of the population in Europe. The Bosporus article calls it one of "
                "very few intercontinental cities in the world.",
         "source": "Istanbul; Bosporus. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "700", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "metres — the Bosporus at its narrowest",
         "title": "Or 750. The body and the infobox disagree. Either way, the world's "
                  "narrowest strait used for international navigation.", "size": "h-sm",
         "source": "Bosporus. Length is given as 30 km and as 31 km on the same page. "
                   + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "3,755", "numsize": "s3", "bg": "",
         "label": "km² — Lake Van",
         "title": "Turkey's largest lake. A saline soda lake with no outlet, at pH 9.7 to 9.8.",
         "size": "h-sm",
         "source": "Lake Van, one of the world's few endorheic lakes over 3,000 km². "
                   + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "The country changed its name in 2022.",
         "sub": "In May 2022 the Turkish government asked the United Nations and other "
                "international organisations to use Türkiye in English. The UN agreed. Until "
                "then the official English name was the Republic of Turkey.",
         "source": "Türkiye. Total area 783,562 km². " + WIKI},
    ],
    """
Istanbul is a city on two continents. It is not, as far as its own encyclopedia entry will commit, the only one.

This is the most repeated fact about the city and the sources will not back it the way people say it. The Istanbul article says it is "a city on two continents" and that about two-thirds of its population live in Europe. The Bosporus article goes one notch further and says Istanbul is "one of very few intercontinental cities in the world". Neither says only. We are not going to upgrade them.

TÜRKIYE BY NUMBERS
Total area — 783,562 km²
Land neighbours — Georgia, Armenia, Azerbaijan, Iran, Iraq, Syria, Greece, Bulgaria
Bosporus — 700 m at its narrowest, or 750
Lake Van — 3,755 km², pH 9.7 to 9.8
Name changed at the UN — May 2022

The Bosporus is the better statistic anyway. It is the world's narrowest strait used for international navigation, which is a mouthful but an exact one, and the page cannot decide whether the narrow point is 700 m or 750 m, or whether the strait is 30 km or 31 km long. Container ships thread it daily.

Lake Van is the one almost nobody mentions. It is the country's largest lake at 3,755 km², it is a saline soda lake with no outlet at all, and the water is strongly alkaline at pH 9.7 to 9.8. Until the Pleistocene it drained southwest. Now it just sits there getting saltier.

And the name. In May 2022 the government asked the UN and other international organisations to use Türkiye in English, and the UN agreed. Until then the official English name was the Republic of Turkey.

What is the most-repeated "fact" about your country that does not survive checking?
""",
    ["turkiye", "istanbul", "bosporus", "lakevan", "geographyfacts", "didyouknow",
     "maps", "worldfacts", "europe", "earthbynumbers"],
)

post(
    "south-africa-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "South Africa<br>has three<br>capital cities.",
         "sub": "Five stats from a country that split the job three ways."},
        {"type": "fact", "kicker": "Stat 02", "bg": "", "size": "h-sm",
         "title": "Pretoria executive. Cape Town legislative. Bloemfontein judicial.",
         "sub": "Parliament sits in Cape Town. The President and Cabinet work from the Union "
                "Buildings in Pretoria. The article states the arrangement without ever "
                "calling it unusual.",
         "source": "South Africa; Pretoria. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "12", "numsize": "s2",
         "bg": "ink", "sea": True,
         "label": "official languages — or 11",
         "title": "The lead and infobox say 12, including South African Sign Language. A "
                  "later section says 11 official spoken languages.", "size": "h-sm",
         "source": "South Africa. The twelfth was approved by the National Assembly on "
                   "3 May 2023. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "69%", "numsize": "s3", "bg": "",
         "label": "of Cape plant species grow nowhere else",
         "title": "Over 9,000 vascular plant species in 78,555 km² — the smallest of the "
                  "world's six floral kingdoms.", "size": "h-sm",
         "source": "Cape Floristic Region, located entirely within South Africa. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "It has another country inside it.",
         "sub": "South Africa encloses Lesotho completely. It also borders Namibia, Botswana, "
                "Zimbabwe, Mozambique and Eswatini — and Eswatini only escapes being enclosed "
                "because it reaches Mozambique.",
         "source": "South Africa. Total area 1,221,037 km². " + WIKI + " " + DS},
    ],
    """
South Africa has three capital cities, and each one does a different third of the job.

Pretoria is the administrative capital and holds the executive: the President, the Cabinet, the Union Buildings. Cape Town is the legislative capital, because that is where Parliament sits. Bloemfontein is regarded as the judicial capital. The article lays this out flatly and never once calls it unusual, which it absolutely is.

SOUTH AFRICA BY NUMBERS
Capitals — 3
Official languages — 12, or 11, depending on the section
Total area — 1,221,037 km²
Cape Floristic Region — over 9,000 vascular plant species, 69% endemic
Countries entirely enclosed — 1

The language count is its own small argument. The lead and the infobox both say twelve official languages, South African Sign Language included, which the National Assembly approved on 3 May 2023. A later section of the same article says South Africa has eleven official spoken languages and lists them. Both are true and the page does not reconcile them.

The statistic we would actually travel for is the plants. The Cape Floristic Region is 78,555 km², sits entirely inside one country, holds over 9,000 vascular plant species, and 69 percent of them grow nowhere else on Earth. It is the smallest of the six recognised floral kingdoms of the world. A fynbos hillside outside Cape Town is doing something no other hillside anywhere does.

And it completely encloses Lesotho, which is a different kind of statistic.

Three capitals: sensible federalism, or an expensive compromise?
""",
    ["southafrica", "capetown", "pretoria", "fynbos", "capefloristicregion",
     "geographyfacts", "didyouknow", "worldfacts", "africa", "earthbynumbers"],
)

post(
    "singapore-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Singapore has<br>grown. Nobody<br>agrees how much.",
         "sub": "Five stats from a country that builds its own land."},
        {"type": "bignum", "kicker": "Stat 02", "number": "580", "numsize": "s3", "bg": "",
         "label": "km² in the 1960s",
         "title": "The same article projects 770 km² by the 2030s — an increase of over 30%.",
         "size": "h-sm",
         "source": "Singapore. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "22%", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "growth since 1965, says another page",
         "title": "And three pages give three current areas: 744.3, 736.3 and 728.3 km².",
         "size": "h-sm",
         "source": "Singapore; Land reclamation in Singapore; City-state. " + WIKI},
        {"type": "fact", "kicker": "Stat 04", "bg": "", "size": "h-sm",
         "title": "Its neighbours stopped selling it sand.",
         "sub": "Indonesia banned sand exports specifically to Singapore in 2007. Vietnam "
                "followed in 2009, and Cambodia the same year with a narrower ban. Malaysia "
                "had banned sand exports generally in 1997.",
         "source": "Land reclamation in Singapore. 14.6 million tons imported in 2010 "
                   "alone. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Four official languages, and one national one.",
         "sub": "English, Malay, Mandarin and Tamil are all official. Malay alone is the "
                "national language. The highest natural point in the country is Bukit Timah "
                "Hill, at 163.63 m.",
         "source": "Singapore. " + WIKI},
    ],
    """
Singapore has been making more of itself for sixty years, and its own encyclopedia entry cannot settle on how much.

One page says reclamation took the land area from roughly 580 km² in the 1960s towards 770 km² by the 2030s, an increase of over 30%. Another says Singapore has increased its land mass by 22% since independence in 1965. A third gives the current area as 728.3 km², while the first says 744.3 and the second says 736.3. They are measuring different things at different dates and nobody has lined them up.

SINGAPORE BY NUMBERS
Land area in the 1960s — about 580 km²
Current area — 744.3 km², or 736.3, or 728.3
Growth since independence — over 30%, or 22%
Sand imported in 2010 alone — 14.6 million tons
Highest natural point — Bukit Timah Hill, 163.63 m

Building land needs sand, and that is where it gets diplomatic. Singapore has used so much that it ran out of its own and imports it. Malaysia banned sand exports in 1997. Indonesia enacted a ban against exporting sand specifically to Singapore in 2007. Vietnam did the same in 2009, and Cambodia followed the same year with a less all-encompassing version.

The language arrangement is the other thing worth knowing. English, Malay, Mandarin and Tamil are the four official languages. Malay on its own is the national language. Those are two different statuses and both are listed.

One more: urbanisation has cost the island 95% of its historical forests, and about 10% of the land is now set aside for parks and nature reserves.

Should a country be allowed to buy sand to build new land?
""",
    ["singapore", "landreclamation", "citystate", "bukittimah", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "southeastasia", "earthbynumbers"],
)

post(
    "greece-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "There is a state<br>inside Greece<br>that bans women.",
         "sub": "Five stats from a self-governing monastic republic."},
        {"type": "bignum", "kicker": "Stat 02", "number": "1046", "numsize": "s3", "bg": "",
         "label": "the year the ban was proclaimed",
         "title": "Mount Athos. The prohibition was proclaimed by several emperors, including "
                  "Constantine Monomachos.", "size": "h-sm",
         "source": "Mount Athos; Monastic community of Mount Athos. Women are prohibited by "
                   "Greek law and religious tradition. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "20", "numsize": "s2",
         "bg": "ink", "sea": True,
         "label": "monasteries across 335.6 km²",
         "title": "A self-governed part of the Greek State, whose sovereignty remains intact. "
                  "The administration sits at Karyes.", "size": "h-sm",
         "source": "Monastic community of Mount Athos. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "100", "numsize": "s2", "bg": "",
         "label": "Orthodox visitors a day, plus 10 others",
         "title": "Men only, each needing a permit called a diamonitirion.", "size": "h-sm",
         "source": "Monastic community of Mount Athos. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Female animals are banned too. Cats are exempt.",
         "sub": "The rule is called the avaton. Cows and sheep are barred along with women, "
                "and the article gives one exception: cats, for their mousing abilities.",
         "source": "Monastic community of Mount Athos. " + WIKI},
    ],
    """
There is a self-governing state inside Greece where no woman has legally set foot for nearly a thousand years.

Mount Athos is 335.6 km² at the end of a peninsula in northern Greece, holding twenty monasteries and governed by them. The Greek constitution describes it as a self-governed part of the Greek State whose sovereignty remains intact. Its administrative centre is Karyes. Women are prohibited from entering by Greek law and by religious tradition, a ban proclaimed by several emperors including Constantine Monomachos in a chrysobull of 1046.

GREECE BY NUMBERS
Mount Athos — 335.6 km², 20 monasteries
The ban on women — proclaimed in a chrysobull of 1046
Daily visitors — 100 Orthodox men and 10 non-Orthodox men
Coastline — 13,676 km, the longest in the Mediterranean basin
Islands — between 1,200 and 6,000 depending on the definition, 227 inhabited

Getting in means a permit called a diamonitirion, and the quota is 100 Orthodox and 10 non-Orthodox male pilgrims a day. Most arrive by ferry from Ouranoupoli. The rule extends to animals: cows and sheep are barred as well, and the article notes exactly one exception, cats, kept for their mousing abilities.

The rest of Greece is doing fine on numbers too. The coastline is 13,676 km, which its own page ranks 11th longest in the world and the longest in the Mediterranean basin. Approximately 80% of the country is mountains or hills. Olympus tops out at 2,918 m at Mytikas.

The island count is the usual mess. The article says between 1,200 and 6,000 depending on the definition, and settles only on 227 inhabited.

A thousand-year rule inside a modern EU state. Where do you land on it?
""",
    ["greece", "mountathos", "athos", "monastery", "geographyfacts", "didyouknow",
     "maps", "worldfacts", "europe", "earthbynumbers"],
)


# ══════════════════════════════════════════════ SPOTLIGHTS ════════

spotlight(
    "spot-armenia",
    "Armenia adopted<br>Christianity before<br>anyone else.",
    "AD 301, and the alphabet came a century later.",
    [["Capital", "Yerevan"], ["Land area", "29,743 km²"], ["Land borders", "4"],
     ["Coastline", "None — landlocked"], ["Currency", "Armenian dram"]],
    "Three reasons",
    [{"name": "Lake Sevan",
      "note": "1,242 km² at 1,900 m — the largest body of water in Armenia and the Caucasus."},
     {"name": "The alphabet",
      "note": "36 letters, developed around 405 AD by Mesrop Mashtots, and still in use."},
     {"name": "The terrain",
      "note": "85.9% mountain area, which the article notes is more than Switzerland or Nepal."}],
    {"title": "Armenia's national mountain is in another country.", "size": "h-sm",
     "sub": "Mount Ararat, 5,137 m, stands in Turkey and is clearly visible from Armenia. "
            "It is regarded as a symbol of the land and appears on the national emblem.",
     "source": "Armenia. " + WIKI},
    "Three to build a trip around",
    [{"name": "Yerevan",
      "note": "Founded in the summer of 782 BC, and called one of the world's oldest continuously inhabited cities."},
     {"name": "Lake Sevan",
      "note": "Soviet drainage dropped its level by about 20 m and its volume by over 40%."},
     {"name": "Mount Aragats",
      "note": "The land rises to 4,090 m here. No point in the country is below 390 m."}],
    """
Armenia became the first state in the world to adopt Christianity as its official religion, in AD 301.

That is the lead of its own article, stated without hedging: under the influence of Gregory the Illuminator, King Tiridates III proclaimed Christianity the state religion in 301, and Armenia thus became the first officially Christian state. Christianity had first appeared there in the 1st century.

ARMENIA BY NUMBERS
Land area — 29,743 km²
Land neighbours — 4, and it is landlocked
Mountain area — 85.9%
Lake Sevan — 1,242 km² at 1,900 m
Alphabet — 36 original letters, around 405 AD

The alphabet is the other founding act. Mesrop Mashtots developed it around 405 AD and it is still in use. Two more letters were added in the Middle Ages to carry foreign sounds, taking it from 36 to 38, and the 1920s orthography reform treats a ligature as a letter, which gets you to 39. Three counts, all correct, depending on the century.

Lake Sevan is the thing to go and look at: 1,242 km² of water at 1,900 m, the largest body of water in Armenia and in the Caucasus, and the second largest lake in the world relative to its altitude. Soviet-era drainage dropped it by around 20 m and cut its volume by more than 40%.

And the mountain on the national emblem is in Turkey. Ararat is 5,137 m, the highest in the region, historically part of Armenia, visible from Yerevan on a clear day and entirely out of reach.

Which country's national symbol sits outside its borders?
""",
    ["armenia", "yerevan", "lakesevan", "ararat", "caucasus", "traveltips",
     "geographyfacts", "worldfacts", "christianity", "earthbynumbers"],
    why_source="Lake Sevan; Armenian alphabet; Armenia. " + WIKI,
    go_source="Armenia; Lake Sevan. " + WIKI,
)

spotlight(
    "spot-rwanda",
    "The land of a<br>thousand hills is<br>not a slogan.",
    "Rwanda, where the mountains hold the last of something.",
    [["Capital", "Kigali"], ["Land area", "26,338 km²"], ["Land borders", "4"],
     ["Coastline", "None — landlocked"], ["Currency", "Rwandan franc"]],
    "Three reasons",
    [{"name": "Volcanoes National Park",
      "note": "160 km² of rainforest across five of the eight Virunga volcanoes. Dian Fossey's base."},
     {"name": "The gorillas",
      "note": "An estimated 1,063 mountain gorillas exist, about 80% of them in the Virungas."},
     {"name": "Nyungwe",
      "note": "1,019 km² of montane rainforest holding 13 primate species, a quarter of Africa's total."}],
    {"title": "On the last Saturday of the month, the country stops.", "size": "h-sm",
     "sub": "Umuganda is a national morning of mandatory community service, 8am to 11am, for "
            "everyone between 18 and 65. Most normal services close and public transport is "
            "limited.",
     "source": "Rwanda. " + WIKI},
    "Three past Kigali",
    [{"name": "Musanze",
      "note": "The base for Volcanoes National Park and for Mount Karisimbi, 4,507 m, the country's high point."},
     {"name": "Nyungwe",
      "note": "Known for its chimpanzees and its canopy walkway, and called the best preserved montane rainforest in Africa."},
     {"name": "Lake Kivu",
      "note": "The western edge, where the hills run down to the DRC border."}],
    """
Rwanda is 26,338 km² and almost none of it is flat. The nickname is pays des mille collines, the land of a thousand hills, and it is doing descriptive work rather than marketing.

RWANDA BY NUMBERS
Land area — 26,338 km², 144th in the world
Land neighbours — 4: Uganda, Tanzania, Burundi, DR Congo
Highest point — Mount Karisimbi, 4,507 m
Volcanoes National Park — 160 km², five of the eight Virunga volcanoes
Mountain gorillas remaining — an estimated 1,063

The gorillas are the reason most people come and the number deserves care. The article's lead says 1,063 as of 2019; its body says 1,063 as of 2025. Same figure, two dates, unreconciled. About 80% of them live in the Virunga Mountains shared between the DRC, Rwanda and Uganda, and the species is listed as endangered. Volcanoes National Park covers five of the eight Virunga volcanoes and was where Dian Fossey based her research.

Nyungwe is the one people skip. It is 1,019 km² of montane rainforest, bamboo, grassland, swamp and bog, described as most likely the best preserved montane rainforest in Africa, and it holds 13 primate species — 25% of Africa's total — including chimpanzees.

The detail that says most about the country is administrative. On the last Saturday of every month, from 8am to 11am, everyone between 18 and 65 is expected to turn out for umuganda, mandatory community service: cleaning streets, building houses. Most services shut and public transport is limited while it happens.

Would a mandatory community morning work where you live?
""",
    ["rwanda", "kigali", "gorillas", "virunga", "nyungwe", "eastafrica",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Volcanoes National Park; Mountain gorilla; Nyungwe Forest. " + WIKI,
    go_source="Rwanda; Nyungwe Forest. " + WIKI,
)

spotlight(
    "spot-panama",
    "Crossing to the<br>Pacific means<br>heading southeast.",
    "Panama, where the canal runs the way nobody expects.",
    [["Capital", "Panama City"], ["Land area", "75,417 km²"],
     ["Land borders", "2 — Colombia, Costa Rica"], ["Official language", "Spanish"],
     ["Currency", "Balboa and US dollar"]],
    "Three reasons",
    [{"name": "The canal",
      "note": "82 km in the infobox, 80 in the body. An average transit took 11.38 hours in 2017."},
     {"name": "Gatun Lake",
      "note": "Ships are lifted to an artificial freshwater lake above sea level, then let down the other side."},
     {"name": "The Darién Gap",
      "note": "Where the Pan-American Highway stops. There is no road, not even a primitive one."}],
    {"title": "Two continents are not joined by road.", "size": "h-sm",
     "sub": "The Pan-American Highway runs about 30,000 km and breaks at the Darién Gap. "
            "Panama and Colombia both oppose building through it, as do environmentalists. "
            "Attempts failed in the 1970s and the 1990s.",
     "source": "Pan-American Highway; Darién Gap. " + WIKI},
    "Three to build a trip around",
    [{"name": "Panama City",
      "note": "The Pacific end of a waterway its own pages measure at 80, 82 or 83 km."},
     {"name": "The locks",
      "note": "Three up and three down per transit. The expanded waterway opened on 26 June 2016."},
     {"name": "Soberanía National Park",
      "note": "More than 525 bird species recorded in one park, half an hour from the capital."}],
    """
Sail from the Atlantic to the Pacific through the Panama Canal and you travel southeast. Not west. Southeast.

The article puts it plainly: while globally the Atlantic is east of the isthmus and the Pacific is west, the general direction of the canal passage from the Atlantic to the Pacific is from northwest to southeast. Panama bends. In formal nautical communications they give up and just say southbound and northbound.

PANAMA BY NUMBERS
Land area — 75,417 km² in the dataset, 74,177.3 km² in the article's body
Land neighbours — 2: Colombia and Costa Rica
Canal length — 82 km in the infobox, 80 in the body, 83 on the Panama page
Average transit in 2017 — 11.38 hours
Currency — the balboa, fixed 1:1 to the US dollar since 1903

A transit is not a trench at sea level. Ships are lifted by locks into Gatun Lake, an artificial freshwater lake above the sea, carried across, and let down the far side — three locks up and three down. The canal opened on 15 August 1914 with the cargo ship SS Ancon, passed to full Panamanian control at noon on 31 December 1999, and the expanded locks began commercial operation on 26 June 2016.

Then there is the gap. The Pan-American Highway runs about 30,000 km and stops dead at the Darién, resuming roughly 106 km later in Colombia. There is no road, not even a primitive one. Attempts failed in the 1970s and the 1990s, and Panama and Colombia both oppose building through it, along with environmental organisations and indigenous groups. North and South America are separated by road.

Would you want a road built through the Darién Gap?
""",
    ["panama", "panamacanal", "dariengap", "centralamerica", "panamacity",
     "traveltips", "geographyfacts", "worldfacts", "maps", "earthbynumbers"],
    why_source="Panama Canal; Darién Gap. " + WIKI,
    go_source="Panama; Panama Canal. " + WIKI,
)

spotlight(
    "spot-taiwan",
    "Over two hundred<br>peaks above<br>3,000 metres.",
    "On an island you can drive across in a morning.",
    [["Capital", "Taipei"], ["Land area", "36,193 km²"], ["Land borders", "None"],
     ["Official language", "Chinese"], ["Currency", "New Taiwan dollar"]],
    "Three reasons",
    [{"name": "The mountains",
      "note": "More than two hundred peaks over 3,000 m. The island is 55% forest and woodland."},
     {"name": "Taroko Gorge",
      "note": "One of only three river-carved gorges in the world cut entirely through pure marble."},
     {"name": "Yushan",
      "note": "3,952 m — the highest point in the western Pacific outside the Kamchatka Peninsula."}],
    {"title": "The island is still being pushed upwards.", "size": "h-sm",
     "sub": "Taiwan formed about 4 to 5 million years ago at a convergent boundary between "
            "the Philippine Sea Plate and the Eurasian Plate. Taroko's page says the area "
            "continues to rise a few millimetres every year.",
     "source": "Geography of Taiwan; Taroko National Park. " + WIKI},
    "Three to build a trip around",
    [{"name": "Taroko",
      "note": "920 km² of national park, re-established on 28 November 1986 after an earlier 1937 version."},
     {"name": "Yushan",
      "note": "For about fifty years under Japanese rule this was the highest mountain in Japan, 176 m above Fuji."},
     {"name": "The east coast",
      "note": "Fault scarps from 120 to 1,200 m, and ocean over 4,000 m deep about 50 km offshore."}],
    """
Taiwan has more than two hundred peaks over 3,000 metres, on an island about 36,000 km² in size.

That is the Geography of Taiwan article's figure. Yushan's page counts 165 mountains above 3,000 m, which is a different convention on the same island, and we have seen 268 quoted elsewhere and could not find it on any page we read. More than two hundred is what the source says, so that is what we will say.

TAIWAN BY NUMBERS
Land area — 36,193 km² in the dataset; 36,197 and 35,808 both appear on Wikipedia
Peaks over 3,000 m — more than two hundred
Highest point — Yushan, 3,952 m
Forest and woodland — 55% of the island
Typhoons — about four direct hits a year

Yushan is the headline. At 3,952 m it is the highest point in the western Pacific region outside the Kamchatka Peninsula, and for about fifty years under Japanese rule it was the highest mountain in Japan, 176 m above Fuji.

Taroko Gorge is the one that does not photograph the way it looks. It is one of only three river-carved gorges in the world cut entirely through pure marble, in a 920 km² national park re-established on 28 November 1986 — an earlier version existed from 1937 and was abolished in 1945.

All of it is still moving. The island formed about 4 to 5 million years ago where the Philippine Sea Plate meets the Eurasian Plate, and the park's page says the area continues to rise a few millimetres every year. On the east coast the mountains quit abruptly: fault scarps of 120 to 1,200 m, and water more than 4,000 m deep about 50 km out.

Which island has the best mountains for its size?
""",
    ["taiwan", "taroko", "yushan", "hiking", "eastasia", "traveltips",
     "geographyfacts", "worldfacts", "mountains", "earthbynumbers"],
    why_source="Geography of Taiwan; Taroko National Park; Yushan. " + WIKI,
    go_source="Taroko National Park; Yushan; Geography of Taiwan. " + WIKI,
)

spotlight(
    "spot-romania",
    "The heaviest<br>building on Earth<br>is in Bucharest.",
    "And the second best-kept river delta in Europe is up the road.",
    [["Capital", "Bucharest"], ["Land area", "238,391 km²"], ["Land borders", "5"],
     ["Official language", "Romanian"], ["Currency", "Romanian leu"]],
    "Three reasons",
    [{"name": "The Palace of the Parliament",
      "note": "About 4,098,500 tonnes. Its own page cannot decide if it is the largest or the third."},
     {"name": "The Danube Delta",
      "note": "4,152 km² — Europe's second largest river delta, and the best preserved on the continent."},
     {"name": "Transfăgărășan",
      "note": "A road climbing to 2,042 m, built 1970 to 1974, usually shut from late October."}],
    {"title": "Eleven World Heritage Sites, and a delta still building itself.", "size": "h-sm",
     "sub": "The country holds 11 UNESCO World Heritage Sites. The Danube Delta was "
            "inscribed in 1991 and records over 320 species of birds during the summer.",
     "source": "Romania; Danube Delta. " + WIKI},
    "Three past Bucharest",
    [{"name": "The Danube Delta",
      "note": "Over 320 bird species in summer, across 4,152 km² of channels, reed and sandbar."},
     {"name": "The palace",
      "note": "1,100 rooms, eight underground levels, 365,000 m² of floor, and 92 m deep."},
     {"name": "The Făgăraș",
      "note": "The range the Transfăgărășan climbs. The road took from 1970 to 1974 to build."}],
    """
The heaviest building in the world is a parliament in Bucharest, and it weighs about 4,098,500 tonnes.

The Palace of the Parliament has 1,100 rooms, eight underground levels with a nuclear bunker at the bottom, 365,000 m² of floor area, and goes 92 m into the ground. Construction started on 25 June 1984 and finished in 1997, having been scheduled to take two years.

ROMANIA BY NUMBERS
Land area — 238,391 km² in the dataset, 238,397 on Wikipedia
Land neighbours — 5: Ukraine, Hungary, Serbia, Bulgaria, Moldova
Palace of the Parliament — about 4,098,500 tonnes, 1,100 rooms
Danube Delta — 4,152 km², over 320 bird species in summer
UNESCO World Heritage Sites — 11

Its own article cannot agree on what kind of record it holds. The lead calls it the largest civilian administrative building in the world, after the Pentagon among military ones. A later section calls it the world's third-largest administrative building, after the Pentagon and Thailand's Sappaya-Sapasathan. The infobox hedges to "world's largest civilian building with an administrative function". The weight is not in dispute.

The Danube Delta is the opposite kind of place and the better reason to go. At 4,152 km² it is Europe's second largest river delta after the Volga, and its own page calls it the best preserved on the continent. Over 320 species of birds are there during summer, and it has been a World Heritage Site since 1991.

Between the two sits the Transfăgărășan, a road built from 1970 to 1974 that climbs to 2,042 m and is usually closed from late October until late June because of snow. Its page says 151 km in the infobox and 90 km in the body, so plan loosely.

Heaviest building on Earth, or just the heaviest thing anyone bothered to weigh?
""",
    ["romania", "bucharest", "danubedelta", "transfagarasan", "carpathians",
     "traveltips", "geographyfacts", "worldfacts", "europe", "earthbynumbers"],
    why_source="Palace of the Parliament; Danube Delta; Transfăgărășan. " + WIKI,
    go_source="Danube Delta; Palace of the Parliament; Transfăgărășan. " + WIKI,
)

spotlight(
    "spot-botswana",
    "A river that<br>never reaches<br>the sea.",
    "It arrives in the middle of a desert, in the dry season.",
    [["Capital", "Gaborone"], ["Land area", "582,000 km²"], ["Land borders", "4"],
     ["Coastline", "None — landlocked"], ["Currency", "Botswana pula"]],
    "Three reasons",
    [{"name": "The Okavango Delta",
      "note": "One of the few interior delta systems that do not flow into a sea or ocean."},
     {"name": "Makgadikgadi",
      "note": "16,000 km² of salt pan, all that is left of a lake once larger than Switzerland."},
     {"name": "Chobe",
      "note": "Known for an elephant population the page estimates at around 50,000."}],
    {"title": "The flood arrives in the dry season.", "size": "h-sm",
     "sub": "About 11 km³ of water a year spreads across the delta. The surge covers 1,200 km "
            "in around a month, and levels peak between June and August — Botswana's dry "
            "winter.",
     "source": "Okavango Delta. " + WIKI},
    "Three to build a trip around",
    [{"name": "The Okavango Delta",
      "note": "Inscribed on 22 June 2014 as the 1000th site on the UNESCO World Heritage List."},
     {"name": "Makgadikgadi",
      "note": "The largest single pan is about 4,900 km². Not one pan but many, with desert between."},
     {"name": "The Kalahari",
      "note": "Around 70% of the country. Population density is 4.1 per km²."}],
    """
The Okavango is a river that never reaches the sea. It runs into the Kalahari, spreads out, and evaporates.

Its article calls it one of the few interior delta systems that do not flow into a sea or ocean, sitting in the central part of the endorheic basin of the Kalahari Desert. Approximately 96 to 98% of the water entering the delta is lost to evapotranspiration, groundwater recharge and evaporation. A small amount leaves through the Thamalakane and Boteti rivers, and some drains into Lake Ngami. The rest just goes up.

BOTSWANA BY NUMBERS
Land area — 582,000 km² in the dataset, 581,730 on Wikipedia
Land neighbours — 4: Namibia, Zimbabwe, Zambia, South Africa
Water entering the delta — about 11 km³ a year
Kalahari Desert — around 70% of the country
Population density — 4.1 per km²

The timing is the strange part. The rain falls in Angola in January and February. The surge travels about 1,200 km in roughly a month, then spreads across the delta over the following months, and the flood peaks between June and August — in the middle of Botswana's dry winter. Animals walk into water that fell a season ago and a country away.

The delta was inscribed on 22 June 2014 as the 1000th site on the UNESCO World Heritage List.

East of it, the Makgadikgadi pans cover 16,000 km² and are what remains of a lake that once covered an area larger than Switzerland. The largest individual pan is about 4,900 km². The page is careful to note it is technically not one pan but many, with sandy desert in between.

We cut the delta's area: the page gives 6,000–15,000 km², 37,500 km² and 15,000 km² in three different places.

Where else does water end a journey without reaching an ocean?
""",
    ["botswana", "okavango", "makgadikgadi", "chobe", "kalahari", "safari",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Okavango Delta; Makgadikgadi Pan; Chobe National Park. " + WIKI,
    go_source="Okavango Delta; Makgadikgadi Pan; Botswana. " + WIKI,
)


# ═══════════════════════════════════════════════════════ TOP 5 ════

top5(
    "top5-caves",
    "The Blue Grotto<br>is a five-minute<br>boat ride.",
    "Opinion. Five caves worth the trouble of getting underground.",
    [
        ("Hang Son Doong", "Quang Binh, Vietnam",
         "The largest known cave passage in the world by volume — over 5 km long, 200 m "
         "high, 150 m wide. One operator has had permission since 2017, and it shuts "
         "entirely from September to December.",
         "Hang Sơn Đoòng. Found in 1990 by Hồ Khanh, surveyed in 2009. " + WIKI),
        ("Veryovkina", "Abkhazia, Georgia",
         "2,209 m deep. It reached 2,223 m in August 2023 and then lost 14 m in August 2024 "
         "when someone remeasured it. Its own page calls it both a world record and the "
         "second deepest known.",
         "Veryovkina Cave, after Krubera. " + WIKI),
        ("Mammoth Cave", "Kentucky, USA",
         "More than 426 miles — 686 km — of passage surveyed as of 2025, which its page says "
         "is over 1.5 times the length of the second longest cave system in the world.",
         "Mammoth Cave National Park. " + WIKI),
        ("Eisriesenwelt", "Werfen, Austria",
         "42 km of cave, of which only the first kilometre is ice and open to visitors. Open "
         "1 May to 26 October. A cable car built in 1955 cut the 90-minute climb to three.",
         "Eisriesenwelt, called the largest ice cave in the world. " + WIKI),
        ("Waitomo", "Waikato, New Zealand",
         "Glowworms on the ceiling: Arachnocampa luminosa, a fungus gnat endemic to New "
         "Zealand. About 500,000 visitors a year before the pandemic, back to that by 2024.",
         "Waitomo Glowworm Caves. " + WIKI),
    ],
    """
The Blue Grotto on Capri is a five-minute boat ride you queue an hour for, lying flat in a rowing boat while someone sings at you. It is blue. That is the whole thing.

Five caves that are worth going underground for. Opinion; the figures are Wikipedia's.

01 HANG SON DOONG, Vietnam — the largest known cave passage in the world by volume. The main passage is more than 5 km long, 200 m high and 150 m wide, with a cross-section believed to be twice that of the next largest, in Malaysia. A local man named Hồ Khanh found the entrance on 10 December 1990 and lost it again; he rediscovered it in 2008, and a British-Vietnamese expedition surveyed it in April 2009. The first tourist group went in during August 2013 at US$3,000 each. One operator has had permission since 2017, and the cave closes entirely from September to December when the river rises.

02 VERYOVKINA, Georgia — 2,209 m deep, and a lesson in how records are made. The depth went to 2,223 m in August 2023 and came back down to 2,209 m in August 2024 after remeasurement. The page's own lead calls it the second deepest known cave on Earth after Krubera, while its timeline records a 2017 world depth record. One caver died of hypothermia at about -1,100 m in 2021.

03 MAMMOTH CAVE, Kentucky — more than 426 miles, or 686 km, of passageway surveyed as of 2025, which makes it the longest known cave system in the world by a margin of more than half again over second place.

04 EISRIESENWELT, Austria — 42 km of cave of which only the first kilometre is ice, and that is the part you walk. Open 1 May to 26 October. Photography is not allowed inside, and warm clothing is advised, which is a polite way of putting it.

05 WAITOMO, New Zealand — a boat under a ceiling of Arachnocampa luminosa, a fungus gnat endemic to the country. About 500,000 people a year went before the pandemic and numbers were back there by 2024.

Which cave have you been in that was better than the photos?
""",
    ["caves", "hangsondoong", "mammothcave", "eisriesenwelt", "waitomo", "caving",
     "travelinspo", "geographyfacts", "worldfacts", "adventuretravel", "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-glaciers",
    "A glacier you<br>drive to is<br>not a glacier.",
    "Opinion. Five that make you work for it, or at least get on a boat.",
    [
        ("Perito Moreno", "Santa Cruz, Argentina",
         "250 km² and 30 km long, with an ice face averaging 74 m above the water. Famous "
         "for being stable while everything else retreated — though it has been going back "
         "on its northern front since 2020.",
         "Perito Moreno Glacier. The ice-dam ruptures have no fixed frequency. " + WIKI),
        ("Baltoro", "Gilgit-Baltistan, Pakistan",
         "63 km of ice with K2 at 8,611 m above it, and Concordia at 4,600 m where it meets "
         "the Godwin-Austen. Research from 2001 to 2011 found it surging rather than "
         "retreating.",
         "Baltoro Glacier, reached from Skardu. " + WIKI),
        ("Vatnajökull", "Iceland",
         "7,700 km², covering about 8% of the country, with several volcanoes underneath it. "
         "The largest and most voluminous ice cap in Iceland.",
         "Vatnajökull, second in Europe by volume after Novaya Zemlya's ice cap. " + WIKI),
        ("Aletsch", "Valais, Switzerland",
         "22.6 km long and 81.7 km², the largest glacier in the Alps. It has lost 20% of its "
         "ice mass since 1850, and retreated 114.6 m in 2006 alone.",
         "Aletsch Glacier, part of a World Heritage Site since 2001. " + WIKI),
        ("Jostedal", "Norway",
         "Jostedalsbreen: 487 km², the largest glacier in continental Europe, running a "
         "little over 60 km. Its Briksdalsbreen arm retreated 146 m in 2006 and ice "
         "climbing there has stopped.",
         "Jostedal Glacier. The national park was established in 1991. " + WIKI),
    ],
    """
A glacier you can drive to is a viewpoint. The coach park, the boardwalk, the eleven minutes you are given before the next group arrives — none of that is the experience people think they are buying.

Five that are worth the trouble. Opinion; the figures are Wikipedia's.

01 PERITO MORENO, Argentina — 250 km², 30 km long, with an ice face averaging 74 m above the water, and the only one on this list you can stand in front of and watch calve. It was for years one of the few glaciers holding equilibrium while the rest retreated, and its page is careful about this now: it says it was previously in equilibrium, that the reason remains debated, and that since 2020 it has been retreating on its northern front. The ice dam it periodically forms and bursts has no reliable schedule.

02 BALTORO, Pakistan — 63 km of ice, approached from Skardu, running beneath K2 at 8,611 m, Broad Peak at 8,047 m and both Gasherbrums. Concordia, where it meets the Godwin-Austen Glacier at 4,600 m, is the trekking destination. Observations between 2001 and 2011 found it surging rather than retreating.

03 VATNAJÖKULL, Iceland — 7,700 km² and about 8% of the country, with volcanoes underneath including Grímsvötn. The largest and most voluminous ice cap in Iceland, and the second largest in Europe after the Severny Island ice cap of Novaya Zemlya.

04 ALETSCH, Switzerland — 22.6 km long, 81.7 km², the largest glacier in the Alps, and the one with the clearest numbers on what is happening: 20% of its ice mass gone since 1850, 3.2 km of retreat since 1870, and a record 114.6 m in 2006 alone.

05 JOSTEDALSBREEN, Norway — 487 km², the largest glacier in continental Europe, a little over 60 km long. Its Briksdalsbreen arm lost 146 m in 2006 and ice climbing there has been terminated.

Which glacier did you see, and is it still the same size?
""",
    ["glaciers", "peritomoreno", "aletsch", "vatnajokull", "baltoro", "jostedalsbreen",
     "travelinspo", "geographyfacts", "worldfacts", "adventuretravel", "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-national-parks",
    "Yellowstone is a<br>traffic jam with<br>geysers.",
    "Opinion. Five parks where the queue is not the main feature.",
    [
        ("Manú", "Madre de Dios, Peru",
         "17,163 km², with more than 1,000 bird species estimated, 4,385 identified plant "
         "species and 155 amphibians. The restricted zone is open to researchers only.",
         "Manú National Park, a World Heritage Site since 1987. " + WIKI),
        ("Jiuzhaigou", "Sichuan, China",
         "720 km² of blue, green and turquoise lakes and stepped waterfalls. Daily numbers "
         "are capped at 41,000 by timed ticket, and its own page admits it is still "
         "relatively difficult to reach.",
         "Jiuzhaigou, inscribed in 1992. 5.11 million visitors in 2024. " + WIKI),
        ("Kakadu", "Northern Territory, Australia",
         "19,804 km², listed in 1981 for both cultural and natural values. More than 5,000 "
         "recorded rock art sites, on land owned by Aboriginal traditional owners and leased "
         "back to the Director of National Parks.",
         "Kakadu National Park. Occupation for at least 40,000 years. " + WIKI),
        ("Gran Paradiso", "Aosta and Piedmont, Italy",
         "Italy's first national park, from 1922, created to stop the Alpine ibex being "
         "poached out. About 3,000 ibex then, 419 left by 1945, 4,000 by 2005. 724 km of "
         "marked trails.",
         "Gran Paradiso National Park, 703 km². " + WIKI),
        ("Plitvice", "Croatia",
         "Sixteen lakes visible from the surface, held apart by travertine barriers that grow "
         "up to 13 mm a year. Nearly 1.5 million visitors in 2024, capped at 12,000 a day.",
         "Plitvice Lakes National Park, founded 1949, inscribed 1979. " + WIKI),
    ],
    """
Yellowstone is a traffic jam with geysers. It is a genuinely extraordinary place that several million people a year experience through a windscreen, waiting for a parking space at Old Faithful.

Five parks where the crowd is not the main feature. Opinion; figures from Wikipedia.

01 MANÚ, Peru — 17,163 km² running from the Andes down into the Amazon. More than 1,000 bird species estimated, 4,385 identified plant species, 155 amphibians, 132 reptiles, 160 mammals. The park is zoned: the restricted use zone admits researchers only, there are five areas open to visitors, and the lower basin has five camping sites, three lodges and a canopy walkway.

02 JIUZHAIGOU, China — 720 km² of stepped waterfalls and lakes that are genuinely turquoise. It is capped at 41,000 visitors a day by timed ticket and still took 5.11 million people in 2024, with over 30,000 a day in peak season. Its own page notes it is relatively difficult to reach compared with other Chinese scenic sites, which is the only reason any of this works.

03 KAKADU, Australia — 19,804 km², inscribed in 1981 for both cultural and natural values. More than 5,000 recorded rock art sites, and archaeological evidence of Aboriginal occupation for at least 40,000 and possibly 65,000 years. Most of the land is owned by Aboriginal traditional owners and leased to the Director of National Parks.

04 GRAN PARADISO, Italy — the country's first national park, established in 1922 on land protected to stop the Alpine ibex being poached to nothing. There were about 3,000 ibex when it was instituted, 4,000 by 1933, and only 419 left by 1945. Back to 4,000 in 2005. The paths laid out for the ibex are now 724 km of marked trails.

05 PLITVICE, Croatia — sixteen lakes held apart by travertine barriers that are still growing, up to 13 mm a year. It is on this list with a warning: nearly 1.5 million people came in 2024, it is capped at 12,000 a day, and in 2018 UNESCO threatened to remove its World Heritage status.

Which famous national park did you find disappointing?
""",
    ["nationalparks", "manu", "jiuzhaigou", "kakadu", "granparadiso", "plitvice",
     "travelinspo", "geographyfacts", "worldfacts", "wildlife", "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-bridges",
    "Tower Bridge is<br>a road with a<br>gift shop in it.",
    "Opinion. Five bridges that are doing something harder.",
    [
        ("Millau Viaduct", "Aveyron, France",
         "343 m of structural height, which made it the tallest bridge in the world for over "
         "two decades, until late 2025. Its page does not say what took the title. 2,460 m "
         "long, opened 16 December 2004.",
         "Millau Viaduct, by Michel Virlogeux and Norman Foster. " + WIKI),
        ("Øresund", "Denmark and Sweden",
         "7,845 m of cable-stayed bridge that stops in the middle of the sea at Peberholm, "
         "an artificial island, and continues as a 4.05 km tunnel. Opened 1 July 2000.",
         "Øresund Bridge. Peberholm is a nature reserve, generally closed to the public. "
         + WIKI),
        ("Danyang–Kunshan", "Jiangsu, China",
         "164.8 km of viaduct carrying the Beijing–Shanghai high-speed line, and the longest "
         "bridge in the world by Guinness designation since 2011.",
         "Danyang–Kunshan Grand Bridge, opened 30 June 2011. " + WIKI),
        ("Si-o-se-pol", "Isfahan, Iran",
         "Thirty-three arches in two superimposed rows across 297.76 m, built between 1599 "
         "and 1602 to work as both a bridge and a dam.",
         "Si-o-se-pol. " + WIKI),
        ("Akashi Kaikyō", "Hyōgo, Japan",
         "A central span of 1,991 m, opened on 5 April 1998. The toll is 2,300 yen and about "
         "23,000 cars cross a day.",
         "Akashi Kaikyō Bridge. " + WIKI),
    ],
    """
Tower Bridge is a Victorian road bridge with a gift shop in it. It is on every London postcard and it is a nice piece of engineering for 1894, and it is not the most interesting bridge within a thousand miles of itself.

Five that are doing something harder. Opinion; the figures are Wikipedia's.

01 MILLAU VIADUCT, France — 343 m of structural height, 2,460 m long, crossing the Tarn valley on seven masts. It was the tallest bridge in the world for over two decades, until late 2025. Its own page says so and then declines to name whatever overtook it, so neither will we. Designed by the engineer Michel Virlogeux with the architect Norman Foster, opened 16 December 2004.

02 ØRESUND, Denmark and Sweden — the one with the trick. It runs 7,845 m from the Swedish coast and then stops in the middle of the strait at Peberholm, an artificial island, where it becomes the 4.05 km Øresund Tunnel and goes under the shipping lane. Opened 1 July 2000. Peberholm is now a nature reserve and public visits are generally not allowed.

03 DANYANG–KUNSHAN, China — 164.8 km of viaduct carrying the Beijing–Shanghai high-speed railway, and the longest bridge in the world in any category by Guinness designation since 2011. You do not look at this one. You ride across it for half an hour.

04 SI-O-SE-POL, Isfahan — thirty-three arches in two superimposed rows, 297.76 m long, built between 1599 and 1602 to serve as both a bridge and a dam. Four hundred years old and still the best place in the city to stand at night.

05 AKASHI KAIKYŌ, Japan — a central span of 1,991 m, opened 5 April 1998. Its page still describes that span in the present tense as the longest of any suspension bridge, and suspension records move, so we will give you the number and the date and leave the ranking alone. The toll is 2,300 yen and about 23,000 cars use it a day.

Which bridge is worth crossing for its own sake?
""",
    ["bridges", "millauviaduct", "oresund", "akashikaikyo", "isfahan", "engineering",
     "travelinspo", "geographyfacts", "worldfacts", "architecture", "earthbynumbers"],
)

top5(
    "top5-monasteries",
    "Mont-Saint-Michel<br>is a gift shop<br>with an abbey<br>on top.",
    "Opinion. Five that are still difficult to reach, which is the point.",
    [
        ("Meteora", "Thessaly, Greece",
         "Twenty-four monasteries at their 16th-century peak, six left, four still working as "
         "monasteries. Until steps were cut into the rock in the 1920s, you got up by "
         "removable ladder or hoisting net.",
         "Meteora, inscribed by UNESCO in 1988. " + WIKI),
        ("Saint Catherine's", "Sinai, Egypt",
         "The world's oldest continuously inhabited Christian monastery, built between 548 "
         "and 565 by order of Justinian I, around the site traditionally held to be the "
         "burning bush.",
         "Saint Catherine's Monastery, a World Heritage Site since 2002. " + WIKI),
        ("Hanging Temple", "Shanxi, China",
         "Built into a cliff face 75 m above the ground, resting on 27 wooden beams, and "
         "combining Confucianism, Buddhism and Taoism in one building. Reopened in May 2016.",
         "Hanging Temple. The body dates it to 491 AD; the infobox says 6th century. "
         + WIKI),
        ("Sumela", "Trabzon, Türkiye",
         "On a steep cliff at about 1,200 m, abandoned after 1923 and closed again in 2015 "
         "for rock falls and restoration. It reopened on 18 May 2019.",
         "Sumela Monastery. On 15 August only 450 to 500 visitors are let inside. " + WIKI),
        ("Rila", "Bulgaria",
         "Founded in the 10th century at 1,147 m, burned down in 1833 and rebuilt between "
         "1834 and 1862. It drew 900,000 visitors in 2008 alone.",
         "Rila Monastery, a World Heritage Site since 1983. " + WIKI),
    ],
    """
Mont-Saint-Michel is a gift shop with an abbey on top. Three and a half million people a year walk up a single medieval street lined with crêperies to reach something genuinely remarkable, and most of what they remember is the street.

Five that are still awkward to get to, which is the entire point of building them where they are. Opinion; the figures are Wikipedia's.

01 METEORA, Greece — monasteries on top of rock pillars in Thessaly. Twenty-four at their 16th-century peak; six remain, of which four still operate as monasteries. Until the 1920s, when steps were cut into the rock, access was by long ladders latched together or by being hauled up in a net. A World Heritage Site since 1988.

02 SAINT CATHERINE'S, Sinai — the world's oldest continuously inhabited Christian monastery, built between 548 and 565 by order of Justinian I around the site traditionally considered to be the burning bush. Its library holds the world's second-largest collection of early codices and manuscripts, outnumbered only by the Vatican. Until the twentieth century you got in through a door high up in the outer wall.

03 HANGING TEMPLE, Shanxi — built into a cliff face 75 m above the ground on 27 wooden beams, and the only place we know of that integrates Confucianism, Buddhism and Taoism in one structure. Its body text dates it to 491 AD and its infobox to the 6th century. Reopened to the public in May 2016 after restoration.

04 SUMELA, Türkiye — set on a steep cliff at about 1,200 m above the Altındere valley, founded around AD 386 by the Turkish Ministry of Culture's dating, and abandoned after the 1923 population exchange. It closed in 2015 for rock falls and restoration and reopened on 18 May 2019. On 15 August only 450 to 500 people are allowed inside.

05 RILA, Bulgaria — founded in the 10th century by the hermit Saint Ivan of Rila, at 1,147 m in the mountains. It burned in 1833 and was rebuilt between 1834 and 1862. 900,000 visitors in 2008 alone, so go early.

Which one of these would you actually make the trip for?
""",
    ["monasteries", "meteora", "sinai", "sumela", "rila", "hangingtemple",
     "travelinspo", "geographyfacts", "worldfacts", "history", "earthbynumbers"],
)

top5(
    "top5-libraries",
    "A library with<br>a queue outside<br>is an exhibition.",
    "Opinion. Five rooms where the books are still the point.",
    [
        ("Admont Abbey", "Styria, Austria",
         "A hall 70 m long, 14 wide and 13 high, built in 1776, with seven cupolas frescoed "
         "by Bartolomeo Altomonte. The abbey says it is the largest monastic library in the "
         "world, and we will let the abbey say it.",
         "Admont Abbey: 70,000 volumes in the hall, about 200,000 in all. " + WIKI),
        ("The Long Room", "Trinity College Dublin",
         "65 m of barrel-vaulted oak holding 200,000 of the library's oldest books. A legal "
         "deposit library since 1801, and home to the Book of Kells since 1661.",
         "The Library of Trinity College Dublin. A €90m restoration began in 2022. "
         + WIKI),
        ("Strahov", "Prague, Czechia",
         "Two halls rather than one: the Theological Hall finished in 1679 and the "
         "Classical-style Philosophical Hall added a century later. Over 200,000 volumes, "
         "3,000 of them manuscripts.",
         "Strahov Monastery. Frescoes by Siard Nosecky and Anton Maulbertsch. " + WIKI),
        ("George Peabody", "Baltimore, USA",
         "An atrium rising 61 feet to a frosted-glass skylight, ringed by five tiers of black "
         "cast-iron balconies. Opened 1878, 300,000 volumes, open to the general public.",
         "George Peabody Library. " + WIKI),
        ("Bibliotheca Alexandrina", "Alexandria, Egypt",
         "Shelf space for eight million books and a reading room of 20,000 m² on eleven "
         "cascading levels. It opened on 16 October 2002 holding 500,000.",
         "Bibliotheca Alexandrina, built to commemorate the ancient library. " + WIKI),
    ],
    """
A library with a queue outside is an exhibition. Beautiful, worth seeing, and functionally a museum of what a library used to be for.

Five rooms where the books are still doing something. Opinion; the figures are Wikipedia's.

01 ADMONT ABBEY, Austria — 70 m long, 14 m wide, 13 m high, built in 1776 to designs by Joseph Hueber, with seven cupolas frescoed by Bartolomeo Altomonte. The hall holds about 70,000 of the monastery's roughly 200,000 volumes. Its page says "Admont Abbey says it contains the largest monastic library in the world", and that attribution matters, so we kept it.

02 THE LONG ROOM, Dublin — 65 m of barrel-vaulted oak, built between 1712 and 1732, holding 200,000 of the library's oldest books. Trinity has been a legal deposit library since 1801, which means Irish publishers must send it a copy of everything they print, and the Book of Kells has been there since 1661. A €90m restoration began in 2022; the page does not say whether the shelves are currently full, so check before you book.

03 STRAHOV, Prague — the one people get wrong because it is two halls. The Theological Hall was completed in 1679; the Philosophical Hall came a century later in Classical style under abbot Václav Mayer. Over 200,000 volumes between them, including more than 3,000 manuscripts.

04 GEORGE PEABODY, Baltimore — an atrium rising 61 feet to a latticed skylight of frosted glass, surrounded by five tiers of ornamental black cast-iron balconies from the Bartlett-Hayward Company. It opened in 1878, holds 300,000 volumes, and the collections are available for use by the general public.

05 BIBLIOTHECA ALEXANDRINA, Egypt — the modern one, inaugurated on 16 October 2002 as a commemoration of the ancient library lost in antiquity. Shelf space for eight million books, a main reading room of 20,000 m² on eleven cascading levels, and 500,000 books on the day it opened. Students from neighbouring universities make up 80% of its patrons, which is the right answer.

Which library have you been in that was still a working library?
""",
    ["libraries", "admont", "trinitycollege", "strahov", "bibliothecaalexandrina",
     "books", "travelinspo", "architecture", "worldfacts", "history", "earthbynumbers"],
)

top5(
    "top5-cable-cars",
    "Sugarloaf is a<br>lift to a<br>gift shop.",
    "Opinion. Five cable cars that are the reason you went.",
    [
        ("Wings of Tatev", "Syunik, Armenia",
         "5.7 km over a gorge to a 9th-century monastery. Its lead calls it the record for "
         "longest non-stop double track cable car; its body calls it the Guinness record for "
         "longest non-stop reversible aerial tramway.",
         "Wings of Tatev. Launched 16 October 2010, record set 23 October 2010. " + WIKI),
        ("Peak 2 Peak", "Whistler, Canada",
         "Still the highest point above the ground in a gondola at 436 m. It held the record "
         "for longest free span between ropeway towers at 3.03 km until 2017, when the Eibsee "
         "Cable Car beat it by 189 m.",
         "Peak 2 Peak Gondola, opened 12 December 2008. 11-minute ride. " + WIKI),
        ("Tianmen Mountain", "Hunan, China",
         "7,455 m of cableway with 98 cars and an ascent of 1,279 m. Its page calls it the "
         "longest passenger cableway of high mountains in the world — and attributes that "
         "claim to tourist publications.",
         "Tianmen Mountain, cable car built in 2005. " + WIKI),
        ("Eibsee Cable Car", "Zugspitze, Germany",
         "The one that took Whistler's span record in 2017, by 189 m. It is one of three "
         "cable cars running to the top of Germany's highest mountain, at 2,962 m.",
         "Zugspitze; Peak 2 Peak Gondola. " + WIKI),
        ("Ngong Ping 360", "Lantau, Hong Kong",
         "5,700 m and 25 minutes, opened in 2006, with glass-bottomed Crystal Cabins added in "
         "April 2009. Its page records service suspensions in 2006, 2007 and 2012.",
         "Ngong Ping 360. " + WIKI),
    ],
    """
Sugarloaf is a lift to a gift shop. Rio is extraordinary and the cable car is a queue, a cabin, a viewing deck and a counter selling fridge magnets, and you have seen the view already because it is on everything.

Five where the ride is the reason you went. Opinion; the figures are Wikipedia's.

01 WINGS OF TATEV, Armenia — 5.7 km across a gorge to a 9th-century monastery, which is a better destination than most cable cars manage. Its own page cannot name its record consistently: the lead says it holds the record for longest non-stop double track cable car, the body says it set the Guinness World Record for the longest non-stop reversible aerial tramway. It launched on 16 October 2010 and took the record on 23 October.

02 PEAK 2 PEAK, Whistler — still the highest point above the ground in a gondola anywhere, at 436 m. It held the record for the longest free span between ropeway towers, 3.03 km, from its opening on 12 December 2008 until 2017. The ride is 11 minutes and 4.4 km.

03 TIANMEN MOUNTAIN, China — 7,455 m of cableway with 98 cars and an ascent of 1,279 m, up to a mountain with a hole through it. Its page describes it as the longest passenger cableway of high mountains in the world and credits that claim to tourist publications, which is exactly the right amount of scepticism.

04 EIBSEE CABLE CAR, Germany — the one that beat Whistler's free span in 2017, by 189 m. It is one of three cable cars running to the summit of the Zugspitze, Germany's highest mountain at 2,962 m. The first of the three was built in 1926.

05 NGONG PING 360, Hong Kong — 5,700 m and 25 minutes over water and hillside to the Big Buddha, with glass-bottomed Crystal Cabins since April 2009. Its page is honest about a rough start: a collision during a trial run in June 2006 left 500 volunteers stuck for two hours, eight suspensions in its first six weeks, and an empty cabin falling during a brake test in June 2007 that kept it shut until the end of that year.

Which cable car was worth the ticket, and which was a queue?
""",
    ["cablecars", "tatev", "peak2peak", "tianmen", "zugspitze", "ngongping360",
     "travelinspo", "geographyfacts", "worldfacts", "engineering", "earthbynumbers"],
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        (OUT / f"{p['slug']}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False))
    print(f"wrote {len(POSTS)} posts")
    for p in POSTS:
        tags = " ".join("#" + t for t in p["tags"])
        full = len(p["caption"]) + 2 + len(tags)
        flag = "  <<< OVER 2200" if full > 2200 else ""
        print(f"  {p['slug']:22s} {p['kind']:9s} {len(p['slides'])} slides  "
              f"{full:4d} caption chars  {len(p['tags'])} tags{flag}")


if __name__ == "__main__":
    main()
