# Post queue

Drafted carousels, in order. Each run takes the top item whose status is
`queued`, verifies the figures listed in its **Verify before building** section,
renders, inspects and publishes, then marks it `posted` here and appends it to
`POSTED.md`.

A row marked `held` is **skipped** — it is drafted but deliberately parked until
its date is closer. Do not take a held item just because it is next in the
table. A row marked `to write` has no draft file yet; if a run reaches one,
treat the queue as empty for that run and pick a fresh topic as the task prompt
describes.

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

| File | Expected slot | Topic | Audience | Status |
| --- | --- | --- | --- | --- |
| 01 | 2026-11-10 | The $60,000 GST test is a rolling 12 months | Contractor | queued |
| 02 | 2026-11-13 | Ring-fencing: why a rental loss will not cut your salary tax | Property | queued |
| 03 | 2026-11-16 | The chattels schedule nobody set up at purchase | Property | queued |
| 04 | 2026-11-19 | Home office: the square metre rate against actual costs | Contractor | queued |
| 05 | 2026-11-22 | The main home exclusion to the bright-line test | Property | queued |
| 07 | 2026-11-25 | Interest is 100% deductible again, and returns still get it wrong | Property | queued |
| 08 | 2026-11-28 | Vehicle claims: kilometre rates against actual costs | Contractor | queued |
| 09 | 2026-12-01 | The intention test outlives the bright-line period | Property | queued |
| 11 | 2026-12-04 | The bach that sat empty: mixed-use asset rules | Property | queued |
| 12 | 2026-12-07 | The withholding rate on your invoices is a choice | Contractor | queued |
| 13 | — | The depreciation you claimed comes back when you sell | Property | bank |

Property leads 7 of the 10 drafted, which holds the two-in-three balance.

A row marked `bank` has no slot. It has no seasonal hook, so it can go out any
time a slot needs filling — a held post not yet due, a topic that turns out to
be stale on the day, a figure that cannot be confirmed. Take it in preference to
inventing a topic from scratch. Post 13 pairs with post 03: 03 sells the
chattels deduction, 13 shows the bill at the other end, so leave some weeks
between them rather than running them back to back.

### Held back

Both are fully drafted and ready; only their timing was wrong at this cadence.
Move each back to `queued` when its slot comes round, and re-verify its figures
then as usual — a draft parked for months is more likely to have gone stale, not
less.

| File | Hold until | Topic | Why held |
| --- | --- | --- | --- |
| 06 | 2027-01-07 | The 15 January provisional tax instalment | Only useful in the week or two before 15 January. At the three-day cadence it would have gone out 25 November, seven weeks early. |
| 10 | 2027-03-16 | Healthy Homes work: deductible repair or capital | Written to lead into the 31 March year end, when the timing of the spend still matters. Would have gone out 7 December. |

The task runs every three days, at 6:36pm Auckland, on days 1, 4, 7, 10, 13, 16,
19, 22, 25, 28 and 31 of each month. Cron restarts that count at the 1st, so the
gap across a month boundary is one to four days rather than three. The dates
above assume no run is skipped.

**The slotted queue runs out after 7 December 2026**, with post 13 in the bank
behind it, so the first run with nothing drafted is around 13 December. After
that a run falls through to picking its own topic and says so in its report —
the designed fallback, not a failure, but a deliberately chosen topic is better.
Topping up in early December avoids the question.

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
