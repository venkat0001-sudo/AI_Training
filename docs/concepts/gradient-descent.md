---
title: Gradient descent — the training rule
aliases: [gd, gradient, training-rule, weight-update, learning-rate, credit-assignment]
date: 2026-06-14
sessions: [F, s2]
lane: f
edge: 3
status: learning
type: concept
up: "[[MOC-foundation-math]]"
recap: "Fog on a mountain: feel the slope, step downhill, repeat. The training rule ∂L/∂w = 2(P−T)·x = error × input — and the ×x is credit assignment: a silent sensor's weight is never punished."
---

# Gradient descent — the training rule

> **Recap:** Fog on a mountain: feel the slope, step downhill, repeat. **The training rule
> ∂L/∂w = 2(P−T)·x = error × input** — and the ×x is credit assignment: a silent sensor's weight
> is never punished.

**Chain:** [[calculus]] ──► **gradient descent** ──► [[regression]] weights ──► backprop ([[neural-nets]]) ──► optimizers (s8: SGD/Adam/momentum)

## What it is (plain words)

You're on a mountain in fog (the loss surface), can't see the bottom. You CAN feel which way the
ground slopes. **Take a small step downhill, check again, repeat — that's the whole algorithm.**
The gradient (vector of partial derivatives) is the GPS saying "error decreases this way"; the
learning rate λ is your stride.

## The anchor numbers — one full thermal tick  ^anchor

```
2 sensors → predict controller temp 10s ahead:
  xA = 0.8 (IOPS load)   xB = 0.6 (norm. temp)   wA = 20   wB = 50   b = 20

① PREDICT   p = 20(0.8) + 50(0.6) + 20 = 66°C
② MEASURE   actual T = 80°C                       → under-called by 14° → throttle too LATE
③ LOSS      L = (66−80)² = 196
④ GRADIENTS error = 2(p−T) = −28
            ∂L/∂wA = −28·0.8 = −22.4    ∂L/∂wB = −28·0.6 = −16.8
⑤ UPDATE    (λ=0.1)  wA → 22.24 ↑    wB → 51.68 ↑    → next tick predicts hotter, closer to 80
```

**Sensor A's weight moved more than B's (−22.4 vs −16.8) because its input was louder (0.8 > 0.6)
— credit assignment, live.** The silent sensor (x=0) gets zero correction automatically: no
`if(asleep) skip`, the math zeroes it for free.

## Numpy twin

```python
import numpy as np
xA, xB, T, lr = 0.8, 0.6, 80.0, 0.1
wA, wB, b = 20.0, 50.0, 20.0
for t in range(25):
    p = wA*xA + wB*xB + b
    e = 2*(p - T)
    wA -= lr*e*xA;  wB -= lr*e*xB;  b -= lr*e
    if t in (0, 1, 24): print(f"tick {t:2d}: pred={p:6.2f}  loss={(p-T)**2:7.2f}")
# tick 0 pred≈66 loss≈196  →  tick 24 pred≈80 loss≈0   (it learned the true temp)
```

## Where it came from / where it goes

builds-on:: [[calculus]] — the gradient is computed BY the chain rule; ∂L/∂w = 2(P−T)·x is a two-link chain (∂L/∂p · ∂p/∂w)
builds-on:: [[vectors]] — the gradient IS a vector; its magnitude = step size (clipping caps it)
feeds:: [[regression]] — how linear & logistic weights get learned (batch/SGD/mini-batch, s2 §12)
feeds:: [[neural-nets]] — backprop = this update run through stacked layers
feeds:: optimizers (s8, 1 Aug) — SGD/momentum/Adam are THIS plus memory of past steps
contrasts-with:: closed-form least squares — one-shot, exact, but only exists for small linear problems; GD wins the moment the model is big or nonlinear
contrasts-with:: [[pca]] — PCA has no loss and no label; GD is loss-driven with the label in hand (opposite sides of the label-entry line)
scroll:: [[2026-07-05_chain-rule-to-gradient_F]] — §5–§7, the derivation + the thermal cycle
scroll:: [[2026-06-14_calculus-foundations_F]] — Hour 2 (gradient, loss, learning rate, local minima)
scroll:: [[2026-07-08_derivative-limit-to-gradient-descent_F]] — single-weight step by hand + the what-if tables (vary T / x / λ)

## Decision boundary

- ✅ Whenever the loss is differentiable and the parameter space is big — i.e., all of deep learning.
- ❌ NOT a one-shot solver: iterative, finds a LOCAL minimum (may not be global).
- ❌ When the problem is tiny and linear, closed-form wins — exact answer, no λ to tune (the Jun-20 notebook implements both to show the trade).
- **λ trade:** too big → overshoot and oscillate (the over-aggressive throttle); too small → calibration takes forever.

## Traps I hit

![[trap-log#^dpdw-w]]

## Depth layers

- **2026-06-14 (F):** fog-mountain intuition, gradient = GPS, learning rate, local minima. → [[2026-06-14_calculus-foundations_F]]
- **2026-06-28 (F):** first numeric loss-shrinking example (in the Bayes-session notes). → [[2026-06-25_bayes-and-ml-taxonomy_s1]]
- **2026-06-27 (s2):** the update rule DERIVED (h = −λf′ ⇒ loss must drop), batch vs SGD vs mini-batch, epochs vs iterations. → [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]] §10, §12
- **2026-07-05 (depth-gated):** derived the training rule BY HAND from the chain rule; the full 2-sensor thermal cycle; credit assignment owned. → [[2026-07-05_chain-rule-to-gradient_F]]
- **2026-07-08 (recall + depth-gate):** rebuilt the single-weight step from scratch after early stumbles (thermostat direction + credit assignment), and produced **what-if tables** — vary `T` (sign/direction), vary `x` (blame), vary `λ` (overshoot). Still owed: ONE→MANY weights = partial derivatives / gradient vector (watched, not rebuilt). → [[2026-07-08_derivative-limit-to-gradient-descent_F]]

## Project brick

**This IS the training engine of R1 (throttle predictor) and R2 (LSTM forecaster).** The anchor
tick reads in firmware terms: under-prediction → negative gradients → weights pushed up → predicts
hotter next tick → throttles earlier. He has shipped the embedded twin already: Vref read-level
calibration walking a BER valley is gradient descent in silicon.

## Formula

```
gradient = [∂L/∂w₁, ∂L/∂w₂, …]        points uphill; training steps OPPOSITE
TRAINING RULE:  ∂L/∂w = 2(p−T)·x      error × input
UPDATE:         w ← w − λ·∂L/∂w       λ = learning rate (stride)
```

## Flashcards

#flashcards/gradient-descent

Prediction 66°C, actual 80°C, sensor inputs 0.8 and 0.6, λ=0.1. Which weight moves more and why? :: wA (−28·0.8 = −22.4 vs −16.8) — correction scales with the input: the louder sensor earns more blame. Credit assignment.
The prediction came in too HOT (P > T). Which way do weights move? :: Gradient 2(P−T)·x is positive → descent SUBTRACTS → weights go down → predicts cooler. Self-correcting by sign.
When does closed-form beat gradient descent? :: Tiny linear problems — exact one-shot answer, no λ to tune. GD wins when the model is big/nonlinear (= all of deep learning).
