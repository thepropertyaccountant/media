# How to build and publish a carousel

Everything needed to produce an Instagram carousel for The Property Accountant
that matches the practice website. Follow this exactly — the point is that every
post looks like it came from the same place.

## 1. Install the brand fonts

The workspace has no brand fonts by default. Google Fonts' CDN is not reachable,
but the GitHub raw host is:

```bash
mkdir -p ~/.fonts && cd ~/.fonts
curl -sSL -o BricolageGrotesque.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz%2Cwdth%2Cwght%5D.ttf"
curl -sSL -o InstrumentSans.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentsans/InstrumentSans%5Bwdth%2Cwght%5D.ttf"
curl -sSL -o IBMPlexMono-Regular.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/IBMPlexMono-Regular.ttf"
curl -sSL -o IBMPlexMono-Medium.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/IBMPlexMono-Medium.ttf"
curl -sSL -o InstrumentSerif-Regular.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentserif/InstrumentSerif-Regular.ttf"
fc-cache -f
```

Check with `fc-list | grep -iE "bricolage|instrument serif"` before rendering.
Slides rendered without these fonts fall back to something generic and must
not be posted. **Instrument Serif is the cover headline** (section 9) and a
missing font fails silently into a generic fallback that you will not see
until you open the image.

## 2. Build the slides

Copy `template/carousel-template.html` and replace the slide contents. Do not
change the CSS. The design rules:

- 1080 × 1350 px, which is 4:5 — Instagram's tallest allowed feed ratio.
- Six to eight slides. Fewer than six feels thin; more than eight loses people.
- Alternate `class="slide"` (light) and `class="slide dark"` (ink) for rhythm.
  Never run three of the same background in a row.
- Slide 1 is the hook: one claim, large, plus a one-line twist underneath.
- The middle slides carry one idea each. If a slide needs two sentences of
  explanation, it is two slides.
- Use the `.rows` ledger block for anything with figures or dates. Put the
  number in the right-hand column, in mono, and colour a bad number `.red`.
- The last slide is always the sign-off: practice name, what it does, the
  Instagram handle, and the "general information, not advice" line. Copy it
  from the template unchanged.

Colour meaning is not decorative, so keep it honest: emerald `--green` /
`--lift` for what the reader keeps or gains, red `--owed` for what they owe or
lose. Never colour a neutral figure red for emphasis.

## 2b. Where the topic comes from

`queue/` holds the next posts already drafted — slide copy, caption and, for
each one, a **Verify before building** list naming every figure it asserts and
the Inland Revenue page to confirm it on. Take the top item whose status in
`queue/README.md` is `queued`, verify its figures as section 7 below requires,
then build from its draft. Mark it `posted` in `queue/README.md` when done.

Nothing in `queue/` is pre-verified. A drafted figure is a starting point and a
pointer to its source, never a number to copy onto a slide unchecked.

## 2c. Put the cover on slide 1

Every post's slide 1 is an illustrated cover. Do this AFTER the carousel HTML
is finished and every figure on it is verified, and BEFORE rendering:

```bash
python3 covers/make_covers.py apply <your-carousel>.html <draft-slug>
```

`<draft-slug>` is the draft's filename without `.md`, e.g.
`44-the-ninety-day-logbook`. The step swaps slide 1 for its cover, appends the
cover stylesheet, and stores the original slide 1 inside the cover so it can
always be rebuilt or reverted. Section 9 is the full specification.

It refuses to run on a slug with no design row, and it never invents a figure.
If it stops, read what it says rather than working around it.

## 3. Render

```bash
python3 template/shoot.py <your-carousel>.html <prefix> <slide-count>
```

Writes `<prefix>-01.png` … and so on. Then look at every slide with the Read
tool before going further. Things that go wrong and are invisible until you
look: text overflowing its slide, a headline colliding with the element below
it, an element stretching full-width when it should hug its content.

## 4. Convert to JPEG

Instagram's API takes JPEG only, 8 MB maximum.

```python
from PIL import Image
import glob
for f in sorted(glob.glob('<prefix>-*.png')):
    Image.open(f).convert('RGB').save(f.replace('.png','.jpg'), 'JPEG', quality=92, optimize=True)
```

## 5. Push to this repo

Name files `YYYY-MM-DD-topic-NN.jpg` so nothing overwrites an earlier post.

```bash
cd /home/claude/media
git fetch --depth 1 origin main && git reset --hard origin/main
cp /path/to/*.jpg .
git add -A
git -c user.email="fm.advisory.services@gmail.com" -c user.name="The Property Accountant" commit -m "Add <topic> carousel"
git push origin main
```

Then confirm each URL serves before posting — a 404 fails the whole post:

```bash
curl -sS -o /dev/null -w "%{http_code} %{content_type}\n" \
  "https://raw.githubusercontent.com/thepropertyaccountant/media/main/<file>.jpg"
```

Expect `200 image/jpeg`.

## 6. Publish

Windsor.ai connector, Instagram account `17841464947553410`:

