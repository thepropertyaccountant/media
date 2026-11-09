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

| # | Expected slot | Topic | Audience | Status |
| --- | --- | --- | --- | --- |
| 01 | 2026-11-10 | The $60,000 GST test is a rolling 12 months | Contractor | queued |
| 02 | 2026-11-13 | Ring-fencing: why a rental loss will not cut your salary tax | Property | queued |
| 03 | 2026-11-16 | The chattels schedule nobody set up at purchase | Property | queued |
| 04 | 2026-11-19 | Home office: the square metre rate against actual costs | Contractor | queued |
| 05 | 2026-11-22 | The main home exclusion to the bright-line test | Property | queued |
| 06 | 2026-11-25 | The 15 January provisional tax instalment | Contractor | queued |
| 07 | 2026-11-28 | Interest is 100% deductible again, and returns still get it wrong | Property | queued |
| 08 | 2026-12-01 | Vehicle claims: kilometre rates against actual costs | Contractor | queued |
| 09 | 2026-12-04 | The intention test outlives the bright-line period | Property | queued |
| 10 | 2026-12-07 | Healthy Homes work: deductible repair or capital | Property | queued |

Property leads 6 of 10, which holds the two-in-three balance.

The task runs every three days, at 6:36pm Auckland, on days 1, 4, 7, 10, 13, 16,
19, 22, 25, 28 and 31 of each month. Cron restarts that count at the 1st, so the
gap across a month boundary is one to four days rather than three. The dates
above assume no run is skipped.

**At this cadence the queue is exhausted around 7 December 2026.** Two of the ten
were written for a date that no longer matches: post 06 (the 15 January
provisional tax instalment) now lands in late November, far too early to be
useful, and post 10 (Healthy Homes, written to lead into the 31 March year end)
lands in early December. Both should be held back and re-slotted nearer their
dates, with something else taking their place in the run order — or re-angled so
the timing hook is dropped. Worth deciding before the queue reaches them.

## Build notes learned from earlier runs

- Force line breaks in headlines with `<br>` and then **look at the render** —
  the browser will still re-wrap a line that is too wide and strand a single
  word. Both headline faults found so far were this.
- `.tag.red` and `.dark .tag` have equal CSS specificity, so `.tag.red` wins on
  a dark slide and renders dark red on dark ink. Put red tags on light slides only.
- `.verdict` is a fixed red and has no `max-width`, so it overflows past about
  22 characters. Keep it short, and only use it for genuinely bad news.
- `.big` is always green. Only use it for a number the reader gains.
- The repo is shared with an unrelated project that force-pushes, which leaves
  the local branch ref in a state where `git push origin main` is rejected as
  non-fast-forward even though `git ls-remote` shows your commit's parent as the
  tip. Pushing the explicit refspec works and is a fast-forward:
  `git push origin HEAD:refs/heads/main`. Never force-push here — the other
  project's commits are in the same history.
