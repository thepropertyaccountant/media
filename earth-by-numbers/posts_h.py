#!/usr/bin/env python3
"""
Earth by Numbers — content set H: run 4 of the 100-buffer push, 2026-11-16.

Eight posts, all top5. This is a deliberately narrow batch and the reason is
worth recording, because a future run will hit the same wall.

WIKIPEDIA WAS UNREACHABLE IN THIS RUN.

Every WebFetch of en.wikipedia.org failed with error_type PROVENANCE_REQUIRED
("the permission request for this URL was not answered in time"). The run is a
scheduled, unattended one, so there was nobody to answer the prompt. WebSearch
returns link lists with no page text, and curl to en.wikipedia.org is refused
by the egress proxy (CONNECT tunnel failed, 403). Seven research agents were
dispatched across Indonesia, Brazil, Australia, Switzerland, the Maldives,
Tuvalu and Egypt; all seven came back with nothing read.

The mledoze/countries dataset IS reachable (raw.githubusercontent.com works),
and its rows for those countries were pulled. But a dataset row gives capital,
area, borders, languages and currency and nothing else — not enough to carry a
crazy post's hook or a spotlight's "why go", and BUILD.md §4 is unambiguous:
every figure must be verified in the run that uses it, never stated from
memory. So the twelve crazy and spotlight posts this batch was meant to contain
were not written. Writing them from recall would have been the one failure mode
BUILD.md names as unrecoverable.

What is left is the format that does not need figures. BUILD.md: "Top 5 lists
are opinion — they need no factual verification, but must say 'opinion' on the
hook slide, must open with a deliberately contentious call, and any hard number
that does appear still needs a source." These eight carry no hard numbers at
all — no distances, heights, areas, counts, dates or prices, in the slides or
in the captions — so there is nothing in them requiring a source, and no slide
carries one. That is a deliberate departure from sets A–G, where the top5 notes
lean on verified Wikipedia figures. These lean on judgement instead.

They also avoid stated superlatives, which are factual claims wearing an
adjective. No entry here is called the largest, deepest, oldest or highest
anything. Where a superlative would be natural the note gives an opinion in the
first person of the account instead.

  top5 (8)  lakes, canyons, fjords, safaris, museums, ski-towns, temples,
            tea-regions

MIX NOTE: this skews the queue. Unposted standing was crazy 22, top5 22,
spotlight 23, and eight top5 takes it to 30/22/23 — the opposite of the even
mix the standing instruction asks for. Accepted knowingly: the alternative was
writing nothing, or writing unverified figures. The next run, with Wikipedia
reachable, should favour crazy and spotlight heavily to pull the mix back.

NOT WRITTEN THIS RUN, and why (all blocked on the same unreachable source):
  - indonesia-crazy. Island counts (the registered figure, the older 13,466,
    and the government figure all needed checking against each other), active
    volcano count, language count, and above all the Jakarta vs Nusantara
    capital question, which cannot be stated either way without reading the
    page. The dataset still lists Jakarta; that is exactly the shape of the
    Nauru catch and needs the article to resolve.
  - brazil-crazy. The border count is the whole post: the dataset lists ten
    neighbours including GUF, French Guiana, which is an overseas department of
    France and not a sovereign state — the same class of error as China's
    sixteen. Resolving it to a defensible claim needs Wikipedia's own wording.
  - australia-crazy. Western Australia's area, Great Barrier Reef extent,
    Anna Creek Station, arid share, coastline. Every one a figure.
  - switzerland-crazy. Bern's status as federal city rather than de jure
    capital is a wording question, not a number, but the post around it needed
    the language percentages, the four-thousander count and the Gotthard
    figures.
  - maldives-crazy. The hook was the lowest high point of any country, with a
    known 2.4 m / 5.1 m contradiction to resolve. Unresolvable without the page.
  - tuvalu-crazy. The .tv lease revenue is volatile and date-stamped, the
    Falepili Union terms are recent, and the sea level figures all carry dates.
  - egypt-crazy. The share of the country that is actually inhabited is the
    hook and exists in several competing versions.
  - The six spotlights (croatia, kenya, malaysia, costa-rica, cambodia,
    azerbaijan). The spotlight shape puts a dataset ledger on slide 2 and
    Wikipedia-sourced items on slides 3 and 5; two of its five slides cannot be
    built from the dataset alone. Azerbaijan is worth keeping for the next run:
    the dataset marks it landlocked, which is defensible only because the
    Caspian is a lake, and that contradiction is a slide in the house style.

Run:  python3 posts_h.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "content"

POSTS = []


def top5(slug, hook_title, hook_sub, entries, caption, tags, hook_size="h-md"):
    """entries: list of 5 (place, where, note). No source field: no figures."""
    slides = [{"type": "hook", "title": hook_title, "sub": hook_sub, "size": hook_size}]
    for i, (place, where, note) in enumerate(entries, start=1):
        slides.append({"type": "rank", "kicker": f"No. {i}", "rank": f"{i:02d}",
                       "place": place, "where": where, "note": note,
                       "bg": "" if i % 2 else "ink"})
    slides[-1]["handle"] = True
    POSTS.append({"slug": slug, "kind": "top5", "slides": slides,
                  "caption": caption.strip(), "tags": tags})


# ════════════════════════════════════════════════════════ LAKES ════

top5(
    "top5-lakes",
    "Lake Como is a<br>car park with<br>a view.",
    "Opinion. Five lakes worth the journey, and Como is not one of them.",
    [
        ("Lake Ohrid", "North Macedonia and Albania",
         "Swim off the rocks below the old town, then take the boat along the cliffs to the "
         "monastery on the headland. The town behind the water is lived in rather than staged."),
        ("Lake Atitlán", "Sololá, Guatemala",
         "Volcanoes on three sides and a different village at every jetty. The passenger boat "
         "is the bus. Leave Panajachel quickly and stay somewhere you can only reach by water."),
        ("Lake Malawi", "Malawi, Mozambique and Tanzania",
         "Clear fresh water, fish that live nowhere else, and beaches with nobody selling you "
         "anything. Cape Maclear to snorkel, Likoma for the cathedral nobody expects."),
        ("Lake Khövsgöl", "Khövsgöl Province, Mongolia",
         "Taiga on one shore, steppe on the other, herders in the hills behind. Go in winter "
         "for the ice and accept that the road in is most of the trip."),
        ("Lake Toba", "North Sumatra, Indonesia",
         "A lake sitting in a volcanic crater with an island in the middle big enough to have "
         "its own roads and villages. Stay on Samosir. The water is warm, which none of the "
         "others manage."),
    ],
    """
