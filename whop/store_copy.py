"""Whop product copy + FAQ. Numbers come from hunta code (BILLING, PLANS, facts) — never hand-typed."""
import ast
import sys
from pathlib import Path

HUNTA = Path("/home/user/audit/hunta")
sys.path.insert(0, str(HUNTA / "press"))
import facts  # noqa: E402

B, F = facts.billing(), facts.facts()
src = (HUNTA / "hunta" / "billing.py").read_text()
PLANS = ast.literal_eval(src[src.index("PLANS: dict[str, dict] = ") + 25:src.index("DEFAULT_PLAN")].strip())
_d = (HUNTA / "hunta" / "demo.py").read_text()
CAPS = ast.literal_eval(_d[_d.index("CAPS = ") + 7:].split("\n")[0])
S, ST = PLANS["solo"], PLANS["studio"]
BOARDS = f"{F['boards_default']} job boards by default ({F['boards_registered']} supported) across South Africa, Zimbabwe and Zambia"

FAQ_FULL = f"""
FAQ

Does anything send without me?
No. Every application arrives in Discord as a card with the job, match reason and PDFs. Nothing goes out until you tap Approve.

Which jobs does it search?
{BOARDS}. One employer is never contacted twice within 30 days, and daily caps keep volume sane.

Can I try it before paying?
Yes. The free demo pack runs the whole pipeline on 1 candidate, capped at {CAPS['total_drafts']} drafts and {CAPS['total_sends']} sends per rolling {CAPS['days']} days: {B['site']}

Why is the price in US dollars?
Whop bills in USD. The plans are set to the rand value; {B['fx_note']}.

No card?
Pay by Lightning ({B['lightning']}, name and tier in the memo) or Mukuru / EFT to {B['mukuru'].split(': ')[1].split(' ·')[0]} (reference: your tenant id). Your licence is issued once payment lands.

What happens after checkout?
You are sent to a short setup page. Your job seekers get a private intake link; they never need to join your Discord.

Can I pay yearly?
Yes. Annual prepay is 25% off: Solo {B['solo_annual']}, Studio {B['studio_annual']}. Email us to arrange it.

Questions?
{B['support']}"""

SHORT_FAQ = f"""
FAQ
Does anything send without me? No. Each application is a Discord card; nothing goes out until you tap Approve.
Can I try first? Yes, free demo pack (1 candidate, {CAPS['total_drafts']} drafts, {CAPS['total_sends']} sends / {CAPS['days']} days): {B['site']}
Why USD? Whop bills in dollars; plans are set to the rand value (R16.31 per $1).
No card? Lightning ({B['lightning']}) or Mukuru / EFT ({B['mukuru'].split(': ')[1].split(' ·')[0]}, ref = tenant id).
Full FAQ in the Hunta forum. Questions: {B['support']}"""
FAQ = SHORT_FAQ

PRODUCTS = {
    "prod_lh6Mq2wTIHqog": {
        "title": "Hunta Solo",
        "headline": f"{S['candidates']} candidates, {S['sends_month']} sends a month. Drafted nightly, sent after your yes.",
        "description": f"""For individual career coaches and job agents.

Hunta hunts vacancies nightly, scores them against each CV, drafts a tailored CV and cover letter, and sends you a one-tap approval card in Discord.

Solo includes:
- {S['candidates']} candidates
- {S['sends_month']} sends a month
- Priority slots
- {BOARDS}
- Human approval on every send

{B['solo_price']} billed every 30 days, or {B['solo_annual']} prepaid. Cancel any time.
""" + FAQ,
    },
    "prod_S3yLSyR1X98sE": {
        "title": "Hunta Studio",
        "headline": f"{ST['candidates']} candidates, fair-use sends, PDFs branded as your agency.",
        "description": f"""For coaching practices and small recruitment agencies.

Studio includes:
- {ST['candidates']} candidates
- Fair-use sends
- White-label CV and cover-letter PDFs
- LLM fallback chain: one provider outage won't stop the run
- {BOARDS}
- Human approval on every send

{B['studio_price']} billed every 30 days, or {B['studio_annual']} prepaid. Cancel any time.
""" + FAQ,
    },
    "prod_YinMTkuhgU2Xv": {
        "title": "Hunta Sovereign",
        "headline": "Self-hosted, unlimited candidates and sends. Your data stays on your servers.",
        "description": f"""For agencies and institutions that need the pipeline on their own infrastructure.

Sovereign includes:
- Self-hosted Docker deployment
- Unlimited candidates and sends
- Signed offline licence
- An onboarding day with us
- {BOARDS}
- Human approval on every send
- Lapsed licence = read-only, never bricked or deleted

{B['sovereign_price']} billed every 30 days. Cancel any time.
""" + FAQ,
    },
}

for _p in PRODUCTS.values():
    assert len(_p["headline"]) <= 80, _p["headline"]
    assert len(_p["description"]) <= 1500, (_p["title"], len(_p["description"]))

if __name__ == "__main__":
    for pid, p in PRODUCTS.items():
        print("=" * 70, pid, p["title"], "\nHEADLINE:", p["headline"], "\n", p["description"][:600])
