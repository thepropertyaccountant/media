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
fc-cache -f
```

Check `fc-list | grep -i archivo` before rendering. Slides rendered without the
brand fonts fall back to something generic and must not be posted.

**Look at every rendered slide with the Read tool before posting.** Text
overflow and collisions are invisible until you look at the image.

### Design rules

1080 × 1350 (4:5, Instagram's tallest feed ratio). Do not edit the CSS in
`build.py` — add content, not styles.

- Alternate light (`bg: ""`) and dark (`bg: "ink"`) backgrounds for rhythm.
  Never three of the same in a row. `sun` (amber) is for one punch slide per
  post, usually the last beat.
- Slide 1 is the hook: one claim, as large as it fits, plus a one-line twist.
- One idea per slide. Two sentences of explanation means it is two slides.
- Numbers are the brand. If a slide has a figure, make the figure the largest
  thing on it (`bignum`).
- Put the source on any slide carrying a figure.

Slide types: `hook`, `ledger`, `bignum`, `rank`, `items`, `fact`, `card`,
`signoff`. See the builders in `build.py` for each one's fields.

---

## 6. Monetisation notes

Selling the account outright breaches Meta's terms. Brand partnerships and an
info-product are the realistic routes, and both need real followers first.
Nothing in this pipeline should compromise accuracy to chase a number.
