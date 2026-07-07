---
title: PCA — principal component analysis
aliases: [principal-component-analysis, principal-components, dim-reduction, loadings, recipe-weights, scree]
date: 2026-06-29
sessions: [F]
lane: m1
edge: 3
status: due
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "PCA = eig the covariance matrix, rank directions by λ, keep the top-K, drop the rest — lossy compression for features. Label never seen: it makes RECIPE weights, not prediction weights."
---

# PCA — principal component analysis

> **Recap:** **PCA = eig the [[covariance]] matrix, rank directions by λ, keep the top-K, drop
> the rest — lossy compression for features.** Label never seen: it makes RECIPE weights, not
> prediction weights.

**Chain:** [[covariance]] ──► [[eigenvectors]] ──► **PCA** ──► feature compression ──► fewer MACs/SRAM ──► on-device inference ([[mcu-deployment]])

## What it is (plain words)

Find the directions where the data actually moves (big λ), photograph along those, and throw away
the directions where it doesn't (λ ≈ 0 = no information). **It's lossy compression for features —
and he already thinks in lossy compression.**

## The anchor numbers  ^anchor

```
The 20-sensor capstone flow:
raw 500×20 → np.cov → 20×20 → eig → scree shows 3 big λ, 17 ≈ 0
→ cumulative variance hits 95% at K=3 → keep 3 numbers per reading, ~⅞ less SRAM/MACs/power

The pizza rule 🍕: each direction's share = its λ ÷ Σλ (and Σλ = trace = total variance)
Temp/Latency 2×2: λ = 500, 0 → PC1 = 100% → 2 features → 1 number (1·T + 2·L), zero loss
3-sensor 3×3:     λ = 4, 1, 1 → PC1 = 4/6 = 66.7% (the common tide), keep 2 → 83.3%
```

Grid-size law: **covariance is (#channels)², NEVER #readings** — `500×20 → 20×20`; `1000×20 →
20×20` (more readings only steady the averages). Unique cells = n(n+1)/2 by symmetry. ^anchor-gridsize

## Numpy twin

```python
import numpy as np
C = np.array([[2,1,1],[1,2,1],[1,1,2]])          # 3 sensors, every pair linked
lam, V = np.linalg.eig(C)
order = np.argsort(lam)[::-1]
lam, V = lam[order], V[:, order]
shares = lam / lam.sum()
print(np.round(lam,2), np.round(shares*100,1))    # [4, 1, 1] → [66.7, 16.7, 16.7]%
print(np.round(V[:,0],3))                          # ±[0.577,0.577,0.577] = [1,1,1] — the common tide
```

## Where it came from / where it goes

builds-on:: [[eigenvectors]] — PC1 IS the top-λ eigenvector of the covariance matrix; PCA adds only "rank and keep"
builds-on:: [[variance-sigma]] — "importance" here = variance along a direction (the trust-vs-importance flip: HIGH variance = informative)
feeds:: [[kmeans]] — s5 pairs them: compress with PCA, then cluster in the small space
feeds:: [[mcu-deployment]] — 20 telemetry channels → 3 = a controller-sized model
feeds:: embedding compression (s24, RAG) — the same math shrinks a 768-dim embedding to fit on-device
contrasts-with:: [[gradient-descent]] — PCA has NO loss and NO label; they live on opposite sides of the label-entry line (pipeline map §1b)
scroll:: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] — §9, §14.I, §21
twin-page:: [PCA 20-sensor walkthrough](../html/2026-06-28_pca-20-sensors-walkthrough_F.html)
lab:: notebook cells 4.1b / 4.6 (project .venv)

## Decision boundary

- ✅ Channels are redundant AND you want compact features reused many times (the eig cost amortizes).
- ❌ **When PCA BETRAYS you:** (1) the rare signal hides in a tiny-λ direction — anomaly/thermal-runaway spike gets thrown away with the "noise"; (2) interpretability dies (kept numbers are blends, not "temperature"); (3) every channel already independent → nothing to compress.
- ❌ It is unsupervised **as a method** even inside a supervised project — the step never sees the label.

## Traps I hit

![[trap-log#^weights-overload]]
![[trap-log#^pca-loss]]
![[trap-log#^pca-supervised]]

## Depth layers

- **2026-06-29 (F):** covariance→eigen→PCA bridge; y=2x toy (λ₁=5, λ₂=0). → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#11. Eigenvectors & Eigenvalues (continues §10)]]
- **2026-06-30 (F):** the 20-sensor capstone + pizza shares + when-PCA-betrays. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#14. 🧭 Deep-dive journey — HOW eigenvectors are computed + every "wait, why?" (2026-06-29/30, VS Code session)]]
- **2026-07-03 (F):** recipe vs prediction weights + the label-entry line (PCA is box [2], before the label). → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#21. ⭐ The two "weights", the label rule, + the perpendicularity drill (2026-07-03)]]
- **⏳ s5 (18 Jul):** the live lecture — should be revision, not new material. Gate on the readiness timeline: own k-means+PCA by 18 Jul to build R1.

## Project brick

**The R1 compression front-end: 20 telemetry channels → 3 principal components → a model that
fits controller SRAM.** Caveat banked: if thermal-runaway hides in a small-λ direction, PCA
deletes the warning — anomaly channels may need to bypass the compressor.

## Formula

```
C = cov(X)  →  eig(C) = (λᵢ, vᵢ)  →  sort by λ  →  keep top-K where cumulative λ-share ≥ 95%
new features = projections onto v₁..v_K          share(i) = λᵢ / Σλ
```

## Flashcards

#flashcards/pca

500 readings × 20 sensors. Covariance matrix size, and why? :: 20×20 — (#channels)², NEVER #readings; each cell = one channel-PAIR averaged over all readings (inner dim cancels).
Name the three ways PCA betrays you. :: Rare signal in a tiny-λ direction gets deleted; interpretability dies (blends, not "temperature"); eig compute only pays off if features are reused.
PCA ran inside your supervised thermal project. Supervised or unsupervised? :: Unsupervised — the label rule is about the METHOD: the PCA step never sees the label, whatever pipeline it sits in.
