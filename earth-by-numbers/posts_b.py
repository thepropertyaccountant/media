#!/usr/bin/env python3
"""
Earth by Numbers — content set B: Top 5s.

FORMAT  top5, 6 slides: a contentious hook, then ranks 1-5.
Opinion posts. The hook slide always picks a fight — a famous place left out,
or a famous place called overrated. That is the engagement mechanism: people
comment to defend the thing you excluded.

Every list says "opinion" on the hook slide so it is never read as measured
fact. Where a hard number appears it carries a source.

Run:  python3 posts_b.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "content"

POSTS = []


def top5(slug, hook_title, hook_sub, entries, caption, tags, hook_size="h-md"):
    """entries: list of 5 (place, where, note)."""
    slides = [{"type": "hook", "title": hook_title, "sub": hook_sub, "size": hook_size}]
    for i, (place, where, note) in enumerate(entries, start=1):
        slides.append({
            "type": "rank", "kicker": f"No. {i}", "rank": f"{i:02d}",
            "place": place, "where": where, "note": note,
            "bg": "" if i % 2 else "ink",
        })
    slides[-1]["handle"] = True
    POSTS.append({"slug": slug, "kind": "top5", "slides": slides,
                  "caption": caption.strip(), "tags": tags})


# ─────────────────────────────────────────────────────────────────
top5(
    "top5-europe-cities",
    "Prague is not<br>on this list.",
    "It stopped being underrated about twenty years ago. Five that still are. Opinion.",
    [
        ("Tbilisi", "Georgia", "Sulphur baths cut into a cliff, Soviet concrete beside carved wooden balconies, and wine made in buried clay pots."),
        ("Porto", "Portugal", "Steeper, cheaper and less polished than Lisbon. Tiled facades falling apart beautifully above a working river."),
        ("Ljubljana", "Slovenia", "A capital you cross on foot in half an hour, with the Alps and the Adriatic each about two hours away."),
        ("Gdańsk", "Poland", "A Hanseatic port rebuilt brick by brick after 1945. Amber, shipyard cranes, and the exact spot the war began."),
        ("Valletta", "Malta", "A fortified limestone city on a peninsula, small enough to feel like a single neighbourhood."),
    ],
    """
Prague is not on this list. Neither is Budapest. Both were genuinely underrated once; neither has been for about twenty years.

Five European cities that still are:

01 TBILISI, Georgia — sulphur baths built into a cliff, Soviet concrete next to carved wooden balconies, and an 8,000-year wine tradition using buried clay qvevri.

02 PORTO, Portugal — steeper, cheaper and rougher than Lisbon, with azulejo tiles peeling off facades above a working river.

03 LJUBLJANA, Slovenia — a capital you can walk across in 30 minutes. Alps one way, Adriatic the other, both about two hours.

04 GDAŃSK, Poland — a Hanseatic port rebuilt brick by brick after 1945. Amber, cranes, and Westerplatte, where the Second World War started.

05 VALLETTA, Malta — a fortified limestone city on a peninsula, compact enough to feel like one neighbourhood.

This is opinion, not data. We're not pretending there's a formula.

Now tell us why we're wrong about Prague.
""",
    ["europe", "traveleurope", "tbilisi", "porto", "ljubljana", "gdansk", "valletta",
     "hiddengems", "underratedtravel", "travelinspo", "earthbynumbers"],
    hook_size="h-lg",
)

top5(
    "top5-surf",
    "Pipeline doesn't<br>make the<br>top five.",
    "Famous is not the same as the best wave on Earth. Opinion, with one measurable fact inside.",
    [
        ("Nazaré", "Portugal", "A canyon roughly 5 km deep runs almost to the beach and funnels Atlantic swell into the largest rideable waves ever recorded."),
        ("Teahupoʻo", "Tahiti", "Not the tallest wave, the heaviest. It breaks over shallow reef carrying an absurd volume of water."),
        ("Jeffreys Bay", "South Africa", "A right-hand point break that runs and runs. Many surfers will argue it is the most perfectly shaped wave anywhere."),
        ("Uluwatu", "Bali, Indonesia", "Reef break under a clifftop temple, reached through a cave you time against the sets."),
        ("Raglan", "New Zealand", "One of the longest left-hand point breaks on Earth. On the right day the ride is measured in minutes."),
    ],
    """
Pipeline isn't on this list. It's the most photographed wave in the world and it still isn't top five.

01 NAZARÉ, Portugal — the Nazaré Canyon is about 5 km deep and runs almost to the shoreline, funnelling and amplifying Atlantic swell into the biggest rideable waves ever recorded. This is the one genuinely measurable entry here.