Lake Como is a road with a lake beside it. The villas are someone else's, the shoreline is spoken for, and the boat you take is full of people taking the same photograph from the same side.

Five lakes that are worth the effort of getting to. Opinion, all of it.

01 LAKE OHRID, North Macedonia and Albania — swim off the rocks under the old town and take the boat along the cliffs to the monastery on the headland. The town behind the water is still a town. The Albanian side is quieter again and almost nobody crosses.

02 LAKE ATITLÁN, Guatemala — volcanoes on three sides and a different village at every jetty, each with its own character and its own opinion of the others. The passenger boat is the local bus. Panajachel is the arrival point, not the destination.

03 LAKE MALAWI, Malawi — fresh water clear enough to snorkel, full of fish found nowhere else on earth, and beaches where nobody approaches you. Cape Maclear for the water, Likoma Island for the cathedral that has no business being there.

04 LAKE KHÖVSGÖL, Mongolia — forest on one side, open steppe on the other, reindeer herders in the hills behind it. Winter turns it to ice you can drive on, which people do. The journey is not incidental to the trip; it is the trip.

05 LAKE TOBA, Indonesia — a crater lake with an island in it large enough to have its own villages, roads and funeral customs. Samosir is where you stay, and the water is warm enough to swim in without flinching.

Which lake was better than the famous one next to it?
""",
    ["lakes", "lakeohrid", "atitlan", "lakemalawi", "khovsgol", "laketoba",
     "travelinspo", "geographyfacts", "worldfacts", "offthebeatenpath",
     "earthbynumbers"],
    hook_size="h-lg",
)

# ══════════════════════════════════════════════════════ CANYONS ════

top5(
    "top5-canyons",
    "You will not<br>remember the<br>Grand Canyon.",
    "Opinion. Five canyons you go into, rather than look at.",
    [
        ("Tiger Leaping Gorge", "Yunnan, China",
         "A trail cut into the gorge wall high above the river, walked village to village with "
         "a guesthouse at the end of each day. There is a low road for buses. Take the high one."),
        ("Vikos Gorge", "Zagori, Epirus, Greece",
         "Stone villages linked by arched packhorse bridges, and a gorge floor you reach down "
         "an old mule path. The Zagori is empty outside summer and better for it."),
        ("Blyde River Canyon", "Mpumalanga, South Africa",
         "Green rather than bare, which is not what a canyon is supposed to look like. The "
         "drive-up viewpoints are busy. The trails below the rim are not."),
        ("Verdon Gorge", "Alpes-de-Haute-Provence, France",
         "Turquoise water at the bottom, limestone walls above it, and a river path that feels "
         "designed by somebody with a grudge. Swim at the Sainte-Croix end afterwards."),
        ("Cañón del Sumidero", "Chiapas, Mexico",
         "Seen from a boat, looking up, with vultures above and crocodiles alongside. Not a "
         "walk, and better for being honest about that."),
    ],
    """
