#!/usr/bin/env python3
"""
Earth by Numbers — content set F: the 100-buffer batch, run 2, 2026-11-09.

Twenty posts. The standing target is 100 approved-and-unposted entries and the
queue stood at 41, so this run writes the per-run maximum of 20 rather than the
full gap. These land approved (make_queue.py --approve-new); there is no
per-post review step any more.

  crazy (7)      china, netherlands, denmark, russia, kazakhstan,
                 papua-new-guinea, norway
  spotlight (7)  jordan, laos, sri-lanka, tanzania, montenegro, ecuador,
                 estonia
  top5 (6)       waterfalls, deserts, volcanoes, diving, wine-regions, castles

Mix is weighted to crazy and spotlight: crazy was furthest behind at 13 against
14 of each of the others.

VERIFICATION (BUILD.md §4 — every figure checked in this run)
Wikipedia pages read this run: China; Time in China; Xinjiang; Mount Scenery;
Netherlands; Baarle-Hertog; Caribbean Netherlands; Hans Island; Denmark;
Kingdom of Denmark; Greenland; Russia; Time in Russia; Kaliningrad Oblast;
Kazakhstan; Baikonur Cosmodrome; Astana; Landlocked country; Papua New Guinea;
Languages of Papua New Guinea; Mount Wilhelm; Norway; Bouvet Island; Queen Maud
Land; Norway–Russia border; Dead Sea; Wadi Rum; Jerash; Jordan; Laos; Plain of
Jars; Luang Prabang; Si Phan Don; Sri Lanka; Sigiriya; Adam's Peak; Mount
Kilimanjaro; Ngorongoro Conservation Area; Lake Tanganyika; Tanzania;
Montenegro; Bay of Kotor; Tara River Canyon; Durmitor; Chimborazo; Ecuador;
Quito; Galápagos Islands; Estonia; Tallinn; Saaremaa; Lahemaa National Park;
Angel Falls; Kaieteur Falls; Iguazu Falls; Dettifoss; Ban Gioc–Detian Falls;
Dasht-e Lut; Lençóis Maranhenses National Park; Simpson Desert; Taklamakan
Desert; Mount Yasur; Stromboli; Ijen; Villarrica; Pacaya; Raja Ampat Islands;
Sipadan; Silfra; Palau; Revillagigedo Islands; Douro DOC; Mosel (wine region);
Langhe; Mendoza Province; Tokaj wine region; Malbork Castle; Himeji Castle;
Mehrangarh; Alcázar of Segovia; Hohensalzburg Fortress; Neuschwanstein Castle.

Ledger rows come from the mledoze/countries dataset so they are checkable
against one file. Wikipedia's own area totals differ from the dataset for
several countries in this batch (Montenegro 13,883 vs 13,812; Sri Lanka 67,240
vs 65,610; Ecuador 283,561 vs 276,841; Estonia 45,335 vs 45,227; China
9,596,961 vs 9,706,961). The two are never mixed inside one source line.

The China border count was computed from the dataset, not recalled: the dataset
lists 16 neighbours for China, two of which are Hong Kong and Macau, China's
own territories. 14 sovereign neighbours, the same number Wikipedia's Russia
article names for Russia.

DROPPED, per the rule that matters most:
  - China's land border length (22,117 km) and any "most neighbours" claim.
    Both appeared only in a model summary of the page, never in fetched text.
  - The Netherlands' lowest point, and a single total-area figure. The article
    gives 41,865 (infobox), 41,850 (body) and 41,543 (European only).
  - Baarle-Hertog's Dutch counter-enclave count. The page says "seven" and then
    "an eighth". The 22 Belgian exclaves are not in dispute, so the post uses
    those and makes the disagreement its own line.
  - Greenland's ice share as a flat number: the Greenland article says 81%, the
    Kingdom of Denmark article says 79%. Attributed, not asserted.
  - "The Russia–Kazakhstan border is the world's longest." The Kazakhstan
    article says so; it cannot be squared with the 8,890 km Canada–US figure
    this account has already published. The 6,846 km length is used bare.
  - Baikonur as the largest operational launch facility. The sentence carries
    Wikipedia's own [failed verification] tag.
  - Papua New Guinea's border length with Indonesia (not stated), its forest
    cover and the "two-thirds unoccupied" claim (summary only), and its
    province count (19 in the body, 22 in the summary).
  - Norway's northernmost settlement (not stated) and a single mainland area
    (323,802 infobox vs 323,808 body).
  - Jordan's desert share as a percentage (not stated) and the water-scarcity
    ranking (appears only in a reference headline).
  - Jerash as "the best-preserved Roman provincial city" and any single
    years-occupied figure. Neither is on the page in those terms.
  - The Mekong's length inside Laos; Si Phan Don's island count and its
    Irrawaddy dolphins. None stated. The name's own gloss is used instead.
  - The Plain of Jars' 270 million cluster bombs. It cannot be reconciled with
    the Laos article's 80 million unexploded for the whole country without
    checking both underlying sources.
  - Sri Lanka's UNESCO site count (not verified) and its endemic bird count:
    the page gives 33 and 27 under different conventions.
  - Tanzania's protected-land share. The only sentence carrying it ("around 38%
    of the nation's area") is garbled on the page.
  - Montenegro's coastline length, highest point and protected share. All three
    came only from a model summary of an unread part of the article.
  - "The Bay of Kotor is often mistaken for a fjord." The word fjord does not
    appear on the page at all. The ria fact does.
  - "The Tara canyon is the deepest in Europe." The page says deepest in
    continental Europe and second in Europe behind the Sulak Canyon. The hedge
    is the slide.
  - Quito as flatly the world's highest capital (the page hedges on whether La
    Paz or Sucre is Bolivia's), and Quito's distance from the equator in km.
  - The Galápagos' endemic share, and their being among UNESCO's first sites in
    prose. Also their distance from the mainland as one number: the lead says
    898 km, the geography section about 1,000 km.
  - The White Desert, Egypt. Its article returned url_not_found, so the entry
    was replaced with Wadi Rum, which was verified for this run anyway.
  - Sipadan's cap of 178 daily permits. Tagged [citation needed]. The permit
    requirement itself is not tagged and is used.
  - Silfra's visibility in metres (not stated), Palau's Jellyfish Lake (not in
    the fetched text), and Revillagigedo's giant mantas and whale sharks (the
    page says only cetaceans, sharks and manta rays).
  - Raja Ampat's island count: 612 in the infobox, "over 1,500" in the body.
  - Mendoza's vineyard altitude, and Nebbiolo as the grape of Barolo and
    Barbaresco. Neither is stated on the pages read.
  - Malbork as the largest castle in the world by land area. The page's claim is
    the largest brick castle, and that is what is used.
  - Himeji as one of Japan's twelve original surviving castles (not stated),
    the Alcázar of Segovia's bow-of-a-ship shape (not stated), and
    Hohensalzburg as "fully preserved" (the page says best preserved).
  - Neuschwanstein's annual visitors as one number: 1.3 million and almost 1.5
    million both appear on the page. Both are quoted.
  - Kilimanjaro's ice disappearing "by mid-century": the lead and the body give
    different dates. The measured 1912–2011 loss is used instead.
  - Greenland's ice share: not used at all, for the reason above.

Run:  python3 posts_f.py
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
    """Same shape as set D and E, plus a source line on the two items slides.

    BUILD.md requires a source on any slide carrying a figure, and the why/where
    items in this set do carry them, so those slides take their own source.
    """
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
    "china-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "China spans five<br>time zones and<br>uses one.",
         "sub": "Five stats from a country that treats the clock as a political question."},
        {"type": "bignum", "kicker": "Stat 02", "number": "5", "bg": "",
         "label": "geographical time zones, one clock",
         "title": "Beijing Time, UTC+8, covers all of them.", "size": "h-sm",
         "source": "Time in China, which calls it the largest sovereign nation officially "
                   "observing only one time zone. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "UTC+6", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "Xinjiang Time — unofficial",
         "title": "Two time standards run side by side out west. The offset is shared with "
                  "Kyrgyzstan.", "size": "h-sm",
         "source": "Time in China. Listed by IANA as Asia/Urumqi, marked unofficial. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "14", "numsize": "s2", "bg": "",
         "label": "sovereign neighbours, not 16",
         "title": "The dataset lists 16. Two of them are Hong Kong and Macau, which are "
                  "China's own.", "size": "h-sm",
         "source": DS + " Wikipedia's Russia article names 14 for Russia. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Third largest country on Earth, measured three ways.",
         "sub": "Wikipedia's infobox says 9,596,961 km². Its own lead rounds to 9.6 million. "
                "The countries dataset says 9,706,961. They are measuring different things.",
         "source": "China. " + DS + " " + WIKI},
    ],
    """
China is about 5,000 km wide and runs on one clock.

Beijing Time, UTC+8, applies from the Pacific coast to the Pamirs. Wikipedia calls China the largest sovereign nation in the world that officially observes only one time zone. It had five until the end of the Second World War, and geographically it still spans five.

