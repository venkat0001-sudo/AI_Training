---
title: Derivatives & the chain rule
aliases: [derivative, derivatives, chain-rule, slope, partial-derivative, u-substitution, instantaneous-slope]
date: 2026-06-14
sessions: [F]
lane: f
edge: 2
status: learning
type: concept
up: "[[MOC-foundation-math]]"
recap: "Derivative = instantaneous slope (speedometer, not trip average). Chain rule = rates MULTIPLY along a chain — the only tool that differentiates a composition, which is every ML gradient."
---

# Derivatives & the chain rule

> **Recap:** Derivative = instantaneous slope (speedometer, not trip average). **Chain rule =
> rates MULTIPLY along a chain** — the only tool that differentiates a composition, which is
> every ML gradient.

**Chain:** slope ──► **derivative** ──► partial derivatives ──► the gradient ──► [[gradient-descent]] ──► backprop ([[neural-nets]], s7)

## What it is (plain words)

Slope = change-in-output ÷ change-in-input; a derivative is that slope **at one exact point** —
your speedometer reads 60 km/h *right now*, not averaged over the trip. When a function nests
inside another (`y ← u ← x`), **the link-rates multiply:** `dy/dx = dy/du · du/dx`.

😄 Sleep → coffee → mood: each hour of sleep buys **2** cups; each cup buys **+3** mood ⇒ **6
mood per hour**. The link-rates (3 and 2) multiply. That's the entire chain rule in one image.

## The anchor numbers  ^anchor

```
y = (5x−2)³ → let u = 5x−2:
   du/dx = 5 (inner)   dy/du = 3u² (outer)   dy/dx = 3u²·5 = 15(5x−2)²   ← leave it FACTORED, done

The method: u-substitution — name the inner u, peel outer × peel inner. Don't expand.
```

**The three layers of knowing** (the honest map that gates depth): SEE it (3B1B intuition) →
SOLVE it (by hand — what the project needs) → BUILD it (the numpy twin). **Recognition ≠ ready
for a ⭐⭐⭐ brick.**

## Numpy twin

```python
import numpy as np
f  = lambda x: (2*x+1)**4
df = lambda x: 8*(2*x+1)**3           # my factored answer
h  = 1e-5
for x in [0, 1, 2]:
    num = (f(x+h)-f(x-h))/(2*h)       # numerical gradient-check — a REAL backprop debug tool
    print(f"x={x}: formula={df(x):.2f} numeric={num:.2f} match={np.isclose(df(x),num,rtol=1e-3)}")
# x=0: formula=8 numeric=8 ✓  (the wrong 8(4x+2)³ would give 64 — mismatch flags it)
```

## Where it came from / where it goes

builds-on:: slope — rise-over-run is the whole idea; the derivative just shrinks the run to a point
feeds:: [[gradient-descent]] — the gradient (vector of partial derivatives) is computed BY the chain rule; ∂L/∂w = 2(P−T)·x is a two-link chain
feeds:: [[neural-nets]] — backprop = this chain rule stacked across layers, computed thousands of times numerically
feeds:: [[regression]] — the s2 update rule (Slide 52's 2(F−y)·x) is this, derived
used-by:: every trained model — "which direction reduces error" is a derivative question
scroll:: [[2026-06-14_calculus-foundations_F]] — the 3-hour foundation walk (slope → derivative → gradient → chain rule)
scroll:: [[2026-07-05_chain-rule-to-gradient_F]] — the depth-gated drill, traps included
video:: 3B1B — Essence of Calculus ch 2–4 (layer-1 intuition ONLY; deliberately stops before SOLVE)

## Decision boundary

- ✅ Any "if I nudge this, how does that move?" question — and compositions REQUIRE the chain rule.
- ✅ Expanding + power rule is fine for a bare polynomial.
- ❌ The expand crutch dies the moment the function can't be expanded — `sigmoid(w·x+b)`, a layer, a loss over a prediction. That's every ML gradient. Learn the chain method, not the crutch.
- Two free sanity-checks: **degree-check** (deg f′ = deg f − 1) and **numerical gradient-check**.

## Traps I hit

![[trap-log#^expand-everything]]
![[trap-log#^degree-drop]]
![[trap-log#^coeff-power]]

## Depth layers

- **2026-06-14 (F, 3-hour block):** slope → derivative (speedometer) → partial derivatives → gradient-as-GPS → chain rule → computational graphs → backprop preview. → [[2026-06-14_calculus-foundations_F]]
- **2026-07-05 (self-study, depth-gated):** pushed from SEE to SOLVE+BUILD — 3 worked examples with my real traps, each rep's mistake smaller and more downstream ("can't start" → "just tidy-up" = what learning for real looks like). → [[2026-07-05_chain-rule-to-gradient_F]]

## Project brick

The chain rule is **the literal training engine of the R1 throttle predictor**: loss doesn't touch
the weight directly (loss ← prediction ← weight), and only the chain rule computes a rate through
that chain. Every gradient in the R2 LSTM forecaster is this, stacked.

## Formula

```
slope = Δoutput / Δinput               derivative = that, at ONE point
chain rule:  dy/dx = dy/du · du/dx     (rates multiply)
power (inner u):  d/dx uⁿ = n·uⁿ⁻¹ · du/dx
degree-check:  deg(f′) = deg(f) − 1
grad-check:    f′(x) ≈ [f(x+h) − f(x−h)] / 2h
```

## Flashcards

#flashcards/calculus

Differentiate y = (5x−2)³ — and name the trap that eats half the cohort. :: u-sub: 3u²·5 = 15(5x−2)². The trap: dropping the cube (u² not u³) gives a LINEAR answer — degree-check catches it (cubic's derivative must be quadratic).
Why can't you "just expand" your way through ML gradients? :: sigmoid(w·x+b) and friends don't expand — compositions need the chain rule; that's literally every loss-through-prediction gradient.
Sleep buys 2 coffees/hour, each coffee +3 mood. d(mood)/d(sleep)? :: 6 per hour — link-rates multiply. That IS the chain rule.
