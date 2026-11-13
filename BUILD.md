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
fc-cache -f
```

Check with `fc-list | grep -i bricolage` before rendering. Slides rendered
without these fonts fall back to something generic and must not be posted.

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