CHINA BY NUMBERS
Geographical time zones — 5
Official time zones — 1, UTC+8
Xinjiang Time — UTC+6, used unofficially and in parallel
Sovereign neighbours — 14
Capital — Beijing. Largest city by urban area — Shanghai

Out in Xinjiang, two time standards run side by side. The official clock is Beijing Time; a lot of people keep Xinjiang Time, two hours behind, which happens to be the same offset as Kyrgyzstan next door. Both are in use. Neither is wrong there.

One correction on the neighbour count, because we nearly got it wrong ourselves. The country dataset we check borders against lists 16 for China. Two of those are Hong Kong and Macau, which are China's own territories, not countries. The real figure is 14 sovereign neighbours — the same number Wikipedia's Russia article lists for Russia.

And the area, which has no single right answer: 9,596,961 km² in Wikipedia's infobox, "9.6 million" in its lead, 9,706,961 in the dataset. Different definitions of what counts, not a mistake.

If your country had one time zone, who would be getting up in the dark?
""",
    ["china", "timezones", "xinjiang", "geographyfacts", "didyouknow", "maps",
     "worldfacts", "asia", "beijing", "earthbynumbers"],
)

post(
    "netherlands-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "The highest point<br>in the Netherlands<br>is in the Caribbean.",
         "sub": "Five stats from a country that is partly 7,000 km away."},
        {"type": "bignum", "kicker": "Stat 02", "number": "870", "numsize": "s3", "bg": "",
         "label": "metres — Mount Scenery, Saba",
         "title": "The highest point in the Kingdom, and in the Netherlands itself since 2010.",
         "size": "h-sm",
         "source": "Mount Scenery, on Saba, Caribbean Netherlands. The Netherlands Antilles "
                   "were dissolved on 10 October 2010. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "322", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "metres — the Vaalserberg",
         "title": "The highest ground in the European Netherlands. Saba is more than 500 "
                  "metres higher.", "size": "h-sm",
         "source": "Netherlands, which gives 322.4 m for the Vaalserberg. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "26%", "numsize": "s3", "bg": "",
         "label": "of the country is below sea level",
         "title": "The name means lower countries. It is not a figure of speech.",
         "size": "h-sm",
         "source": "Netherlands. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "There are 22 Belgian exclaves inside the Netherlands.",
         "sub": "Baarle-Hertog is 26 separate parcels of land. Dutch enclaves sit inside the "
                "Belgian ones — the article says seven, then describes an eighth.",
         "source": "Baarle-Hertog. " + WIKI},
    ],
    """
The highest point in the Netherlands is a volcano in the Caribbean.

Mount Scenery, on the island of Saba, reaches 870 m. Since the Netherlands Antilles were dissolved on 10 October 2010, Saba has been a special municipality of the Netherlands, which makes that summit the highest point not just of the Kingdom but of the country.

NETHERLANDS BY NUMBERS
Highest point — Mount Scenery, 870 m, on Saba
Highest point in Europe — the Vaalserberg, 322.4 m
Below sea level — 26% of the country
Belgian exclaves inside Dutch territory — 22
Land borders — 2: Belgium and Germany

The European high point, the Vaalserberg, is 322.4 m. Saba is more than 500 metres higher. The Caribbean Netherlands is Bonaire, Sint Eustatius and Saba, classed in Dutch law as public bodies rather than municipalities, which is a distinction the law cares about more than anyone else does.

Then there is Baarle. The Belgian municipality of Baarle-Hertog is 26 separate parcels of land, 22 of which sit entirely inside the Netherlands. Inside those Belgian exclaves sit Dutch enclaves. Wikipedia says there are seven, and then in the next sentence describes an eighth. Its own table lists eight. We are not going to pretend to settle it.

One figure we will not give you is the total area. The article says 41,865 km² in the infobox, 41,850 in the body, and 41,543 for the European part alone.

Which country's highest point would surprise you most?
""",
    ["netherlands", "saba", "caribbeannetherlands", "baarlehertog", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "europe", "earthbynumbers"],
)

post(
    "denmark-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "In 2022 Denmark<br>got a new land<br>border. With Canada.",
         "sub": "Five stats from a kingdom that is almost entirely somewhere else."},
        {"type": "bignum", "kicker": "Stat 02", "number": "1,280", "numsize": "s3", "bg": "",
         "label": "metres of Canada–Denmark border",
         "title": "It crosses Hans Island, 1.3 km² of bare rock in the Arctic.",
         "size": "h-sm",
         "source": "Hans Island: agreed 11 June 2022, signed 14 June, ratified by the "
                   "Folketing 19 December 2023. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "68", "numsize": "s2",
         "bg": "ink", "sea": True,
         "label": "km — the border with Germany",
         "title": "Until 2022 that was the only land border the kingdom had.",
         "size": "h-sm",
         "source": "Denmark. " + WIKI},
        {"type": "fact", "kicker": "Stat 04", "bg": "", "size": "h-sm",
         "title": "Denmark is 43,094 km². Greenland is 2,166,086 km².",
         "sub": "Same kingdom. Wikipedia puts the whole realm at about 2.2 million km², and "
                "calls Greenland the world's largest island.",
         "source": "Denmark; Greenland. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "The dispute was conducted in bottles.",
         "sub": "Danish crews left a flag and a bottle of schnapps. Canadian crews left a flag "
                "and a bottle of Canadian Club. It ran for decades and was called the Whisky "
                "War.",
         "source": "Hans Island. " + WIKI},
    ],
    """
Denmark acquired a new land border in 2022, and it is with Canada.

Hans Island is 1.3 km² of bare rock in the Arctic, claimed by both countries since the 1970s. On 11 June 2022 the Danish, Greenlandic, Canadian and Nunavut governments agreed to split it. The agreement was signed on 14 June and ratified by the Danish parliament on 19 December 2023. The result is an international land border 1,280 m long.

DENMARK BY NUMBERS
Canada–Denmark border — 1,280 m, across Hans Island
Germany border — 68 km, and until 2022 the only one
Denmark — 43,094 km²
Greenland — 2,166,086 km², the world's largest island
The whole kingdom — about 2.2 million km²

That last set of numbers is the real story. Metropolitan Denmark is an archipelago of 406 islands and a peninsula, and it is about two percent of the kingdom it governs. Greenland is the rest.

The best part is how the dispute was run. Danish naval crews landing on the rock left a flag and a bottle of schnapps. Canadian crews came back and left a flag and a bottle of Canadian Club. This went on for decades and got called the Whisky War, which is the most civilised territorial conflict on record and probably the only one anybody misses.

We left out one number on purpose. Greenland's ice cover is 81% on the Greenland article and 79% on the Kingdom of Denmark article, and we are not picking a side.

Would you rather settle a border dispute in court or in bottles?
""",
    ["denmark", "greenland", "hansisland", "canada", "arctic", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "earthbynumbers"],
)

post(
    "russia-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Russia has the<br>same surface area<br>as Pluto.",
         "sub": "Wikipedia's own comparison. Five stats from the largest country there is."},
        {"type": "bignum", "kicker": "Stat 02", "number": "11", "numsize": "s2", "bg": "",
         "label": "time zones, UTC+2 to UTC+12",
         "title": "Kaliningrad Time at one end, Kamchatka Time at the other.",
         "size": "h-sm",
         "source": "Time in Russia. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "14", "numsize": "s2",
         "bg": "ink", "sea": True,
         "label": "countries on its land borders",
         "title": "Norway at one end of the list, North Korea at the other.",
         "size": "h-sm",
         "source": "Russia, which names all fourteen in a footnote. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "15,125", "numsize": "s3", "bg": "",
         "label": "km² — Kaliningrad Oblast",
         "title": "Russian ground with no land route to Russia. Poland south, Lithuania north "
                  "and east.", "size": "h-sm",
         "source": "Kaliningrad Oblast, which calls it a semi-exclave because it has sea "
                   "access. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "The fourth-longest coastline on Earth.",
         "sub": "Over 37,653 km, plus 850 km on the Caspian. By land area Russia is bigger "
                "than Australia, than Antarctica, and than Europe — most of which it is in.",
         "source": "Russia. " + WIKI},
    ],
    """
Russia has roughly the same surface area as Pluto. That is Wikipedia's comparison, not ours.

RUSSIA BY NUMBERS
Area — 17,098,246 km², first in the world
Time zones — 11, from UTC+2 to UTC+12
Land borders — 14 countries
Coastline — over 37,653 km, fourth-longest on Earth
Kaliningrad Oblast — 15,125 km², with no land route to the rest of the country

Eleven time zones means Kaliningrad Time at one end and Kamchatka Time at the other, a twelve-hour spread inside one state. Two zones were abolished in 2010 and later restored, so the number has not been stable.

The fourteen neighbours run Norway, Finland, Estonia, Latvia, Belarus, Ukraine, Lithuania, Poland, Georgia, Azerbaijan, Kazakhstan, Mongolia, China, North Korea. Note Norway and North Korea on the same list. There are also maritime boundaries with Japan and the United States — the Diomede Islands, one American and one Russian, are 3.8 km apart.

Kaliningrad is the strangest piece. It is 15,125 km² of Russia on the Baltic with Poland to the south and Lithuania to the north and east, and every land route between it and the rest of the country runs through NATO and EU members. Wikipedia calls it a semi-exclave rather than an exclave, because it has its own sea access.