02 TEAHUPO'O, Tahiti — not the tallest, the heaviest. It breaks over shallow reef and the lip carries a frankly unreasonable volume of water.

03 JEFFREYS BAY, South Africa — a right-hand point break that simply keeps going. The shape argument ends here for a lot of people.

04 ULUWATU, Bali — reef break beneath a clifftop temple, accessed through a cave you time against the sets.

05 RAGLAN, New Zealand — one of the longest left-hand point breaks anywhere. You measure the ride in minutes, not seconds.

Ranking waves is opinion. The canyon is the only part you can put a number on.

Go on then — defend Pipeline.
""",
    ["surf", "surfing", "nazare", "teahupoo", "jeffreysbay", "uluwatu", "raglan",
     "surftravel", "waves", "traveltheworld", "earthbynumbers"],
)

top5(
    "top5-trains",
    "The Orient<br>Express is a<br>hotel on wheels.",
    "Not a journey. Five rail trips where the window is the point. Opinion.",
    [
        ("Trans-Siberian", "Moscow – Vladivostok", "Around 9,300 km and roughly seven days across eight time zones. The longest continuous rail service in the world."),
        ("Qinghai–Tibet", "Xining – Lhasa", "Crosses the Tanggula Pass above 5,000 m. The carriages supply supplementary oxygen because passengers need it."),
        ("Belgrade – Bar", "Serbia – Montenegro", "435 km, 254 tunnels, 435 bridges. Mountains down to the Adriatic in a single day, for the price of a pizza."),
        ("Bergen Line", "Oslo – Bergen", "About seven hours across the Hardangervidda plateau. Snow and emptiness between two very different Norwegian cities."),
        ("TranzAlpine", "Christchurch – Greymouth", "Coast to coast over New Zealand's Southern Alps in under five hours, through gorges and beech forest."),
    ],
    """
The Orient Express is a very good hotel that happens to move. It is not a great train journey. You are paying to look at the dining car.

Five where the window is the point:

01 TRANS-SIBERIAN, Moscow–Vladivostok — roughly 9,300 km, about seven days, eight time zones. The longest continuous rail service on Earth.

02 QINGHAI–TIBET, Xining–Lhasa — over the Tanggula Pass above 5,000 m. The carriages are pressurised and pipe in supplementary oxygen, because without it people struggle.

03 BELGRADE TO BAR — 435 km, 254 tunnels, 435 bridges, mountains to the Adriatic in one day. Probably the best value scenic rail journey in Europe by a distance.

04 BERGEN LINE, Oslo–Bergen — about seven hours across the Hardangervidda plateau.

05 TRANZALPINE, Christchurch–Greymouth — across the Southern Alps in under five hours.

A flight deletes the distance. A train makes you feel it. That's the whole argument.

Which one would you actually book?
""",
    ["trains", "trainjourney", "transsiberian", "tranzalpine", "slowtravel",
     "railtravel", "traveltheworld", "bucketlist", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-beach-towns",
    "Bali is not a<br>beach destination<br>any more.",
    "It is a traffic jam with a beach attached. Five that still work. Opinion.",
    [
        ("Jericoacoara", "Brazil", "Reached across sand dunes by 4WD. No paved roads, no street lights, and the whole village walks up a dune at sunset."),
        ("Taghazout", "Morocco", "A fishing village turned surf town. Atlantic point breaks, argan oil, and tagine for the price of a coffee."),
        ("Paje", "Zanzibar, Tanzania", "Kitesurfing flats on a turquoise lagoon, with a tide that walks out almost to the horizon twice a day."),
        ("An Bang", "Vietnam", "Hoi An's beach, minus Hoi An's crowds. Seafood shacks on the sand and a lantern-lit old town 15 minutes away."),
        ("Lagos", "Portugal", "Golden cliffs and sea caves on the Algarve, in a town that still functions outside of summer."),
    ],
    """
Bali had its moment. Canggu is now a traffic jam with a beach attached, and Seminyak is a shopping centre. Say it.

Five beach towns that still work:

01 JERICOACOARA, Brazil — you arrive by 4WD across sand dunes. No paved roads, no street lighting, and at sunset the entire village climbs the big dune to watch.

02 TAGHAZOUT, Morocco — a fishing village that became a surf town without becoming a resort. Atlantic point breaks and tagine for the price of a flat white.

03 PAJE, Zanzibar — kitesurfing flats on a turquoise lagoon, with a tide that retreats almost to the horizon twice a day.