The Grand Canyon is the one everybody sees and nobody experiences. You park, you look, you take the photograph that has already been taken, and you leave having stood on the edge of something you never entered.

Five canyons you go into. Opinion, all of it.

01 TIGER LEAPING GORGE, China — the high trail is cut into the wall of the gorge, far above the water, and you walk it between villages with somewhere to sleep at the end of each day. There is a road along the bottom for coach parties. Ignore it.

02 VIKOS GORGE, Greece — the Zagori villages above it are built entirely of stone and linked by arched packhorse bridges, and the path down to the gorge floor is an old mule track. Out of season you will have the whole thing to yourself.

03 BLYDE RIVER CANYON, South Africa — green, forested and wet, which is not how a canyon is meant to behave. The viewpoints on the rim road are drive-up and crowded. Walk below the rim and the crowd evaporates.

04 VERDON GORGE, France — limestone walls with improbably turquoise water at the bottom, and a path along the river that involves ladders and a tunnel and a torch. Swim at the lake end when you are done with being frightened.

05 CAÑÓN DEL SUMIDERO, Mexico — this one you see from below, from a boat, with the walls going straight up and crocodiles on the banks. It is not a hike and does not pretend to be, which I respect more than most viewpoints.

Which canyon did you walk into instead of looking at?
""",
    ["canyons", "tigerleapinggorge", "vikos", "blydeRiverCanyon", "verdon",
     "sumidero", "hiking", "travelinspo", "geographyfacts", "worldfacts",
     "earthbynumbers"],
    hook_size="h-lg",
)

# ═══════════════════════════════════════════════════════ FJORDS ════

top5(
    "top5-fjords",
    "Geirangerfjord<br>is a cruise<br>terminal.",
    "Opinion. Five fjords where the boat is not the problem.",
    [
        ("Scoresby Sound", "Ittoqqortoormiit, East Greenland",
         "Icebergs the size of buildings, one village of painted houses, and essentially no "
         "infrastructure. Getting there is a flight, a boat and a great deal of patience."),
        ("Lysefjord", "Rogaland, Norway",
         "Walk to Kjerag or Preikestolen in the morning and take the ferry down the fjord "
         "afterwards, in that order. Norway without the coach park at the famous one."),
        ("Doubtful Sound", "Fiordland, New Zealand",
         "Wetter, longer and much quieter than its neighbour. You get there by boat across a "
         "lake and a bus over a pass, which filters out everyone in a hurry."),
        ("Kenai Fjords", "Alaska, United States",
         "Tidewater glaciers dropping ice into the sea while sea lions watch from the rocks. "
         "Go out of Seward on the smallest boat you can book."),
        ("Arnarfjörður", "Westfjords, Iceland",
         "The Westfjords are the part of Iceland the ring road skips, which is the whole "
         "recommendation. Dynjandi at the head of it, gravel roads, and a hot pot with nobody "
         "in it."),
    ],
    """
