---
title: MOC — Module 1 · ML Fundamentals
date: 2026-07-07
lane: m1
type: moc
up: "[[HOME]]"
recap: "M1 in one map: raw data → working predictors (s1–s6, 20 Jun – 19 Jul). The vocabulary every later module reuses."
---

# 🗺️ MOC — Module 1 · ML Fundamentals

> **The arc in five lines:** s1 teaches you to *look at data before trusting it* ([[ml-workflow]],
> [[metrics]], [[cross-validation]]). s2 builds the first predictor — a neuron is just
> [[regression|logistic regression]], trained against [[cross-entropy]]. s3 grows the alternatives
> ([[trees-svm]]) and their splitting currency, [[entropy]]. s4 stacks weak learners into strong
> ones ([[ensembles]]). s5 drops the labels entirely ([[kmeans]], [[pca]]). Module ends 19 Jul —
> the M1 gate on the readiness timeline ([[2026-07-04_thermal-ml-project-map_F]] §0).

## Concepts in learning order

1. [[ml-taxonomy]] — AI → ML → classic/deep: the bloodline · ⭐ · **atom live**
2. [[ml-workflow]] — Y=F(X,W); data challenges; the elephant · ⭐⭐ · **atom live**
3. [[metrics]] — confusion matrix, precision/recall/F1 · ⭐⭐ · **atom live**
4. [[cross-validation]] — the U-curve dip; rotating folds · ⭐⭐ · **atom live**
5. [[regression]] — linear & logistic: the first predictor, the future neuron · ⭐⭐⭐ · **atom live**
6. [[cross-entropy]] — the loss, derived from likelihood · ⭐⭐⭐ · **atom live**
7. [[trees-svm]] — decision trees & SVMs (s3) · ⭐⭐⭐ · *seed — s3 notes owed*
8. [[entropy]] — the suspense meter; trees' splitting currency · ⭐⭐⭐ · **atom live (stub — resume before s4)**
9. [[ensembles]] — bagging, forests, boosting (s4, 11 Jul) · ⭐⭐ · *seed*
10. [[kmeans]] — clustering without labels (s5, 18 Jul) · ⭐⭐ · *seed*
11. [[pca]] — keep the cigar's long axis (s5, but pre-built from Foundation) · ⭐⭐⭐ · **atom live**
12. [[mcu-deployment]] — what survives on a microcontroller · ⭐⭐⭐ · **stub**

## The scrolls of this arc

- [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]] — s1 full PPT walk (77 slides)
- [[2026-06-25_bayes-and-ml-taxonomy_s1]] — Bayes + the ML bloodline
- [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]] — s2 deck+transcript master notes
- [[2026-07-05_entropy_F]] — the s3-rescue entropy stub (⏳ incomplete)
- [[2026-07-10_primer_s4]] — Friday primer for s4 ensembles

## Status board (needs the Dataview plugin)

```dataview
TABLE status, edge, recap FROM "concepts" WHERE lane = "m1" SORT edge DESC
```

## Seeds pending

**Due before s4 (11 Jul):** [[entropy]] resume (formula/twin/info-gain) — on the T-minus-3 math-prep map.
**Due at/after s3 notes:** [[trees-svm]] · [[gini-impurity]].
**Due at s4:** [[ensembles]] (+ log-odds "amount of say").
**Due at s5 (18 Jul — the R1 gate):** [[kmeans]].
**Later:** [[naive-bayes]] · [[kl-divergence]] (M4) · [[attention]] (s14).

## Arc consolidation

⏳ owed at module boundary (19 Jul): `00_m1-fundamentals-consolidated.md` + one-page formula card.
