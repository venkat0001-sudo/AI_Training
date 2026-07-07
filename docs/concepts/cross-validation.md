---
title: Validation & K-fold cross-validation
aliases: [k-fold, kfold, validation-set, holdout, train-test-split, early-stopping]
date: 2026-06-27
sessions: [s1]
lane: m1
edge: 2
status: learning
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "Training error only ever falls; validation error falls THEN RISES — stop at the dip. K-fold answers 'you want MORE of my precious data?!': the validation fold rotates, so every sample trains AND validates."
---

# Validation & K-fold cross-validation

> **Recap:** Training error only ever falls; **validation error falls THEN RISES — stop at the
> dip.** K-fold answers "you want MORE of my precious data?!": the validation fold rotates, so
> every sample trains AND validates.

**Chain:** [[ml-workflow]] (overfitting is the disease) ──► **validation/CV** (the alarm + the fix) ──► honest [[metrics]] ──► model/hyperparameter selection

## What it is (plain words)

Carve out a slice the model **never trains on** — its only job is to imitate the unseen future.
As model complexity (or training time) grows, training error keeps falling toward 0, but the
validation slice starts disagreeing: **its error bottoms out and turns back up. That dip is your
model.** Grading on data you tuned on is grading your own homework.

## The anchor numbers  ^anchor

```
The split: ~80% train / 20% test, with a validation holdout carved from the training side.

K-fold (K=10, S62): the validation fold SLIDES each round —
round 1 → 93%, round 2 → 90%, round 3 → 91%, …, round 10 → 95%
FINAL = average(all 10 rounds)   → every sample trained AND validated, nothing wasted

The U-curve: underfit (both errors high) → OPTIMAL (validation minimum ✓) → overfit
             (train error → 0 while validation error climbs)
```

## Numpy twin

```python
import numpy as np, matplotlib.pyplot as plt
rng = np.random.default_rng(1)
x = np.linspace(0, 1, 30); y = np.sin(2*np.pi*x) + rng.normal(0, .3, 30)
tr = rng.permutation(30)[:20]; va = np.setdiff1d(np.arange(30), tr)
degs = range(1, 15); tr_e, va_e = [], []
for d in degs:
    c = np.polyfit(x[tr], y[tr], d)
    tr_e.append(np.mean((np.polyval(c, x[tr]) - y[tr])**2) + 1e-12)   # ε keeps log-scale happy at perfect fits
    va_e.append(np.mean((np.polyval(c, x[va]) - y[va])**2) + 1e-12)
plt.semilogy(degs, tr_e, label='train (only falls)'); plt.semilogy(degs, va_e, label='validation (falls, then RISES)')
plt.axvline(degs[int(np.argmin(va_e))], ls='--'); plt.legend(); plt.xlabel('model complexity (degree)')
plt.title('pick the model at the validation dip'); plt.show()
```

## Where it came from / where it goes

builds-on:: [[ml-workflow]] — exists because "fit on train ≠ fit on test"; the validation slice is the unseen-world stand-in
feeds:: [[metrics]] — the score each fold reports is one of these; CV just averages it honestly
feeds:: hyperparameter tuning — how many iterations, what α, what depth: all chosen at the validation dip (early stopping included)
feeds:: [[ensembles]] — s4's bagging is fold-thinking turned into a modelling strategy (resample, train many, aggregate)
scroll:: [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]] — §13 (S60–62)

## Decision boundary

- ✅ Any time you choose between models/hyperparameters — the choice must be made on data the candidates never trained on.
- ✅ K-fold when data is precious (it always is) — every sample serves both roles across rounds.
- ❌ NOT on time-series with naive shuffling — random folds leak the future into training (telemetry! use time-ordered splits). 
- ❌ Never report the test-set score you also tuned on — that's the homework-grading trap again, one level up.

## Depth layers

- **2026-06-27 (s1):** the U-curve, early-stopping logic, the rotating-fold mechanic, the "10% more of my precious data?!" dialogue. → [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]]

## Project brick

**Validate the thermal model on DRIVES it never trained on** — the firmware translation is exact:
a GC heuristic tuned on one benchmark that falls apart on customer workloads is an overfit model
that skipped validation. For telemetry sequences, folds must respect time order.

## Formula

```
K-fold: train on (K−1) folds, validate on the 1 held out; rotate K times; report the average.
1 epoch = (dataset ÷ batch) iterations — stop training at the validation dip, not at train-error 0.
```

## Flashcards

#flashcards/cross-validation

Training error is still falling. Why would you EVER stop? :: Validation error already turned upward — past the dip you're memorizing noise. Train error falling is not evidence of learning; it's guaranteed.
The student objects: "validation steals 10% of my precious data!" The professor's answer? :: K-fold — the validation fold rotates each round, so every sample is used for training AND validation; final score = the average of the K rounds.
Why does naive K-fold break on your thermal telemetry? :: Shuffled folds leak the FUTURE into training (the model peeks ahead in time). Sequences need time-ordered splits.
