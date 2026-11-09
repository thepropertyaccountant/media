#!/usr/bin/env python3
"""
Earth by Numbers — content set C: country spotlights.

FORMAT  spotlight, 5 slides:
  1 hook      an interesting stat about the country
  2 ledger    key stats, all exact, straight from the dataset
  3 items     the best reasons to go
  4 fact      one more angle
  5 items     where to go + handle

Every figure on the ledger slide comes from the country dataset (BUILD.md),
so it is checkable. Qualitative travel content is deliberately kept
qualitative - no invented precision.

Run:  python3 posts_c.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "content"
DS = "Figures: mledoze/countries dataset (CC-BY-SA)."

POSTS = []


def spotlight(slug, hook, hook_sub, rows, why_title, why, extra, go_title, go,
              caption, tags, hook_size="h-lg", extra_bg="sun"):
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


# ─────────────────────────────────────────────────────────── Mongolia
spotlight(
    "spot-mongolia",
    "Mongolia has<br>exactly two<br>neighbours.",
    "They happen to be China and Russia. There is nobody else.",
    [["Capital", "Ulaanbaatar"], ["Land area", "1,564,110 km²"],
     ["Land borders", "2 — China, Russia"], ["Official language", "Mongolian"],
     ["Currency", "Tögrög (₮)"]],
    "Three reasons",
    [{"name": "Space", "note": "Among the least densely populated countries on Earth. You can drive for hours and see nobody."},
     {"name": "The steppe", "note": "Grassland to the horizon in every direction, still worked by herders on horseback."},
     {"name": "Gobi", "note": "A cold desert of dunes, canyons and dinosaur fossil beds."}],
    {"title": "A country the size of Western Europe, squeezed between two superpowers.",
     "sub": "1.56 million km², and the only two land routes in or out belong to China and Russia.",
     "source": DS},
    "Three that justify the drive",
    [{"name": "Gorkhi-Terelj", "note": "Granite formations and ger camps, close enough to Ulaanbaatar for a first taste."},
     {"name": "Orkhon Valley", "note": "UNESCO-listed grassland that was the centre of the Mongol empire."},
     {"name": "Gobi, South", "note": "Khongoryn Els dunes and the Flaming Cliffs, where the first dinosaur eggs were found."}],
    """
Mongolia borders exactly two countries. China and Russia. That is the entire list.

It is 1.56 million km² — roughly the size of Western Europe — and every road and rail line in or out passes through one of two superpowers. There is no third option. No port. No neutral neighbour.

MONGOLIA BY NUMBERS
Capital — Ulaanbaatar
Area — 1,564,110 km²
Land borders — 2
Official language — Mongolian
Currency — tögrög

It is also one of the least densely populated countries on Earth. Grassland runs to the horizon in every direction and a significant share of the population still herds livestock on horseback.

WHERE TO GO
Gorkhi-Terelj for granite formations and ger camps near the capital. The Orkhon Valley, UNESCO listed, which was the heart of the Mongol empire. The southern Gobi for the Khongoryn Els dunes and the Flaming Cliffs, where the first dinosaur eggs known to science were found.

Could you handle a week with no phone signal?
""",
    ["mongolia", "gobi", "steppe", "travelmongolia", "geographyfacts", "adventuretravel",
     "offthebeatenpath", "worldfacts", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Portugal
spotlight(
    "spot-portugal",
    "Portugal has<br>one land<br>border.",
    "And it has barely moved in seven hundred years.",
    [["Capital", "Lisbon"], ["Land area", "92,090 km²"],
     ["Land borders", "1 — Spain"], ["Official language", "Portuguese"],
     ["Currency", "Euro (€)"]],
    "Three reasons",
    [{"name": "The coast", "note": "Atlantic the whole way down, from cold northern surf beaches to the Algarve's sea caves."},
     {"name": "Value", "note": "Still among the cheapest countries in Western Europe to eat and sleep well in."},
     {"name": "The food", "note": "A country that takes salt cod seriously enough to claim a recipe for every day of the year."}],
    {"title": "One of the oldest continuously defined borders in Europe.",
     "sub": "Portugal's frontier with Spain has been substantially unchanged since the late 13th century.",
     "source": "Source: Wikipedia."},
    "Three past Lisbon",
    [{"name": "Porto", "note": "Steeper, rougher and cheaper, on a working river."},
     {"name": "Alentejo", "note": "Cork oaks, wheat and whitewashed hill towns. Almost nobody goes."},
     {"name": "Azores", "note": "Nine volcanic islands in the mid-Atlantic, closer to nothing than to anywhere."}],
    """