04 AN BANG, Vietnam — Hoi An's beach without Hoi An's crowds. Seafood shacks directly on the sand, lantern-lit old town 15 minutes up the road.

05 LAGOS, Portugal — golden cliffs and sea caves on the Algarve, in a town that still has a life in February.

Opinion, obviously. The rule we used: would you go in the off season?

Tell us the one we've just ruined by posting it.
""",
    ["beach", "beachtown", "jericoacoara", "taghazout", "zanzibar", "hoian", "lagos",
     "travelinspo", "surftravel", "traveltheworld", "earthbynumbers"],
)

top5(
    "top5-food-cities",
    "Paris doesn't<br>make the<br>top five.",
    "Great restaurants, overrated eating city. Five where the street food beats the fine dining. Opinion.",
    [
        ("George Town", "Penang, Malaysia", "Chinese, Malay and Indian cooking collided here for two centuries. The result is arguably the best street food on Earth."),
        ("Oaxaca", "Mexico", "Seven moles, each taking a day to make. Markets selling chapulines, tlayudas and mezcal from the same stall."),
        ("Istanbul", "Türkiye", "Where the Balkans, the Caucasus and the Levant meet and eat. Breakfast alone takes two hours and fourteen plates."),
        ("Osaka", "Japan", "The city's own word for eating yourself bankrupt is kuidaore. Takoyaki, okonomiyaki, kushikatsu, done at counters."),
        ("Lima", "Peru", "Japanese, Chinese, African, Andean and Spanish traditions folded together over 150 years. Ceviche is only the entry point."),
    ],
    """
Paris has extraordinary restaurants and is an overrated eating city. Those are different claims and both are true.

Five where the street food outguns the fine dining:

01 GEORGE TOWN, Penang — two centuries of Chinese, Malay and Indian cooking in one small place. Char kway teow, assam laksa, nasi kandar. Probably the best street food on Earth.

02 OAXACA, Mexico — seven distinct moles, each taking a day. Markets selling chapulines, tlayudas and mezcal from the same stall.

03 ISTANBUL — where the Balkans, the Caucasus and the Levant meet and eat. Turkish breakfast is a two-hour, fourteen-plate event.

04 OSAKA — the local word kuidaore means to eat yourself into ruin. Takoyaki, okonomiyaki, kushikatsu, all at counters.

05 LIMA — Japanese, Chinese, African, Andean and Spanish traditions folded together over 150 years. Nikkei and chifa are the interesting part; ceviche is just the door.

The pattern: the best eating cities are port cities and trade crossroads. Food gets interesting where cultures were forced to share a kitchen.

Where should we have put Bangkok?
""",
    ["food", "foodtravel", "streetfood", "penang", "oaxaca", "istanbul", "osaka",
     "lima", "foodie", "traveltheworld", "earthbynumbers"],
)

top5(
    "top5-stargazing",
    "Iceland is a<br>bad place to<br>see the stars.",
    "Too much cloud, too much summer daylight. Five skies that actually deliver. Opinion.",
    [
        ("Atacama Desert", "Chile", "The driest non-polar desert on Earth, at altitude, with almost no cloud. This is where the world puts its biggest telescopes."),
        ("Aoraki Mackenzie", "New Zealand", "An International Dark Sky Reserve where the lighting is regulated by law. Southern sky, Magellanic Clouds, no haze."),
        ("NamibRand", "Namibia", "A private reserve in the Namib with effectively zero light pollution and some of the darkest measured skies on the planet."),
        ("La Palma", "Canary Islands", "Above the cloud layer at 2,400 m. A sky-protection law has limited light pollution here since 1988."),
        ("Jasper", "Canada", "One of the largest accessible dark sky preserves in the world, with aurora on top of the stars."),
    ],
    """
Iceland is a bad stargazing destination. It is cloudy, it is wet, and for months of the year it barely gets dark. People go for the aurora and come back having seen weather.

Five skies that actually deliver:

01 ATACAMA DESERT, Chile — the driest non-polar desert on Earth, at altitude, almost permanently cloudless. There is a reason the world's major observatories are built here rather than anywhere else.

02 AORAKI MACKENZIE, New Zealand — an International Dark Sky Reserve where outdoor lighting is restricted by law. The southern sky, the Magellanic Clouds, and almost no haze.

03 NAMIBRAND, Namibia — a private reserve in the Namib with essentially no light pollution for hundreds of kilometres.

04 LA PALMA, Canary Islands — observatories sit at 2,400 m, above the cloud layer. A sky-protection law has restricted light pollution since 1988.

