# Markdown notes recipe (the "cakewalk + journey-recall" standard)

Read this **whenever saving learnings to a `.md` notes doc** (`docs/YYYY-MM-DD_<topic>_<F|sN>.md`).
His 2026-07-02 directive upgraded the notes standard. The bar, in his words:

> "If I show these notes to a new person, he should be able to understand it like a cakewalk. Very,
> very simple... And notes are for future purpose — we forget things very soon; once we see the notes
> we should be able to recall the journey we have gone through and the examples we have learned from."

## The two-reader test (every notes doc must pass BOTH)

1. **The stranger test (cakewalk):** someone with zero context — not an engineer, not from his course —
   can read top-to-bottom and follow every step. Model: the upGrad TA session notes he loves
   (e.g. `Linear_Algebra_Foundations_resources/...Notes-Session-3.docx`). Their winning pattern:
   - "**Why Are We Learning This?**" cold open before anything is defined
   - one-line plain definitions: *"A vector is simply an ordered collection of numbers."*
   - a tiny example **immediately** after every claim: `[10, 20]` — never abstract symbols first
   - a "**Real World Example:**" block, then an "**ML Connection**" block, for every concept
   - short sentences, generous whitespace, zero unexplained jargon
2. **The future-him test (journey recall):** six months later, skimming the doc re-lights the whole
   learning *journey* — including what he got WRONG. The misconception→correction beats are the
   strongest recall hooks; never sand them off into a clean textbook summary.

## Required skeleton

```
# Title — plain words
> One-liner: what this doc holds + which session/tag (_F = Foundation extension, _sN = session N)

## 0. Revision ladder        ← recall-don't-re-read: numbered one-line rungs, each → §link
## Why are we learning this? ← 2-3 lines, the problem this topic solves (stranger-friendly)
## Per-concept sections, EACH built as:
   1. Plain-words definition (one line, simple)
   2. The tiny numeric example — the EXACT numbers from the session, fully worked
   2b. ⭐ THE NUMPY TWIN (mandatory, 2026-07-04): a fenced ```python block right under the
       numbers — ONE Jupyter-cell-ready snippet (imports included, ~5–15 lines). **If the
       concept has a shape, the cell MUST PLOT it** (labeled matplotlib: arrows/bell/cloud/
       bowl) and print the anchor numbers as the check; numbers-only is allowed only when
       there is no honest shape. He runs the cell, SEES the concept — the visual anchor is
       the learning mechanism; the code is how he learns to BUILD it.
   3. The analogies that were actually used: 😄 funny · 🔧 SSD · 🌍 generic
   4. The journey: "The trap I fell into..." misconception + its correction (verbatim spirit)
   5. The formula — LAST, every symbol decoded in plain language
   6. Decision boundary: ✅ use when / ❌ NOT when (unmissable)
   7. ML destination: where in the course/pipeline this cashes out + why it matters
## Key Takeaways             ← cluster end: punchy bullet list
## Formula sheet             ← compact, one block, symbols decoded
```

Not every concept needs every block — but **2 (numbers), 2b (numpy twin), 6 (boundary), 7
(destination) are never optional**, and 4 (the journey) is mandatory whenever a misconception
actually happened in session.

## Front-matter + the consolidated lifecycle (2026-07-04 — the hub reads these)

- **Every notes doc starts with YAML front-matter** (Obsidian-native; `tools/build_hub.py` scans it):
  `title`, `date`, `sessions: [F|s1..s32]`, `concepts: [slugs matching tools/web.json]`,
  `type: notes|consolidated|map|ledger|primer|research`, `recap:` one-line reactivation hook (shows on hub cards).
- **Consolidated docs:** when a concept arc completes (e.g. linear algebra after s5), distill its
  chunks into `docs/00_<concept>-consolidated.md` (`00_` sorts first; `type: consolidated` pins it as
  the arc's cover scroll in the hub). It must END with a **one-page formula card** (one screen,
  printable: every formula of the arc, symbols decoded).
- After saving any artifact: update `tools/web.json`, run `python3 tools/build_hub.py`, commit
  `index.html` alongside. A trap corrected in-session also gets one line in `docs/trap-log.md`.

## Hard rules

- **Numbers are the memory anchors.** Preserve every worked example with the *exact* values computed
  in session (`[5,4,1]`, cov = −500, λ1 = 98.58%...). Changing the numbers breaks his recall path.
- **Narrative over summary.** Capture the FLOW of how understanding was built (misconception →
  vote-intuition → 4-case table → formula), not just the destination. Big is fine; a summary can be
  distilled later. He said this explicitly.
- **Simple beats complete.** If a sentence needs a comma-chain, split it. One idea per line.
- **Every table/diagram carries a one-line "how to read this."**
- **Analogies ride along.** The funny/SSD/generic examples used in the lesson go INTO the notes —
  they're retrieval cues, not decoration.
- Notes and their HTML twin must agree on numbers and analogies (same anchors, two formats).
- Commit + push notes to the repo (his standing artifact rule).
