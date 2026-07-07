---
title: MOC — Module 1 · ML Fundamentals
date: 2026-07-07
lane: m1
type: moc
up: "[[HOME]]"
recap: "M1 in one map: raw data → working predictors (s1–s6, 20 Jun – 19 Jul). The vocabulary every later module reuses."
---

# 🗺️ MOC — Module 1 · ML Fundamentals

> **The arc in five lines:** s1 teaches you to *look at data before trusting it* (EDA, metrics,
> cross-validation). s2 builds the first predictor — a neuron is just logistic regression. s3 grows
> the alternatives (trees, SVMs) and their splitting currency, entropy. s4 stacks weak learners
> into strong ones (ensembles). s5 drops the labels entirely (K-means, PCA). Module ends 19 Jul —
> the M1 gate on the readiness timeline ([[2026-07-04_thermal-ml-project-map_F]] §0).

## Concepts in learning order

*(links go live as atoms are created — unlinked slugs are seeds waiting for migration)*

1. [[ml-taxonomy]] — AI → ML → classic/deep: the bloodline · ⭐
2. [[ml-workflow]] — EDA, preprocessing, the loop · ⭐⭐
3. [[cross-validation]] — grade on data you didn't tune on · ⭐⭐
4. [[regression]] — linear & logistic: the first predictor, and the future neuron · ⭐⭐⭐
5. [[trees-svm]] — decision trees & SVMs: the if/else predictors · ⭐⭐⭐
6. [[entropy]] — the suspense meter; trees' splitting currency · ⭐⭐⭐ · **atom live** (stub — resume before s4)
7. [[ensembles]] — bagging, forests, boosting (s4, 11 Jul) · ⭐⭐
8. [[kmeans]] — clustering without labels (s5, 18 Jul) · ⭐⭐
9. [[pca]] — keep the cigar's long axis (s5, 18 Jul) · ⭐⭐⭐
10. [[mcu-deployment]] — what survives on a microcontroller · ⭐⭐⭐

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

## Arc consolidation

⏳ owed at module boundary (19 Jul): `00_m1-fundamentals-consolidated.md` + one-page formula card.
