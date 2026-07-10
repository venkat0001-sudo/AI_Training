---
title: 🏠 HOME — the vault compass
date: 2026-07-07
type: moc
recap: "Start here. MOCs by arc, the readiness countdown, and the live boards (due / incomplete / recent)."
---

# 🏠 HOME — the vault compass

> **The goal, one breath:** become an **exceptional edge-AI engineer** — proven by the on-device
> [[thermal-project|thermal-throttle ML project]], built brick-by-brick from this course.
> Course: IIT KGP + upGrad, May 2026 → 10 Jan 2027.

## 🔖 Resume here — last touched 2026-07-10 (read this first on a new device)

**Where we are:** Foundation math, deep in the gradient-descent arc. Two artifacts shipped today:
the full R1 story scroll [[2026-07-10_line-to-gradient-thermal-fit_F]] and a new [[expected-value]] atom.

**▶️ CONTINUE LATER (a thread that didn't fully land — sleepy, he'll re-ask):**
- **The gradient ↔ multi-weight connection.** For `y = w₀x₀ + w₁x₁ + w₂x₂ + …`: (a) that sum **IS a
  dot product** `w·x` — the *same* sum-of-products shape as EV `= Σ pᵢvᵢ` he just learned; (b) each
  weight gets its **own** partial `∂L/∂wᵢ = 2·err·xᵢ` — the input that rode next to `wᵢ` in the sum is
  exactly the `xᵢ` that scales its gradient (credit assignment). The gradient = the vector of those
  partials, one slot per weight. **Unfinished check to reopen with:** if `x₂ = 0` this tick, then
  `∂L/∂w₂ = 0` → weight `w₂` is frozen this step (a silent sensor is never punished). Resume gently.

**📌 PICK UP LATER (owed deliverable — a real build):**
- **The continuation interactive HTML + drill:** Partial Derivative → Gradient → Gradient Descent →
  best-fit line, run **START→END on the temperature numerics** so the big picture lands as one image.
  He'll teach it to his friend (she loved the first line-vs-curve page,
  [the line-vs-curve HTML](../html/2026-07-09_line-vs-curve-slope_F.html), and understood it
  completely — this is the sequel). **Build it his way: step by step, ONE beat per
  message, NOT the whole thing in one lump** (his explicit, repeated process ask).
- His StatQuest recollection is **correct** (confirmed): fix slope → wiggle intercept → SSR is a 2D **U**
  → best intercept; then both vars → SSR is a 3D **bowl** → gradient (two partials) → walk to the middle.

**🗓️ Also queued (from earlier):** he brings exam date/format + weekly hours → then we build a ⭐-triage
study plan (exam-track vs mastery-track). s4 = **ensembles** (Sat 11 Jul): he watches StatQuest Random
Forests tonight, revises AM, syncs tomorrow night → probe his understanding, rebuild any ⭐⭐⭐ gap.

**Minor open:** Troll 2 break-even reward = `0.83/0.17 ≈ $4.88` (below that, the bet turns bad).

## The maps

- [[MOC-foundation-math]] — the math runway (vectors → σ → bell → covariance → eigen → calculus → GD)
- [[MOC-m1-ml-fundamentals]] — M1: raw data → working predictors (20 Jun – 19 Jul)
- [[MOC-thermal-project]] — 🎯 the project: rungs, readiness timeline, papers
- *(M2–M6 MOCs get created at each module's first session: deep learning · NLP/Transformers · GenAI/LLMs · RAG · agents/MLOps)*

## The countdown strip (from the readiness timeline)

**Next gate: 18 Jul — own k-means + PCA → R1 buildable. M1 ends 19 Jul (module-boundary ritual:
consolidated doc + formula card + next paper).** Full dated ladder: [[2026-07-04_thermal-ml-project-map_F]] §0.

## The ledgers

- [[recall-ledger]] — what's due when (the interval ladder)
- [[trap-log]] — 🪤 the misconception ledger, exam gold, one embeddable line per trap

## Live boards (need the Dataview plugin)

```dataview
TABLE recap, edge FROM "concepts" WHERE status = "due" SORT edge DESC
```

```dataview
TABLE recap, status FROM "concepts" WHERE contains(tags, "incomplete")
```

```dataview
TABLE file.mtime AS touched, type FROM "concepts" OR "maps" SORT file.mtime DESC LIMIT 10
```
