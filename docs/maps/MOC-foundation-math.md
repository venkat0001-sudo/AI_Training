---
title: MOC — Foundation math (the runway)
date: 2026-07-07
lane: f
type: moc
up: "[[HOME]]"
recap: "The math everything stands on: vectors → σ → the bell → covariance → eigen → calculus → gradient descent — each atom feeding the next, ending at the pipeline map."
---

# 🗺️ MOC — Foundation math (the runway)

> **The arc in five lines:** vectors give you the objects and the dot product ([[vectors]]).
> Spread gives you σ ([[variance-sigma]]) and its shape, the bell ([[normal-distribution]]).
> Two spreads together give covariance ([[covariance]]), whose special arrows are the
> eigenvectors ([[eigenvectors]]) that power [[pca]]. Meanwhile calculus ([[calculus]]) builds
> the slope machinery that [[gradient-descent]] turns into training. The whole shelf is arranged
> on [[ml-pipeline]].

## Concepts in learning order

1. [[vectors]] — magnitude · dot · cosine · ⭐⭐⭐ · **atom live**
2. [[variance-sigma]] — deviations → variance → σ; speedometer-not-judge · ⭐⭐⭐ · **atom live**
3. [[normal-distribution]] — the bell, σ bands, z-scores · ⭐⭐⭐ · **atom live**
4. [[probability]] — marginal/joint/conditional · ⭐⭐ · **stub** (own worked doc owed)
5. [[bayes]] — flip the conditional; the base-rate trap · ⭐⭐ · **atom live**
6. [[covariance]] — the vote engine + the matrix · ⭐⭐ · **atom live**
7. [[eigenvectors]] — stretch-not-rotate; det(C−λI)=0 · ⭐⭐ · **atom live**
8. [[calculus]] — derivative + chain rule (depth-gated) · ⭐⭐ · **atom live**
9. [[gradient-descent]] — the training rule 2(P−T)·x · ⭐⭐⭐ · **atom live**
10. [[ml-pipeline]] — the six-box map + the label-entry line · ⭐⭐ · **atom live**

## The scrolls of this arc

- [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] — the 860-line spine (feeds atoms 1–3, 6–7)
- [[2026-06-14_calculus-foundations_F]] — the 3-hour calculus walk ([[2026-06-14_calculus-notes-raw_F|raw source]])
- [[2026-07-05_chain-rule-to-gradient_F]] — the depth-gated chain-rule drill
- [[2026-07-02_ml-pipeline-math-map_F]] — the pipeline × math map

## Status board (needs Dataview)

```dataview
TABLE status, edge, recap FROM "concepts" WHERE lane = "f" SORT edge DESC
```

## Seeds pending

[[z-score]] (alias-resolved into [[normal-distribution]] for now) · [[correlation]] (Pearson/Spearman — taught only in passing) · [[attention]] (forward seed from [[vectors]])

## Arc consolidation

⏳ owed: `00_foundation-math-consolidated.md` + one-page formula card (natural slot: after s5 closes the PCA arc).