05 JASPER, Canada — one of the largest accessible dark sky preserves anywhere, and you get aurora on top.

The rule: altitude, dryness, and a local government that regulates lighting. Pretty scenery is irrelevant if the air is wet.

Where did you see the best night sky of your life?
""",
    ["stargazing", "darksky", "atacama", "aoraki", "namibia", "lapalma", "jasper",
     "astrophotography", "nightsky", "traveltheworld", "earthbynumbers"],
)

top5(
    "top5-islands",
    "The Maldives<br>is the most<br>overrated island<br>on Earth.",
    "You are paying for a photograph. Five islands almost nobody goes to. Opinion.",
    [
        ("Socotra", "Yemen", "A third of its plant life exists nowhere else. The dragon's blood trees look like something drawn for a different planet."),
        ("São Tomé and Príncipe", "Gulf of Guinea", "Volcanic spires wrapped in rainforest, abandoned colonial plantations, and almost no tourism infrastructure at all."),
        ("Lord Howe Island", "Australia", "Only 400 visitors are permitted at any one time. A UNESCO site with a two-peaked volcanic skyline."),
        ("Flores", "Azores, Portugal", "Waterfalls down every cliff face, crater lakes on top, and weather that changes four times before lunch."),
        ("Svalbard", "Norway", "At 78°N, closer to the pole than to Oslo. Polar night for months, and more polar bears than people."),
    ],
    """
The Maldives is the most overrated island destination on Earth. You fly for a day to sit on a resort you cannot leave, on an island engineered to look like its own brochure. It is a photograph you are allowed to stand inside.

Five islands almost nobody goes to:

01 SOCOTRA, Yemen — roughly a third of its plant species exist nowhere else. The dragon's blood trees look like set design for a film about another planet.

02 SÃO TOMÉ AND PRÍNCIPE — volcanic spires wrapped in rainforest in the Gulf of Guinea, with abandoned colonial plantations and effectively no tourism industry.

03 LORD HOWE ISLAND, Australia — a hard cap of 400 visitors at any one time. UNESCO listed, two volcanic peaks, and a lagoon.

04 FLORES, Azores — waterfalls down every cliff, crater lakes on top, and four kinds of weather before lunch.

05 SVALBARD, Norway — 78°N, closer to the North Pole than to Oslo. Months of polar night, and more polar bears than people.

Some of these are hard to reach and one is genuinely difficult to enter. That is the point of the list.

Which island did we unfairly write off?
""",
    ["islands", "socotra", "saotome", "lordhowe", "azores", "svalbard", "offthebeatenpath",
     "hiddengems", "traveltheworld", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-cheap-stays",
    "Thailand is<br>not cheap<br>any more.",
    "It is good value. That is different. Five places where a month still costs very little. Opinion.",
    [
        ("Georgia", "Caucasus", "Many nationalities get a full year visa-free on arrival — among the most generous policies anywhere. Tbilisi rents stay low."),
        ("Albania", "Balkans", "Adriatic and Ionian coastline at a fraction of Croatian prices, and a capital that has become genuinely interesting."),
        ("Vietnam", "Southeast Asia", "Still the cheapest serious food culture in Asia. Da Nang and Hoi An cost a fraction of Bangkok."),
        ("Colombia", "South America", "Medellín's spring climate year round, no heating or cooling bills, and a strong local currency story for visitors."),
        ("Türkiye", "Anatolia", "Outside Istanbul's tourist core, costs drop steeply. Izmir and Antalya run far cheaper than anywhere comparable in the EU."),
    ],
    """
Thailand is not cheap any more. It is good value, which is a different claim. Bangkok and the islands now cost real money.

Five places where a month still costs very little:

01 GEORGIA — many nationalities get a full year visa-free on arrival, which is among the most generous entry policies in the world. Tbilisi rents remain low and the food is excellent.

02 ALBANIA — Adriatic and Ionian coast at a fraction of Croatian prices, and Tirana has become genuinely interesting rather than merely cheap.

03 VIETNAM — still the best cheap food culture in Asia. Da Nang and Hoi An run far below Bangkok.

04 COLOMBIA — Medellín sits in spring weather all year, so you pay nothing to heat or cool anything.

05 TÜRKIYE — outside Istanbul's tourist core, costs fall steeply. Izmir and Antalya undercut anywhere comparable in the EU.

Check current visa rules before you book anything. Entry policies change more often than prices do, and we are not a visa service.

