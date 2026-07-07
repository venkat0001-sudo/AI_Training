---
title: Eigenvectors & eigenvalues (λ)
aliases: [eigenvalues, eigenvector, eigenvalue, lambda, eigen, λ]
date: 2026-06-29
sessions: [F]
lane: f
edge: 2
status: due
type: concept
up: "[[MOC-foundation-math]]"
recap: "An eigenvector is an arrow the matrix can only STRETCH, never ROTATE; λ is the stretch factor. On a covariance matrix: eigenvector = a direction in the data, λ = how much variance lives there."
---

# Eigenvectors & eigenvalues (λ)

> **Recap:** **An eigenvector is an arrow the matrix can only STRETCH, never ROTATE; λ is the
> stretch factor.** On a covariance matrix: eigenvector = a direction in the data, λ = how much
> variance lives there.

**Chain:** [[covariance]] ──► **eigenvectors/λ** ──► [[pca]] ──► feature compression ──► fewer MACs/SRAM ──► on-device inference

## What it is (plain words)

A matrix is a machine that eats an arrow and generally does two things: rotates it AND stretches
it. **A few special arrows slide through without bending — same heading out as in, only longer or
shorter. Those are the eigenvectors; the stretch factor is the eigenvalue λ.** (The pasta press:
most noodles come out bent; eigen-noodles come out straight, just longer. 💪 gym-bro version: pure
gains, no twist.)

## The anchor numbers  ^anchor

The Temp/Latency 2×2, fully by hand (data on the line L = 2T+20):

```
        T      L
   T [ 100    200 ]      det(C−λI)=0 → λ² − 500λ = 0 → λ₁ = 500 (100%), λ₂ = 0
   L [ 200    400 ]      (C−500I)v = 0 → −400x + 200y = 0 → y = 2x → v₁ = [1, 2]

verify:  C·[1,2] = [500, 1000] = 500·[1,2]  ✓  stretched ×500, not rotated
read:    v₁ = "1 part Temp, 2 parts Latency" → Latency swings 2× per unit Temp — the eigenvector
         RECOVERED the built-in relationship L = 2T+20
```

The 3×3 twin (every pair cov = 1): λ = 4, 1, 1 → v₁ = `[1,1,1]` = the common-mode tide ("all
sensors rise together"); the repeated λ=1 leaves a 2-D differential plane. Sanity checks: trace
6 = Σλ ✓, det 4 = Πλ ✓. ^anchor-3x3

## Numpy twin

```python
import numpy as np
C = np.array([[100, 200], [200, 400]])
lam, V = np.linalg.eig(C)
print(lam)                       # [0. 500.] — the two stretch factors
v1 = V[:, np.argmax(lam)]
print(v1)                        # ±[0.447, 0.894] = [1,2] normalized (numpy may flip the sign — direction is what matters)
print(C @ v1, lam.max() * v1)    # equal ✓  C·v = λ·v, stretch-not-rotate
```

## Where it came from / where it goes

builds-on:: [[covariance]] — the covariance matrix is the machine; its eigenvectors are the data cloud's natural axes
builds-on:: [[vectors]] — "did the arrow's direction survive?" is a question about direction vs magnitude
feeds:: [[pca]] — rank directions by λ, keep the top — that IS PCA
feeds:: [[neural-nets]] — the matrix-as-machine picture is the mental model for every layer (`output = A·x`)
scroll:: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] — §10–§14, §19, §21
video:: [3B1B — Eigenvectors & eigenvalues (ch.14)](https://www.youtube.com/watch?v=PFDu9oVAE-g)
twin-page:: [eigen by hand, 2×2 vs 3×3](../html/2026-07-02_eigen-by-hand-2x2-vs-3x3_F.html)

## The recipe (and why each step exists)

```
1. eigenvalues:   solve det(C − λI) = 0
2. eigenvectors:  for each λ, solve (C − λI)v = 0
```
- **Why λI, not λ?** C is a matrix, λ a scalar — shapes clash. `λI` is λ sitting down the
  diagonal: the **adapter** that makes the subtraction legal.
- **Why det = 0?** `(C−λI)v = 0` says a NONZERO arrow gets crushed to nothing — only a
  **collapsing** matrix does that, and det = 0 is the fingerprint of collapse (det = area-scaling
  factor; 0 = plane squashed flat).
- **Honest limit:** past 2×2 the polynomial gets ugly (degree n) — learn the mechanics small,
  then trust `np.linalg.eig` (QR algorithm) for real sizes.

## Decision boundary

- ✅ Finding the "natural axes" of a dataset — directions of maximum spread or minimum redundancy.
- ❌ Do NOT read eigenvalue size as feature IMPORTANCE for prediction — λ measures variance in the data, not predictive power (a high-variance feature can be useless for a specific label).
- ❌ Eigenvector components are **recipe weights (loadings)** — how to BLEND features — NOT the model's prediction weights (those come from [[gradient-descent]], label in hand).

## Traps I hit

![[trap-log#^eig-always-11]]
![[trap-log#^v1-frequent]]
![[trap-log#^weights-overload]]

## Depth layers

- **2026-06-29 (F):** matrix-as-machine, the `[[2,0],[0,3]]`-by-hand journey — the dimension snag, the [1,1]-always-eigenvector misconception dying. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#12. 🧭 The learning flow — how we actually built this (the journey, wrong turns included)]]
- **2026-06-30 (F):** HOW to compute — det(C−λI)=0 collapse intuition, λI adapter, 5×5 run (λ₁=2.70/64.9%). → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#14. 🧭 Deep-dive journey — HOW eigenvectors are computed + every "wait, why?" (2026-06-29/30, VS Code session)]]
- **2026-07-02 (F):** the 3×3 fully by hand — cubic, repeated λ → solution PLANE, trace/det sanity checks. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §19
- **2026-07-03 (F):** recipe weights vs prediction weights untangled (the two "weights" born in different boxes, opposite sides of the label line). → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#21. ⭐ The two "weights", the label rule, + the perpendicularity drill (2026-07-03)]]

## Project brick

Common-mode vs differential, in his language: **v₁=[1,1,1] = "all rails rise together" (bulk
thermal drift); the λ=1 leftover plane = differential jitter between sensors** — exactly how a
storage engineer already decomposes noise, now as math the thermal forecaster's [[pca]] front-end
will run.

## Formula

```
A·v = λ·v            v: the un-rotatable arrow    λ: its stretch factor
det(C − λI) = 0      the λ-values that make C−λI collapse = the eigenvalues
Σλ = trace(C)        eig re-slices the SAME total variance along the cigar instead of the axes
```

## Flashcards

#flashcards/eigenvectors

Feed `[1,1]` to the matrix `[[2,0],[0,3]]`. Eigenvector or not, and why? :: Not — unequal pull (×2 east, ×3 north) tips the diagonal toward the stronger leg: out comes `[2,3]` ≈ 56°, rotated. `[1,1]` survives only equal-pull matrices.
Why must det(C−λI) = 0 to find eigenvalues? :: (C−λI)v=0 crushes a NONZERO arrow to nothing — only a collapsing matrix does that, and det=0 is collapse's fingerprint.
v₁ = [1,2] on the Temp/Latency matrix. What does it SAY about the features? :: "1 part Temp, 2 parts Latency" — Latency swings 2× per unit Temp; the eigenvector recovered L = 2T+20 from the covariance alone.
