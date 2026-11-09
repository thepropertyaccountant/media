#!/usr/bin/env python3
"""
Earth by Numbers — content set A: crazy-stats posts and Top 5s.

FORMATS
  crazy     5 slides. One country, five stats. Slide 1 is the hook stat.
  top5      6 slides. Slide 1 is a deliberately contentious hook, then ranks 1-5.
  spotlight 5 slides. Hook stat, key stats, why go, one more angle, where to go.

RULES
  Every stat slide carries a `source`. Facts come from Wikipedia or from the
  country dataset (see BUILD.md). Opinion posts say so on the hook slide.
  The final slide of every post sets handle: true.

Run:  python3 posts_a.py
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


# ══════════════════════════════════════════════ CRAZY STATS ════════

post(
    "japan-crazy", "crazy",
    [
        {"type": "hook", "title": "Japan gained<br>7,273 islands<br>without gaining<br>any land.", "size": "h-lg",
         "sub": "Five stats from the strangest recount in modern geography."},
        {"type": "bignum", "kicker": "Stat 02", "number": "6,852", "numsize": "s3", "bg": "",
         "label": "the official count from 1987 to 2023",
         "title": "Counted by hand, off a paper map.", "size": "h-sm",
         "source": "Japan Coast Guard survey, 1987. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "14,125", "numsize": "s3", "bg": "ink", "sea": True,
         "label": "the count after digital mapping in 2022",
         "title": "More than double, overnight.", "size": "h-sm",
         "source": "Geospatial Information Authority of Japan, 2023. " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "100,000+", "numsize": "s3", "bg": "",
         "label": "landmasses the computer actually detected",
         "title": "Only those with a 100 m circumference made the list.", "size": "h-sm",
         "source": "Same size threshold as the 1987 survey. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun",
         "title": "Japan's territory did not change by one square metre.",
         "sub": "Nothing was discovered. The old method merged clusters of small islands into single entries. Better maps pulled them apart.",
         "source": WIKI},
    ],
    """
Japan has 14,125 islands. For 35 years the official number was 6,852.

Nothing was discovered. No territory was gained. Not one square metre.

The 1987 figure came from the Japan Coast Guard, counting by hand off a paper map. That method quietly merged clusters of small islands into single entries, because at that resolution they looked like one thing.

In 2022 the Geospatial Information Authority recounted using digital mapping. The computer detected more than 100,000 separate landmasses. Only those with a circumference of 100 metres or more made the official list — the exact same threshold the 1987 survey used.

Result: 14,125.

Japan's territorial waters, its land area and its borders are all unchanged. The only thing that changed was the measuring instrument.

Makes you wonder which other numbers in the atlas are just old equipment.

What's a "fact" you learned at school that turned out to be measurement error?
""",
    ["japan", "geographyfacts", "islands", "didyouknow", "worldfacts", "maps",
     "cartography", "geography", "traveljapan", "earthbynumbers"],
)

post(
    "canada-crazy", "crazy",
    [
        {"type": "hook", "title": "Canada's<br>coastline is<br>longer than<br>the equator.", "size": "h-lg",
         "sub": "Six times longer. Five stats about a country with very crinkly edges."},
        {"type": "bignum", "kicker": "Stat 02", "number": "243,042", "numsize": "s3", "bg": "",
         "label": "km of coastline — the world's longest",
         "title": "The equator is 40,075 km.", "size": "h-sm",
         "source": "Statistics Canada. The CIA Factbook says 202,080 km — coastlines are famously hard to measure. " + WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "52,455", "numsize": "s3", "bg": "ink", "sea": True,
         "label": "islands",
         "title": "Baffin Island alone is larger than Spain.", "size": "h-sm",
         "source": "Statistics Canada. Baffin Island: 507,451 km². " + WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "8,890", "numsize": "s3", "bg": "",
         "label": "km of border with the United States",
         "title": "The longest international border on Earth.", "size": "h-sm",
         "source": "Statistics Canada. Next: Russia–Kazakhstan, 6,846 km. " + WIKI},
        {"type": "fact", "kicker": "Stat 05 — the myth", "bg": "sun",
         "title": "Canada does not have more lakes than the rest of the world combined.",
         "sub": "It has more lake AREA than any country, and 563 lakes bigger than 100 km². The real version is impressive enough.",
         "source": "Environment and Climate Change Canada. " + WIKI},
    ],
    """
Canada's coastline is roughly six times the length of the equator.

01 — 243,042 km of coastline, the longest of any country. The equator is 40,075 km. (The CIA Factbook says 202,080 km. Both are "right" — coastline length depends entirely on how finely you measure, which is a genuine unsolved problem in geography called the coastline paradox.)

02 — 52,455 islands. Baffin Island on its own is bigger than Spain.

03 — 8,890 km of border with the United States, the longest international border on Earth. Second place is Russia–Kazakhstan at 6,846 km.

04 — 9,984,670 km² of land, second largest country in the world, behind Russia.

05 — And the myth: Canada does NOT have more lakes than the rest of the world combined. That one is false and it is everywhere. What's true is that Canada has more lake AREA than any country, including 563 lakes larger than 100 km². The accurate version is more impressive than the myth.

