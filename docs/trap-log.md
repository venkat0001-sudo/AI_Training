---
title: Trap log — the misconception ledger
date: 2026-07-04
sessions: []
concepts: [meta]
type: ledger
recap: Every trap I fell into, one line each — the strongest recall hooks I own. Read before exams.
---

# 🪤 Trap Log — my greatest hits of wrong turns

> One line per trap: the wrong belief → the correction, with a link to the full story.
> These are **exam gold**: each one marks a spot where intuition misfires — mine did, so will half the cohort's.
> Maintained at every session (new trap → new row, newest on top).

| Date | The trap (what I believed) | The correction (what's true) | Full story |
|---|---|---|---|
| 2026-07-03 | "PCA gives me the price-prediction weights" | PCA gives **recipe weights (loadings)** — how to *blend* features. Prediction weights come later, from gradient descent, using the label | [linear-algebra §21](2026-06-28_linear-algebra-vectors-dot-cosine_F.md) |
| 2026-07-03 | "PCA is like gradient descent — it also reduces a loss" | PCA has **no loss and no label** — it reshapes features. They live on opposite sides of the label-entry line | [pipeline map §1b](2026-07-02_ml-pipeline-math-map_F.md) |
| 2026-07-03 | "PCA can't be used in my supervised project — it's unsupervised" | The label rule is about the **method, not the pipeline**: PCA-the-step never sees the label, so it's unsupervised *even inside* a supervised project | [taxonomy notes](2026-06-25_bayes-and-ml-taxonomy_s1.md) |
| 2026-06-30 | "±1σ is the outlier fence" | ~1 in 3 readings falls outside ±1σ **by design**. Outliers live beyond ±2σ/±3σ | [linear-algebra §16](2026-06-28_linear-algebra-vectors-dot-cosine_F.md) |
| 2026-06-30 | "mean of [10,20,30] = 30" (grabbed the max) | mean = sum/count = **20**. Spell-check: deviations must sum to 0 — mine summed to −30, alarm fired | [linear-algebra §15.1](2026-06-28_linear-algebra-vectors-dot-cosine_F.md) |
| 2026-06-29 | "v₁ is the most frequent reading in the data matrix" | v₁ is a **direction (a blend of features)**, not a row; PCA is about *spread*, not frequency | [linear-algebra §14.F](2026-06-28_linear-algebra-vectors-dot-cosine_F.md) |
| 2026-06-29 | "the eigenvector is always [1,1]" | Each matrix has its **own** eigenvectors; [1,1] was special to one matrix. Length & sign don't matter — direction does | [linear-algebra §14.F](2026-06-28_linear-algebra-vectors-dot-cosine_F.md) |
| 2026-06-25 | "a 99%-accurate alarm means 99% sure when it fires" | Base rates rule: with rare events the posterior can be ~50% or worse — count the buckets | [Bayes notes](2026-06-25_bayes-and-ml-taxonomy_s1.md) |
