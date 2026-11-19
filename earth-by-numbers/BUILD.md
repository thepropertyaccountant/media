# Earth by Numbers — how this account runs

Faceless Instagram account, `@earth_by_numbers`, Windsor.ai Instagram account id
**17841435841293051**. Do not confuse it with 17841464947553410, which is The
Property Accountant and must never receive this content.

Everything lives in this repo because **every scheduled run starts in a fresh
workspace with no memory of the last one**. `queue.json` is the only state.

---

## 1. Posting (runs twice a day, automatic)

```bash
git clone --depth 1 https://github.com/thepropertyaccountant/media /home/claude/media
cd /home/claude/media/earth-by-numbers
```

Read `queue.json`. Take the **first** entry where `posted_at` is null **and**
`approved` is true. If there is no such entry, stop and say so — never invent a
post, never post an unapproved one.

Confirm every image URL serves before publishing. A single 404 fails the post:

```bash
for u in <the entry's image urls>; do
  curl -sS -o /dev/null -w "%{http_code} %{content_type}\n" "$u"
done
```

Expect `200 image/jpeg` for all of them.

Publish with the Windsor.ai connector:

```
execute_action(
  connector = "instagram",
  action    = "create_carousel_post",     # 2-10 images
  account   = "17841435841293051",
  params    = { "image_urls": [...in slide order...], "caption": "..." }
)
```

Then set `posted_at` (UTC ISO timestamp) and `media_id` on that entry, and push:

```bash
git add queue.json
git -c user.email="fm.advisory.services@gmail.com" \
    -c user.name="Earth by Numbers" commit -m "Posted <slug>"
git push origin main
```

**Push the state back every time.** If the push fails the next run will post the
same thing twice.

### Slots

`11:31` and `23:31` UTC. Chosen to hit US evening and Europe midday while
avoiding the 14:00–17:00 UTC window where scheduled runs get delayed. Retune
from real data once about three weeks of Instagram insights exist — Windsor can
read them with `get_data` on the `instagram` connector.

---

## 2. Content (weekly top-up, needs approval)

Target: keep **at least 28 approved, unposted** entries — two weeks of buffer.
At 2/day the queue burns 14 a week, so a normal week means writing ~14.

Write new posts into `content/<slug>.json`, then:

```bash
python3 posts_<x>.py      # if you added a generator file
python3 build.py --all    # renders content/*.json -> img/*.jpg
python3 make_queue.py     # appends as approved=false
python3 make_covers.py --all   # turns each new slide 1 into a poster cover
```

New posts land **unapproved**. The posting task skips them. Felix approves by
saying so, and then `approved` is flipped to true and pushed. That is the whole
approval gate — it does not depend on tool permissions.

---

## 3. The three formats

| Kind | Slides | Shape |
|---|---|---|
| `crazy` | 5 | One country, five stats. Slide 1 is the hook stat. |
| `top5` | 6 | A contentious hook, then ranks 1–5. |
| `spotlight` | 5 | Hook stat, key stats, why go, one more angle, where to go. |

Every post's **last slide** sets `handle: true` so `@earth_by_numbers` appears.
`make_queue.py` interleaves the kinds so the grid alternates.

**Top 5s must pick a fight on slide 1.** A famous place left out, or called
overrated. That is the engagement mechanism — people comment to defend the thing
you excluded. Always label the list as opinion on that slide so it is never read
as measured fact.

### Captions

Hook line that works alone (Instagram truncates), then the numbered points,
then a question that is genuinely answerable. Hashtags last, 9–11 of them.
Limit is 2200 characters.

### Voice

Direct and plain. No exclamation marks, no emoji, no "unlock" or "ultimate" or
"hidden gem" as filler. Comfortable saying something the reader will not enjoy.
Willing to say a famous place is overrated and say why. Never breathless.

---

## 4. The rule that matters most

**Every figure must be verified in the run that uses it. Never state a number
from memory.**