Geirangerfjord is beautiful and you will share it with four thousand people who arrived at the same time you did on the same hull. The village exists to process them. The fjord does not care, but you will.

Five fjords where the boat is part of the experience rather than the obstacle. Opinion.

01 SCORESBY SOUND, Greenland — a fjord system so large it stops reading as a fjord, with icebergs the size of office blocks and one small village of painted houses at the mouth of it. There is no easy way in, which is why there is nobody there.

02 LYSEFJORD, Norway — the right order is to walk up to Kjerag or Preikestolen first and take the ferry along the water afterwards, so you see from below what you stood on. It is the famous Norwegian experience without the famous Norwegian crowd.

03 DOUBTFUL SOUND, New Zealand — longer, wetter and far quieter than Milford next door. You cross a lake by boat and a pass by bus to reach it, and that small inconvenience removes most of the people.

04 KENAI FJORDS, Alaska — glaciers that come down to the sea and calve into it, with sea lions hauled out on the rocks and puffins going past at head height. Book the smallest boat that will take you.

05 ARNARFJÖRÐUR, Iceland — the Westfjords are the bit the ring road misses, so almost nobody goes. Dynjandi falls down the back of this one, the roads are gravel, and the hot pots have nobody in them.

Which fjord did you have to yourself?
""",
    ["fjords", "greenland", "norway", "newzealand", "alaska", "westfjords",
     "travelinspo", "geographyfacts", "worldfacts", "adventuretravel",
     "earthbynumbers"],
    hook_size="h-lg",
)

# ══════════════════════════════════════════════════════ SAFARIS ════

top5(
    "top5-safaris",
    "The Serengeti in<br>migration season<br>is a traffic jam.",
    "Opinion. Five parks where you are not queueing for a lion.",
    [
        ("South Luangwa", "Eastern Province, Zambia",
         "The place people come to walk rather than drive, with leopards along the river after "
         "dark and camps that shut when the rains arrive."),
        ("Mana Pools", "Mashonaland West, Zimbabwe",
         "Flood terraces, albida forest and elephants standing on their back legs to reach the "
         "pods. You can walk here unguided, which is either the appeal or the warning."),
        ("Gorongosa", "Sofala, Mozambique",
         "A park emptied by war and put back animal by animal. Come for the restoration as "
         "much as the game, and talk to the people doing it."),
        ("Ruaha", "Iringa, Tanzania",
         "Baobabs, sand rivers and serious predator country, without the vehicle convoys of "
         "the parks in the north."),
        ("Majete", "Lower Shire Valley, Malawi",
         "Another park rebuilt from almost nothing, in a country nobody thinks of for safari. "
         "Small, close to the road, and quiet enough to hear things."),
    ],
    """
The migration is extraordinary and watching it from the back of a queue of identical vehicles is not. When thirty drivers are radioing each other about the same river crossing, you are at an event, not in a wilderness.

Five parks where that does not happen. Opinion.

01 SOUTH LUANGWA, Zambia — the place to walk rather than drive, which changes the whole register of the thing: you notice tracks, dung, birds, the direction of the wind. Leopards along the river after dark are close to a given. The camps close when the rains come, and the green season has its own argument.

02 MANA POOLS, Zimbabwe — flood terraces under albida trees, with elephants standing up on their back legs to reach the pods. Famously a place you are allowed to walk unguided, which is either the reason to go or the reason not to.

03 GORONGOSA, Mozambique — a park that was emptied by a civil war and has been restored animal by animal over decades. The wildlife is coming back and the story of how is more interesting than most game drives. Talk to the people running it.

04 RUAHA, Tanzania — baobabs, sand rivers and genuinely serious predator country, several hours from anywhere, with none of the convoy behaviour of the northern circuit. The same country, a completely different experience.