Portugal has exactly one land neighbour, and that border has barely shifted in seven centuries.

It is one of the oldest continuously defined frontiers in Europe — substantially settled since the late 1200s, while almost every other border on the continent was redrawn repeatedly by war.

PORTUGAL BY NUMBERS
Capital — Lisbon
Area — 92,090 km²
Land borders — 1 (Spain)
Official language — Portuguese
Currency — euro

That single border is the whole story of the place. With Spain to the east and nothing but Atlantic to the west, Portugal went outward by sea instead — which is why Portuguese is an official language on four continents.

WHERE TO GO, past Lisbon:
Porto — steeper, rougher, cheaper, on a working river.
Alentejo — cork oaks, wheat, whitewashed hill towns, almost no visitors.
Azores — nine volcanic islands in the middle of the Atlantic.

Lisbon or Porto? Pick one and defend it.
""",
    ["portugal", "lisbon", "porto", "azores", "alentejo", "traveleurope",
     "geographyfacts", "travelinspo", "worldfacts", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Morocco
spotlight(
    "spot-morocco",
    "Morocco shares<br>a land border<br>with Spain.",
    "In Africa. Two Spanish cities sit on the Moroccan coast.",
    [["Capital", "Rabat"], ["Land area", "446,550 km²"],
     ["Land borders", "Algeria, Spain, W. Sahara"], ["Official languages", "Arabic, Berber"],
     ["Currency", "Dirham (د.م.)"]],
    "Three reasons",
    [{"name": "Four landscapes", "note": "Atlantic coast, Mediterranean coast, the High Atlas, and the Sahara — inside one country."},
     {"name": "The medinas", "note": "Fez el Bali is one of the largest car-free urban areas anywhere in the world."},
     {"name": "Proximity", "note": "A three-hour flight from much of Europe into somewhere genuinely different."}],
    {"title": "Ceuta and Melilla are Spanish cities on the African mainland.",
     "sub": "They are part of the European Union, bordered entirely by Morocco — which is why Spain appears on Morocco's border list.",
     "source": "Source: Wikipedia."},
    "Three beyond Marrakech",
    [{"name": "Chefchaouen", "note": "A blue-painted town in the Rif mountains, cool and slow."},
     {"name": "Taghazout", "note": "Atlantic surf village south of Agadir."},
     {"name": "Merzouga", "note": "Erg Chebbi dunes, where the Sahara starts properly."}],
    """
Morocco has a land border with Spain. In Africa.

Ceuta and Melilla are Spanish cities sitting on the North African mainland, entirely surrounded by Moroccan territory. They are part of the European Union. You can walk from Morocco into the EU without crossing water.

MOROCCO BY NUMBERS
Capital — Rabat (not Marrakech, and not Casablanca)
Area — 446,550 km²
Official languages — Arabic and Berber (Amazigh)
Currency — dirham

Inside one country you get Atlantic coast, Mediterranean coast, the High Atlas with snow on it, and the Sahara. Very few countries that size carry that much variety.

Fez el Bali, the old medina of Fez, is one of the largest car-free urban areas on Earth. Not a pedestrianised zone — a medieval city that cars were never able to enter.

WHERE TO GO, past Marrakech:
Chefchaouen — blue-painted town in the Rif mountains.
Taghazout — Atlantic surf village south of Agadir.
Merzouga — the Erg Chebbi dunes, where the Sahara begins in earnest.

Did you know the EU has a land border with Morocco?
""",
    ["morocco", "marrakech", "chefchaouen", "sahara", "fez", "travelmorocco",
     "geographyfacts", "travelafrica", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Peru
spotlight(
    "spot-peru",
    "Peru has three<br>official<br>languages.",
    "Two of them were spoken there long before Spanish arrived.",
    [["Capital", "Lima"], ["Land area", "1,285,216 km²"],
     ["Land borders", "5"], ["Official languages", "Spanish, Quechua, Aymara"],
     ["Currency", "Sol (S/.)"]],
    "Three reasons",
    [{"name": "Three countries in one", "note": "Desert coast, high Andes and Amazon rainforest, all inside the same borders."},
     {"name": "The food", "note": "Japanese, Chinese, African, Andean and Spanish traditions folded together over 150 years."},
     {"name": "Depth of history", "note": "Civilisations here are older than the Inca by thousands of years."}],
    {"title": "Quechua is still spoken by millions of people.",
     "sub": "It was the administrative language of the Inca empire and remains official in Peru today, alongside Aymara.",
     "source": "Source: Wikipedia."},
    "Three past Machu Picchu",
    [{"name": "Arequipa", "note": "White volcanic-stone city under three volcanoes, beside the Colca Canyon."},
     {"name": "Huáscarán", "note": "Glaciated peaks and turquoise lakes in the Cordillera Blanca."},
     {"name": "Northern coast", "note": "Adobe ruins of Chan Chan and Moche pyramids, with almost no crowds."}],
    """
