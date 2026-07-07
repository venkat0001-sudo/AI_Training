---
title: Atlas migration log — 2026-07-07 (the full-vault revamp)
date: 2026-07-07
sessions: []
concepts: [meta]
type: ledger
up: "[[HOME]]"
recap: "What changed when the vault went Obsidian-Atlas: 20 concept atoms extracted, trap-log made embeddable, MOCs + HOME built, hub extended. Read this to navigate the revamped notes."
---

# 🧭 Atlas migration log — 2026-07-07

> The vault was restructured through the `obsidian-notes` skill (v2). **No scroll lost a word of
> narrative** — atoms were *extracted*, scrolls were *re-plumbed* (front-matter + pointer links).
> Anchor numbers were lifted verbatim; nothing was re-authored.

## How to navigate now (the 30-second tour)

1. **Start at [[HOME]]** — MOCs, the dated countdown, the live boards.
2. **Concepts live in `concepts/` atoms** — one file per concept, named by its web.json slug.
   Each atom: recap-claim → chain → anchor numbers (`^anchor`) → numpy twin → typed links →
   decision boundary → embedded traps → depth layers → project brick → formula → flashcards.
3. **Scrolls (dated files) are unchanged journey records** — each now points to its atoms up top.
4. **Follow `builds-on::` links DOWN to re-ground** (covariance → σ → mean); follow `feeds::` UP
   to see what a concept unlocks. Every link carries its why.
5. **[[trap-log]]** is now one-trap-per-line with block IDs — atoms EMBED traps, the trap lives once.

## What was created

**20 concept atoms** (`docs/concepts/`): vectors · variance-sigma · normal-distribution ·
covariance · eigenvectors · pca · calculus · gradient-descent · bayes · ml-taxonomy ·
probability *(stub)* · regression · cross-entropy · ml-workflow · cross-validation · metrics ·
ml-pipeline · thermal-project · mcu-deployment *(stub)* · entropy *(stub, from the test-drive)*.

**Navigation** (`docs/maps/` + root): [[HOME]] · [[MOC-foundation-math]] ·
[[MOC-m1-ml-fundamentals]] · [[MOC-thermal-project]]. M2–M6 MOCs get created at each module's
first session.

## What was changed (and why)

- **trap-log.md: table → one-line-per-trap.** Obsidian cannot block-reference table rows; each
  trap now carries `^id` so atoms embed instead of copy. +2 traps recovered from the LA scroll's
  journey sections (`^vec-column`, `^cov-meanproduct`). Content verbatim otherwise.
- **Every doc gained `up:`** (Breadcrumbs/Dataview hierarchy) and slug-true `concepts:` lists.
- **Bayes scroll:** the five display-name wikilinks (`[[Bayes' Theorem]]` etc.) were repointed to
  real slugs via aliases — they would have spawned five orphan notes. Header 🐸 → 🍥 (standing
  2026-07-03 directive).
- **web.json:** +2 nodes (`cross-entropy`, `metrics`), +6 edges — the vault and the hub graph
  stay mirrors (46 nodes · 54 edges).
- **build_hub.py:** now scans `docs/concepts/` and `docs/maps/` (atoms self-report their slug);
  hub rebuilt: **50 artifacts, zero warnings**.
- **Skill sharpened to v2** after the entropy test-drive + research (evergreen-notes/CS231n/LYT):
  declarative recap-claims, no-links-in-fences rule, heading-freeze + block-ID preference,
  systems-concept variant for M3–M6, `twin-page::`/`lab::`/`video::`/`paper::` link types,
  seeds-pending sections in MOCs, source-of-record rule for HTML-only and chat-only concepts.

## Evidence (measured after pass 6)

- Wikilinks in vault: **~6 → 440**
- Typed links with whys (`builds-on::`, `feeds::`, …): **0 → 129**
- Spaced-repetition flashcards embedded in atoms: **0 → 56** (plugin-ready, `#flashcards/<slug>`)
- Per-pass commits: skill+entropy test-drive → pass 1 (LA, 6 atoms) → pass 2 (calculus) →
  pass 3 (bayes) → pass 4 (s2 + web.json) → pass 5 (s1 + metrics node) → pass 6 (nav + hub).
  `git log --oneline` shows the full trail; each pass is independently revertible.

## Adversarial review — 2026-07-07 (post-migration audit, all fixes applied)

Full audit run as if reviewing a stranger's work. **Verified clean:** diff integrity (every
deletion accounted for — zero narrative loss), all wikilinks/heading anchors/block embeds resolve
(0 broken), 0 alias collisions, all 16 numpy twins execute without failure, atom
statuses/lanes/edges mirror web.json exactly. **Defects found and fixed (9):**

1. Hub parser kept surrounding quotes on YAML-quoted recaps → literal `\"` on hub cards. Fixed in `build_hub.py`.
2. **Regression I introduced:** wikilinking the recall-ledger topics broke the hub's due-parser
   (`\|` fragmented the cells; due count 6 → 0). Parser now splits on unescaped `|` only and
   renders link display text. Due=6 restored.
3. Eigenvectors twin comment claimed `[0.447, 0.894]`; numpy prints the sign-flipped vector. Comment now says ± (sign is free — the atom's own lesson).
4. Normal-distribution twin printed −1.27 (2-dp rounding) vs the scroll's −1.26σ anchor. Now prints −1.265 with the anchor tie-in.
5. Cross-validation twin hit a log-scale warning at perfect fits — ε added.
6. `trained-by::` was used in regression.md but missing from the skill vocabulary — added to the skill (it will recur for neural nets/LSTM).
7. MOC-foundation claimed a bare `[[z-score]]` "alias-resolves" — it does not (aliases don't resolve bare links); rephrased with the correct `[[normal-distribution|z-score]]` form.
8. web.json edge why had an unbalanced paren. Fixed.
9. Entropy atom's chain used an `&nbsp;` indentation hack — normalized to the standard two-chain-lines form.

**Accepted-by-design (reviewed, not changed):** anchors exist in both atom and scroll (atom =
distilled home, scroll = journey; embeds source from atoms); depth layers use heading links
rather than block IDs (§-numbered headings are stable; the heading-freeze rule is in force).

## Known debts (deliberate, tracked)

- **Stubs:** [[entropy]] (resume before s4, 11 Jul — T-minus-3 map) · [[probability]] (own worked
  doc) · [[mcu-deployment]] (budget-numbers treatment).
- **Seeds pending:** [[trees-svm]] + [[gini-impurity]] (s3 notes never written — the biggest gap),
  [[ensembles]] (s4), [[kmeans]] (s5), [[naive-bayes]], [[kl-divergence]], [[attention]].
- **In-body first-mention linking inside the two giant scrolls** (s1 99KB, LA 62KB) was done at
  header/section level, not every paragraph — deepen opportunistically when a scroll is next touched.
- **Plugins to install** for full effect: Dataview (boards), Breadcrumbs (trails), Spaced
  Repetition (the 56 cards), Templater, Obsidian Git, Strange New Worlds, Note Refactor.
- Consolidated docs + formula cards owed at the M1 boundary (19 Jul).