The line we liked most is a footnote: by land area Russia is larger than Australia, than Antarctica, and than Europe — a large part of which it occupies.

Which of the fourteen neighbours did you forget?
""",
    ["russia", "kaliningrad", "timezones", "geographyfacts", "didyouknow", "maps",
     "worldfacts", "borders", "pluto", "earthbynumbers"],
)

post(
    "kazakhstan-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "Russia rents a<br>piece of Kazakhstan<br>until 2050.",
         "sub": "Five stats from the largest landlocked country on Earth."},
        {"type": "bignum", "kicker": "Stat 02", "number": "2050", "numsize": "s3", "bg": "",
         "label": "the year the Baikonur lease ends",
         "title": "Russia operates the spaceport inside Kazakhstan for US$115 million a year.",
         "size": "h-sm",
         "source": "Baikonur Cosmodrome. Lease agreed with Kazakhstan in 2005. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "1961", "numsize": "s3",
         "bg": "ink", "sea": True,
         "label": "12 April — Gagarin launched from here",
         "title": "Sputnik 1 went up from the same place. The pad is now called Gagarin's "
                  "Start.", "size": "h-sm",
         "source": "Baikonur Cosmodrome. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "6,846", "numsize": "s3", "bg": "",
         "label": "km of border with Russia",
         "title": "Kazakhstan is the ninth-largest country and the largest landlocked one.",
         "size": "h-sm",
         "source": "Kazakhstan; Landlocked country. Area 2,724,910 km². " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "About 4% of Kazakhstan is in Europe.",
         "sub": "The Ural River is taken as the dividing line. Wikipedia calls Kazakhstan one "
                "of only two landlocked countries with territory on two continents.",
         "source": "Kazakhstan. " + WIKI},
    ],
    """
Russia rents a piece of Kazakhstan, and the lease runs to 2050.

Baikonur Cosmodrome sits inside Kazakhstan and is operated by Russia under an agreement ratified in 2005, at a rent that has stayed fixed at US$115 million a year. Sputnik 1 launched from there. So did Vostok 1, carrying Yuri Gagarin, on 12 April 1961. The pad they both used is now called Gagarin's Start.

KAZAKHSTAN BY NUMBERS
Area — 2,724,910 km², ninth in the world
Rank among landlocked countries — first
Border with Russia — 6,846 km
Share of the country in Europe — about 4%
Baikonur lease — to 2050, at US$115 million a year

It is the largest landlocked country there is, and it stays landlocked despite a long Caspian coast, because the Caspian is in effect a lake with no route out for ocean-going ships. The Volga–Don Canal connects it to the Black Sea but cannot take large vessels.

The Ural River is conventionally taken as the Europe–Asia dividing line, and about 4% of Kazakhstan lies west of it. Wikipedia calls the country one of only two landlocked states with territory on two continents.

The capital has been renamed more often than most countries manage: Aqmoly in 1830, Akmolinsk in 1832, Tselinograd in 1961, Akmola in 1991, Astana in 1998, Nur-Sultan in 2019, and Astana again in 2022. It became the capital in December 1997, while it was still called Akmola.

One number we cut: the Kazakhstan article calls the Russian border the world's longest land border, which does not square with the 8,890 km Canada–US figure. We give the length and leave the ranking alone.

Should a country be able to lease territory to another one?
""",
    ["kazakhstan", "baikonur", "astana", "landlocked", "spaceflight", "geographyfacts",
     "didyouknow", "worldfacts", "centralasia", "earthbynumbers"],
)

post(
    "papua-new-guinea-crazy", "crazy",
    [
        {"type": "hook", "size": "h-lg",
         "title": "840 languages.<br>Or 839. Or 832.",
         "sub": "Five stats from the most linguistically diverse country on Earth, which "
                "cannot settle its own headline number."},
        {"type": "bignum", "kicker": "Stat 02", "number": "840", "numsize": "s2", "bg": "",
         "label": "known spoken languages",
         "title": "The lead says 840. The infobox says 839. A prime minister said 832 in 2006.",
         "size": "h-sm",
         "source": "Papua New Guinea; Languages of Papua New Guinea, citing Ethnologue. "
                   + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "4", "bg": "ink", "sea": True,
         "label": "languages with statutory recognition",
         "title": "Tok Pisin, English, Hiri Motu and PNG Sign Language. No law actually "
                  "proclaims an official language.", "size": "h-sm",
         "source": "Languages of Papua New Guinea. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "14%", "numsize": "s3", "bg": "",
         "label": "living in urban centres, 2023",
         "title": "462,840 km², one land border, and almost nobody in a town.",
         "size": "h-sm",
         "source": "Papua New Guinea. The land border is with Indonesia. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "Highlands valleys were unseen from outside until the 1930s.",
         "sub": "Prospectors exploring them found valleys holding over a million people. "
                "Aerial surveys in the 1950s found more. Some tribes were uncontacted by "
                "Westerners until the 1960s and 1970s.",
         "source": "Papua New Guinea. " + WIKI},
    ],
    """
Papua New Guinea has 840 languages. Or 839. Or 832. Its own encyclopedia entry cannot decide.

The lead of the Wikipedia article says 840 known spoken languages, "making it the most linguistically diverse country in the world." The infobox on the same page says 839. The languages article says 840, citing Ethnologue, and then quotes a former prime minister saying 832 in 2006 — languages, he specified, not dialects. The spread is not sloppiness. It is what happens when you have to decide where a dialect ends and a language begins, eight hundred times.

PAPUA NEW GUINEA BY NUMBERS
Known spoken languages — 840, or 839, or 832
Languages with statutory recognition — 4
Area — 462,840 km²
Land borders — 1, with Indonesia
Urban population — 14% in 2023

The four recognised languages are Tok Pisin, English, Hiri Motu and Papua New Guinean Sign Language. There is a footnote worth reading: no specific legislation actually proclaims official languages in Papua New Guinea at all.

Mount Wilhelm, at 4,509 m, is the highest point, and the summit is where three provinces meet.

The geography explains the languages. Prospectors exploring the highlands in the 1930s found inhabited valleys holding over a million people that nobody outside had seen. Aerial surveys in the 1950s found more of them. Some tribes remained uncontacted by Westerners until the 1960s and 1970s. Put enough mountains between enough valleys for long enough and you get eight hundred languages.

How many languages are spoken in your country, properly counted?
""",
    ["papuanewguinea", "languages", "linguistics", "tokpisin", "geographyfacts",
     "didyouknow", "worldfacts", "oceania", "melanesia", "earthbynumbers"],
)

post(
    "norway-crazy", "crazy",
    [
        {"type": "hook", "size": "h-md",
         "title": "The most remote<br>island on Earth<br>is Norwegian.",
         "sub": "Five stats from a country with territory in both polar regions."},
        {"type": "bignum", "kicker": "Stat 02", "number": "49", "numsize": "s2", "bg": "",
         "label": "km² — Bouvet Island",
         "title": "Ninety-three percent glacier, uninhabited, 1,700 km from the nearest land.",
         "size": "h-sm",
         "source": "Bouvet Island, called the world's most remote island. The nearest land is "
                   "Queen Maud Land, Antarctica. " + WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink", "size": "h-sm",
         "title": "Norway claims 2,700,000 km² of Antarctica.",
         "sub": "Queen Maud Land, held as a dependent territory. In June 2015 Norway formally "
                "claimed the gap between it and the South Pole. The Antarctic Treaty System "
                "suspends all such claims while it holds.",
         "source": "Queen Maud Land. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "196", "numsize": "s3", "bg": "",
         "label": "km of border with Russia",
         "title": "Norway's shortest land border. Sweden is 1,619 km, Finland 727 km.",
         "size": "h-sm",
         "source": "Norway; the border article gives 195.7 km of land border. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun", "size": "h-sm",
         "title": "28,953 km of coast. Or 100,915 km.",
         "sub": "The first is the mainland including fjords. The second adds the islands, of "
                "which Norway has 239,057 registered. Both figures sit on the same page.",
         "source": "Norway. " + WIKI},
    ],
    """
The most remote island in the world belongs to Norway, and nothing lives on it.

Bouvet Island is 49 km² of rock in the South Atlantic, ninety-three percent of it under glacier, uninhabited. The nearest land is Queen Maud Land in Antarctica, about 1,700 km south. Wikipedia calls it the world's most remote island without hedging.

NORWAY BY NUMBERS
Bouvet Island — 49 km², 93% glacier, uninhabited
Nearest land to it — 1,700 km away, and it is Antarctica
Queen Maud Land — 2,700,000 km² claimed
Border with Russia — 196 km, the shortest of three
Coastline — 28,953 km, or 100,915 km with the islands

Norway holds three dependencies, all of them polar or subpolar: Bouvet Island, Peter I Island and Queen Maud Land. Queen Maud Land alone is a claim on 2,700,000 km² of Antarctica — eight times the Norwegian mainland. In June 2015 Norway formally claimed the wedge between it and the South Pole, closing a gap left open since 1939. All of it is suspended under the Antarctic Treaty System, which parks every territorial claim for as long as the treaty holds.

