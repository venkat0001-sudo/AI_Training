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