05 MAJETE, Malawi — another rebuild, in a country that barely registers as a safari destination. It is small and close to the road and you will hear things you cannot see, which is most of the pleasure.

Where did you see more by seeing fewer vehicles?
""",
    ["safari", "zambia", "zimbabwe", "mozambique", "tanzania", "malawi",
     "wildlife", "travelinspo", "geographyfacts", "worldfacts", "earthbynumbers"],
)

# ══════════════════════════════════════════════════════ MUSEUMS ════

top5(
    "top5-museums",
    "The Louvre is a<br>logistics<br>exercise.",
    "Opinion. Five museums you can actually look at things in.",
    [
        ("Museo Nacional de Antropología", "Mexico City, Mexico",
         "Purpose-built and arranged by region, so the country makes sense by the time you "
         "leave. The courtyard alone justifies the entry."),
        ("MASP", "São Paulo, Brazil",
         "Paintings hung on glass easels in the middle of the room, so you walk around them and "
         "find the label on the back. Nobody else does this and everybody else should."),
        ("Rijksmuseum", "Amsterdam, Netherlands",
         "Dutch painting in a building renovated by people with judgement. Go late and walk the "
         "Gallery of Honour backwards against the flow."),
        ("Kunsthistorisches", "Vienna, Austria",
         "Habsburg collecting habits, which is why the Bruegels are all in one room. The "
         "building is part of the exhibit and the café is not a compromise."),
        ("Museum of Islamic Art", "Doha, Qatar",
         "On its own spit of land, with the light handled properly and galleries that do not "
         "set out to exhaust you. The best argument here for small."),
    ],
    """
The Louvre is a building full of extraordinary things that is very bad at letting you look at them. You queue, you follow arrows, you are moved past the famous painting at walking pace by a room of raised phones. The collection is not the problem. The experience is.

Five museums that get this right. Opinion.

01 MUSEO NACIONAL DE ANTROPOLOGÍA, Mexico City — purpose-built, generous with space, and laid out region by region so that by the time you come out the other end the country actually makes sense to you. The courtyard and its canopy are worth the ticket on their own.

02 MASP, São Paulo — the paintings hang on glass easels in the middle of the room rather than on walls, so you walk around them, see them from behind, and find the label on the back. It sounds like a gimmick and it completely changes how you look.

03 RIJKSMUSEUM, Amsterdam — Dutch painting shown in a building that was renovated by people who clearly thought hard about it. Go in the last couple of hours and walk the Gallery of Honour in the wrong direction, against everybody else.

04 KUNSTHISTORISCHES, Vienna — the product of Habsburg collecting, which is why an absurd number of the Bruegels are in a single room. The building itself is half the visit, and the café is genuinely good rather than tolerable.

05 MUSEUM OF ISLAMIC ART, Doha — sitting on its own spit of land, with light handled better than almost anywhere, and galleries that are not trying to defeat you. The strongest case on this list for a museum you can finish.

Which museum did you leave feeling better than when you arrived?
""",
    ["museums", "mexicocity", "saopaulo", "amsterdam", "vienna", "doha",
     "arttravel", "travelinspo", "citybreak", "worldfacts", "earthbynumbers"],
)

# ═══════════════════════════════════════════════════════ SKIING ════

top5(
    "top5-ski-towns",
    "Aspen is a<br>shopping centre<br>with a chairlift.",
    "Opinion. Five places to ski where lunch is not a mortgage.",
    [
        ("Myoko Kogen", "Niigata, Japan",
         "Snow in quantities that stop being funny, old onsen hotels, and trees to ski between. "
         "Nozawa takes the crowds. This does not."),
        ("Bansko", "Blagoevgrad, Bulgaria",
         "A gondola out of a real working town with the Pirin behind it, and an après scene "
         "that is cheap and unembarrassed. The lift queues are the price you pay."),
        ("Gudauri", "Mtskheta-Mtianeti, Georgia",
         "Treeless, wide open and built for touring off the back of the lifts. Drive up the "
         "military highway, stop for khinkali, let the weather decide the rest."),
        ("Jasná", "Liptov, Slovakia",
         "Both sides of a proper mountain, lifts that work, and the Tatras looking far more "
         "serious than the lift pass suggests."),
        ("Las Leñas", "Mendoza, Argentina",
         "Steep, remote, and open when the northern hemisphere is not. Marte is the lift "
         "everybody comes for and it is shut more often than it runs."),
    ],
    """