```
execute_action(
  connector = "instagram",
  action    = "create_carousel_post",
  account   = "17841464947553410",
  params    = { "image_urls": [ ...raw URLs in slide order... ], "caption": "..." }
)
```

Caption limit is 2200 characters. Structure: a hook line that works alone,
because Instagram truncates the rest; then the explanation in short paragraphs;
then what to do about it; then the "general information, not advice" line; then
eight to twelve hashtags mixing NZ property and Auckland accounting terms.

## 7. Log it

Append the topic to `POSTED.md` so later runs do not repeat it.

## Voice

Same as the website. Direct, plain, no exclamation marks, no "unlock" or
"maximise" or "game-changer", no emoji. Comfortable telling the reader something
they will not enjoy hearing. Write to one person who has this problem right now,
not to an audience.

## The rule that matters most

Every figure, threshold, date and rule must be verified against current Inland
Revenue guidance — `ird.govt.nz` or `taxtechnical.ird.govt.nz` — by searching
for it in the run that uses it. Never state a tax figure from memory, and never
carry one forward from an older post without rechecking. If a figure cannot be
confirmed against an Inland Revenue source, leave it out and pick a different
angle. A wrong number published under a Chartered Accountant's name is worse
than no post at all.

## 8. Refresh the dashboard

Felix watches the account on one dashboard, "The Property Accountant Instagram
Content": https://claude.ai/artifact/DDDC4p98ciRaGVjeZV8vJv

Its content list is a file, `dashboard/queue.json`, built from `POSTED.md` and
`queue/README.md`. After the post is logged and pushed (and after any change to
the queue), rebuild it and hand the new copy to the dashboard:

1. `python3 dashboard/snapshot.py` — rewrites `dashboard/queue.json`. Commit and
   push it with the log.
2. Read the dashboard's current record of the file: ArtifactData `get`, the
   dashboard's url, collection `datasets`, doc_id `queue`. Note its `version`
   and the old file address in `source.url` (`/_blob/<id>`).
3. Upload the new file: the Artifact tool with the dashboard's `url`,
   `file_path` set to `dashboard/queue.json`, and `asset: true`. It returns a
   new `/_blob/<id>` address.
4. Point the dashboard at it: ArtifactData `update` on `datasets`/`queue`, with
   `if_version` from step 2 and data
   `{"source": {"url": "<new address>"}, "updated": {"at": "<UTC now, ISO>", "by": "Posting task"}, "edit": {"via": "claude", "at": "<UTC now, ISO>"}}`.
   Use `update`, not `set`, and change nothing else in that record.
5. Remove the old file: the Artifact tool, `action: "delete"`, the dashboard's
   `url`, and `path` set to the old id (the 32 characters after `/_blob/`).
   Only after step 4 has succeeded.

Do not write to anything else in the dashboard — not its page, not its other
data sources. Never create a second dashboard: there is one, and its address is
above. If any of these steps fails, say so in the report and leave it; the post
itself is done and must not be redone or undone because of the dashboard.

## 9. Covers

Felix asked for this on 19 November 2026: slide 1 of every carousel is an
illustrated cover carrying the post's own headline, so the feed draws people
in instead of opening on plain type. `covers/cover.py` draws it,
`covers/make_covers.py` applies it, `covers/preview.py` and
`covers/measure.py` check it.

**It is a cosmetic change to slide 1 and nothing else.** It re-presents words
that already exist and have already been verified. It does not generate
claims, it does not reword anything, and it is not a place a figure can enter
a post. If a change to it would alter what the account asserts rather than
how slide 1 looks, it is out of scope — stop and ask Felix.

### What a cover is

Top 900px is a flat-vector illustration built from the post's subject — a
rental house, a set of keys, a calendar, a car, an open ledger, a till roll, a
front door, a survey plan. Bottom 450px is a dark type band: a kicker, the
post's headline in Instrument Serif, a hairline, then up to three figures. The
brand mark sits at the illustration's top-left.

The docstring at the top of `cover.py` is the full specification, including
why the band is 450px rather than the brief's 340px and why label sizes are
scaled up from it. Read it before changing any of it.

### Where the words come from — the rule that matters most here

**Nothing on a cover is typed into it.** The headline and the figures are read
back out of the finished carousel's own HTML, by `apply`, after the run has
verified every figure against Inland Revenue. The cover is a view of
validated content, never a source of it. If a value cannot be derived the
build stops and names the slug; it does not guess and does not fall back to
something plausible.

**This is why covers are derived at render time and not from the queue draft,
which is where @earth_by_numbers derives them.** That account's content files
hold finished slides. This account's queue holds drafts whose figures are
explicitly unverified — `queue/README.md` calls a drafted figure "a starting
point and a pointer to its source, never a number to copy onto a slide
unchecked". On 19 November 2026 draft 08 had petrol and diesel both at
$1.20/$0.37 when Inland Revenue quotes diesel at $1.30/$0.38, and the run
corrected it. A cover built from that draft would now be contradicting slide 3
of its own post in the profile grid. Deriving after verification makes that
impossible by construction. **Do not move this earlier in the pipeline.**