Peru has three official languages: Spanish, Quechua and Aymara. Two of them predate the Spanish by a long way.

Quechua was the administrative language of the Inca empire and is still spoken by millions of people today. It is not a heritage project — it is official, and it is alive.

PERU BY NUMBERS
Capital — Lima
Area — 1,285,216 km²
Land borders — 5 (Bolivia, Brazil, Chile, Colombia, Ecuador)
Official languages — Spanish, Quechua, Aymara
Currency — sol

Geographically it is three countries stacked together: a desert coastline, the high Andes, and Amazon rainforest. You can go from sea-level desert to 4,000 m to jungle without leaving the country.

The history is deeper than most people realise. Caral on the coast is among the oldest known urban sites in the Americas — thousands of years before the Inca, who are comparatively recent.

WHERE TO GO, past Machu Picchu:
Arequipa — white volcanic-stone city under three volcanoes, next to the Colca Canyon.
Huascarán — glaciated peaks and turquoise lakes in the Cordillera Blanca.
The northern coast — Chan Chan's adobe ruins and Moche pyramids, almost empty.

Could you name Peru's five neighbours?
""",
    ["peru", "machupicchu", "arequipa", "quechua", "andes", "amazon", "travelperu",
     "geographyfacts", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Georgia
spotlight(
    "spot-georgia",
    "Georgia borders<br>Russia and<br>Türkiye.",
    "And Armenia, and Azerbaijan. Four neighbours, no two alike.",
    [["Capital", "Tbilisi"], ["Land area", "69,700 km²"],
     ["Land borders", "4"], ["Official language", "Georgian"],
     ["Currency", "Lari (₾)"]],
    "Three reasons",
    [{"name": "The wine", "note": "An 8,000-year tradition using qvevri — clay vessels buried in the ground. UNESCO-listed."},
     {"name": "Its own alphabet", "note": "Georgian script looks like nothing else on Earth and is used by almost nobody else."},
     {"name": "The Caucasus", "note": "5,000-metre peaks and villages reachable only in summer."}],
    {"title": "Many nationalities can stay a full year, visa-free.",
     "sub": "One of the most generous entry policies anywhere — check your own passport's rules before booking.",
     "source": "Entry rules change. Verify before travel."},
    "Three past Tbilisi",
    [{"name": "Svaneti", "note": "Medieval stone defence towers under glaciated peaks."},
     {"name": "Kakheti", "note": "The wine region. Qvevri buried in courtyards, poured by the people who made it."},
     {"name": "Vardzia", "note": "A cave monastery carved into a cliff across thirteen levels."}],
    """
Georgia borders Russia, Türkiye, Armenia and Azerbaijan. Four neighbours, and no two of them alike in language, alphabet or alliance.

It sits exactly where Europe stops being Europe, and it has spent most of its history being argued over by whoever was largest at the time.

GEORGIA BY NUMBERS
Capital — Tbilisi
Area — 69,700 km²
Land borders — 4
Official language — Georgian
Currency — lari

Georgia has its own alphabet. Not a variant of Cyrillic or Latin — its own script, used essentially nowhere else, and recognised by UNESCO.

It also has an 8,000-year winemaking tradition using qvevri, large clay vessels buried in the ground. That method is itself UNESCO-listed. This is plausibly where wine was invented.

Many nationalities can stay a full year visa-free, which is among the most generous policies in the world — but check your own passport before you book, because entry rules change.

WHERE TO GO, past Tbilisi:
Svaneti — medieval stone defence towers under glaciated peaks.
Kakheti — the wine region, poured in courtyards by the people who made it.
Vardzia — a cave monastery carved thirteen levels into a cliff.

