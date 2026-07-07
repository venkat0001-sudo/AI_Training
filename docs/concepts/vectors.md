---
title: Vectors — magnitude · dot product · cosine
aliases: [vector, magnitude, dot-product, cosine-similarity, norm, dot]
date: 2026-06-28
sessions: [F]
lane: f
edge: 3
status: due
type: concept
up: "[[MOC-foundation-math]]"
recap: "A vector = direction + magnitude, separable. Dot product measures alignment but is contaminated by loudness; cosine divides out both lengths and keeps only the heading."
---

# Vectors — magnitude · dot product · cosine

> **Recap:** A vector = direction + magnitude, **separable**. Dot product measures alignment but
> is contaminated by loudness; cosine divides out both lengths and keeps only the heading.

**Chain:** **vectors** ──► [[covariance]] ──► [[eigenvectors]] ──► [[pca]]
**Chain:** **dot product** ──► the neuron's core op `w·x` ──► [[regression]] ──► attention scores ([[attention]], s14)

## What it is (plain words)

An ordered list of numbers, drawn as an arrow. It has two separable properties: **which way it
points (direction) and how long it is (magnitude)** — and every similarity tool is a choice about
which of the two you keep.

## The anchor numbers  ^anchor

```
Walk 3 east, 4 north → |v| = √(9+16) = 5          (magnitude = the straight-line distance)

Netflix genres [Action, Comedy, Romance]:
A = [5, 4, 1]     reference (casual rater)         |A| ≈ 6.48
D = [10, 8, 2]    A's PERFECT TWIN (A doubled)     |D| ≈ 12.96
C = [2, 8, 100]   A's OPPOSITE (Romance fanatic)   |C| ≈ 100.3

dot:    A·D = 84    A·C = 142   → dot says C wins — WRONG (volume beat taste)
cosine: A,D = 1.00  A,C = 0.22  → cosine says D wins — RIGHT (heading only)
```

**The two lies of the raw dot product:** same direction different volume → wildly different
scores (`[1,1]·[1,1]=2` vs `[10,10]·[10,10]=200`); different directions → can give the SAME score
(`[1,0]·[5,0]=5` and `[5,5]·[1,0]=5`).

## Numpy twin

```python
import numpy as np
A, D, C = np.array([5,4,1]), np.array([10,8,2]), np.array([2,8,100])
cos = lambda a,b: (a@b)/(np.linalg.norm(a)*np.linalg.norm(b))
print("|A| =", round(np.linalg.norm(A),2))          # 6.48
print("dot  A·D =", A@D, "  A·C =", A@C)            # 84, 142  ← dot picks C (wrong)
print("cos  A,D =", round(cos(A,D),2), "  A,C =", round(cos(A,C),2))  # 1.0, 0.22 ← cosine picks D ✓
```

## Where it came from / where it goes

builds-on:: Pythagoras — magnitude is √(sum of squares), the same move in any dimension
feeds:: [[covariance]] — deviation columns are vectors; each covariance cell is their dot ÷ (n−1)
feeds:: [[regression]] — the neuron's core operation IS a dot product: `score = w·x`
feeds:: [[gradient-descent]] — the gradient is a vector; its magnitude = step size (gradient clipping caps it)
feeds:: [[attention]] — attention scores are query·key dot products, scaled by √d for the exact magnitude-contamination reason cosine fixes
used-by:: RAG vector search (s24) — cosine over embeddings is the retrieval backbone
scroll:: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] — §1–§6, the A/D/C walk
video:: [3B1B — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)

## Decision boundary

- ✅ **Magnitude** when you need one number for "how big/far/steep" — size, not similarity.
- ✅ **Dot product** ONLY when all vectors are ~the same length (unit-normalized), or raw activation strength is the point.
- ✅ **Cosine** the moment magnitudes vary — which in real data is always (some users rate 5 items, some 5,000).
- ❌ Cosine when direction is meaningless and size IS the signal (comparing two amplitudes).

## Traps I hit

![[trap-log#^vec-column]]

## Depth layers

- **2026-06-28 (F, hands-on lab):** magnitude → dot's two lies → cosine; the A/D/C and walking-bearing examples. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F]]
- **2026-06-29 (VS Code session):** the dimension snag — a vector is a COLUMN (2×1), standing up; my cols-of-first = rows-of-second rule was right, my arrow was lying down. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#12. 🧭 The learning flow — how we actually built this (the journey, wrong turns included)]]

## Project brick

One telemetry snapshot (temp, clock, latency…) IS a feature vector; the thermal forecaster's every
neuron computes `w·x` — **a dot product is the single instruction the whole model is made of** (the
MAC, in his silicon language).

## Formula

```
|v| = √(v₁² + … + vₙ²)                 magnitude — size, direction stripped
A·B = a₁b₁ + … + aₙbₙ                  dot — alignment, contaminated by size
cos(A,B) = A·B / (|A|·|B|)             cosine — divide out BOTH sizes, keep heading; range −1…+1
```

## Flashcards

#flashcards/vectors

Dot product ranked C=[2,8,100] above the perfect twin D=[10,8,2]. What lied, and what fixes it? :: C's ×100 magnitude bulldozed the score (volume beat taste). Cosine divides out both magnitudes: A·D→1.00, A·C→0.22.
When is raw dot product the RIGHT tool? :: When all vectors are ~same length (unit-normalized) — then magnitude can't distort ranking; it's also the raw op inside every neuron.
cos = 0 means what, geometrically and in ML terms? :: 90° apart — perpendicular, unrelated; zero taste overlap between the two vectors.