Aspen is a retail experience with snow around it. The skiing is good. So is the skiing in a hundred places where a sandwich does not cost what a lift pass should, and where the village was there before the marketing was.

Five of them. Opinion.

01 MYOKO KOGEN, Japan — snow arrives here in volumes that become slightly absurd, and the resorts are old, unpolished and built around onsen rather than boutiques. Nozawa and Hakuba absorb the foreign crowd. This sits quietly next door with the same weather.

02 BANSKO, Bulgaria — a gondola that leaves from an actual town with an actual old quarter, the Pirin mountains behind it, and an evening scene that is cheap and entirely unembarrassed about it. The morning lift queue is the trade-off and it is a real one.

03 GUDAURI, Georgia — above the treeline, wide open, and the best lift-served touring terrain on this list. You get there up the military highway, which is an experience in itself, and you eat khinkali at the end of the day. Weather closes it regularly.

04 JASNÁ, Slovakia — both faces of a serious mountain, a lift system that works properly, and the Tatras looking considerably more alpine than the price of the pass implies. The most underrated skiing in Europe, and I will take the arguments.

05 LAS LEÑAS, Argentina — steep, remote and running in the northern summer. The upper mountain is the reason to come and the lift that serves it spends a lot of the season on wind hold. Go anyway.

Which resort gave you better skiing than the one with the reputation?
""",
    ["skiing", "japow", "bansko", "gudauri", "jasna", "laslenas", "snowboarding",
     "wintertravel", "travelinspo", "worldfacts", "earthbynumbers"],
)

# ══════════════════════════════════════════════════════ TEMPLES ════

top5(
    "top5-temples",
    "Angkor at sunrise<br>is a queue.",
    "Opinion. Five temples worth standing in front of.",
    [
        ("Borobudur", "Central Java, Indonesia",
         "A stone diagram of the cosmos that you read by climbing it, terrace by terrace. Book "
         "the early entry and skip the sunrise package."),
        ("Kailasa at Ellora", "Maharashtra, India",
         "Not built but carved downwards out of the rock, courtyard, tower and all. The single "
         "most astonishing thing on this list."),
        ("Bagan", "Mandalay Region, Myanmar",
         "A plain of brick temples you cycle between, most of them empty, some of them yours "
         "for an hour. The balloons are a distraction from the version at ground level."),
        ("Preah Vihear", "Preah Vihear, Cambodia",
         "On a cliff at the top of an escarpment, approached along a causeway rather than "
         "through a gate. The approach and the drop at the end of it are the reason to come."),
        ("Tōdai-ji", "Nara, Japan",
         "A hall built to house a bronze Buddha, with deer outside and a sense of scale that "
         "photographs refuse to carry. Nara over Kyoto, every time."),
    ],
    """
Angkor Wat at sunrise is a field of people photographing a silhouette, arranged in rows, having got up at four to do it. Go at lunchtime when everybody has gone back to sleep, and go to Preah Khan and Beng Mealea instead, and you will have had a better day.

Five temples worth standing in front of. Opinion.

01 BOROBUDUR, Indonesia — a stone diagram of the Buddhist cosmos, and the way you read it is by walking up it, terrace by terrace, with the carved panels unfolding as you climb. Take the earliest ordinary entry. The sunrise package is an upsell.

02 KAILASA AT ELLORA, India — it was not built. It was carved downwards out of the hillside, courtyard, gateway, tower and all, by removing everything that was not the temple. Standing in that excavated courtyard is the most astonishing twenty minutes on this list.