Which of these is already too expensive?
""",
    ["budgettravel", "digitalnomad", "georgia", "albania", "vietnam", "colombia",
     "turkiye", "slowtravel", "traveltheworld", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-nightlife",
    "Ibiza is<br>finished.",
    "It became a venue for people who can afford tables. Five cities where the night is still the city's own. Opinion.",
    [
        ("Berlin", "Germany", "Still the reference point. Industrial spaces, no photos, no dress code you can buy your way past, and nights that run into Monday."),
        ("Tbilisi", "Georgia", "A club scene born out of protest, built inside a Soviet-era stadium. Political in a way almost nowhere else is."),
        ("Belgrade", "Serbia", "Floating clubs moored on the Danube and Sava. Summer nights happen on the water, which changes the whole physics of it."),
        ("Medellín", "Colombia", "Salsa, reggaeton and a city that treats dancing as a basic skill rather than a night out."),
        ("Mexico City", "Mexico", "Everything from mezcalerías in Roma to warehouse parties, across a city too large to ever be fully colonised by tourists."),
    ],
    """
Ibiza is finished. It stopped being a destination and became a venue — a place where the experience is now priced by proximity to a table.

Five cities where the night still belongs to the city:

01 BERLIN — still the reference point. Industrial spaces, stickers over your phone camera, a door policy you cannot buy your way past, and nights that end on Monday.

02 TBILISI — a club scene that grew directly out of political protest, operating inside a Soviet-era stadium. It means something there in a way it doesn't anywhere else.

03 BELGRADE — splavovi, floating clubs moored on the Danube and the Sava. In summer the whole night happens on the water.

04 MEDELLÍN — salsa and reggaeton in a city where dancing is a basic competence, not an event.

05 MEXICO CITY — mezcalerías in Roma through to warehouse parties, in a city far too big to be fully colonised by visitors.

The pattern: the best nightlife is in cities where locals outnumber visitors and the scene answers to them.

Which city would you put above Berlin?
""",
    ["nightlife", "berlin", "tbilisi", "belgrade", "medellin", "mexicocity",
     "clubbing", "citybreak", "traveltheworld", "travelinspo", "earthbynumbers"],
)

top5(
    "top5-road-trips",
    "Route 66 is<br>the most<br>overrated drive<br>in the world.",
    "Mostly a frontage road past closed motels. Five that earn the hire car. Opinion.",
    [
        ("Carretera Austral", "Chile", "1,240 km of mostly gravel through Patagonian fjords, glaciers and temperate rainforest. Ferries are part of the road."),
        ("Pamir Highway", "Tajikistan", "The second-highest international road on Earth, crossing passes above 4,600 m through the Wakhan Corridor."),
        ("Garden Route", "South Africa", "Indian Ocean coast, mountain passes and forest between Cape Town and Port Elizabeth, with wildlife as a side quest."),
        ("Ring Road", "Iceland", "1,332 km around an entire country. Waterfalls, black beaches, glacier lagoons, and weather doing all of it at once."),
        ("West Coast", "New Zealand", "Glaciers meeting rainforest meeting the Tasman Sea, on a road with almost nobody else on it."),
    ],
    """
Route 66 is the most overrated drive on Earth. Large parts of it no longer exist as a continuous road, and much of what remains is a frontage road running past closed motels selling nostalgia for itself.

Five that earn the hire car:

01 CARRETERA AUSTRAL, Chile — 1,240 km of largely gravel road through Patagonian fjords, glaciers and temperate rainforest. Ferries are part of the route, not a detour.

02 PAMIR HIGHWAY, Tajikistan — the second-highest international highway in the world, over passes above 4,600 m, through the Wakhan Corridor with Afghanistan on the far bank.

03 GARDEN ROUTE, South Africa — coast, mountain passes and forest, with wildlife as an optional extra.

04 RING ROAD, Iceland — 1,332 km around an entire country, and the weather will try every one of its options on you.

05 WEST COAST, New Zealand — glaciers, rainforest and the Tasman Sea, on a road with almost no one else on it.

The rule: a great drive needs the landscape to change. Distance alone is just commuting.

What's the best road you've ever driven?
""",
    ["roadtrip", "carreteraaustral", "pamirhighway", "gardenroute", "ringroad",
     "newzealand", "driving", "traveltheworld", "travelinspo", "earthbynumbers"],
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        (OUT / f"{p['slug']}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False))
    print(f"wrote {len(POSTS)} posts")
    for p in POSTS:
        print(f"  {p['slug']:22s} {len(p['slides'])} slides  {len(p['caption'])} chars")


if __name__ == "__main__":
    main()
