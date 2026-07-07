---
title: Variance & standard deviation (σ)
aliases: [variance, standard-deviation, std-dev, sigma, σ, spread, deviations]
date: 2026-06-28
sessions: [F]
lane: f
edge: 3
status: owned
type: concept
up: "[[MOC-foundation-math]]"
recap: "σ = the typical distance a reading sits from the mean, in real units. Variance is neutral — a speedometer, not a judge: LOW = trustworthy, HIGH = informative; the question decides which you want."
---

# Variance & standard deviation (σ)

> **Recap:** σ = the typical distance a reading sits from the mean, in real units. **Variance is
> neutral — a speedometer, not a judge:** LOW = trustworthy, HIGH = informative; the question
> decides which you want.

**Chain:** mean ──► deviations ──► **variance/σ** ──► [[normal-distribution]] ──► z-scores
**Chain:** **variance** ──► [[covariance]] (the diagonal) ──► [[eigenvectors]] ──► [[pca]]

## What it is (plain words)

Deviations = each value's distance from the mean (a signed list, always sums to 0). Variance =
the average of the squared deviations (one number, squared units). **σ = √variance — the same
spread, back in units a human can read and put on a datasheet.**

## The anchor numbers  ^anchor

```
Drive A (steady):  [98, 100, 102, 99, 101]     Drive B (jittery): [80, 120, 90, 110, 100]
mean A = 100                                   mean B = 100          ← IDENTICAL means!
dev A:  −2, 0, +2, −1, +1                      dev B: −20, +20, −10, +10, 0
var A = 10/4  = 2.5   σ_A ≈ 1.58 µs            var B = 1000/4 = 250   σ_B ≈ 15.81 µs
→ 100 ± 1.6: steady ✅                          → 100 ± 16: jitter-bomb 🔥
```

**The mean said "identical drives." σ exposed the lie** — Drive B's fat σ is the p99 tail blowout,
the QoS support ticket the average hid.

Second anchor — the sensor-selection pair: ^anchor-yesman
```
Sensor A (voltage rail): [3.30, 3.30, 3.31, 3.30, 3.30]  var ≈ 0.00002  → yes-man, tells nothing, DROP
Sensor B (die temp):     [42, 55, 71, 63, 88]            var ≈ 297.7    → the throttling story lives here, KEEP
```

## Numpy twin

```python
import numpy as np
A = np.array([98,100,102,99,101]); B = np.array([80,120,90,110,100])
for name, d in (("A",A), ("B",B)):
    print(name, "mean", d.mean(), " var", d.var(ddof=1), " σ", round(d.std(ddof=1),2))
# A: mean 100.0  var 2.5    σ 1.58   ← same mean...
# B: mean 100.0  var 250.0  σ 15.81  ← ...σ is the whole story
```

## Where it came from / where it goes

builds-on:: the mean — deviations are measured against ONE referee (value − mean), never value-vs-neighbour
feeds:: [[normal-distribution]] — μ sets the bell's peak, σ sets its width; the bell IS σ drawn as a shape
feeds:: [[covariance]] — variance is covariance of a feature with ITSELF; that's why variances sit on the diagonal
feeds:: [[pca]] — "importance" in PCA = variance along a direction; the trust-vs-importance flip lives there
used-by:: feature selection — near-zero-variance features are deletable dead weight (cost SRAM/MACs, add nothing)
scroll:: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] — §15 (the full drill), §17 (trust vs importance)
video:: [StatQuest — The Normal Distribution](https://www.youtube.com/watch?v=rzFX5NWojp0)

## Decision boundary

- ✅ **raw deviation** — you care about ONE point (how big is this outlier?).
- ✅ **σ** — you want the typical spread in real units (thresholds, ±, datasheets).
- ✅ **variance (σ²)** — inside math machinery ([[covariance]], optimization) where squared form combines cleanly.
- ❌ Never read variance as good/bad by itself: **LOW wins the reliability question, HIGH wins the information question** — same number, different verdicts.

## Why we square (the L2 flavour)

Average the RAW deviations → always 0 (below cancels above — the mean is the balance point,
rigged in every dataset). **Square first → no cancellation, and big misses get punished extra**
(dev 20 → 400, dev 10 → 100). Absolute value would be L1: kills signs but treats all gaps evenly.

## Traps I hit

![[trap-log#^mean-max]]
![[trap-log#^sigma-fence]]

## Depth layers

- **2026-06-28 (F):** variance built inside the covariance walk (votes, §7). → [[2026-06-28_linear-algebra-vectors-dot-cosine_F]]
- **2026-06-30 (F, the hard drill):** deviations→square→σ ladder; two-drive anchor; **the trust-vs-importance reconciliation** (speedometer, not judge); yes-man sensor. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#15. Variance & Standard Deviation — the FULL deep-dive (2026-06-30)]]

## Project brick

Sensor triage for the thermal forecaster: **the flat 3.30 V yes-man rail gets dropped; the swinging
die-temp channel (var ≈ 297.7) is where the throttling story lives.** σ of the temperature channel
is also the jitter the forecaster must not confuse with trend.

## Formula

```
deviation_i = x_i − x̄                       signed; Σ deviations = 0 (built-in spell-check)
variance    = Σ (x_i − x̄)² / (n−1)          squared units; n−1 = sample shyness correction
σ           = √variance                      real units — "typically x̄ ± σ"
```

## Flashcards

#flashcards/variance-sigma

Two drives both average 100 µs. What number exposes the jitter-bomb, and what were its two values? :: σ — Drive A σ≈1.58 (steady), Drive B σ≈15.81 (p99 blowout). The mean hid it completely.
Why square deviations instead of just averaging them? :: Raw deviations ALWAYS sum to 0 (mean = balance point). Squaring kills cancellation and punishes big misses extra (L2 flavour).
A feature reads [50,50,50,50]. Trust verdict vs training verdict? :: Trust: GOOD (rock-steady). Training: DROP — zero discriminating power by construction, still costs SRAM/MACs. Variance is a speedometer, not a judge.