Is Georgia in Europe or Asia? Settle it in the comments.
""",
    ["georgia", "tbilisi", "svaneti", "caucasus", "wine", "travelgeorgia",
     "geographyfacts", "offthebeatenpath", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Nepal
spotlight(
    "spot-nepal",
    "Nepal is<br>landlocked<br>between two<br>giants.",
    "China on one side, India on the other. Nothing else.",
    [["Capital", "Kathmandu"], ["Land area", "147,181 km²"],
     ["Land borders", "2 — China, India"], ["Official language", "Nepali"],
     ["Currency", "Nepalese rupee (₨)"]],
    "Three reasons",
    [{"name": "The mountains", "note": "Eight of the world's ten highest peaks sit on or across Nepal's borders."},
     {"name": "Trekking access", "note": "Few places on Earth let you walk into high mountains this easily or this cheaply."},
     {"name": "The range", "note": "Subtropical jungle in the south, 8,000-metre peaks in the north, inside 200 km."}],
    {"title": "Nepal has never been colonised.",
     "sub": "Unusually for the region, it was never ruled by a European power — which is part of why its culture reads so differently to its neighbours'.",
     "source": "Source: Wikipedia."},
    "Three routes",
    [{"name": "Annapurna Circuit", "note": "The classic. Over the Thorong La pass at 5,416 m."},
     {"name": "Everest Base Camp", "note": "Busy, and still extraordinary. Fly into Lukla."},
     {"name": "Chitwan", "note": "Lowland jungle with rhino and tiger. Nobody expects this from Nepal."}],
    """
Nepal has two neighbours: China and India. Between them they hold about a third of humanity.

Nepal sits in the gap, landlocked, 147,181 km², with the Himalaya forming its northern wall.

NEPAL BY NUMBERS
Capital — Kathmandu
Area — 147,181 km²
Land borders — 2
Official language — Nepali
Currency — Nepalese rupee

Eight of the world's ten highest mountains stand on or across its borders, Everest included. The country runs from subtropical jungle in the south to 8,000-metre peaks in the north, and the whole transition happens in about 200 kilometres.

It was also never colonised by a European power — unusual for the region, and a large part of why Nepali culture reads so differently from its neighbours'.

WHERE TO GO
Annapurna Circuit — the classic, over the Thorong La at 5,416 m.
Everest Base Camp — busy, and still extraordinary.
Chitwan — lowland jungle with rhino and tiger, which almost nobody associates with Nepal.

Mountains or jungle — which Nepal would you go for?
""",
    ["nepal", "himalaya", "everest", "annapurna", "kathmandu", "trekking",
     "travelnepal", "geographyfacts", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Chile
spotlight(
    "spot-chile",
    "Chile is longer<br>than the width<br>of Australia.",
    "And averages barely 180 km across.",
    [["Capital", "Santiago"], ["Land area", "756,102 km²"],
     ["Land borders", "3"], ["Official language", "Spanish"],
     ["Currency", "Chilean peso ($)"]],
    "Three reasons",
    [{"name": "Every climate", "note": "The driest desert on Earth at one end, glaciers and fjords at the other."},
     {"name": "The Atacama sky", "note": "Where the world builds its largest telescopes, because the air is that clear."},
     {"name": "Patagonia", "note": "Granite towers, ice fields and wind that genuinely knocks people over."}],
    {"title": "One country, roughly 4,300 km from top to bottom.",
     "sub": "It spans desert, Mediterranean valleys, temperate rainforest, fjords and ice — because it covers that much latitude.",
     "source": "Source: Wikipedia."},
    "Three to build a trip around",
    [{"name": "San Pedro de Atacama", "note": "Salt flats, geysers and the clearest night sky you will ever stand under."},
     {"name": "Torres del Paine", "note": "The W trek, five days under granite towers."},
     {"name": "Carretera Austral", "note": "1,240 km of mostly gravel through fjords and rainforest."}],
    """
Chile is roughly 4,300 km long and averages under 200 km wide. It is a country shaped like a road.

That extreme shape is the whole point of visiting. Because it covers so much latitude, you get the driest non-polar desert on Earth at the top and glaciers and fjords at the bottom, with Mediterranean wine valleys and temperate rainforest in between.

CHILE BY NUMBERS
Capital — Santiago
Area — 756,102 km²
Land borders — 3 (Argentina, Bolivia, Peru)
Official language — Spanish
Currency — Chilean peso