The land borders are Sweden at 1,619 km, Finland at 727 km, and Russia at 196 km. The border article gives the Russian land section as 195.7 km, plus 23.2 km of marine border in the Varangerfjord.

The coastline figure depends entirely on what you count. The mainland including fjords is 28,953 km. Add the islands — there are 239,057 registered — and it becomes 100,915 km. The coastal baseline, which is the straight-line version, is 2,532 km.

Which is the honest way to measure a coastline?
""",
    ["norway", "bouvetisland", "queenmaudland", "antarctica", "arctic", "geographyfacts",
     "didyouknow", "maps", "worldfacts", "earthbynumbers"],
)


# ══════════════════════════════════════════════ SPOTLIGHTS ════════

spotlight(
    "spot-jordan",
    "The lowest point<br>on Earth is<br>getting lower.",
    "Jordan, where the lowest land in the world is also shrinking.",
    [["Capital", "Amman"], ["Land area", "89,342 km²"], ["Land borders", "5"],
     ["Official language", "Arabic"], ["Currency", "Jordanian dinar"]],
    "Three reasons",
    [{"name": "Wadi Rum",
      "note": "721 km² of protected desert, a UNESCO site since 2011, and Jordan's largest wadi."},
     {"name": "The Dead Sea",
      "note": "Salinity of 342 g/kg in 2011, which Wikipedia puts at 9.6 times the ocean."},
     {"name": "Jerash",
      "note": "Greek and Roman architecture on a scale the article says is unmatched outside Italy."}],
    {"title": "The lowest land on Earth will not hold still.", "size": "h-sm",
     "sub": "The Dead Sea article gives its surface as 439.78 m below sea level in 2025. "
            "Jordan's own article says 420 m. The lake covered 1,050 km² in 1930 and covers "
            "605 km² now.",
     "source": "Dead Sea; Jordan. " + WIKI},
    "Three to build a trip around",
    [{"name": "Petra",
      "note": "The Nabataean city, and the reason most visitors come to Jordan at all."},
     {"name": "Aqaba",
      "note": "Jordan's whole coastline is 26 km, on the Gulf of Aqaba. Otherwise it is landlocked."},
     {"name": "Jerash",
      "note": "Absorbed into the Roman province of Arabia in AD 106. Nicknamed the Pompeii of the East."}],
    """
The lowest land on Earth is in Jordan, and it is getting lower.

The Dead Sea article puts the lake's surface at 439.78 m below sea level as of 2025, and calls its shores the lowest land-based elevation on Earth. Jordan's own article says 420 m. Both are on Wikipedia. The reason they disagree is that the lake is receding fast: 1,050 km² of surface in 1930, 605 km² today.

JORDAN BY NUMBERS
Land area — 89,342 km²
Land neighbours — 5
Coastline — 26 km, all of it on the Gulf of Aqaba
Dead Sea surface — 439.78 m below sea level in 2025
Dead Sea salinity — 342 g/kg in 2011, or 9.6 times the ocean

That salinity is why you float. It is also why the water is 304 m deep and holds nothing alive, which makes it, in Wikipedia's words, the deepest hypersaline lake in the world. The article gives 304 m in the body and 298 m in the infobox, so take your pick.

Wadi Rum is 721 km² of protected sandstone desert, a UNESCO World Heritage Site since 2011 and the largest wadi in the country. Lawrence of Arabia was filmed there in 1962, which the article credits with kick-starting Jordanian tourism, and Rogue One was shot there more recently.

Jerash is the one people skip. It is described as one of the largest and best-preserved sites of Greek and Roman architecture in the world outside Italy, absorbed into the Roman province of Arabia in AD 106, and nicknamed the Pompeii of the East. Settlement on the site goes back to human remains dated around 7500 BC.

Petra or Jerash — which would you give the extra day to?
""",
    ["jordan", "petra", "wadirum", "deadsea", "jerash", "middleeast", "traveltips",
     "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Wadi Rum; Dead Sea; Jerash. " + WIKI,
    go_source="Jordan; Jerash. " + WIKI,
)

spotlight(
    "spot-laos",
    "Laos is the most<br>heavily bombed<br>country per head.",
    "Wikipedia's framing, not ours. Also the only landlocked country in Southeast Asia.",
    [["Capital", "Vientiane"], ["Land area", "236,800 km²"], ["Land borders", "5"],
     ["Coastline", "None — landlocked"], ["Currency", "Lao kip (LAK)"]],
    "Three reasons",
    [{"name": "The Plain of Jars",
      "note": "Over 2,100 stone jars across 129 confirmed sites, placed as early as 1240–660 BC."},
     {"name": "Luang Prabang",
      "note": "A World Heritage Site since 1995, for Lao architecture beside colonial streets."},
     {"name": "Si Phan Don",
      "note": "The name means four thousand islands. The article will not commit to a count."}],
    {"title": "Eighty million bombs in Laos never went off.", "size": "h-sm",
     "sub": "Between 1964 and 1973 the US dropped more than 2 million tons on Laos, nearly as "
            "much as all the bombs dropped in the Second World War. The leftovers still kill "
            "or maim about 50 people a year.",
     "source": "Laos. " + WIKI},
    "Three past Vientiane",
    [{"name": "Luang Prabang",
      "note": "Thirty-odd Buddhist temples in a town small enough to walk end to end."},
     {"name": "Xiangkhouang",
      "note": "The Plain of Jars. UNESCO inscribed the megalithic jar sites in 2019."},
     {"name": "Si Phan Don",
      "note": "Mekong islands in the far south, half of them submerged when the river floods."}],
    """
Laos is, in Wikipedia's own words, the most heavily bombed country in history relative to the size of its population.

Between 1964 and 1973 the United States dropped more than 2 million tons of bombs on it — nearly as much as all the bombs dropped during the Second World War, and The New York Times is quoted putting it at nearly a ton for every person in Laos. Some 80 million of them failed to explode and are still in the ground. Unexploded ordnance kills or maims about 50 people a year.

LAOS BY NUMBERS
Land area — 236,800 km²
Land neighbours — 5: China, Myanmar, Thailand, Cambodia, Vietnam
Coastline — none, the only landlocked country in Southeast Asia
Bombs that failed to explode — about 80 million
Stone jars documented on the Plain of Jars — over 2,100

That is the context, and it is also why the Plain of Jars took until 2019 to become a World Heritage Site. There are over 2,100 stone jars across 129 confirmed sites, and dating by optically stimulated luminescence puts them in place as early as 1240 to 660 BC. Nobody knows who made them or why. One site alone holds 392.

Luang Prabang has been inscribed since 1995, for a mix of Lao architecture, French colonial buildings and more than thirty Buddhist temples in a town you can cross on foot.

In the far south, Si Phan Don means four thousand islands. The article declines to count them and notes that half go under when the Mekong floods, which seems like the honest position.

What is the most interesting country you have never seriously considered visiting?
""",
    ["laos", "luangprabang", "plainofjars", "siphandon", "mekong", "southeastasia",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Plain of Jars; Luang Prabang; Si Phan Don. " + WIKI,
    go_source="Luang Prabang; Plain of Jars; Si Phan Don. " + WIKI,
)

spotlight(
    "spot-sri-lanka",
    "Sri Lanka has<br>two capitals and<br>neither is obvious.",
    "One makes the laws. The other does everything else.",
    [["Capital, per dataset", "Colombo"], ["Land area", "65,610 km²"],
     ["Land borders", "None"], ["Official languages", "Sinhala, Tamil"],
     ["Currency", "Sri Lankan rupee"]],
    "Three reasons",
    [{"name": "Sigiriya",
      "note": "A citadel on a 180 m granite column, built under King Kashyapa in the 5th century."},
     {"name": "Adam's Peak",
      "note": "2,243 m, and holy to Buddhists, Hindus, and some Muslims and Christians at once."},
     {"name": "The endemism",
      "note": "27% of its 3,210 flowering plants and 22% of its mammals exist nowhere else."}],
    {"title": "Colombo is not the legislative capital.", "size": "h-sm",
     "sub": "Sri Jayawardenepura Kotte is. Wikipedia lists Colombo as the executive and "
            "judicial capital and the largest city, and its neighbour as the legislative "
            "one. The dataset we check against lists only Colombo.",
     "source": "Sri Lanka. " + WIKI + " " + DS},
    "Three past the beaches",
    [{"name": "Sigiriya",
      "note": "Inscribed by UNESCO in 1982. The site sits 349 m above sea level."},
     {"name": "Adam's Peak",
      "note": "Climbed between December and May. The pilgrimage season peaks in April."},
     {"name": "Pidurutalagala",
      "note": "The highest point in the country, 2,524 m, above the hill-country tea towns."}],
    """
Sri Lanka has two capitals, and the one you have heard of is not the legislative one.

Sri Jayawardenepura Kotte holds the legislature. Colombo is the executive and judicial capital and the largest city, and the article calls it the political, financial and cultural centre of the country. The countries dataset we check against lists only Colombo, which is how this sort of thing quietly becomes wrong everywhere.

