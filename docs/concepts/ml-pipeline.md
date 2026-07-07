---
title: The ML pipeline — which math powers which box
aliases: [pipeline, label-entry-line, six-box-pipeline, pipeline-map]
date: 2026-07-02
sessions: [F]
lane: f
edge: 2
status: owned
type: concept
up: "[[MOC-foundation-math]]"
recap: "Six boxes, one label-entry line: features → PCA (linear algebra, NO label) ══ label enters ══ model → loss → gradient descent (calculus, label in hand). Know which math powers which box and half the course untangles."
---

# The ML pipeline — which math powers which box

> **Recap:** Six boxes, one label-entry line: **features → PCA (linear algebra, NO label) ══
> label enters ══ model → loss → gradient descent (calculus, label in hand).** Know which math
> powers which box and half the course untangles.

**Chain:** data ──► [[vectors]]/[[covariance]]/[[pca]] prep ──► ══ THE LABEL-ENTRY LINE ══ ──► [[regression]] model ──► loss ([[cross-entropy]]/MSE) ──► [[gradient-descent]] ──► [[metrics]]/[[cross-validation]] ──► edge deployment ([[mcu-deployment]])

## The anchor — the house-price flow  ^anchor

```
[1] 20 raw house features ─┐
[2] PCA (covariance→eigen) │  math: LINEAR ALGEBRA   label? NO  ← UNSUPERVISED (recipe weights)
════════════ ⬇ LABEL (price) ENTERS HERE ⬇ ════════════
[3] model: price = w₁c₁+…+b│  math: LINEAR ALGEBRA
[4] loss = (guess − price)²│  math: CALCULUS+PROB    label? YES ← SUPERVISED
[5] gradient descent       │  → PREDICTION weights
[6] trained weights w₁..b ─┘  the model is built
```

**The misconception this map killed:** "PCA is like gradient descent — it also reduces a loss."
No — boxes [2] and [5] sit on opposite sides of the label line. ![[trap-log#^pca-loss]]

## Where it came from / where it goes

builds-on:: every foundation atom — this is the shelf they all sit on
feeds:: the Daily Compass — every new concept opens with "we are HERE on this map"
scroll:: [[2026-07-02_ml-pipeline-math-map_F]] — the full map doc (phase × math master table, concept→algorithm cheat-table)
used-by:: [[pca]] · [[gradient-descent]] · [[regression]] — their contrasts-with links resolve against this line

## Decision boundary

- ✅ Open ANY new topic by placing it on this strip — which box, which math, which side of the label line.
- ❌ A concept you can't place here is a concept you'll misapply (the whole point of the map).

## Flashcards

#flashcards/ml-pipeline

Where exactly does the label enter the pipeline, and what changes there? :: Between feature-prep (PCA — unsupervised, recipe weights) and the model/loss/GD boxes (supervised, prediction weights). Everything before the line never sees the answer.
Which math powers box [4]–[5], and which powers box [2]? :: Loss + gradient descent = calculus (+probability for cross-entropy); PCA prep = pure linear algebra (covariance → eigenvectors).
