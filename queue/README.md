# Post queue

Drafted carousels. Each run picks one post as **Which post a run takes** sets
out below, verifies the figures listed in its **Verify before building**
section, renders, inspects and publishes, then marks it `posted` here and
appends it to `POSTED.md`.

Every row has a draft file behind it. If a run ever finds nothing eligible —
the run order is finished, every bank row is posted or outside its window —
it picks a fresh topic as the task prompt describes and says so in its report.

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

## Cadence

Changed 13 November 2026 at Felix's request: **one post every day from
14 November to 13 December 2026, then back to one every three days** (days 1,
4, 7, 10, 13, 16, 19, 22, 25, 28 and 31 of the month, 6:36pm Auckland). The
task prompt carries the same dates, and a run that fires on an off day after
13 December stops without posting.

## Which post a run takes

Read down this list and take the first one that applies.

1. A row in **Held back** whose hold-until date is today or earlier. Its date
   has come round; treat it as queued and build it.
2. The top row in **Run order** whose status is `queued`.
3. The first row in **The bank**, reading down, whose window is `open` or
   includes today's date. Skip a dated row outside its window — it is not lost,
   it waits.

Then one check on the mix, before building: look at the last two rows of
`POSTED.md`. If both were agent-side, take the first eligible **Property** row
instead. If the last four were all property, take the first eligible **Agent**
row instead. The bank is ordered to keep the feed at two property posts to one
agent post without this check; the check is there for when rows get skipped.

If a post's figures cannot be confirmed on the day, skip it, leave its status
alone, say so in the report, and take the next eligible row. Mark a row
`posted` only when it is live.

A row marked `held` with no date that has arrived, or with a hold reason
instead of a date, is never built.

## Run order

Posts with a slot. At the daily cadence these run on consecutive days from
14 November.

| File | Expected slot | Topic | Audience | Status |
| --- | --- | --- | --- | --- |
| 01 | 2026-11-10 | The $60,000 GST test is a rolling 12 months | Agent | posted |
| 02 | 2026-11-13 | Ring-fencing: why a rental loss will not cut your salary tax | Property | posted |
| 03 | 2026-11-14 | The chattels schedule nobody set up at purchase | Property | queued |
| 04 | 2026-11-15 | Home office: the square metre rate against actual costs | Agent (re-angle) | queued |
| 05 | 2026-11-16 | The main home exclusion to the bright-line test | Property | queued |
| 07 | 2026-11-17 | Interest is 100% deductible again, and returns still get it wrong | Property | queued |
| 08 | 2026-11-18 | Vehicle claims: kilometre rates against actual costs | Agent (re-angle) | queued |
| 09 | 2026-11-19 | The intention test outlives the bright-line period | Property | queued |
| 11 | 2026-11-20 | The bach that sat empty: mixed-use asset rules | Property | queued |
| 12 | 2026-11-21 | The withholding rate on your invoices is a choice | Agent (re-angle) | queued |

"Agent (re-angle)" marks a draft written before 9 November 2026 for a tradie
and consultant audience. Its tax rules stand; its examples, caption and
hashtags have to be rewritten for a commission-paid salesperson before
building. See the audience section below. Drafts 19 onward were written for
agents from the start and need no re-angling.

## The bank

54 drafted posts with no fixed slot: 37 property, 17 agent-side.
Fifty of them were added on 13 November 2026 (files 19, 20, 22 and 23 to 69).
The first rows are dated — each waits for its window, then goes out at the
first slot inside it. The rest are in the order they should run, two property
to one agent, with neighbouring topics kept apart.

At one post a day the first 22 open rows carry the feed from 22 November to
13 December. At one every three days the rest last into April 2027.