Which of these five did you already know?
""",
    ["canada", "geographyfacts", "coastline", "didyouknow", "worldfacts", "maps",
     "mythbusting", "geography", "travelcanada", "earthbynumbers"],
)

post(
    "vatican-crazy", "crazy",
    [
        {"type": "hook", "title": "There is a<br>country where<br>nobody is<br>born.", "size": "h-lg",
         "sub": "Five stats about a sovereign state smaller than Central Park."},
        {"type": "bignum", "kicker": "Stat 02", "number": "0.44", "bg": "",
         "label": "square kilometres — the entire country",
         "title": "Monaco, the second-smallest, is nearly five times bigger.", "size": "h-sm",
         "source": DS + " " + WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink",
         "title": "No hospital. No maternity ward. No native-born citizens.",
         "sub": "Citizenship is granted by appointment to serve the Holy See, not by birth.",
         "source": WIKI},
        {"type": "fact", "kicker": "Stat 04", "bg": "",
         "title": "Lose the job, lose the citizenship.",
         "sub": "Vatican citizenship ends when the appointment does. Anyone left stateless automatically reverts to Italian nationality.",
         "source": WIKI},
        {"type": "bignum", "kicker": "Stat 05", "number": "~800", "numsize": "s2", "bg": "sun",
         "label": "residents in the whole country",
         "title": "Fewer people than live in a single large apartment block.", "size": "h-sm",
         "source": WIKI},
    ],
    """
Vatican City is the only country on Earth where nobody is born a citizen.

01 — The whole country is 0.44 km². It is smaller than Central Park. Monaco, the second-smallest country, is nearly five times the size.

02 — There is no hospital and no maternity ward. Nobody is born there, so nobody acquires citizenship by birth.

03 — Citizenship is granted on appointment — you get it by being given a job serving the Holy See. Cardinals, Swiss Guards, officials.

04 — When the job ends, the citizenship ends with it. Anyone who would be left stateless automatically becomes an Italian citizen instead.

05 — Around 800 people live there. Fewer than occupy a single large apartment building in most cities.

It is the only country in the world whose population is, in effect, a staff list.

Would you take a citizenship you could be fired from?
""",
    ["vatican", "vaticancity", "geographyfacts", "smallestcountry", "didyouknow",
     "worldfacts", "rome", "italy", "geography", "earthbynumbers"],
)

post(
    "zimbabwe-crazy", "crazy",
    [
        {"type": "hook", "title": "One country<br>has 16 official<br>languages.", "size": "h-lg",
         "sub": "More than anywhere else on Earth. It holds the world record."},
        {"type": "bignum", "kicker": "Stat 02", "number": "16", "bg": "",
         "label": "official languages under the 2013 constitution",
         "title": "Zimbabwe holds the Guinness World Record for it.", "size": "h-sm",
         "source": WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink",
         "title": "Sign language is one of the sixteen.",
         "sub": "Very few constitutions anywhere give a signed language equal official standing with spoken ones.",
         "source": WIKI},
        {"type": "fact", "kicker": "Stat 04", "bg": "",
         "title": "The constitution lets languages be added, never removed.",
         "sub": "New official languages can be created by an Act of Parliament. There is no mechanism to take one off the list.",
         "source": WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun",
         "title": "Three of the sixteen do almost all the work.",
         "sub": "Shona and Ndebele are what most people speak. English still runs government and business — a direct inheritance of colonial rule.",
         "source": WIKI},
    ],
    """
Zimbabwe recognises 16 official languages. No country recognises more.

Chewa. Chibarwe. English. Kalanga. Koisan. Nambya. Ndau. Ndebele. Shangani. Shona. Sign language. Sotho. Tonga. Tswana. Venda. Xhosa.

01 — All 16 were formalised in the 2013 constitution. Zimbabwe holds the Guinness World Record for the most official languages in a single country.

02 — Zimbabwean Sign Language is one of them. Very few constitutions anywhere give a signed language equal official standing alongside spoken ones.

03 — Languages can be added to the list by an Act of Parliament. There is no mechanism to remove one.

04 — For comparison: South Africa has 11 (12 since sign language was added). India lists 22 scheduled languages but only two at union level. Most countries manage one.

05 — In practice three do the work. Shona and Ndebele are what most Zimbabweans speak. English still runs government, business and schooling — a direct inheritance of colonial rule, and the uncomfortable part of the story.

Recognising a language and resourcing it are not the same thing.