SRI LANKA BY NUMBERS
Land area — 65,610 km² in the dataset, 67,240 km² on Wikipedia
Coastline — 1,585 km
Land borders — none
Highest point — Pidurutalagala, 2,524 m
Endemic share — 27% of 3,210 flowering plants, 22% of mammals

The endemism is the real reason to go. Sri Lanka and the Western Ghats of India were among the first eighteen global biodiversity hotspots named, on the strength of species found nowhere else, and the article claims the highest biodiversity per unit area of any Asian country for flowering plants and every vertebrate group except birds. On birds it is honest about the dispute: some ornithologists accept 33 endemics, others only 27.

Sigiriya is a citadel on a granite column about 180 m high, built out into a city and fortress under King Kashyapa, who reigned 477 to 495 CE. UNESCO inscribed it in 1982.

Adam's Peak is 2,243 m and is revered by four religions at once. The footprint at the top is the Buddha's in Buddhist tradition, Hanuman's or Shiva's in Sri Lankan Hindu tradition, and Adam's or St Thomas the Apostle's in some Islamic and Christian ones. Climbing season runs December to May and peaks in April.

Which country's second capital city caught you out?
""",
    ["srilanka", "sigiriya", "adamspeak", "colombo", "biodiversity", "southasia",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Sigiriya; Adam's Peak; Sri Lanka. " + WIKI,
    go_source="Sigiriya; Adam's Peak; Sri Lanka. " + WIKI,
)

spotlight(
    "spot-tanzania",
    "A crater with<br>25,000 animals<br>living inside it.",
    "Tanzania, where the famous mountain is not even the best statistic.",
    [["Capital", "Dodoma"], ["Land area", "945,087 km²"], ["Land borders", "8"],
     ["Official languages", "Swahili, English"], ["Currency", "Tanzanian shilling"]],
    "Three reasons",
    [{"name": "Ngorongoro",
      "note": "The world's largest inactive, intact and unfilled caldera. 610 m deep, floor 260 km²."},
     {"name": "Kilimanjaro",
      "note": "5,895 m, and the highest free-standing mountain above sea level in the world."},
     {"name": "Lake Tanganyika",
      "note": "The world's longest freshwater lake, holding 16% of its available fresh water."}],
    {"title": "Kilimanjaro has nearly lost its ice.", "size": "h-sm",
     "sub": "Almost 85 percent of the ice cover disappeared between October 1912 and June "
            "2011, falling from 11.40 km² to under 1 km². The article's projections for the "
            "rest do not agree with each other.",
     "source": "Mount Kilimanjaro. " + WIKI},
    "Three to build a trip around",
    [{"name": "Ngorongoro Crater",
      "note": "About 25,000 large animals live on the floor, most of them ungulates."},
     {"name": "Kilimanjaro",
      "note": "Three cones: Kibo at the summit, Mawenzi at 5,149 m, Shira at 4,005 m."},
     {"name": "Lake Tanganyika",
      "note": "1,471 m deep, second only to Baikal. Tanzania holds 46% of the lake."}],
    """
There is a crater in Tanzania with about 25,000 large animals living inside it.

Ngorongoro is described as the world's largest inactive, intact and unfilled volcanic caldera. It is 610 metres deep and its floor covers 260 km², and the roughly 25,000 large animals on that floor are mostly ungulates. They are in there because the walls are 610 m high, not because anyone put them there.

TANZANIA BY NUMBERS
Land area — 945,087 km²
Land neighbours — 8
Ngorongoro — 610 m deep, floor 260 km², about 25,000 large animals
Kilimanjaro — 5,895 m
Lake Tanganyika — 1,471 m deep, 16% of the world's available fresh water

Kilimanjaro is the headline and it is a strange mountain: not part of a range, rising 4,900 m above its own plateau base, and described as the highest free-standing mountain above sea level in the world. It is three volcanic cones — Kibo at the top, Mawenzi at 5,149 m and Shira at 4,005 m. Surveys have put the summit at 5,892 m in 1999, 5,902 m in 2008 and 5,899 m in 2014, which tells you something about measuring mountains.

Lake Tanganyika is the one that deserves more attention. It is the world's longest freshwater lake and the second deepest, after Baikal in both cases, at 1,471 m. It holds 16% of the world's available fresh water, is shared between Tanzania, the DRC, Burundi and Zambia, and Tanzania has 46% of it.

The ice is the sad number. Almost 85 percent of Kilimanjaro's ice cover went between October 1912 and June 2011, from 11.40 km² down to under 1 km².

Crater floor or summit — which one would you spend the week on?
""",
    ["tanzania", "ngorongoro", "kilimanjaro", "laketanganyika", "safari", "eastafrica",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Ngorongoro Conservation Area; Mount Kilimanjaro; Lake Tanganyika. " + WIKI,
    go_source="Ngorongoro Conservation Area; Mount Kilimanjaro; Lake Tanganyika. " + WIKI,
)

spotlight(
    "spot-montenegro",
    "Montenegro uses<br>the euro without<br>being in the euro.",
    "A country smaller than Northern Ireland, with a canyon over a kilometre deep.",
    [["Capital", "Podgorica"], ["Land area", "13,812 km²"], ["Land borders", "5"],
     ["Official language", "Montenegrin"], ["Currency", "Euro (EUR)"]],
    "Three reasons",
    [{"name": "The Bay of Kotor",
      "note": "A ria — a drowned river canyon — 28 km long, with 107.3 km of shoreline."},
     {"name": "Durmitor",
      "note": "Eighteen glacial lakes called the mountain eyes, under Bobotov Kuk at 2,523 m."},
     {"name": "The Tara canyon",
      "note": "1,333 m at its deepest, which is a serious figure for a country this size."}],
    {"title": "The Tara is not the deepest canyon in Europe.", "size": "h-sm",
     "sub": "Its own article says deepest in continental Europe, and second in Europe behind "
            "the Sulak Canyon. The depth is 1,333 m in the infobox and 1,300 m in the body. "
            "Durmitor's page drops the hedge entirely.",
     "source": "Tara River Canyon; Durmitor. " + WIKI},
    "Three past the coast",
    [{"name": "Kotor",
      "note": "The Natural and Culturo-Historical Region of Kotor, a UNESCO site since 1979."},
     {"name": "Durmitor",
      "note": "National park founded in 1952, World Heritage Site since 1980."},
     {"name": "Podgorica",
      "note": "Capital of a country that voted itself into existence on 21 May 2006."}],
    """
Montenegro spends euros and is not in the eurozone.

It adopted the Deutsche Mark in the late 1990s and then moved to the euro along with Germany, without ever joining the currency union that issues it. Wikipedia's phrasing is flat: it "adopted the euro, although not part of the Eurozone."

MONTENEGRO BY NUMBERS
Land area — 13,812 km² in the dataset, 13,883 km² on Wikipedia
Land neighbours — 5
Bay of Kotor — 28 km long, 107.3 km of shoreline
Tara canyon — 1,333 m deep
Independence referendum — 21 May 2006, 55.5% in favour

The independence vote is worth the detail. The EU set a 55% threshold, and the result came in at 55.5% — 230,661 votes for and 185,002 against. The electoral commission reckoned the threshold was cleared by about 2,300 votes. Parliament declared independence on 3 June 2006.

The Bay of Kotor gets called a fjord constantly. It is not one, and its article does not even use the word: it is a ria, the drowned canyon of the vanished Bokelj River, 28 km long with 107.3 km of shoreline and a maximum depth of 60 m. The Natural and Culturo-Historical Region of Kotor has been a World Heritage Site since 1979.

Inland, Durmitor has eighteen glacial lakes nicknamed Gorske Oči, the mountain eyes, and a high point of 2,523 m at Bobotov Kuk. The national park dates from 1952 and was inscribed in 1980.

And the Tara canyon, which everyone including us wanted to call the deepest in Europe. Its own article says deepest in continental Europe, second in Europe behind the Sulak Canyon in Dagestan. We will take 1,333 m and leave the title alone.

Which small country punches furthest above its weight?
""",
    ["montenegro", "kotor", "durmitor", "taracanyon", "balkans", "adriatic",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Bay of Kotor; Durmitor; Tara River Canyon. " + WIKI,
    go_source="Bay of Kotor; Durmitor; Montenegro. " + WIKI,
)

spotlight(
    "spot-ecuador",
    "The point farthest<br>from Earth's centre<br>is not Everest.",
    "It is in Ecuador, and it sticks out 2.1 km further.",
    [["Capital", "Quito"], ["Land area", "276,841 km²"],
     ["Land borders", "2 — Colombia, Peru"], ["Official language", "Spanish"],
     ["Currency", "US dollar (USD)"]],
    "Three reasons",
    [{"name": "Chimborazo",
      "note": "6,263 m above the sea, and 6,384.4 km from the centre of the Earth."},
     {"name": "The Galápagos",
      "note": "127 islands, 19 of them over a square kilometre, out in the Pacific."},
     {"name": "Quito",
      "note": "At 2,850 m, either the highest or second-highest capital, depending on Bolivia."}],
    {"title": "Ecuador's money is the US dollar.", "size": "h-sm",
     "sub": "Adopted on 13 April 2000, with the sucre eliminated that September. Ecuador is "
            "also one of seventeen megadiverse countries, with 1,600 bird species on the "
            "mainland and 38 more endemic to the Galápagos.",
     "source": "Ecuador. " + WIKI},
    "Three to build a trip around",
    [{"name": "Chimborazo",
      "note": "An ice-capped inactive volcano. Last known eruption around AD 550."},
     {"name": "The Galápagos",
      "note": "A World Heritage Site since 1978, carrying UNESCO reference number 1."},
     {"name": "Quito",
      "note": "Its historic centre was among the first sites UNESCO declared, in 1978."}],
    """