03 BAGAN, Myanmar — a plain covered in brick temples that you move between on a bicycle, most of them completely empty, some of them yours alone for an hour. Everybody photographs the balloons. The ground-level version is the better one.

04 PREAH VIHEAR, Cambodia — strung along the top of an escarpment, approached up a long causeway so you arrive through a sequence rather than at a gate, and ending at a drop. Barely visited compared with Angkor, an hour's drive away.

05 TŌDAI-JI, Nara, Japan — a wooden hall built to contain a colossal bronze Buddha, with deer wandering the approach and a sense of scale that no photograph has ever carried. Nara rather than Kyoto, every single time.

Which temple did you have to yourself?
""",
    ["temples", "borobudur", "ellora", "bagan", "preahvihear", "todaiji",
     "templearchitecture", "travelinspo", "geographyfacts", "worldfacts",
     "earthbynumbers"],
)

# ══════════════════════════════════════════════════════════ TEA ════

top5(
    "top5-tea-regions",
    "Afternoon tea in<br>London is not<br>a tea region.",
    "Opinion. Five places where it is grown, picked and drunk on the spot.",
    [
        ("Wazuka", "Kyoto Prefecture, Japan",
         "Clipped green rows stacked up a river valley, a train and a bus from Kyoto, and "
         "almost nobody making the trip. Drink the gyokuro where it grows."),
        ("Nuwara Eliya", "Central Province, Sri Lanka",
         "Cool, wet and colonial in a way that is strange to sit inside. Take the train up "
         "through the estates; it is the better half of the visit."),
        ("Wuyi Mountains", "Fujian, China",
         "Rock oolong grown between sandstone cliffs, with a river to raft down between "
         "tastings. The tea is supposed to taste of the ground it came from, and it does."),
        ("Rize", "Black Sea Region, Türkiye",
         "Tea on the steepest hillsides anybody has tried to farm, cloud sitting in the "
         "valleys, and a glass handed to you everywhere you stop. Not a tourist region."),
        ("Darjeeling", "West Bengal, India",
         "Overpriced, overrun in season, and still worth it for the estates and the narrow "
         "gauge railway. Stay out of the town and up in the gardens."),
    ],
    """
Afternoon tea in a London hotel is a pastry service with a hot drink attached. It has nothing to do with tea as a crop, a place or a practice, and the leaf in the pot is usually the least considered thing on the table.

Five places where tea is grown, picked and drunk within sight of the same hillside. Opinion. Assam is not here and I will defend that.

01 WAZUKA, Japan — a valley of clipped green terraces stacked up the hillsides, a short train and bus from Kyoto, and almost no visitors despite that. Small producers will sit you down and brew gyokuro properly, which takes longer and tastes like something else entirely.

02 NUWARA ELIYA, Sri Lanka — cool, wet, and colonial in a way that is genuinely odd to sit inside. The reason to go is the train up through the estates, which is one of the great rail journeys and costs very little.

03 WUYI MOUNTAINS, China — rock oolong grown in the gaps between sandstone cliffs, which is where the mineral character is supposed to come from, and does. There is a river to raft down between tastings, which is a better structure for a day than it sounds.

04 RIZE, Türkiye — tea planted on hillsides too steep to be sensible, with cloud sitting in the valleys most mornings and a glass pressed on you at every stop. Nobody is there for tourism, which is most of the appeal.

05 DARJEELING, India — expensive, crowded in season, and still worth going to for the estates themselves and the narrow gauge railway that grinds up to them. Stay out of the town and up in the gardens.

Which growing region changed how you drink it?
""",
    ["tea", "wazuka", "nuwaraeliya", "wuyi", "rize", "darjeeling", "teaculture",
     "travelinspo", "foodtravel", "worldfacts", "earthbynumbers"],
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        path = OUT / f"{p['slug']}.json"
        path.write_text(json.dumps(p, indent=2, ensure_ascii=False))
        print(f"wrote {path.name}  {len(p['slides'])} slides  "
              f"caption {len(p['caption'])} chars  {len(p['tags'])} tags")
    print(f"{len(POSTS)} posts")


if __name__ == "__main__":
    main()