| File | Window | Topic | Audience | Status |
| --- | --- | --- | --- | --- |
| 47 | 1–14 Jan (or last week of Apr) | GST is due on the 28th. Except twice a year. | Agent | bank |
| 48 | 15 Jan – 6 Feb | The tax on last year's rent is due 7 February | Property | bank |
| 69 | 1 Jun – 6 Jul | The rental return for the year to 31 March is due 7 July | Property | bank |
| 23 | open | A room on Airbnb: the first $65 a night is not income | Property | bank |
| 24 | open | Your rental can lose cash and still owe tax | Property | bank |
| 14 | open | Entertainment is half. Your own lunch is nothing. | Agent (re-angle) | bank |
| 25 | open | Airbnb collects 15% GST on your listing. You may get 8.5% back. | Property | bank |
| 26 | open | Fixing it is deductible. Making it better is not. | Property | bank |
| 27 | open | The champagne is half. The tea towels are whole. | Agent | bank |
| 28 | open | The legal bill for buying the rental may be deductible | Property | bank |
| 29 | open | GST registered for the Airbnb? The house is in the GST net too. | Property | bank |
| 30 | open | The suit is not deductible. Neither is the haircut. | Agent | bank |
| 31 | open | Your rent is what the tenant paid, not what landed in your account | Property | bank |
| 32 | open | Secured on the rental does not mean deductible | Property | bank |
| 33 | open | Your bank deposit is not your commission | Agent | bank |
| 34 | open | Empty between tenants. Still deductible. | Property | bank |
| 35 | open | Inherited the house? The bright-line test does not apply. | Property | bank |
| 36 | open | Year one on commission is not tax free. It is deferred. | Agent | bank |
| 37 | open | You can claim the paint. You cannot claim the weekend. | Property | bank |
| 38 | open | Under $1,000 comes off in full. Unless you bought six at once. | Property | bank |
| 22 | open | This year's provisional tax is sized on last year's income | Agent | bank |
| 39 | open | Not every body corporate levy is deductible | Property | bank |
| 40 | open | Bought off the plans? Your bright-line clock started early. | Property | bank |
| 41 | open | The drive to the office is not a business trip | Agent | bank |
| 42 | open | Renting to family at mates' rates caps your deductions | Property | bank |
| 43 | open | Flatmate in your own home? The rent is income. | Property | bank |
| 44 | open | Ninety days of logbook buys three years of claims | Agent | bank |
| 45 | open | A boarder paying $245 a week or less is not taxable income | Property | bank |
| 46 | open | The bond is not income. Until you keep some of it. | Property | bank |
| 19 | open | The marketing you pay for is deductible. If it stays paid by you. | Agent | bank |
| 49 | open | Separating? The property transfer is not a bright-line sale. | Property | bank |
| 50 | open | Moving out and renting the house? Value the chattels that week. | Property | bank |
| 51 | open | Throwing out the old carpet can be a deduction | Property | bank |
| 52 | open | Leaky building repairs can be deductible. The upgrade is not. | Property | bank |
| 16 | open | What underpaying actually costs | Agent (re-angle) | bank |
| 53 | open | Sold inside two years at a loss? The loss is locked away. | Property | bank |
| 55 | open | Bright-line tax is on the profit. Know what comes off the price. | Property | bank |
| 54 | open | Paying your partner for the admin needs sign-off first | Agent | bank |
| 56 | open | GST registered? Your rental is still outside it. | Property | bank |
| 13 | open | The depreciation you claimed comes back when you sell | Property | bank |
| 57 | open | Income protection premiums may be deductible. Life cover is not. | Agent | bank |
| 58 | open | Breaking a fixed rate on the rental loan? The fee is deductible. | Property | bank |
| 59 | open | Rental in a trust? $10,001 of profit is taxed at 39%. | Property | bank |
| 20 | open | Fees came off your commission before you saw it. Were they claimed? | Agent | bank |
| 60 | open | Moving the rental into your trust no longer restarts the clock | Property | bank |
| 62 | open | Two rentals, one at a loss. Can it offset the other? | Property | bank |
| 61 | open | Inland Revenue wrote a fact sheet for real estate. Read the list. | Agent | bank |
| 63 | open | The flat in Brisbane goes in your New Zealand return | Property | bank |
| 65 | open | The drive to your rental is deductible. With a record. | Property | bank |
| 64 | open | Sponsoring the school fair is advertising, if you do it right | Agent | bank |
| 66 | open | The insurer paid for the repair. You cannot claim it too. | Property | bank |
| 67 | open | Subdividing does not restart your bright-line clock | Property | bank |
| 15 | open | Paying GST on money you have not been paid | Agent (re-angle) | bank |
| 68 | open | Moved overseas? The Auckland rental still files here. | Property | bank |

Each draft's header says when it lands best and which other posts to keep it
away from. Where a draft says to leave some weeks between it and another post,
check `POSTED.md` and skip it for now if the other one went out in the last
fortnight.

### What is different about the 13 November drafts

They were written after checking each topic against Inland Revenue's site, and
every **Verify before building** list carries the wording found that day and
the page it was found on. That makes them better starting points. It does not
make them verified: BUILD.md's rule still applies in full, and each run
confirms every figure and rule itself before building.

Several drafts carry a **DO NOT STATE** list. Those are points the topic
invites that could not be confirmed against an Inland Revenue source. They are
as much a part of the draft as the slides.

Three things came out of that research that a run should know:

- **Post 28 (legal fees) contradicts the practice website.** IR264 allows
  legal fees on buying a rental where total legal fees for the year are $10,000
  or less. The site's rental deductions guide lists legal costs of buying under
  what cannot be claimed. Build from IR264 and say so in the report.
- **The early payment discount is not 6.7%.** It is reset each year: 4.25% for
  the 2027 income year. Post 36 uses it.
