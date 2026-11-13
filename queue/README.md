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
| 01 | 2026-11-10 | The $60,000 GST test is a rolling 12 months | Agent | posted |
| 02 | 2026-11-13 | Ring-fencing: why a rental loss will not cut your salary tax | Property | posted |
| 03 | 2026-11-16 | The chattels schedule nobody set up at purchase | Property | queued |
| 04 | 2026-11-19 | Home office: the square metre rate against actual costs | Contractor | queued |
| 05 | 2026-11-22 | The main home exclusion to the bright-line test | Property | queued |
| 07 | 2026-11-25 | Interest is 100% deductible again, and returns still get it wrong | Property | queued |
| 08 | 2026-11-28 | Vehicle claims: kilometre rates against actual costs | Contractor | queued |
| 09 | 2026-12-01 | The intention test outlives the bright-line period | Property | queued |
| 11 | 2026-12-04 | The bach that sat empty: mixed-use asset rules | Property | queued |
| 12 | 2026-12-07 | The withholding rate on your invoices is a choice | Contractor | queued |
| 13 | — | The depreciation you claimed comes back when you sell | Property | bank |
| 14 | — | Entertainment is half. Your own lunch is nothing. | Contractor | bank |
| 15 | — | Paying GST on money you have not been paid | Contractor | bank |
| 16 | — | What underpaying actually costs | Contractor | bank |
| 19 | — | Marketing and advertising an agent funds themselves | Agent | to write |
| 20 | — | Franchise, desk and administration fees paid to the agency | Agent | to write |
| 21 | — | Commission clawback when a deal falls over | Agent | to write |
| 22 | — | Smoothing provisional tax across a big year and a thin one | Agent | to write |

### Keeping the mix right

Of the 10 slotted posts, 6 are property and 4 are agent-side. The bank holds
1 property and 3 agent-side, plus 4 agent topics still to write.

**Do not work through the bank in order.** A run of agent posts back to back
is two weeks of a property-led feed talking to one half of the audience, and it
reads as a change of direction rather than a run of good posts. Take a banked
agent post when a slot needs filling and the posts around it are property, and
otherwise space them. If several slots need filling at once, draft property
topics rather than emptying the bank.

### The property shortfall — standing requirement

Confirmed by Felix on 9 November 2026: the two-in-three property ratio stays.
That makes the library lopsided, and the arithmetic is worth stating plainly.

| | Count |
| --- | --- |
| Agent-side posts once 19 to 22 are written | 12 |
| Property posts needed to run those at 2:1 | 24 |
| Property posts held (including the 2 posted) | 10 |
| **Property shortfall** | **14** |

Posting 2 property to every 1 agent consumes property twice as fast. At the
current library the property side runs dry after roughly 15 posts — about 45
days at one post every three days — and strands around 7 agent posts with
nothing to interleave them against.

**So property topics are the drafting priority from here, not agent ones.**
Write agent posts 19 to 22 when there is room, but a run that has spare capacity
should be drafting property. Do not let the ratio slip by default: if a slot
comes up and the only thing drafted is agent-side, that is the signal the
property bank needs filling, not a reason to post agent content twice running.

Rough deployment notes, where a post has one:

- 14 (entertainment) — late November or December, and around vendor entertaining.
- 16 (interest and penalties) — just after a provisional tax instalment date.
- 15 — no hook, use any time, and see the fit note below before building.

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

**The slotted queue runs out after 7 December 2026**, with six posts in the bank
behind it, so nothing is drafted only from about 25 December. After
that a run falls through to picking its own topic and says so in its report —
the designed fallback, not a failure, but a deliberately chosen topic is better.
Topping up in early December avoids the question.

## The non-property audience is real estate agents, not tradies

Changed 9 November 2026. Everything on the non-property side is now written for
a self-employed real estate salesperson paid lumpy commission by an agency —
not for builders, plumbers or electricians. The task prompt carries this too.

Posts 01 to 18 were drafted for a tradie and consultant audience. Re-angle a
draft before building it: change the examples, the caption framing and the
hashtags. The tax rules in the **Verify before building** sections are unchanged
and still apply.