The farthest point on the Earth's surface from the Earth's centre is not Everest. It is a volcano in Ecuador.

Chimborazo is 6,263 m above sea level, which is nowhere near Everest's 8,849 m. But it sits almost on the equator, where the planet bulges, so its summit is 6,384.4 km from the centre of the Earth — 2.1 km further out than Everest's summit, at 6,382.3 km. Measured from the middle rather than from the sea, Chimborazo wins.

ECUADOR BY NUMBERS
Land area — 276,841 km² in the dataset, 283,561 km² on Wikipedia
Land neighbours — 2
Chimborazo — 6,263 m high, 6,384.4 km from Earth's centre
Quito — 2,850 m above sea level
Currency — the US dollar, since 13 April 2000

Huascarán in Peru is a very close second, by either 20 or 40 metres depending on which footnote you read, and the article admits the margins of error in both summit elevations make the question hard to settle outright. We will take the claim as stated and flag the asterisk.

Quito is the other place the numbers get slippery. At 2,850 m the article calls it "either the highest or the second-highest national capital city in the world" — if La Paz counts as Bolivia's capital, La Paz tops the list; if Sucre does, Quito does. Its historic centre was one of the first sites UNESCO ever declared, in 1978, alongside Kraków.

Ecuador also uses the US dollar, adopted on 13 April 2000 after the sucre was eliminated that September, and is one of seventeen megadiverse countries, with 1,600 bird species on the mainland alone.

Does height mean above the sea, or out from the centre?
""",
    ["ecuador", "chimborazo", "quito", "galapagos", "andes", "southamerica",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Chimborazo; Galápagos Islands; Quito. " + WIKI,
    go_source="Chimborazo; Galápagos Islands; Quito. " + WIKI,
)

spotlight(
    "spot-estonia",
    "Estonia has<br>2,355 islands and<br>318 metres of hill.",
    "The flattest genuinely interesting country in Europe, and the most online.",
    [["Capital", "Tallinn"], ["Land area", "45,227 km²"],
     ["Land borders", "2 — Latvia, Russia"], ["Official language", "Estonian"],
     ["Currency", "Euro (EUR)"]],
    "Three reasons",
    [{"name": "Tallinn Old Town",
      "note": "A UNESCO site since 1997, and one of the best-preserved medieval cities in Europe."},
     {"name": "The forest",
      "note": "48% of the land was forest as of 2012. Bogs and mires cover another 23.2%."},
     {"name": "Saaremaa",
      "note": "2,673 km² of island, with a meteorite crater at Kaali 110 m across."}],
    {"title": "Estonia put voting on the internet in 2005.", "size": "h-sm",
     "sub": "Wikipedia calls it the first country in the world to introduce nationwide "
            "binding internet voting, in the 2005 local elections. In 2023, 51% of all votes "
            "were cast online — the first time more than half were.",
     "source": "Estonia. " + WIKI},
    "Three past Tallinn",
    [{"name": "Lahemaa",
      "note": "747 km², established 1971, the first area designated a national park in the USSR."},
     {"name": "Saaremaa",
      "note": "The largest and most populous Estonian island, out in the Baltic."},
     {"name": "Suur Munamägi",
      "note": "The summit of Estonia, 318 m. Only a tenth of the country clears 100 m."}],
    """
Estonia has 2,355 islands and its highest point is 318 metres.

The island count is specific: 2,355 in total including internal waters, of which 2,222 are in the Baltic Sea. The lede of the same article says "over 2,300 other islands and islets" and does not reconcile the two. There is also a reference titled "Estonia gains 95 islands, but loses 4 square kilometers with updated map," which is the most Estonian headline imaginable.

ESTONIA BY NUMBERS
Land area — 45,227 km² in the dataset, 45,335 km² on Wikipedia
Islands — 2,355, of which 2,222 are in the Baltic
Highest point — Suur Munamägi, 318 m
Forest — 48% of the land as of 2012
Bogs and mires — 23.2%; protected areas — 19.4%

Only 10% of the country's terrain clears 100 m. What it has instead is cover: nearly half of it forest, almost a quarter bog and mire, and 19.4% of the land formally protected.

Tallinn's Old Town has been a World Heritage Site since 1997 and is described as one of the best-preserved medieval cities in Europe. At its medieval peak the city had about 8,000 people, city walls and 66 defence towers.

The other thing Estonia is known for is being online. It was the first country in the world to introduce nationwide binding internet voting, in the 2005 local elections, and the first to offer e-residency, in 2014. In the 2023 parliamentary elections 51% of all votes were cast over the internet — the first time anywhere that more than half were.

Saaremaa, 2,673 km², is the largest island, and it has nine meteorite craters at Kaali, the biggest 110 m across. The impact is dated either to around 4000 BCE or as recently as 660 BCE, depending which estimate you prefer.

Would you vote online if your country let you?
""",
    ["estonia", "tallinn", "saaremaa", "lahemaa", "baltics", "eresidency",
     "traveltips", "geographyfacts", "worldfacts", "earthbynumbers"],
    why_source="Tallinn; Estonia; Saaremaa. " + WIKI,
    go_source="Lahemaa National Park; Saaremaa; Estonia. " + WIKI,
)


# ═══════════════════════════════════════════════════════ TOP 5 ════

top5(
    "top5-waterfalls",
    "Niagara is a<br>car park with<br>a waterfall.",
    "Opinion. Five falls where you are not queueing for the viewing platform.",
    [
        ("Angel Falls", "Canaima, Venezuela",
         "979 m total with an 807 m plunge: the world's tallest uninterrupted waterfall, "
         "though its own article concedes Tugela Falls may be taller. A flight, then a boat.",
         "Angel Falls, in Canaima National Park. " + WIKI),
        ("Kaieteur Falls", "Guyana",
         "A 226 m single drop and one of the most powerful single-drop waterfalls in the "
         "world. The airstrip is a fifteen-minute walk from the top.",
         "Kaieteur Falls: 660 m³/s in the infobox, 663 in the body. " + WIKI),
        ("Iguazu Falls", "Argentina and Brazil",
         "The infobox says 275 drops. The body says the number runs from 150 to 300 "
         "depending on the water level. Either way: 2.7 km of edge, drops up to 82 m.",
         "Iguazu Falls, inscribed 2013; the two parks in 1984 and 1986. " + WIKI),
        ("Dettifoss", "Iceland",
         "Only 44 m high and 100 m wide, but 193 m³/s goes over it. Reputed second most "
         "powerful in Europe, and only second largest in Iceland by volume.",
         "Dettifoss, behind Urriðafoss on volume. " + WIKI),
        ("Ban Gioc–Detian", "China and Vietnam",
         "A 30 m drop straddling the border, 272 km north of Hanoi. Called the fourth "
         "largest waterfall along a national border, after Iguazu, Victoria and Niagara.",
         "Ban Gioc–Detian Falls. " + WIKI),
    ],
    """
Niagara is a car park with a waterfall in it. Enormous flow, genuinely impressive, and you will see it over four hundred shoulders from a railing with a gift shop behind you.

Five where that does not happen. This is opinion; the numbers are Wikipedia's.

01 ANGEL FALLS, Venezuela — 979 m total, with a single plunge of 807 m, which its article calls the world's tallest uninterrupted waterfall. It also admits there is still uncertainty over whether Angel Falls or Tugela Falls in South Africa is taller. Reaching it means flying to Canaima camp and then taking a river boat.

02 KAIETEUR FALLS, Guyana — a 226 m single drop over a sandstone cliff, described as one of the most powerful single-drop waterfalls in the world. Average flow is 660 m³/s in the infobox and 663 in the body. The airstrip is about a fifteen-minute walk from the top, which is the best access-to-spectacle ratio on this list.

03 IGUAZU FALLS, Argentina and Brazil — the infobox says 275 drops and the body says the count fluctuates between 150 and 300 with the water level. There is 2.7 km of edge and drops of up to 82 m. The falls were inscribed by UNESCO in 2013; the Argentine and Brazilian parks in 1984 and 1986.

04 DETTIFOSS, Iceland — 44 m high, 100 m wide, 193 m³/s. Reputed to be the second most powerful waterfall in Europe after the Rhine Falls, and only the second largest in Iceland by volume, behind Urriðafoss. Small numbers, serious noise.

05 BAN GIOC–DETIAN, China and Vietnam — a 30 m drop that straddles the border, 272 km north of Hanoi. Its article ranks it the fourth largest waterfall along a national border, after Iguazu, Victoria and Niagara. Which does put Niagara back on a list, fairly.

