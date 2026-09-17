# Hunta — pricing (decided 2026-09-17, founder-approved mandate)

Currency: list in **ZAR** (home market), show USD equivalents for ZW/ZM/diaspora.
Bill monthly via **Whop**; annual = 2 months free; affiliates 30% recurring 12 months.

| Tier | ZAR/mo | ~USD | Candidates | Sends | Extras |
|---|---|---|---|---|---|
| **Demo** | R0 forever | $0 | 1 | 5/mo | full pipeline, Discord card, PDFs, 72 h purge |
| **Solo** | R299 | $17 | 3 | 100/mo | priority hunt slots |
| **Studio** | R799 | $45 | 15 | fair-use (20/day/candidate guard-rail) | white-label PDFs, brand header |
| **Sovereign** | R2 499 | $140 | unlimited | guard-rail | self-hosted, onboarding day, data never leaves |

## Why these numbers

- **Demo R0/forever** is the marketing budget. 1 candidate × 5 sends shows the whole loop
  (hunt → card → tap → send) without costing us anything: ~1 hunt-minute/day on Actions,
  cents of LLM on the customer's own key. The upgrade trigger is natural: the *second*
  candidate. "You upgrade when your bench asks" is the honest funnel.
- **Solo R299** ≈ one bundled CV-and-letter sale at prevailing coach rates (R600–R1 500).
  If Hunta doesn't produce at least one bundle a month, the customer cancels in-app and is
  right to. Price-to-value ratio ~5:1 — the minimum for word of mouth.
- **Studio R799** is priced for throughput, not seats: a CV studio that triples writer
  output earns it back in one extra order a week. White-label is the wedge — studios sell
  their brand, so the PDF header carrying *their* logo is the feature they'll pay the jump for.
- **Sovereign R2 499** undercuts one junior-recruiter-day and removes the two objections
  agencies actually have (data residency, vendor lock-in). Onboarding day included because
  self-host failures are support tickets; a guided day is cheaper.
- **USD mirrors** use ~R17.5/$; round to $17/$45/$140 for clean cards. ZW/ZM buyers pay in
  USD via Whop or sats via coinos — the memo/tenant mapping already exists in billing.py.
- **Affiliates 30% / 12 months** because coaches talk to coaches; Whop runs it natively and
  30% is the number that makes a coach mention you unprompted.

## Lines to use verbatim

- "The demo is free forever. You upgrade when your second candidate asks for it — that's
  the whole sales funnel."
- "R299 is one CV bundle at your prices. If Hunta doesn't make you one bundle a month,
  cancel in the app — no retention call, we'd rather you left happy."
- "Annual is two months free, because cashflow beats churn arithmetic."
- "Sovereign costs less than a junior recruiter's Tuesday."

## Never

- Discount in public. Discount in private for: universities, NGOs, cohorts of ≥10 coaches.
- "Cheap" as a selling point. The selling point is hours; the price is just not a barrier.
- Per-send pricing. It incentivises spam and contradicts the 20/day guard-rail story.