How many languages are official where you live?
""",
    ["zimbabwe", "languages", "africa", "geographyfacts", "linguistics", "didyouknow",
     "worldfacts", "signlanguage", "geography", "earthbynumbers"],
)

post(
    "lesotho-crazy", "crazy",
    [
        {"type": "hook", "title": "In this country,<br>sea level<br>does not<br>exist.", "size": "h-lg",
         "sub": "Five stats from the only nation entirely above 1,000 metres."},
        {"type": "bignum", "kicker": "Stat 02", "number": "1,400m", "numsize": "s3", "bg": "", "sea": True,
         "label": "Lesotho's LOWEST point",
         "title": "The highest low point of any country on Earth.", "size": "h-sm",
         "source": "Junction of the Orange and Makhaleng rivers. " + WIKI},
        {"type": "fact", "kicker": "Stat 03", "bg": "ink",
         "title": "The only independent state lying entirely above 1,000 m.",
         "sub": "Over 80% of the country sits above 1,800 metres. There is nowhere low to go.",
         "source": WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "3,482m", "numsize": "s3", "bg": "",
         "label": "Thabana Ntlenyana, the high point",
         "title": "The highest peak in southern Africa.", "size": "h-sm",
         "source": WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun",
         "title": "One neighbour. All the way around.",
         "sub": "Lesotho is completely surrounded by South Africa — one of only three countries in the world enclosed by a single other state.",
         "source": DS + " " + WIKI},
    ],
    """
The lowest place in Lesotho is 1,400 metres above sea level.

That is higher than the summit of Ben Nevis — and it is a river junction, not a mountain.

01 — 1,400 m is the highest "lowest point" of any country on Earth. It sits where the Orange and Makhaleng rivers meet.

02 — Lesotho is the only independent state that lies entirely above 1,000 metres. There is nowhere in the country that is low.

03 — Over 80% of it sits above 1,800 metres.

04 — The high point, Thabana Ntlenyana, reaches 3,482 m. It is the highest peak in southern Africa.

05 — It has exactly one neighbour, South Africa, completely surrounding it. Only three countries in the world are enclosed by a single other state: Lesotho, San Marino and Vatican City.

Because of the altitude it snows — in southern Africa — and there is a ski field. They call it the Kingdom in the Sky, which for once is not a tourism board exaggerating.

Would you rather live somewhere with no sea level, or no mountains at all?
""",
    ["lesotho", "africa", "geographyfacts", "mountains", "travelafrica", "didyouknow",
     "worldfacts", "geography", "kingdominthesky", "earthbynumbers"],
)

post(
    "iceland-crazy", "crazy",
    [
        {"type": "hook", "title": "Iceland just<br>lost the last<br>thing that<br>made it unique.", "size": "h-md",
         "sub": "For centuries it had no mosquitoes. That ended in October 2025."},
        {"type": "fact", "kicker": "Stat 02", "bg": "",
         "title": "Iceland was essentially mosquito-free until October 2025.",
         "sub": "Greenland has them, and it is colder. Scotland and Norway have them at similar latitudes. Iceland, somehow, did not.",
         "source": WIKI},
        {"type": "bignum", "kicker": "Stat 03", "number": "~1,300", "numsize": "s3", "bg": "ink", "sea": True,
         "label": "insect species known in Iceland",
         "title": "Worldwide, over a million have been described.", "size": "h-sm",
         "source": WIKI},
        {"type": "bignum", "kicker": "Stat 04", "number": "~100%", "numsize": "s2", "bg": "",
         "label": "of Iceland's electricity is renewable",
         "title": "Roughly 70% hydro, 30% geothermal, and almost nothing else.", "size": "h-sm",
         "source": "2025 figures: 70.5% hydro, 29.4% geothermal, 0.1% fossil. " + WIKI},
        {"type": "fact", "kicker": "Stat 05", "bg": "sun",
         "title": "90% of Icelandic homes are heated by the ground itself.",
         "sub": "Geothermal district heating. It also keeps Reykjavík's pavements free of ice in winter.",
         "source": WIKI},
    ],
    """
Iceland spent centuries as one of the only inhabited places on Earth with no mosquitoes. That ended in October 2025.

01 — Iceland was essentially mosquito-free until October 2025. What made it strange is that it shouldn't have been: Greenland has mosquitoes and it is colder. Scotland and Norway have them at similar latitudes. Iceland had the standing water, the summer and the wildlife to feed on.

02 — Only around 1,300 insect species are known in Iceland. Over a million have been described worldwide. Midges, though, are everywhere — Mývatn literally translates as "midge lake".

03 — Effectively 100% of Iceland's electricity is renewable. In 2025: 70.5% hydro, 29.4% geothermal, 0.1% fossil fuel.

04 — About 85% of ALL energy used in the country — not just electricity — comes from domestic renewable sources.

05 — 90% of Icelandic homes are heated geothermally, straight from the ground. The same system keeps Reykjavík's pavements clear of ice in winter.

A country that runs on heat from under its own feet, and has just inherited the world's most annoying insect.

Does this change whether you'd go?
""",
    ["iceland", "travelIceland", "geographyfacts", "reykjavik", "geothermal",
     "renewableenergy", "didyouknow", "worldfacts", "geography", "earthbynumbers"],
)


def main():
    OUT.mkdir(exist_ok=True)
    for p in POSTS:
        (OUT / f"{p['slug']}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False))
    print(f"wrote {len(POSTS)} posts")
    for p in POSTS:
        print(f"  {p['slug']:20s} {p['kind']:9s} {len(p['slides'])} slides")


if __name__ == "__main__":
    main()