Tell us which one we got wrong, and which waterfall you would put first.
""",
    ["waterfalls", "angelfalls", "kaieteur", "iguazufalls", "dettifoss", "travelinspo",
     "naturephotography", "geographyfacts", "worldfacts", "adventuretravel",
     "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-deserts",
    "Everyone names<br>the Sahara. Few<br>see any of it.",
    "Opinion. Five deserts with something specific to look at. One of them is not a desert.",
    [
        ("Dasht-e Lut", "Iran",
         "The hottest land surface ever recorded: 70.7 °C by satellite in 2005. That is the "
         "ground, not the air, which may have been 30–54 °C at the time.",
         "Dasht-e Lut: MODIS on NASA's Aqua satellite, 2003–2010. 51,800 km², UNESCO 2016. "
         + WIKI),
        ("Lençóis Maranhenses", "Brazil",
         "Dunes that fill with freshwater lagoons from January to June. It is not a desert: "
         "the rain is about 1,200 mm a year and deserts get under 250 mm.",
         "Lençóis Maranhenses National Park. " + WIKI),
        ("Simpson Desert", "Australia",
         "The world's longest parallel sand dunes, some ridges unbroken for 200 km, topping "
         "out at Big Red at 40 m. No maintained roads cross it, and it closes for summer.",
         "Simpson Desert, closed over summer since 2008–09. " + WIKI),
        ("Taklamakan", "China",
         "337,000 km², which its own article calls slightly smaller than Germany. Below "
         "−20 °C in winter, up to 40 °C in summer. Two highways and a railway cross it.",
         "Taklamakan Desert, 15th largest desert by area. " + WIKI),
        ("Wadi Rum", "Jordan",
         "721 km² of protected sandstone, a UNESCO site since 2011. Lawrence of Arabia was "
         "shot here in 1962, which the article credits with starting Jordanian tourism.",
         "Wadi Rum Protected Area. " + WIKI),
    ],
    """
The Sahara is the desert everyone can name and the one you are least likely to see properly. It is 9 million square kilometres and most trips are a camel, a camp and a dune you share with a coach party.

Five deserts with something specific to go and look at. Opinion, except the figures.

01 DASHT-E LUT, Iran — the hottest land surface temperature ever recorded, 70.7 °C, measured by the MODIS instrument on NASA's Aqua satellite in 2005. Read that carefully: it is the temperature of the ground, not the air, which the article says could have been anywhere from 30 to 54 °C. As of 2020 there were no permanent weather stations in the desert at all. 51,800 km², a World Heritage Site since 2016.

02 LENÇÓIS MARANHENSES, Brazil — the ringer. It looks like a desert and it is not one: the rain is about 1,200 mm a year and the definition of a desert is under 250 mm. Between January and June the valleys between the dunes fill with freshwater lagoons, and about 60,000 people a year go to swim in them.

03 SIMPSON DESERT, Australia — an erg containing the world's longest parallel sand dunes, some ridges running unbroken for up to 200 km. The biggest, Nappanerica or Big Red, is 40 m. No maintained roads cross it, four-wheel drives must carry extra fuel and water, and it has been closed over summer since 2008–09.

04 TAKLAMAKAN, China — 337,000 km², which its article helpfully describes as slightly smaller than Germany. Winter can drop below −20 °C and summer reach 40 °C. Very little water, hazardous to cross, and now crossed by two highways and a railway anyway.

05 WADI RUM, Jordan — 721 km² of protected sandstone, a World Heritage Site since 2011 and the largest wadi in Jordan. Lawrence of Arabia was filmed there in 1962, and the article credits those desert scenes with kick-starting the country's tourism industry.

Which desert did we leave out that belongs at number one?
""",
    ["deserts", "dashtelut", "lencoismaranhenses", "simpsondesert", "taklamakan", "wadirum",
     "travelinspo", "geographyfacts", "worldfacts", "adventuretravel", "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-volcanoes",
    "Vesuvius is a<br>day trip, not<br>a volcano.",
    "Opinion. Five that are actually doing something while you stand there.",
    [
        ("Mount Yasur", "Tanna, Vanuatu",
         "361 m, erupting nearly continuously for several hundred years. Its glow is what "
         "drew Captain Cook to the island in 1774.",
         "Mount Yasur. The government publishes alert levels 0–5, and an eruption may occur "
         "at any level. " + WIKI),
        ("Stromboli", "Aeolian Islands, Italy",
         "Almost continuous eruption for the past 2,000 to 5,000 years, which earned it the "
         "name Lighthouse of the Mediterranean. A hiker near the summit was killed in 2019.",
         "Stromboli: 924 m in the infobox, 926 m in the body. " + WIKI),
        ("Ijen", "Java, Indonesia",
         "Blue flames up to five metres high, from sulphuric gas igniting at up to 600 °C. "
         "The crater lake is the largest highly acidic one in the world.",
         "Ijen. The lake was measured below pH 0.3 in 2001. " + WIKI),
        ("Villarrica", "Chile",
         "2,860 m, and one of only a small number of volcanoes worldwide with an active lava "
         "lake in the crater — intermittent, in this case. Guided climbs go from Pucón.",
         "Villarrica. Climbs are suspended for cloud or volcanic activity. " + WIKI),
        ("Pacaya", "Guatemala",
         "Dormant for over 70 years, then erupting vigorously from 1961 and frequently since. "
         "One of Central America's most active volcanoes over the last 500 years.",
         "Pacaya, 2,552 m. Increased unrest reported from early 2026. " + WIKI),
    ],
    """
Vesuvius is a day trip. You take a bus to a car park, walk up a gravel path, look into a quiet crater and go and see Pompeii, which is the actual reason you came.

Five volcanoes that are doing something while you are standing there. Opinion; figures from Wikipedia.

01 MOUNT YASUR, Vanuatu — 361 m, and erupting nearly continuously for several hundred years. The glow is what attracted Captain Cook to Tanna in 1774. It is easy to reach and usually safe to approach, and the Vanuatu government publishes alert levels from 0 to 5 with the note that an eruption may occur at any of them.

02 STROMBOLI, Italy — in almost continuous eruption for the past 2,000 to 5,000 years, which is how an island gets called the Lighthouse of the Mediterranean. Treat it seriously: a hiker near the summit was killed by flying debris in July 2019, and the highest alert level was issued again in July 2024.

03 IJEN, Java — the blue fire is ignited sulphuric gas emerging from cracks at up to 600 °C, with flames up to five metres high, and the article calls it the largest blue flame area in the world. The crater lake is the largest highly acidic one on Earth, measured below pH 0.3. Two hundred miners carry 75 to 90 kg loads 300 m up to the rim, which is the part of the trip worth thinking about.

04 VILLARRICA, Chile — 2,860 m, one of a small number of volcanoes anywhere with an active lava lake in the crater, though an intermittent one. Guided climbs run from Pucón and get suspended for cloud or activity. In 2015 an eruption forced 3,385 people out of nearby towns.

05 PACAYA, Guatemala — dormant for over 70 years, then erupting vigorously from 1961 and frequently ever since, and one of Central America's most active volcanoes over the last 500 years. Unrest picked up again in early 2026.

Which volcano have you actually stood on, and was it worth it?
""",
    ["volcanoes", "mountyasur", "stromboli", "ijen", "villarrica", "pacaya",
     "travelinspo", "geographyfacts", "worldfacts", "adventuretravel", "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-diving",
    "The Barrier Reef<br>is not the dive<br>you think it is.",
    "Opinion. Five places where the water is doing something a brochure cannot.",
    [
        ("Raja Ampat", "West Papua, Indonesia",
         "1,508 fish species and 537 coral species recorded; Konservasi Indonesia calls the "
         "diversity here the highest recorded on Earth. The same page says 600 and 1,700 "
         "elsewhere.",
         "Raja Ampat Islands. " + WIKI),
        ("Sipadan", "Sabah, Malaysia",
         "The only oceanic island in Malaysia, rising 600 m straight off the seabed, with a "
         "limestone cave beneath it called the turtle tomb. Entry needs a Sabah Parks permit.",
         "Sipadan, closed for a month in November 2023 to let the reef recover. " + WIKI),
        ("Silfra", "Þingvellir, Iceland",
         "A rift between the North American and Eurasian plates, filled with Langjökull "
         "meltwater at 2–4 °C. In the Cathedral you can see nearly the whole 100 m fissure.",
         "Silfra. Dived in a dry suit. " + WIKI),
        ("Revillagigedo", "Mexico",
         "Socorro and its neighbours: a UNESCO site since 2016 inside a 150,000 km² "
         "protected area. No tourism facilities and no fresh water, so you live on the boat.",
         "Revillagigedo Islands. " + WIKI),
        ("Palau", "Micronesia",
         "The Rock Islands became a World Heritage Site in 2012, and in 2015 Palau protected "
         "80% of its waters — the first country to do it.",
         "Palau. " + WIKI),
    ],
    """
The Great Barrier Reef is not the dive you think it is. It is 2,300 km long, most operators work the same accessible fraction of it, and a lot of people come up having seen a bleached patch from a day boat full of snorkellers.