Research source: **Wikipedia** (Felix's instruction), plus the country dataset
below. Where a primary source is already cited in the slide (Statistics Canada,
the Geospatial Information Authority of Japan), keep it — it is stronger than
Wikipedia and Wikipedia cites it anyway.

This is not boilerplate. Three claims were caught and corrected while building
the first batch, each of which would have been published as fact:

- **Japan has 6,852 islands** — superseded. A 2023 digital recount by the
  Geospatial Information Authority returned 14,125.
- **Canada has more lakes than the rest of the world combined** — false. It has
  more lake *area* than any country. Different claim.
- **Iceland has no mosquitoes** — expired. True for centuries, not since
  October 2025.

A viral post with a wrong number gets screenshotted and quote-tweeted, and the
account never recovers. If a figure cannot be confirmed, cut it and use another
angle.

Prefer **stable** facts — capitals, land areas, borders, elevations,
superlatives — over volatile ones like population. Posts sit in the queue for
up to two weeks before going out, and stable facts do not rot.

### The dataset

`https://raw.githubusercontent.com/mledoze/countries/master/countries.json`
(CC-BY-SA). Reachable from the workspace; most other APIs are not.

Gives exact `capital`, `area`, `borders`, `languages`, `currencies`,
`landlocked`, `unMember`. **No population** — get that from Wikipedia if needed,
and round it hard.

Compute superlatives from it rather than recalling them. It is how the China
border count was caught: the dataset lists 16 neighbours for China, but two are
Hong Kong and Macau, which are China's own territories. The correct claim is 14
sovereign neighbours, tied with Russia.

---

## 5. Rendering

```bash
pip install --break-system-packages playwright pillow   # if missing
python3 build.py content/<slug>.json      # one post
python3 build.py --all                    # everything
```

Fonts are **not** installed by default in a fresh workspace. Google Fonts' CDN is
unreachable; the GitHub raw host works:

```bash
mkdir -p ~/.fonts && cd ~/.fonts
B=https://raw.githubusercontent.com/google/fonts/main/ofl
curl -sSL -o ArchivoBlack.ttf  "$B/archivoblack/ArchivoBlack-Regular.ttf"
curl -sSL -o SpaceGrotesk.ttf  "$B/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf"
curl -sSL -o SpaceMono-Regular.ttf "$B/spacemono/SpaceMono-Regular.ttf"
curl -sSL -o SpaceMono-Bold.ttf    "$B/spacemono/SpaceMono-Bold.ttf"
curl -sSL -o InstrumentSerif-Regular.ttf "$B/instrumentserif/InstrumentSerif-Regular.ttf"
curl -sSL -o Archivo.ttf           "$B/archivo/Archivo%5Bwdth,wght%5D.ttf"
fc-cache -f
```

The last two are the cover fonts (section 7) — Instrument Serif for the hook
and the stat numerals, Archivo for the kicker and labels. They are not optional:
without them every cover falls back to a generic serif and the whole set stops
looking like one account.

Check `fc-list | grep -iE 'archivo|instrument|space'` before rendering. Slides
rendered without the brand fonts fall back to something generic and must not be
posted.

**Look at every rendered slide with the Read tool before posting.** Text
overflow and collisions are invisible until you look at the image.

### Design rules

1080 × 1350 (4:5, Instagram's tallest feed ratio). Do not edit the CSS in
`build.py` — add content, not styles. Cover styles are the one exception and
they live in `cover.py`, appended to `CSS` rather than edited into it. See
section 7.

- Alternate light (`bg: ""`) and dark (`bg: "ink"`) backgrounds for rhythm.
  Never three of the same in a row. `sun` (amber) is for one punch slide per
  post, usually the last beat.
- Slide 1 is the hook: one claim, as large as it fits, plus a one-line twist.
- One idea per slide. Two sentences of explanation means it is two slides.
- Numbers are the brand. If a slide has a figure, make the figure the largest
  thing on it (`bignum`).
- Put the source on any slide carrying a figure.

Slide types: `poster`, `hook`, `ledger`, `bignum`, `rank`, `items`, `fact`,
`card`, `signoff`. See the builders in `build.py` for each one's fields —
`poster` lives in `cover.py`.

**Slide 1 of every post is a `poster`.** `hook` is the old cover and is kept
only so `make_covers.py --force` can re-derive a cover from the original
wording. Do not write a new post with a `hook` slide 1 expecting it to ship.

---

## 6. Monetisation notes

Selling the account outright breaches Meta's terms. Brand partnerships and an
info-product are the realistic routes, and both need real followers first.
Nothing in this pipeline should compromise accuracy to chase a number.


---

## 7. Covers

Felix asked for this on 19 November 2026: every post's cover should set the
scene with an illustration, with the contentious headline still doing the
talking. `cover.py` builds it, `make_covers.py` converts posts to it.

### What a cover is

Top 920px is a flat-vector landscape, built as 4–6 stacked planes whose
lightness steps monotonically back to front, so depth reads with no outlines.
Bottom 430px is a dark type band: kicker and region label, then the hook in
Instrument Serif, a hairline, and three stats. `01` and a short rule sit at the
illustration's top-left, the brand mark top-right.

The docstring at the top of `cover.py` is the full specification, including why
the band is 430px rather than the brief's 340px and why label sizes are scaled
up from it. Read that before changing any of it.

### Converting

```bash
python3 make_covers.py --list         # what is still on the old hook cover
python3 make_covers.py --all          # convert every unposted post
python3 make_covers.py --limit 12     # convert the next 12 only
python3 make_covers.py --force        # re-derive covers after changing cover.py
python3 build.py --all                # then re-render
```

**This is resumable and has no progress file.** A post whose slide 1 is `hook`
has not been converted; one whose slide 1 is `poster` has. So a run that stops
part way — on usage, on anything — is picked up by the next run with `--limit`,
and nothing can get out of step with the repo. `--all` only touches unposted
posts; posts already on Instagram keep the covers they went out with.

`--force` rebuilds from each cover's stored `was_hook`, never from the cover
it is replacing, so it is idempotent however many times it runs.

### What a human chooses, and what is derived

Per post, exactly three choices, in the `POSTERS` table in `make_covers.py`:
the archetype, the palette anchors, and the one human-scale element. Colours
come from the subject — Atlantic greys for Nazaré, laterite reds for Rwanda,
basalt and ash for Yasur — never from a shared palette.

Everything else is read out of the post's own slides. The hook is slide 1's
existing title. The stats come from the post's `bignum` slides (crazy) or its
`ledger` rows (spotlight). **No figure is ever typed into a cover.**

Where a `crazy` post carries fewer than three figures of its own, the gap is
filled from the mledoze/countries dataset — the source section 4 sanctions —
and never with a value the post already states. Two fills are blocked by hand
in `FILL_SKIP`, because the dataset contradicts the post's own headline: Nauru
has no capital city, which is that post's whole hook, and South Africa has
three. **The dataset's `borders` field is never used as a fill**, for the China
reason recorded in section 4: it counts Hong Kong and Macau, and a figure that
needs a caveat cannot live in a three-word stat column.

### Decisions already taken — do not quietly reverse them

- **The hook is the display line**, not the place name. The place name is the
  kicker above it. A 26px kicker cannot carry a fight, and the fight is the
  point of slide 1.
- **Top 5 covers illustrate the No. 1 pick** (Felix, 19 Nov 2026, choosing it
  over an adapted variant). It does move the reveal onto the cover; the
  contentious line still runs in the display serif so slide 1 still picks the
  fight. Top 5 stat columns state no figures at all — a Top 5 is opinion, and
  section 4's rule stands.
- **The old `sub` twist line is not on the cover.** There is no room for it
  beside two lines of display serif and the stat grid, so **it has to be the
  caption's second paragraph instead** — the Portugal pattern: hook, twist,
  then the body. This is not automatic and it is not safe to assume. When the
  first 70 posts were converted it was already true of 52 of them and silently
  false for the other 18, whose twist would have been published nowhere at
  all. `make_covers.py` now prints a list of any post in that state at the end
  of every run; it is not a warning to scroll past. After fixing a caption in
  `content/`, rebuild queue.json's copy with `make_queue.full_caption(spec)` —
  queue.json holds the caption *plus the hashtag block*, and that is the copy
  the posting task actually publishes, so editing the content file alone
  publishes a caption with no hashtags.
- **The hook is sized to two lines, never three.** `disp_size()` explains why:
  three lines only fits when every stat label is short, and a cover that clips
  its headline on the one post with long labels is not a system.

### Adding an archetype

`ARCHETYPES` in `cover.py` maps a name to a function returning the
illustration's SVG. Keep to the depth rules in that file's docstring: flat
fills only, monotonic lightness, one haze band per junction, a lit face and a
shadow face on every major form, exactly one human-scale element.

Two traps, both already paid for:

- **Do not take water from the plane ramp.** The ramp's middle planes carry the
  warm family, so a sea drawn from `planes[1]` comes out sand-coloured and the
  headlands read as boxes in a desert. Derive water from the sky instead, as
  `a_coast_cliff` and `a_fjord` do.
- **Nothing is drawn with a gradient except sky, haze and light sources.** The
  volcano had an ash plume; as a flat shape it reads as a chimney stack on the
  summit, and there is no honest way to make it a gradient. It was removed.

**Look at every cover with the Read tool before pushing.** A contact sheet of
all of them at 252px is enough to catch a broken archetype; the ones that look
wrong get opened full size. That is how the coast, fjord and volcano faults
above were all found.