How the drafted non-property posts fare against the new audience:

| # | Post | Fit | What it needs |
| --- | --- | --- | --- |
| 08 | Vehicle: kilometre rates | Strongest | Barely needs changing. Driving between viewings is the job. Swap the examples to open homes and appraisals. |
| 01 | $60,000 GST rolling 12 months | Strong | Better for agents than tradies — one big settlement can cross it mid-year. Rewrite slide 5's ledger as commission on two settlements. |
| 06 | 15 January provisional tax | Strong | A strong year drives next year's instalments. Re-angle to the commission cycle. Still held until 2027-01-07. |
| 14 | Entertainment and your own lunch | Strong | Client lunches, open home catering, closing gifts. Swap the Christmas-do framing for vendor entertaining. |
| 16 | Interest and penalties | Good | Lands well after a big commission year. Minor reframing. |
| 04 | Home office | Good | Agents work from home between viewings. Minor reframing. |
| 15 | GST payments or invoice basis | Marginal | Built on being paid late on 30-day terms. Agents are paid by the agency on settlement, so the pain is weaker. Rework around settlement timing straddling a GST period, or leave it. |
| 12 | Schedular payment withholding rate | Good | Unblocked — Felix confirmed on 9 Nov 2026 that schedular payments do apply to real estate. Re-angle the examples to commission from an agency. Still pin down the correct activity row and rate (see below). |
| 17 | Bad debts | **Retired** | Moved to `queue/retired/`. An unpaid-customer problem; agents are paid by the agency. |
| 18 | Investment Boost | **Retired** | Moved to `queue/retired/`. Aimed at buying plant; agents buy little that qualifies. |

### Post 12: resolved, with one detail still to pin down

**Felix confirmed on 9 November 2026 that schedular payments do apply to real
estate salespeople.** That is his professional judgement as the Chartered
Accountant whose name goes on the post, and it settles whether the topic
applies. Build post 12 for this audience.

What it does not settle is which activity row the commission sits under and
therefore what the standard rate is. Real estate is not named on the IR330C,
and the row that most likely covers it — "Commissions to insurance agents and
sub-agents and salespeople" — is grammatically ambiguous about whether
"salespeople" stands alone. The form says its list is not exhaustive and points
to schedule 4 of the Income Tax Act 2007.

So before building: confirm the activity row and rate that apply to a real
estate salesperson, against schedule 4 or current IRD guidance, or ask Felix.
Do not print a rate for real estate on a slide on the strength of the
applicability confirmation alone — that confirmed the topic, not the number.

### Retired posts

`queue/retired/` holds posts withdrawn when the audience changed. They are kept,
not deleted, because their research and sources were checked and are sound — if
the audience ever widens again, start from those files. **Never build from
`queue/retired/`.**

### Agent topics to write (19 to 22)

Rows 19 to 22 in the run order are topics only, with no draft files behind them.
They were chosen because they have no tradie equivalent in the queue and fit a
commission-paid salesperson directly. Each still needs the full treatment: an
angle with a trap in it, slide copy, a caption, and a **Verify before building**
list naming every figure and the Inland Revenue page to confirm it on.

- **19 — Marketing and advertising an agent funds themselves.** Where the agent
  rather than the vendor carries the cost of photography, staging, signage and
  listing promotion, and when that is deductible. Check how a vendor-paid
  recharge is treated, and the GST side.
- **20 — Franchise, desk and administration fees paid to the agency.** The
  standing deductions taken out of commission before it reaches the agent, and
  whether they are being claimed at all. Check the treatment of a franchise fee
  against an ordinary service fee.
- **21 — Commission clawback when a deal falls over.** What happens when
  commission already returned as income is repaid in a later year. Check whether
  it is a deduction in the year of repayment or an amendment to the earlier
  return — this is the trap and it must be sourced properly.
- **22 — Smoothing provisional tax across a big year and a thin one.** The
  structural problem of commission income: this year's instalments are sized on
  last year's result. Check the estimation option and any other mechanism before
  naming one, and keep it distinct from held post 06.

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