The one line not read out of a verified slide is the kicker, which is the
draft's own title, or a shorter label in the design row. A kicker carrying an
ASCII digit is rejected, because it is the one place a figure could sneak on
to a cover unchecked. That guard has already caught three of this repo's own
kickers ("15 January", "7 February", "7 July") — tax dates are exactly the
sort of figure that has to come off a verified slide.

### What a human chooses, and what is derived

Per post, three choices, in the `COVERS` table in `make_covers.py`: the
archetype, the palette anchors, and the one human-scale element. Colours come
from the subject — asphalt greys for vehicle posts, survey blues for
bright-line, ledger greens for GST — never from a house palette. Everything
else is derived.

### Running it

```bash
python3 covers/make_covers.py                      # drafts with no design row
python3 covers/make_covers.py --twist              # the sub-line report, below
python3 covers/make_covers.py apply <html> <slug>  # put the cover on slide 1
python3 covers/make_covers.py apply <html> <slug> --force   # re-derive
python3 covers/make_covers.py revert <html>        # put the original back
python3 covers/preview.py                          # contact sheets of all covers
python3 covers/measure.py <page.html>              # the browser assertions
```

**Both levels are resumable and neither has a progress file.** A draft with a
`COVERS` row is designed; one without is not, and `make_covers.py` with no
arguments prints what is outstanding. A slide 1 with class `cover` has been
converted; a plain one has not. So a run that stops part way — on usage, on
anything — is picked up by the next one, and nothing can drift out of step
with the repo.

`--force` always rebuilds from the original slide stored in the cover's
`<template class="was-hook">`, never from the cover it is replacing, so it is
idempotent however many times it runs. It also means the change is
reversible: `revert` puts the original slide 1 back, and the result is
byte-identical to the pre-cover file apart from the appended stylesheet.

**Only unposted posts get covers.** Instagram copies images at publish time,
so re-rendering a posted cover changes nothing live and only makes the repo
disagree with the real feed. `make_covers.py` reads `queue/README.md` and
excludes anything marked `posted`.

### The sub line under the old headline

The cover has no room for the `sub` that sat under slide 1's headline, and
there are 17 unposted drafts whose sub is not carried anywhere in their
caption sketch. Felix's instruction, 19 November 2026: **do not edit the
drafts — the run carries the sub into the caption it writes.**

That works here and would not on @earth_by_numbers, because this repo stores
no published caption. Each run composes the caption fresh from the draft's
`## Caption` section, so the fix belongs in the run, not in the draft. The
task prompt carries this instruction too. `make_covers.py --twist` prints the
17; it is not a list to scroll past.

### Adding or changing an archetype

`ARCHETYPES` in `cover.py` maps a name to a function returning the SVG. Keep
to the depth rules in that file's docstring: flat fills only, lightness
stepping monotonically front to back, a lit face and a shadow face on every
major form, gradients only for the background wash and light sources, exactly
one human-scale element.

Decisions already taken — do not quietly reverse them:

- **`backdrop()` takes a style and has no default.** One shared backdrop is
  how 32 of 70 covers on the other account came out with the same silhouette:
  invisible post by post, obviously a template in the three-wide profile grid.
- **`lightsource()` takes a chance, currently 0.50.** Roughly half the covers
  have no light source. A glow on all 60 is its own kind of template.
- **No archetype carries more than about seven of the sixty.** The first pass
  put a whole house on thirteen; `front_door` and `site_plan` were added and
  the assignments spread to break that up. Check the spread after adding
  posts.
- **The headline's `<br>` breaks are dropped on the cover.** They were
  measured for the original slide at h-xl and force three, four and five line
  headlines at the cover's size. Only the line breaking changes; not one word
  does.
- **The warm bend in `expand()` is light (0.17/0.11/0.05).** At 0.30/0.22/0.10
  every ramp collapsed toward the same beige-olive and sixty covers read as
  one house palette, which is the fault the per-post anchors exist to prevent.
- **Fewer stat columns, never an invented figure.** `fit_stats()` drops to two
  columns or one rather than ellipsise a value, and a cover with no derivable
  figure gets no stat row at all. A value that will not fit is dropped whole:
  half a figure is a wrong one.

### Verify like this, not by eye

1. `python3 covers/preview.py` writes a contact sheet of every cover at 252px
   to the scratch directory, and **you look at it with the Read tool**. That is
   what caught the ledger rendering as a pyramid, the folder as a featureless
   crate, the till roll as a tower block with lit windows, and thirteen
   identical houses.
2. `python3 covers/measure.py <page>` then asserts in the browser what looking
   cannot tell you: that no band overflows, no stat value is ellipsised, no
   headline runs past two lines, and every slide is 1080x1350.
3. After re-rendering, `git status` should show only the slide-1 files you
   expect. If other slides changed, the render is not deterministic.
4. No caption, headline or slide 2+ should appear in the diff at all. If one
   does, that is the scope rule being broken, and it gets backed out.

**Preview output is never published and never committed.** It is written
outside the repo, and because a draft has no verified figures it fills the
stat row from drafted ones purely to get something of the right shape into the
band. Its job is to check illustrations and typography, nothing else.