The Atacama is where the world's major observatories are built, because the combination of altitude, dryness and near-permanent cloudlessness is almost unmatched anywhere.

WHERE TO GO
San Pedro de Atacama — salt flats, geysers, and the clearest night sky you will ever stand under.
Torres del Paine — the W trek, five days beneath granite towers.
Carretera Austral — 1,240 km of mostly gravel road through fjords and rainforest.

Desert or Patagonia — which end of Chile are you starting at?
""",
    ["chile", "atacama", "patagonia", "torresdelpaine", "carreteraaustral",
     "travelchile", "geographyfacts", "southamerica", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Vietnam
spotlight(
    "spot-vietnam",
    "Vietnam is<br>1,650 km long<br>and 50 km wide<br>at the middle.",
    "Which is why the north and south feel like different countries.",
    [["Capital", "Hanoi"], ["Land area", "331,212 km²"],
     ["Land borders", "3 — China, Laos, Cambodia"], ["Official language", "Vietnamese"],
     ["Currency", "Đồng (₫)"]],
    "Three reasons",
    [{"name": "The food", "note": "Regional and specific. Pho in Hanoi is a different dish to pho in Saigon, and people will tell you so."},
     {"name": "Value", "note": "Still among the cheapest serious food cultures in Asia."},
     {"name": "The coast", "note": "Over 3,000 km of it, most of which sees very few foreign visitors."}],
    {"title": "Hanoi and Ho Chi Minh City are 1,100 km apart.",
     "sub": "Different climates, different accents, different food. Treating Vietnam as one destination is the standard mistake.",
     "source": "Source: Wikipedia."},
    "Three past Ha Long Bay",
    [{"name": "Ha Giang Loop", "note": "Limestone mountains on the Chinese border, ridden by motorbike over three or four days."},
     {"name": "Phong Nha", "note": "Cave country, including some of the largest cave passages on Earth."},
     {"name": "An Bang", "note": "Hoi An's beach, minus Hoi An's crowds."}],
    """
Vietnam is about 1,650 km from top to bottom and narrows to roughly 50 km at its waist. The shape explains almost everything about the place.

Hanoi and Ho Chi Minh City are around 1,100 km apart, with different climates, different accents and genuinely different food. Treating Vietnam as a single destination is the standard mistake.

VIETNAM BY NUMBERS
Capital — Hanoi
Area — 331,212 km²
Land borders — 3 (China, Laos, Cambodia)
Official language — Vietnamese
Currency — đồng

Northern pho is clear, restrained, herb-light. Southern pho is sweeter, cloudier, piled with herbs and sprouts. People hold firm views. Both are correct.

WHERE TO GO, past Ha Long Bay:
Ha Giang Loop — limestone mountains on the Chinese border, by motorbike over three or four days. Probably the best thing in the country.
Phong Nha — cave country, including some of the largest cave passages on Earth.
An Bang — Hoi An's beach without Hoi An's crowds.

North or south — which Vietnam is better? Choose carefully.
""",
    ["vietnam", "hanoi", "hoian", "hagiang", "phongnha", "travelvietnam",
     "streetfood", "geographyfacts", "travelinspo", "earthbynumbers"],
    hook_size="h-md",
)

# ─────────────────────────────────────────────────────────── Namibia
spotlight(
    "spot-namibia",
    "Namibia has<br>nine recognised<br>languages.",
    "One of them is German. That is not an accident.",
    [["Capital", "Windhoek"], ["Land area", "825,615 km²"],
     ["Land borders", "4"], ["Recognised languages", "9"],
     ["Currency", "Namibian dollar ($)"]],
    "Three reasons",
    [{"name": "Emptiness", "note": "Among the least densely populated countries on Earth. Roads with nobody on them for hours."},
     {"name": "The dunes", "note": "Sossusvlei's red dunes rise to around 300 m above a dead white clay pan."},
     {"name": "Self-drive", "note": "One of the easiest African countries to travel independently by vehicle."}],
    {"title": "The Namib is where the desert runs into the Atlantic.",
     "sub": "Cold ocean current, hot desert air, and a fog that is the only reliable water source for most life on the Skeleton Coast.",
     "source": "Source: Wikipedia."},
    "Three that justify the drive",
    [{"name": "Sossusvlei", "note": "Red dunes and the dead camelthorn trees of Deadvlei."},
     {"name": "Etosha", "note": "A salt pan large enough to be seen from orbit, ringed with waterholes."},
     {"name": "Fish River Canyon", "note": "Among the largest canyons on Earth, and almost empty of people."}],
    """
