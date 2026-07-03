# Flashcards + spaced-recall system

Read this when: building a flashcard deck, when he returns after a gap (check what's due), or when
setting up / running scheduled recall. Goal: recall at **scientifically-spaced intervals** so nothing
he learned quietly evaporates (his 2026-07-02 directive).

## 1. The interval ladder (expanding rehearsal — spacing-effect standard)

```
learn (day 0) → +1d → +3d → +7d → +16d → +35d → +60d → graduated (spot-check quarterly)
```
- **Pass** at a step → advance to the next, longer interval.
- **Stumble** → drop back one step (not to zero) and re-ground only the weak link.
- A topic *used* naturally inside a newer lesson counts as a pass (e.g. covariance used while
  learning PCA = its recall done that day). Don't double-drill what daily work already rehearsed.
- Recall right before the related next class beats an arbitrary slot — when a ladder date falls
  within ~2 days of a weekend session that builds on the topic, snap the recall to the pre-class slot.

## 2. The recall ledger (single source of truth)

Lives in the repo: **`docs/recall-ledger.md`** — one row per topic: anchor artifacts, learn date,
last recall, ladder step, next-due. Maintain it:
- **At session start:** check the ledger; if topics are due, open with a recall sprint (recall first,
  teach second — per the SKILL.md recall-sprint rules).
- **After any recall or new topic:** update the row(s) + commit with the session's other artifacts.

## 3. Deck format (SAGE FLASH-SCROLL — match the exemplar)

Exemplar: `html/2026-06-26_mcu-deployment-flashcards_s1.html`. Self-contained HTML: 3D flip card
(question front / answer back), Space to flip, `✔ Got it` / `↺ Again` marking, deck filters,
progress bar, Sage-Mode palette (same as teaching pages). Save as
`html/YYYY-MM-DD_<topic>-flashcards_<F|sN>.html`. Keep "Again" cards cycling until cleared.
**⛔ NO frog emoji/symbol on any deck (2026-07-03 directive)** — the exemplar's pulsing-frog header is
superseded: use the 🍥 Uzumaki spiral as the header mark instead.

## 4. Card-writing rules (retrieval, not recognition)

- **Front = a prompt that forces reconstruction:** "predict the sign of cov(T,C) when temp rises and
  clock throttles — and WHY", not "what is covariance?".
- **Answer = the anchor + the why:** the exact session numbers (cov = −500, λ = 2, cosine = 0.22)
  plus one line of reasoning. Numbers are his memory keys — reuse them verbatim from the notes doc.
- **Card mix per topic (aim):** ~1/3 concept-in-own-words, ~1/3 tiny numeric compute, ~1/3 decision
  boundary — including **wrong-tool cards** ("when does dot product LIE to you?").
- **Connection cards** across topics ("variance is covariance of ___ with ___") — the web, not islands.
- Voice-answerable: he often answers out loud; avoid "write the formula" fronts.
- 15–25 cards per deck max; split big topics.

## 5. Scheduled recall (cloud routines) — the automation layer

Recall must not depend on him remembering to remember. Use the **schedule skill** (scheduled remote
agents) to fire recall sessions:
- The scheduled agent's job on each firing: read `docs/recall-ledger.md` → find due topics → build or
  refresh a due-cards flashcard deck (format §3, cards per §4, sourced from the `docs/*.md` notes) →
  commit + push → notify him it's ready.
- In-chat recall (conversation sprints) still happens at session start regardless — the cloud deck is
  the "he didn't open a session today" safety net.
- **Never create/modify the cron schedule without his explicit confirmation of days + time (IST).**
  His context: works office hours, classes weekend mornings (10am–1pm IST); pre-class Saturday
  morning + a mid-week evening slot are the natural candidates. Confirm before creating.
