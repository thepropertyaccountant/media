# Post queue

Ten drafted carousels, in order. Each run takes the top unposted item, verifies
the figures listed in its **Verify before building** section, renders, inspects
and publishes, then marks it posted here and appends it to `POSTED.md`.

## Why these are drafted and not pre-rendered

The slide copy, caption and structure in each file are finished — they are not
outlines. What is deliberately *not* baked in is any tax figure that has been
rendered into a JPEG, because BUILD.md's one hard rule is that every figure is
verified against Inland Revenue **in the run that uses it**. A pre-rendered
image cannot be re-verified; it can only be re-rendered. Drafting to this point
removes the slow part of the work (choosing the topic, finding the angle,
writing the copy, writing the caption) and keeps the part that protects the
practice.

Each file flags its figures as `VERIFY:` with the value last known good and the
Inland Revenue page to check it on. If a figure has moved, change the number in
the slide copy and the caption before rendering. If a figure cannot be
confirmed against an Inland Revenue source, drop that slide and that caption
sentence, or skip the post and take the next one — do not publish it unverified.

## Run order

| # | Suggested date | Topic | Audience | Status |
| --- | --- | --- | --- | --- |
| 01 | 2026-11-16 | The $60,000 GST test is a rolling 12 months | Contractor | queued |
| 02 | 2026-11-23 | Ring-fencing: why a rental loss will not cut your salary tax | Property | queued |
| 03 | 2026-11-30 | The chattels schedule nobody set up at purchase | Property | queued |
| 04 | 2026-12-07 | Home office: the square metre rate against actual costs | Contractor | queued |
| 05 | 2026-12-14 | The main home exclusion to the bright-line test | Property | queued |
| 06 | 2026-12-21 | The 15 January provisional tax instalment | Contractor | queued |
| 07 | 2027-01-11 | Interest is 100% deductible again, and returns still get it wrong | Property | queued |
| 08 | 2027-01-18 | Vehicle claims: kilometre rates against actual costs | Contractor | queued |
| 09 | 2027-01-25 | The intention test outlives the bright-line period | Property | queued |
| 10 | 2027-02-01 | Healthy Homes work: deductible repair or capital | Property | queued |

Property leads 6 of 10, which holds the two-weeks-in-three balance.

## Build notes learned from earlier runs

- Force line breaks in headlines with `<br>` and then **look at the render** —
  the browser will still re-wrap a line that is too wide and strand a single
  word. Both headline faults found so far were this.
- `.tag.red` and `.dark .tag` have equal CSS specificity, so `.tag.red` wins on
  a dark slide and renders dark red on dark ink. Put red tags on light slides only.
- `.verdict` is a fixed red and has no `max-width`, so it overflows past about
  22 characters. Keep it short, and only use it for genuinely bad news.
- `.big` is always green. Only use it for a number the reader gains.
- The repo is shared with an unrelated project that force-pushes. If `git push`
  is rejected as non-fast-forward while `git ls-remote` shows your commit's
  parent as the tip, it is that race — fetch and push again rather than forcing.
