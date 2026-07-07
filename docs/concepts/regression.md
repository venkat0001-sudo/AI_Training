---
title: Linear & logistic regression — the first predictor, and the neuron
aliases: [linear-regression, logistic-regression, sigmoid, log-odds, odds, perceptron, neuron, bias-term, regularization, ridge, lasso]
date: 2026-06-27
sessions: [s2]
lane: m1
edge: 3
status: learning
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "Linear: predict the raw line value w·x+b. Logistic: the log of the ODDS is a linear function of the features — run Z through the sigmoid and out comes a probability. A single neuron IS logistic regression."
---

# Linear & logistic regression — the first predictor, and the neuron

> **Recap:** Linear: predict the raw line value `w·x+b`. Logistic: **the log of the ODDS is a
> linear function of the features** — run Z through the sigmoid and out comes a probability.
> **A single neuron IS logistic regression.**

**Chain:** [[vectors]] (dot = the neuron's core op) ──► **regression** ──► [[neural-nets]] (stack the neuron, s7)
**Chain:** [[ml-taxonomy]] ──► **regression** (first ML citizen) ──► trained by [[gradient-descent]] against [[cross-entropy]]/MSE

## What it is (plain words)

One machine, two read-outs. Compute the weighted score `Z = w·x + b`. **Read the raw value →
linear regression (predict a number). Squash it through the S-curve → logistic regression
(predict a probability).** The decision boundary is where Z = 0 — a hyperplane whose normal is
the weight vector.

## The anchor numbers  ^anchor

```
THE MODEL (S36, the ⭐⭐⭐ line):   log( P/(1−P) ) = θ₀ + θ₁x₁ + … + θₙxₙ = Z
rearranged:                       P(y=1|x) = e^Z/(1+e^Z) = sigmoid(Z)

sigmoid landmarks: crosses 0.5 at Z=0 · →1 as Z→∞ · →0 as Z→−∞
boundary: Z = 0 (P=0.5) — a STRAIGHT line; make Z polynomial ⇒ curved boundary

the update rule, derived (S47–50): set step h = −λ·f'(a) ⇒ loss change ≈ −λ(f'(a))² ≤ 0, always downhill
                                   a ← a − λ·f'(a)
linear-regression gradient (S52):  ∂E/∂θⱼ = 2·Σ(F(xⁱ)−yⁱ)·xⱼⁱ = 2 × error × input
```

**The XOR wall (S24):** a single perceptron draws ONE straight boundary — AND/OR separable, XOR
not (Minsky & Papert 1969 → the AI winter). The fix is stacking → [[neural-nets]].

**Regularization (S27–29):** penalize weight size. **L2 (ridge) = parabola** near zero, slope→0,
shrinks-never-zeroes; **L1 (lasso) = the V**, constant slope, drives weights to EXACTLY 0 →
sparsity/feature selection. Elephant warning: "with four parameters I can fit an elephant" (von
Neumann). ^anchor-regularization

## Numpy twin

```python
import numpy as np, matplotlib.pyplot as plt
z = np.linspace(-6, 6, 200)
p = np.exp(z)/(1+np.exp(z))
plt.plot(z, p); plt.axvline(0, ls='--'); plt.axhline(0.5, ls='--')
plt.title('sigmoid: crosses 0.5 exactly at Z=0 — the boundary'); plt.show()
# logistic gradient check: (label − predicted prob) × input
y, x = 1, 2.0
for th in (0.0, 1.0, 3.0):
    pred = 1/(1+np.exp(-th*x))
    print(f"θ={th}: pred={pred:.3f}  grad=(y−p)·x={ (y-pred)*x :+.3f}")  # shrinks toward 0 as pred→label
```

## Where it came from / where it goes

builds-on:: [[vectors]] — the score IS a dot product; a neuron fires hardest when input aligns with its weight vector (r⃗·w⃗ = |r||w|cosθ)
builds-on:: [[ml-taxonomy]] — the first citizens of classic ML; weights learned, not hand-set
trained-by:: [[gradient-descent]] — batch/SGD/mini-batch (mini-batch stamped "PRACTICAL AND USEFUL"); 1 epoch = (dataset ÷ batch) iterations
feeds:: [[cross-entropy]] — maximizing the likelihood of the logistic model IS minimizing cross-entropy (derived, not decreed)
feeds:: [[neural-nets]] — a layer = many logistic regressions; XOR forces the stack
contrasts-with:: [[trees-svm]] — the sibling clan: axis-aligned if/else cuts vs one smooth hyperplane
scroll:: [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]] — the 62-slide master walk

## Decision boundary

- ✅ **Linear** when the target is a NUMBER and the relationship is roughly straight (+ closed-form exists for small problems).
- ✅ **Logistic** when you need a PROBABILITY with a confidence read-out, cheap inference, explainable weights.
- ❌ Neither draws curved boundaries with raw features — polynomial Z or stacked neurons buy curvature (at overfit risk: the elephant).
- ❌ Linear regression for probabilities — the line escapes [0,1]; that's the whole reason the sigmoid exists.

## Depth layers

- **2026-06-27 (s2):** the full arc — neuron history (MP 1943 → perceptron 1958), dot-as-core-op, wᵀx=0 geometry, bias-fold trick, XOR/AI-winter, polynomial + L1/L2, sigmoid/odds/log-odds, GD update derived, MLE→cross-entropy, batch/SGD/mini-batch. → [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]]
- **2026-07-05 (F):** the s2 Slide-52 rule `2(F−y)·x` re-derived by hand from the chain rule. → [[2026-07-05_chain-rule-to-gradient_F]]

## Project brick

**R1 candidate #1: a logistic throttle/no-throttle classifier** — SRAM-sized, nanosecond
inference, weights a firmware reviewer can read (`0.7·temp + 0.4·workload…`), trained against
[[cross-entropy]] with the base-rate lesson from [[bayes]] in hand.

## Formula

```
linear:    y′ = w·x + b                     logistic:  P(y=1|x) = sigmoid(θᵀx)
THE MODEL: log(P/(1−P)) = θᵀx = Z           boundary:  Z = 0  (P = 0.5)
update:    θⱼ ← θⱼ − r·∂L/∂θⱼ               lin-reg gradient: 2·Σ(pred−y)·xⱼ
ridge L2:  MSE + α·½Σθᵢ²  (shrinks)         lasso L1:  MSE + α·Σ|θᵢ|  (zeroes → sparsity)
```

## Flashcards

#flashcards/regression

State THE MODEL of logistic regression in one sentence. :: The log of the odds is a LINEAR function of the features: log(P/(1−P)) = θᵀx — sigmoid just rearranges it back to a probability.
Why does L1 zero weights while L2 only shrinks them? :: Near zero L2 (parabola) has slope→0 — pressure fades; L1 (the V) keeps CONSTANT slope all the way → weights hit exactly 0 → free feature selection.
Why can't one perceptron learn XOR, and what fixed it? :: One perceptron = ONE straight boundary; XOR's 1s sit on opposite corners (needs two lines). Stacking neurons into layers (s7) buys curved boundaries — after a 20-year AI winter.
