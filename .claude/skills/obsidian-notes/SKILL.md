---
name: obsidian-notes
description: >-
  Generate or convert study notes into Obsidian-native, connection-maximal markdown for the
  8-month IIT KGP AI course vault (docs/). Use this skill WHENEVER the user asks to: save/write
  notes "in Obsidian format", create a concept note, convert/migrate/rewrite existing docs/*.md
  notes into Obsidian structure, add wikilinks/backlinks/MOCs, "preserve the connection web",
  extract atomic concepts from a session scroll, or build/refresh a Map of Content. Layered ON
  TOP of ai-embedded-tutor's markdown-notes-recipe: that recipe still owns the pedagogy (numeric
  anchors, numpy twins, traps, decision boundaries); THIS skill owns the vault architecture —
  atomic concept notes, typed links, block anchors, aliases, MOCs, and the sync contract with
  tools/web.json. Invoke it for any note the user will read inside Obsidian.
---

# Obsidian Atlas — the connection-preserving note system

## 0. The problem this skill solves (read once, believe forever)

The course runs 8 months (May 2026 → 10 Jan 2027, 32 sessions + foundation). By the end the vault
will hold 100–200 concepts across ~50+ scrolls. Today, concepts live BURIED inside long dated
session files — "standard deviation" has no address, so when covariance needs to point back at it,
there is nothing to point at. Links that can't be made at write-time are never made later. The
connection web the learner depends on (his single strongest stated preference) rots by default.

The fix: **every concept gets exactly one permanent, atomic, linkable home**, every mention of a
known concept anywhere becomes a wikilink to that home, and every link carries its *why*. Notes
then accumulate INTO the web instead of beside it.

**Division of labor:** `ai-embedded-tutor/references/markdown-notes-recipe.md` still governs
*content* (cakewalk + journey-recall, exact numbers preserved, numpy twins that plot, traps,
decision boundaries, analogies ride along). This skill governs *structure and connection*. When
writing any note, satisfy BOTH.

**The vault is `docs/`** (it has the `.obsidian/` config with community plugins). All paths below
are relative to `docs/`.

## 1. The four layers of the vault

```
docs/
├── HOME.md                          ← layer 3: the single entry dashboard
├── maps/                            ← layer 3: MOCs, one per arc/module
│   ├── MOC-foundation-math.md
│   ├── MOC-m1-ml-fundamentals.md
│   ├── MOC-m2-deep-learning.md ... (m3-nlp-transformers, m4-genai-llms, m5-rag, m6-agents-mlops)
│   └── MOC-thermal-project.md       ← the project rungs R0–R6 as a map
├── concepts/                        ← layer 1: ATOMIC concept notes (the link targets)
│   ├── standard-deviation.md
│   ├── covariance.md
│   ├── entropy.md ...
├── <dated session scrolls>          ← layer 2: the existing journey journals (stay at docs/ root,
│   2026-07-05_chain-rule-to-gradient_F.md      naming unchanged: YYYY-MM-DD_<topic>_<F|sN>.md)
├── recall-ledger.md · trap-log.md   ← layer 4: ledgers (existing, unchanged location)
└── 00_<arc>-consolidated.md         ← layer 4: arc consolidations (existing convention)
```

- **Layer 1 — concept atoms** are the permanent homes. One concept = one file = one slug. They
  accrete depth over 8 months; they are never split per-session.
- **Layer 2 — session scrolls** stay narrative and dated, exactly the current style. They are the
  *journey record*; atoms cite them, they cite atoms. NEVER delete or hollow out a scroll — the
  misconception→correction narrative in scrolls is the strongest recall asset.
- **Layer 3 — MOCs** are curated tables of contents per arc, because at 150+ notes the global
  graph view becomes a hairball; MOCs are the human-scale navigation the graph can't give.
- **Layer 4 — ledgers/maps/consolidated** keep their existing conventions, but gain wikilinks.

## 2. The naming law (slugs are the spine — get this wrong and the web breaks)

- **`tools/web.json` node slugs are the canonical concept names.** A concept atom's filename IS
  its web.json slug: node `gradient-descent` ⇔ `concepts/gradient-descent.md`. One source of truth.
- Creating an atom for a concept web.json doesn't know yet → add the node to web.json in the same
  session (end-of-session hub routine). Creating a web.json node → the atom may lag, but the slug
  is now reserved.
- **Slugs are immutable once created.** Obsidian auto-updates wikilinks on rename, but web.json,
  `build_hub.py`, flashcard decks, and HTML pages will NOT follow. If a name proves wrong, keep
  the slug and fix the display via `title:` + `aliases:`.
- Slug style: lowercase-kebab, the most specific unambiguous name (`cross-entropy`, not `loss2`).
- **Granularity rule (when is something an atom?):** it deserves its own file iff at least one is
  true: (a) another concept will ever need to link to it by name; (b) it has its own decision
  boundary; (c) it has its own numeric anchor. Otherwise it's a section inside its parent atom.
  (σ deserves an atom; "the −1 in n−1" is a section inside `variance-sigma`.)

## 3. Front-matter schemas (Dataview reads these — keep fields exact)

**Concept atom** (`concepts/<slug>.md`):

```yaml
---
title: Standard deviation (σ)          # display name, free to change
aliases: [std-dev, sigma, σ, spread]   # every name the concept answers to — REQUIRED, see §5
date: 2026-06-07                       # first-learned date
sessions: [F]                          # every session that touched it — append over time
lane: f                                # f | m1..m6  (mirrors web.json)
edge: 3                                # 1–3 ⭐ edge-relevance grade (mirrors web.json)
status: owned                          # owned | learning | due | upcoming (mirrors web.json)
type: concept
up: "[[MOC-foundation-math]]"          # parent MOC (Breadcrumbs/Dataview hierarchy)
recap: One breath that re-lights it — σ is the average distance from the mean; jitter, not center.
---
```

**Session scroll** — keep the existing schema (`title/date/sessions/concepts/type/recap/tags`)
and ADD: `up: "[[MOC-<arc>]]"`, and make `concepts:` entries match atom slugs exactly (they become
clickable via §5 rules in the body).

**MOC**: `type: moc`, `lane:`, `up: "[[HOME]]"`.

Statuses/edge/lane MUST stay in sync with web.json — they are the same fact in two mirrors (§8).

## 4. The concept-atom template (the required skeleton)

```markdown
---
(front-matter per §3)
---

# {Title}

> **Recap:** {the one-breath reactivation hook — same text as front-matter recap}

**Chain:** [[variance-sigma]] ──► **σ** ──► [[normal-distribution]] ──► [[z-score]]
*(the concept's place in the arrow-line, every link real — this is the Daily Compass edge chain, written down)*

## What it is (plain words)
One-to-three lines, zero symbols. A stranger follows it.

## The anchor numbers  ^anchor
The ONE worked example that owns this concept — exact session values, never changed.
`[2,4,4,4,5,5,7,9] → μ=5 → σ=2`   ← block-anchored: other notes EMBED this, never re-type it.

## Numpy twin
One Jupyter-ready cell (imports included). If the concept has a shape, it PLOTS the shape
and prints the anchor numbers as the check. (Recipe: markdown-notes-recipe.md §2b.)

## Where it came from / where it goes (typed links — the web, see §5)
builds-on:: [[mean]] — σ measures distance *from the mean*; no mean, no σ
builds-on:: [[variance-sigma]] — σ = √variance, same fact in the data's units
feeds:: [[normal-distribution]] — σ sets the bell's width
feeds:: [[standardization]] — z = (x−μ)/σ is how features get comparable
contrasts-with:: [[iqr]] — IQR survives outliers; σ gets dragged
used-by:: [[pca]] — scale features first or the big-σ feature hijacks the axes

## Decision boundary
✅ use when …  ·  ❌ NOT when … (unmissable; wrong-tool cases included)

## Traps I hit
![[trap-log#^sigma-outlier]]  ← embed the ledger line; the trap lives ONCE, in trap-log.md

## Depth layers (the 8-month accretion log — see §6)
- **2026-06-07 (F, first contact):** spread around mean; jitter analogy. → [[2026-06-07_stats-foundations_F#§3]]
- **2026-07-25 (s7):** reappears inside weight-initialization variance. → [[2026-07-25_neural-nets_s7#…]]

## Project brick
Which piece of the rung-1 thermal model this builds (project-map §2 language) —
e.g. "σ of the temperature channel = the jitter the forecaster must not confuse with trend."

## Flashcards
#flashcards/standard-deviation
Q :: A cards (3–6, per flashcards-spaced-recall.md card rules) — optional but preferred.
```

Skip a section only when it honestly has nothing (a `type: moc` link dump needs no numpy twin).
**Anchor numbers, decision boundary, and typed links are NEVER optional** in a concept atom.

## 5. The linking law (the heart of the skill — enforce ruthlessly)

1. **First-mention rule.** In ANY note, the first mention of a concept that has (or deserves) an
   atom becomes a wikilink: "…divide the covariance by both [[standard-deviation|σ]]s…". Later
   mentions in the same note stay plain (link density ≠ link spam). This is exactly the user's
   covariance→σ requirement: every concept grounds back to its basics *at the point of use*.
2. **Typed links, each with a why.** Relations use Dataview inline fields — the fixed vocabulary:
   - `builds-on::` (points DOWN at prerequisites — the "link back to basics" direction)
   - `feeds::` (points UP at what this unlocks next)
   - `contrasts-with::` (the decision-boundary sibling: mean↔median, L1↔L2, RNN↔attention)
   - `used-by::` (algorithms/projects that consume it)
   - `trap::` (links into trap-log entries)
   - `project-brick::` (the thermal-project piece it builds)
   - `scroll::` (the session scroll(s) where the journey happened)
   Every typed link carries a trailing `— why` clause, same discipline as web.json edges. **A link
   without a why is noise; a why without a link is rot.**
3. **`builds-on::` chains must bottom out.** Follow any concept's builds-on chain and you reach
   foundation atoms (mean, vectors, probability, derivative). If a chain dead-ends at a missing
   prerequisite, create the stub atom (see 5.5). This makes the whole tower walkable downward from
   ANY concept — backprop → chain-rule → derivative → slope in three clicks, in Jan as in Jul.
4. **Section/block precision beats file links.** Link to the exact place: `[[scroll#§7]]`,
   `[[trap-log#^cov-sign]]`. Give every numeric anchor a block ID (`^anchor`, `^cov-3x3`) and
   **embed** (`![[covariance#^anchor]]`) instead of re-typing numbers — anchors then live in ONE
   file, and the "notes and twins must agree" rule becomes structurally guaranteed.
5. **Unresolved links are seeds, not errors.** Teaching regression and attention comes up? Write
   `[[attention]]` NOW. Obsidian tracks unresolved links; when s14 arrives the atom is created and
   every prior mention lights up retroactively. Sprinkle forward-links deliberately at the
   "feeds::" beat — future sessions inherit a pre-built inbound web.
6. **Aliases make links happen.** Concepts get every surface form in `aliases:` (σ, std-dev,
   "amount of say", log-odds…). **Collision rule:** an alias must be unambiguous vault-wide — σ
   may alias standard-deviation only until sigmoid claims overlap; then keep the alias on the
   dominant owner and always link the other explicitly (`[[sigmoid|σ(z)]]`).
7. **⛔ The matrix-literal hazard.** `A = [[2,0],[0,3]]` outside a code span IS a wikilink to a
   note named "2,0],[0,3". Every matrix/list literal must sit in backticks or a fenced block. When
   migrating old notes, grep for `[[` that isn't a real link and fence it.
8. **MOC membership.** Every atom links up (`up:` field) and every MOC lists the atom. No orphans:
   a note reachable only by search is a note lost by October.

## 6. Depth-layer accretion (the 8-month re-entry problem no single session sees)

Concepts in this course RETURN at deeper levels: entropy (s3 trees → cross-entropy loss →
KL/M4), chain rule (F → backprop s7 → vanishing gradients s10 → LoRA training M4), dot product
(F → neuron s2 → convolution s9 → attention scores s14). The naive failure is a second note
("entropy-2", "entropy-for-nns") that severs the web.

**Rule: one concept, one atom, forever.** A re-encounter appends a dated entry to `## Depth
layers` (what NEW understanding arrived + link to the new scroll), updates `sessions:`, upgrades
`status:`/`edge:` if changed, and adds any new typed links (entropy gains `feeds:: [[kl-divergence]]`
in M4). The atom is a *living* note; its history is the depth-layer log. A *distinct* concept that
merely shares a name (cross-entropy is not entropy) gets its own atom + `builds-on:: [[entropy]]`
+ `contrasts-with::` clarifying the difference.

## 7. MOCs and HOME (navigation that survives scale)

- **One MOC per arc/module** (foundation, m1…m6, thermal-project). Contents: a 5-line "story of
  this arc" → curated concept list in LEARNING ORDER (not alphabetical), each with its recap line
  → the arc's scrolls → the arc's consolidated doc + formula card → a Dataview status board:

  ````markdown
  ```dataview
  TABLE status, edge, recap FROM "concepts" WHERE lane = "m1" SORT edge DESC
  ```
  ````
- **HOME.md**: the compass — link to all MOCs, the readiness-timeline strip from the project map,
  and three live queries: due recalls (`status = "due"`), stubs/half-taught
  (`contains(tags,"incomplete")`), and recently touched (`sort file.mtime desc limit 10`).
- MOCs are curated by hand; queries supplement, never replace, the curated order.

## 8. The web.json sync contract (two mirrors, one truth)

The vault graph (human) and `tools/web.json` (hub/machine) describe the SAME web:
- atom created/status changed ⇒ same change lands in web.json the same session (existing
  end-of-session routine: update web.json → `python3 tools/build_hub.py` → commit `index.html`).
- every `builds-on::`/`feeds::` between two web.json-known concepts ⇒ a web.json edge with the
  same why (edges are directional: builds-on reversed = feeds).
- conflict ⇒ **web.json wins on slugs; the vault wins on prose.**
- `build_hub.py` currently scans `docs/*.md` front-matter — extending it to walk `docs/concepts/`
  and `docs/maps/` is a required follow-up the first time atoms exist; flag it, don't let the hub
  silently go blind.

## 9. Migration protocol (rewriting the existing notes — do NOT lose the journey)

When asked to convert existing notes (may run file-by-file across weeks):
1. **Inventory first.** Read the scroll + web.json; list which of its concepts already have atoms,
   which need creating, which are stubs to seed.
2. **Extract, don't move.** For each concept: create the atom, DISTILL into it (plain-words, the
   anchor numbers with block IDs, twin, boundary, typed links, project brick) — but the scroll
   keeps its full narrative. Atom links `scroll:: [[the-scroll#§n]]`; scroll's first-mentions
   become links to atoms. The scroll loses nothing; it gains addresses.
3. **Fence the hazards** (§5.7), add `up:`, normalize front-matter to §3.
4. **Wire the MOC** + web.json nodes/edges for anything new.
5. **One scroll per pass, committed per pass** — reviewable, resumable, interruptible.
6. **Never** rewrite the prose voice, "improve" the humor, or change a single anchor number.
   Migration is re-plumbing, not re-authoring. Traps stay verbatim.

## 10. Weekly hygiene (5 minutes that saves the web — run at the module-boundary ritual too)

- **Orphan sweep:** any concept atom with zero inlinks? Wire or merge it.
- **Unresolved-link triage:** which seeds are due to become atoms this module?
- **Stub debt:** `#incomplete` notes (like the entropy stub) — resurface before the session that
  needs them (entropy → before s4 math-prep).
- **Sync audit:** vault statuses vs web.json statuses agree? Hub rebuilt?
- **Alias audit:** new collisions (σ-class problems) as new modules import old symbols?

## 11. Definition of done (per note, before commit)

- [ ] front-matter complete per §3; slug matches web.json (or node added)
- [ ] every first mention of a known concept is a wikilink; typed links each carry a why
- [ ] builds-on chain bottoms out at foundation atoms (stubs seeded if not)
- [ ] anchor numbers block-anchored once, embedded elsewhere (never re-typed)
- [ ] matrix/list literals fenced (§5.7)
- [ ] `up:` set + listed in its MOC; depth-layer entry added if this was a re-encounter
- [ ] web.json + hub updated in the same session; recall-ledger row touched if learning happened
- [ ] pedagogy bar still met (markdown-notes-recipe: journey, traps, boundary, twin, analogies)