Five places where the water is doing something specific. Opinion; the numbers are Wikipedia's.

01 RAJA AMPAT, Indonesia — 1,508 fish species and 537 coral species recorded, and Konservasi Indonesia is quoted saying marine surveys suggest the marine life diversity here is the highest recorded on Earth. The same article elsewhere says more than 600 hard corals and more than 1,700 reef fish, so even the inventory cannot keep up. It sits in the Coral Triangle.

02 SIPADAN, Malaysia — the only oceanic island in Malaysia, rising 600 m straight off the seabed on an extinct volcanic cone, with a limestone cave underneath known as the turtle tomb. Green and hawksbill turtles nest there. Visiting requires a permit from Sabah Parks, and the island was closed for a month in November 2023 to let the ecosystem recover.

03 SILFRA, Iceland — a rift in the Mid-Atlantic Ridge, the boundary between the North American and Eurasian plates, filled with groundwater that started as meltwater from Langjökull and seeped through porous lava rock. It is 2 to 4 °C, dived in a dry suit, and in the section called the Cathedral you can see almost the full 100 m of fissure end to end.

04 REVILLAGIGEDO, Mexico — Socorro and its neighbours, inscribed in July 2016 and sitting inside a protected area of 150,000 km². There are no tourism facilities and no reliable fresh water on the islands, so visitors stay aboard expedition vessels. Cetaceans, sharks and manta rays.

05 PALAU — the Rock Islands became a World Heritage Site in 2012, and in 2015 Palau officially protected 80% of its water resources, which the article says made it the first country to do so.

Which dive have you done that ruined every dive after it?
""",
    ["scubadiving", "rajaampat", "sipadan", "silfra", "palau", "socorro",
     "divetravel", "travelinspo", "worldfacts", "adventuretravel", "earthbynumbers"],
)

top5(
    "top5-wine-regions",
    "Bordeaux is a<br>brand with<br>vineyards attached.",
    "Opinion. Five regions where the wine is the point, not the label.",
    [
        ("Douro", "Portugal",
         "A royal charter of 10 September 1756 made this the first wine region in the world "
         "with a formal demarcation. The Alto Douro has been a World Heritage Site since 2001.",
         "Douro DOC. The 1756 demarcation covered Port. " + WIKI),
        ("Mosel", "Germany",
         "The Calmont at Bremm is the steepest recorded vineyard in the world, at a 65-degree "
         "incline. Riesling was on 59.7% of the region's vineyard surface in 2008.",
         "Mosel wine region: 9,034 hectares in 2008. " + WIKI),
        ("Tokaj", "Hungary",
         "Home of aszú, called the world's oldest botrytised wine, and supposedly the "
         "earliest wine appellation — a claim its own page disputes with Chianti's 1716.",
         "Tokaj wine region. The decree is dated 1737 or 1757; UNESCO 2002. " + WIKI),
        ("Langhe", "Piedmont, Italy",
         "Barolo and Barbaresco come from here. Part of the Langhe was inscribed on 22 June "
         "2014 as the Vineyard Landscape of Piedmont.",
         "Langhe. " + WIKI),
        ("Mendoza", "Argentina",
         "Seventy percent of Argentina's 1.5 billion litres of wine, made at the foot of the "
         "Andes by around 1,200 wineries.",
         "Mendoza Province. The 1,200-winery figure is from 2005. " + WIKI),
    ],
    """
Bordeaux is a brand with vineyards attached. The wine can be extraordinary and the visit is a chateau car park, a tasting room priced off a label, and a region that long ago worked out it does not need to be interesting.

Five regions where the place is the reason. Opinion; dates and figures from Wikipedia.

01 DOURO, Portugal — a royal Portuguese charter dated 10 September 1756 defined the production region for Port, which its article says made the Douro the world's first wine region to have a formal demarcation. The Alto Douro Wine Region has been a World Heritage Site since 2001. Terraces cut into schist above a river, and nobody has made it convenient.

02 MOSEL, Germany — the Calmont vineyard at Bremm is, at a 65-degree incline, the steepest recorded vineyard in the world. In 2008 Riesling was planted on 59.7% of the region's 9,034 hectares. Slate, river bends, and wine that argues with everything else on this list.

03 TOKAJ, Hungary — the home of aszú, which its article calls the world's oldest botrytised wine, made from individually picked botrytised grapes. It also claims "supposedly the world's earliest system of wine appellation" and then immediately notes the claim is disputed by Chianti, whose territory was defined in 1716. Its own founding decree is dated either 1737 or 1757; the page does not choose. World Heritage Site since 2002.

04 LANGHE, Italy — Barolo and Barbaresco. Part of the Langhe was inscribed on 22 June 2014 as part of the Vineyard Landscape of Piedmont: Langhe-Roero and Monferrato. Also truffles, which is not a coincidence.

05 MENDOZA, Argentina — about 70% of Argentina's 1.5 billion litres of wine production, from roughly 1,200 wineries at the foot of the Andes.

So who really was first, Douro in 1756 or Tokaj in 1737? Both pages hedge. Tell us which claim you believe.
""",
    ["wine", "douro", "mosel", "tokaj", "langhe", "mendoza", "winetravel",
     "travelinspo", "worldfacts", "vineyards", "earthbynumbers"],
)

top5(
    "top5-castles",
    "Neuschwanstein is<br>a fantasy, not<br>a fortress.",
    "Opinion. Its foundation stone was laid in 1869 and the fortifications were left out "
    "on purpose.",
    [
        ("Malbork Castle", "Poland",
         "The world's largest brick castle on completion in 1406, enclosing 21 hectares — "
         "four times the area inside Windsor. Built by the Teutonic Order.",
         "Malbork Castle, a World Heritage Site since 1997. " + WIKI),
        ("Himeji Castle", "Japan",
         "Eighty-three buildings, intact for almost 700 years. Himeji burned in the Second "
         "World War and the castle survived. Earthquakes have left it virtually undamaged.",
         "Himeji Castle, inscribed 11 December 1993. " + WIKI),
        ("Mehrangarh", "Jodhpur, India",
         "Walls up to 36 m high and 21 m wide, standing about 122 m above the plains. "
         "Founded in 1459 by Rao Jodha of the Rathore clan.",
         "Mehrangarh. " + WIKI),
        ("Hohensalzburg", "Austria",
         "250 m by 150 m, which its article says makes it one of the largest medieval castles "
         "in Europe, and one of the best preserved. Construction began in 1077.",
         "Hohensalzburg Fortress. " + WIKI),
        ("Alcázar of Segovia", "Spain",
         "Its page says this silhouette inspired the castle in Disney's Snow White of 1937. "
         "Neuschwanstein's page claims Sleeping Beauty and Cinderella instead.",
         "Alcázar of Segovia, part of the Old Town of Segovia, UNESCO 1985. " + WIKI),
    ],
    """
Neuschwanstein is a fantasy, not a fortress. The foundation stone went down on 5 September 1869, it was commissioned by Ludwig II as a retreat and a tribute to Wagner, and its own article notes that real fortifications — the single most important feature of a medieval aristocratic estate — were dispensed with. It is a 19th-century historicist palace that looks like a castle, visited by 1.3 million people a year, or almost 1.5 million, depending which paragraph of the page you read.

Five castles that were built to be fought over. Opinion; figures from Wikipedia.

01 MALBORK CASTLE, Poland — on completion in 1406 the world's largest brick castle, and still the largest brick complex in Europe. The outer walls enclose 21 hectares, four times the area inside Windsor Castle. Built by the Teutonic Order; a World Heritage Site since 1997.

02 HIMEJI CASTLE, Japan — 83 buildings of storehouses, gates, corridors and turrets, with defensive systems from the feudal period. It has stood almost 700 years. Most of the surrounding city burned to the ground in the Second World War and the castle came through intact; earthquakes have left it virtually undamaged. Registered on 11 December 1993.

03 MEHRANGARH, India — walls up to 36 m high and 21 m wide, on a hilltop about 122 m above the plains of Jodhpur. The foundation was decided on 12 May 1459, under Rao Jodha of the Rathore clan.

04 HOHENSALZBURG, Austria — 250 m long and 150 m wide, which its article says makes it one of the largest medieval castles in Europe and one of the best preserved. Construction began in 1077 under Archbishop Gebhard von Helfenstein.

05 ALCÁZAR OF SEGOVIA, Spain — and a loose end. Its page says this castle's silhouette inspired the one in Disney's Snow White and the Seven Dwarfs of 1937. Neuschwanstein's page says it inspired Sleeping Beauty Castle and Cinderella Castle. Both are stated flatly. They cannot both be the castle people mean.

Which castle actually impressed you in person?
""",
    ["castles", "malbork", "himejicastle", "mehrangarh", "hohensalzburg", "segovia",
     "neuschwanstein", "travelinspo", "worldfacts", "history", "earthbynumbers"],
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
        print(f"  {p['slug']:24s} {p['kind']:9s} {len(p['slides'])} slides  "
              f"{full:4d} caption chars  {len(p['tags'])} tags{flag}")


if __name__ == "__main__":
    main()