- **The bond-for-damage question is unsettled on Inland Revenue's own pages**
  (IR264 says not income; an older web page says income). Post 46 has a slide
  that is only built if that is resolved.

### Held back

Drafted, and not to be built until the condition is met.

| File | Hold until | Topic | Why held |
| --- | --- | --- | --- |
| 06 | 2027-01-07 | The 15 January provisional tax instalment | Only useful in the week or two before 15 January. Re-angle to the commission cycle when it runs. |
| 10 | 2027-03-16 | Healthy Homes work: deductible repair or capital | Written to lead into the 31 March year end, when the timing of the spend still matters. |
| 21 | Felix confirms the treatment | Commission clawed back after you have filed | **Needs Felix.** No Inland Revenue guidance was found on whether a repaid commission is deducted in the year of repayment or the earlier return is amended. The draft is written with that slide left open. Do not build until the file itself says the treatment has been sourced. |

When a dated hold comes round, build the post, re-verify its figures as usual —
a draft parked for months is more likely to have gone stale, not less — and
mark it `posted` in this table.

### Keeping the mix right

Confirmed by Felix on 9 November 2026: property leads, at roughly two posts in
three. Counting everything not yet posted — the run order, the bank and the
two dated holds — the library now stands at 43 property and 21 agent-side,
which is the ratio. The earlier property shortfall is closed.

When the bank next needs topping up, keep to the same proportion, and draft
for agents directly: IR830 and IR830A (below) are written for that audience
and are the place to start.

## The non-property audience is real estate agents, not tradies

Changed 9 November 2026. Everything on the non-property side is now written for
a self-employed real estate salesperson paid lumpy commission by an agency —
not for builders, plumbers or electricians. The task prompt carries this too.

Posts 01 to 18 were drafted for a tradie and consultant audience. Posts 19
onward were written for agents and need no re-angling. For the older ones,
re-angle a draft before building it: change the examples, the caption framing and the
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
| 12 | Schedular payment withholding rate | Good | Re-angle the examples to commission from an agency. Depends on the schedular payment question — confirm it against IR830 on the day (see below). |
| 17 | Bad debts | **Retired** | Moved to `queue/retired/`. An unpaid-customer problem; agents are paid by the agency. |
| 18 | Investment Boost | **Retired** | Moved to `queue/retired/`. Aimed at buying plant; agents buy little that qualifies. |

### Inland Revenue has published guidance for real estate salespeople

Found 13 November 2026, and worth reading before any agent-side post:

- **IR830, "Income tax and GST in the real estate industry"** (August 2026) —
  https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir800---ir899/ir830/ir830.pdf
- **IR830A, "Business expenses in the real estate industry"** (August 2026) —
  https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir800---ir899/ir830a/ir830a.pdf
- Both are linked from https://www.ird.govt.nz/topics/working-in-the-real-estate-industry

### The schedular payment question

The task prompt says it is not established that a salesperson's commission is
a schedular payment, and tells a run to resolve it against schedule 4 of the
Income Tax Act or current Inland Revenue guidance before relying on it.

IR830 is current Inland Revenue guidance, and as read on 13 November 2026 it
says: "Commissions paid to real estate salespersons/agents are schedular
payments and tax is usually withheld at a rate of 20%", and "Tax is worked out
on the GST exclusive amount." That was read through a fetch tool that returns
text in fragments, so it has not been checked word for word.

**So the position is: resolvable, not resolved for you.** A run building a
post that depends on it — 12, 20, 33 and one slide of 36 — opens IR830 itself,
confirms the sentence, and quotes it. If IR830 cannot be read on the day, or
no longer says that, the post is skipped. The earlier note in this file that
Felix confirmed the point on 9 November is not a substitute for the source.

For post 12 specifically: the rate IR830 gives is the usual one, and the
draft's point is that the rate can be chosen. Confirm the minimum and the
no-notification rate on the IR330C as the draft says, and take the standard
rate for real estate from IR830, not from the IR330C's table, which does not
name real estate.

### Retired posts

`queue/retired/` holds posts withdrawn when the audience changed. They are kept,
not deleted, because their research and sources were checked and are sound — if
the audience ever widens again, start from those files. **Never build from
`queue/retired/`.**

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
- Ledger row labels wrap at about 17 characters and will strand a word. Add
  `style="max-width:none;white-space:nowrap"` to each `.lab` and keep labels
  under about 24 characters. Every label in drafts 19 to 69 was measured in
  the brand fonts and fits on one line at that setting.
- Headline line breaks in drafts 19 to 69 were also measured in the brand
  fonts and every line fits inside the slide. That is not a reason to skip
  looking at the render. If a figure changes on the day, the line it sits on
  changes width with it.
- A ledger on a light slide puts `.fig.red` (a pale red made for dark ink) on
  paper. Keep ledgers on dark slides.
