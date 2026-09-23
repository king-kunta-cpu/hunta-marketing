# Hunta — pricing (decided 2026-09-17, founder-approved mandate)

Currency: **ZAR everywhere** (home market is ZA; ZW/ZM pay sats via Lightning or the ZAR-equivalent rate).
Bill monthly via **Whop**; annual = 25% off (the cash lever that funds the build); affiliates 30% recurring 12 months.

| Tier | ZAR/mo | ~USD | Candidates | Sends | Extras |
|---|---|---|---|---|---|
| **Demo** | R0 forever | $0 | 1 | 5/mo | full pipeline, Discord card, PDFs, 72 h purge |
| **Solo** | R4,999 | ~$278 | 3 | 100/mo | priority hunt slots |
| **Studio** | R9,999 | ~$555 | 15 | fair-use (20/day/candidate guard-rail) | white-label PDFs, brand header |
| **Sovereign** | R15,000 | ~$833 | unlimited | guard-rail | self-hosted, onboarding day, data never leaves |

## Why these numbers

- **Demo R0/forever** is the marketing budget. 1 candidate × 5 sends shows the whole loop
  (hunt → card → tap → send) without costing us anything: ~1 hunt-minute/day on Actions,
  cents of LLM on the customer's own key. The upgrade trigger is natural: the *second*
  candidate. "You upgrade when your bench asks" is the honest funnel.
- **Solo R4,999** ≈ two-to-three bundled CV-and-letter sales at prevailing coach rates
  (R600–R1 500), plus the 8–12 h of hunt-and-rewrite it deletes. If Hunta doesn't earn its keep
  the customer cancels in-app and is right to. Annual R45,000 (25% off) is the prepay close —
  one deal ≈ six months of runway, cash now.
- **Studio R9,999** is priced for throughput, not seats: a CV studio that triples writer
  output earns it back in one extra order a week. White-label is the wedge — studios sell
  their brand, so the PDF header carrying *their* logo is the feature they'll pay the jump for.
- **Sovereign R15,000** undercuts one junior-recruiter-day and removes the two objections
  agencies actually have (data residency, vendor lock-in). Onboarding day included because
  self-host failures are support tickets; a guided day is cheaper.
- **Prices are ZAR, set 2026-09-23 by the service-first decision memo: Solo R4,999 / Studio R9,999 / Sovereign R15,000 monthly; annual 25% off.** ZW/ZM buyers pay sats via coinos or the ZAR-equivalent rate.
  Billing is enforced fail-closed (`hunta billing grant`); the Whop webhook path exists in billing.py.
- **Affiliates 30% / 12 months** because coaches talk to coaches; Whop runs it natively and
  30% is the number that makes a coach mention you unprompted.

## Lines to use verbatim

- "The demo is free forever. You upgrade when your second candidate asks for it — that's
  the whole sales funnel."
- "Solo is R4,999 a month — two or three CV bundles at your rates, and the ten hours of typing is gone.
  If it doesn't earn its keep, cancel in the app, no retention call."
- "Annual prepay is R45,000 — three months free, one payment, provisioned same day."
- "Sovereign costs less than a junior recruiter's Tuesday."

## Never

- Discount in public. Discount in private for: universities, NGOs, cohorts of ≥10 coaches.
- "Cheap" as a selling point. The selling point is hours; the price is just not a barrier.
- Per-send pricing. It incentivises spam and contradicts the 20/day guard-rail story.