Namibia recognises nine languages, and one of them is German. That is a direct inheritance of German colonial rule, which ended over a century ago and is still legible in the street names.

NAMIBIA BY NUMBERS
Capital — Windhoek
Area — 825,615 km²
Land borders — 4 (Angola, Botswana, South Africa, Zambia)
Recognised languages — 9, including Afrikaans, German, English, Herero and Khoekhoe
Currency — Namibian dollar

It is also nearly empty. Among the lowest population densities of any country on Earth, which means roads with nobody on them for hours at a time.

The Namib is where a desert runs straight into the Atlantic. A cold current meets hot desert air and produces a dense fog — which is the only dependable water source for most living things on the Skeleton Coast. There are beetles that stand on dune crests at dawn and drink condensation off their own backs.

WHERE TO GO
Sossusvlei — red dunes and the dead camelthorn trees of Deadvlei.
Etosha — a salt pan visible from orbit, ringed with waterholes.
Fish River Canyon — one of the largest canyons anywhere, almost deserted.

Desert or ocean? Namibia refuses to choose.
""",
    ["namibia", "sossusvlei", "skeletoncoast", "etosha", "desert", "travelafrica",
     "travelnamibia", "geographyfacts", "travelinspo", "earthbynumbers"],
)

# ─────────────────────────────────────────────────────────── Slovenia
spotlight(
    "spot-slovenia",
    "Slovenia fits<br>the Alps and the<br>Mediterranean<br>into 20,000 km².",
    "You can ski in the morning and swim in the afternoon. People do.",
    [["Capital", "Ljubljana"], ["Land area", "20,273 km²"],
     ["Land borders", "4"], ["Official language", "Slovene"],
     ["Currency", "Euro (€)"]],
    "Three reasons",
    [{"name": "Scale", "note": "Nothing is more than a couple of hours from anything else. One base covers the country."},
     {"name": "Forest", "note": "More than half of Slovenia is forested — among the highest shares in Europe."},
     {"name": "Caves", "note": "Classic karst country. The word 'karst' is named after this region."}],
    {"title": "Four borders, four different worlds.",
     "sub": "Austria, Italy, Hungary and Croatia — Alpine, Mediterranean, Pannonian and Balkan influences all meeting in one small country.",
     "source": "Source: Wikipedia."},
    "Three past Lake Bled",
    [{"name": "Soča Valley", "note": "A river an unreasonable shade of turquoise, running through a WWI front line."},
     {"name": "Škocjan Caves", "note": "An underground canyon with a river at the bottom. UNESCO-listed."},
     {"name": "Piran", "note": "A Venetian-era town on a thumb of land poking into the Adriatic."}],
    """
Slovenia is 20,273 km² and contains the Alps, the Mediterranean, the Pannonian plain and classic karst country. You can ski in the morning and swim in the Adriatic in the afternoon, and people actually do it.

SLOVENIA BY NUMBERS
Capital — Ljubljana
Area — 20,273 km²
Land borders — 4 (Austria, Italy, Hungary, Croatia)
Official language — Slovene
Currency — euro

Those four neighbours are the whole character of the place: Alpine, Mediterranean, Pannonian and Balkan influences meeting in a country smaller than Wales.

More than half of it is forest, among the highest proportions in Europe. And the word "karst" — used worldwide for limestone cave landscapes — is named after the Kras region here. This is the type specimen.

WHERE TO GO, past Lake Bled:
Soča Valley — a river an unreasonable shade of turquoise, running through a First World War front line.
Škocjan Caves — an underground canyon with a river at the bottom, UNESCO listed.
Piran — a Venetian-era town on a thumb of land poking into the Adriatic.

Smallest country you've visited that surprised you most?
""",
    ["slovenia", "ljubljana", "lakebled", "soca", "piran", "traveleurope",
     "geographyfacts", "hiddengems", "travelinspo", "earthbynumbers"],
    hook_size="h-md",
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        (OUT / f"{p['slug']}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False))
    print(f"wrote {len(POSTS)} posts")
    for p in POSTS:
        print(f"  {p['slug']:18s} {len(p['slides'])} slides  {len(p['caption'])} chars")


if __name__ == "__main__":
    main()
