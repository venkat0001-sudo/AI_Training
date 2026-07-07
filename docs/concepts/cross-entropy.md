---
title: Cross-entropy — the loss derived from likelihood
aliases: [log-loss, cross-entropy-loss, likelihood, mle, maximum-likelihood, negative-log-likelihood]
date: 2026-06-27
sessions: [s2]
lane: m1
edge: 3
status: learning
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "Not decreed — DERIVED: maximize the likelihood of the logistic model, take the log (product→sum), flip the sign, and cross-entropy falls out. The loss every classifier (and every neural net) trains against."
---

# Cross-entropy — the loss derived from likelihood

> **Recap:** Not decreed — **DERIVED: maximize the likelihood of the logistic model, take the log
> (product→sum), flip the sign, and cross-entropy falls out.** The loss every classifier (and
> every neural net) trains against.

**Chain:** [[probability]] (independence → product) ──► likelihood ──► log ──► **cross-entropy** ──► THE loss of [[neural-nets]] (incl. QLoRA on-device, s20)
**Chain:** [[entropy]] (the suspense meter) ──► **cross-entropy** (suspense measured against the TRUE labels)

## What it is (plain words)

You want the θ that makes the observed labels **most probable**. Write that probability
(the likelihood), log it so the product becomes a sum, and maximize. **Minimizing cross-entropy
IS maximizing likelihood** — the standard classification loss has a derivation, not just a
definition.

## The anchor derivation  ^anchor

```
one formula, both classes:  P(y|x;θ) = LR(x)^y · (1−LR(x))^(1−y)     (y=1 picks left, y=0 right)
whole dataset (independent): L(θ) = ∏ᵢ LR(xⁱ)^yⁱ · (1−LR(xⁱ))^(1−yⁱ)
log it (product → sum):      log L = Σᵢ [ yⁱ·log LR(xⁱ) + (1−yⁱ)·log(1−LR(xⁱ)) ]   ← cross-entropy, negated
the gradient (clean!):       ∂logL/∂θⱼ = (yⁱ − LR(xⁱ)) · xⱼⁱ  =  (label − predicted prob) × input
```

**Same shape as the linear-regression gradient** (error × input) — one gradient grammar across
both regressions.

## Numpy twin

```python
import numpy as np
p = np.linspace(0.001, 0.999, 300)
loss_y1 = -np.log(p)          # true label = 1
import matplotlib.pyplot as plt
plt.plot(p, loss_y1); plt.xlabel('predicted P(y=1)'); plt.ylabel('loss when y=1')
plt.title('cross-entropy: confident-and-WRONG is punished brutally (p→0 ⇒ loss→∞)')
plt.show()
print("p=0.9 →", round(-np.log(0.9),3), "  p=0.5 →", round(-np.log(0.5),3), "  p=0.01 →", round(-np.log(0.01),2))
# 0.105 · 0.693 · 4.61 — the confident wrong answer costs 44× the confident right one
```

## Where it came from / where it goes

builds-on:: [[probability]] — the independence assumption is what turns the joint into a product
builds-on:: [[entropy]] — same −Σ p·log p machinery; entropy scores ONE distribution's mixedness, cross-entropy scores predictions against TRUE labels (formal boundary owed with the entropy resume)
builds-on:: [[regression]] — the model whose likelihood is being maximized is logistic regression
feeds:: [[neural-nets]] — THE classification loss of the whole DL half of the course
feeds:: KL divergence (M4 seed: [[kl-divergence]]) — cross-entropy = entropy + KL
contrasts-with:: MSE — regression's loss; use cross-entropy for class probabilities, MSE for numbers
scroll:: [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]] — §11 (S53–S56)

## Decision boundary

- ✅ Classification with probabilistic outputs — it punishes confident-wrong predictions brutally (−log 0.01 ≈ 4.6 vs −log 0.9 ≈ 0.1), which is exactly the pressure that calibrates confidence.
- ❌ Regression targets → MSE; and if labels are soft/noisy, blind confidence-punishment can over-fit label noise.

## Depth layers

- **2026-06-27 (s2):** derived from MLE, S53–S56; the clean (y−p)·x gradient. → [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]]
- **⏳ owed (entropy resume, before s4):** the formal entropy ↔ cross-entropy boundary, once [[entropy]]'s −Σp·log₂p lands.

## Project brick

**The loss of the R1 throttle/no-throttle classifier** — and later of every on-device network
down to QLoRA fine-tuning (s20). Training against it is what makes the model's "P(throttle)=0.92"
a calibrated number rather than a vibe.

## Formula

```
CE(y, p) = −[ y·log p + (1−y)·log(1−p) ]        minimize CE ⟺ maximize likelihood
∂/∂θⱼ = (p − y)·xⱼ                               error × input, again
```

## Flashcards

#flashcards/cross-entropy

Where does cross-entropy COME FROM (not what is it)? :: Maximize the likelihood of the logistic model → log turns the product into a sum → negate → cross-entropy. MLE in a trench coat.
Model says P=0.01 for the true class. Roughly what loss, vs P=0.9? :: −log(0.01) ≈ 4.6 vs −log(0.9) ≈ 0.105 — confident-and-wrong costs ~44× confident-and-right. That asymmetry IS the calibration pressure.
The logistic gradient came out as (y − p)·x. Why is that familiar? :: Same grammar as linear regression's 2(pred−y)·x — error × input, credit assignment included, across both regressions.
