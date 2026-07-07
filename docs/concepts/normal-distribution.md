---
title: Normal distribution — the bell, σ bands, z-scores
aliases: [bell-curve, gaussian, z-score, 68-95-99.7]
date: 2026-06-07
sessions: [F]
lane: f
edge: 3
status: owned
type: concept
up: "[[MOC-foundation-math]]"
recap: "The bell is σ drawn as a shape: peak at μ, width set by σ. ±1σ≈68%, ±2σ≈95%, ±3σ≈99.7% — and ±1σ is NOT the outlier fence (1 in 3 readings lives outside it by design)."
---

# Normal distribution — the bell, σ bands, z-scores

> **Recap:** The bell is [[variance-sigma|σ]] drawn as a shape: peak at μ, width set by σ.
> ±1σ≈68%, ±2σ≈95%, ±3σ≈99.7% — and **±1σ is NOT the outlier fence (1 in 3 readings lives outside
> it by design).**

**Chain:** [[variance-sigma]] ──► **the bell** ──► z-scores / standardization ──► [[probability]] (areas ARE probabilities) ──► [[bayes]]

## What it is (plain words)

The shape most noisy real-world readings pile into: **most values crowd the mean, fewer live in
the tails, symmetrically.** Small σ → razor-thin spike (steady drive); big σ → wide hill (jittery
drive). It's the picture of σ.

## The anchor numbers  ^anchor

The jittery drive from [[variance-sigma#^anchor|the two-drive anchor]]:

```
Drive B: μ = 100, σ = 15.81 µs

±1σ = 84.2 – 115.8   ≈ 68%  of reads   → 80 & 120 fall OUTSIDE ±1σ... normal! (1 in 3 does)
±2σ = 68.4 – 131.6   ≈ 95%             → 80 & 120 sit INSIDE → normal jitter, NOT outliers
±3σ = 52.6 – 147.4   ≈ 99.7%           → a 150+ µs read = dead-tail → go investigate

z-score of the 80 µs read: (80 − 100)/15.81 = −1.26σ    (band-position as one number)
```

## Numpy twin

```python
import numpy as np, matplotlib.pyplot as plt
mu, sigma = 100, 15.81
x = np.linspace(40, 160, 400)
y = np.exp(-(x-mu)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
plt.plot(x, y)
for k, c in ((1,'gold'), (2,'orange'), (3,'red')):
    plt.axvspan(mu-k*sigma, mu+k*sigma, alpha=.12, color=c, label=f'±{k}σ')
plt.axvline(80, ls='--'); plt.title('Drive B latency bell: μ=100, σ=15.81 — 80µs is only −1.26σ')
plt.legend(); plt.show()
print("z(80) =", round((80-mu)/sigma, 2))   # −1.26 ✓ inside ±2σ → not an outlier
```

## Where it came from / where it goes

builds-on:: [[variance-sigma]] — μ sets the peak, σ sets the width; no σ, no bell
feeds:: [[probability]] — the area under a slice of the bell IS the probability a reading lands there
feeds:: [[bayes]] — those areas become the likelihoods Bayes multiplies
feeds:: standardization — z = (x−μ)/σ on every value → mean 0, σ 1 → °C and mV channels on equal footing before [[covariance]]/[[pca]]
used-by:: anomaly detection — beyond ±3σ = off-distribution = "go investigate" (ECC retry, read-disturb, throttle)
scroll:: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] — §16 (the bell as σ's shape)
twin-page:: [bell-curve σ/latency page](../html/2026-06-30_bell-curve-sigma-latency_F.html) · [normal_distribution page](../html/normal_distribution.html) — html/ sits outside the docs vault, so these are relative markdown links, not wikilinks
video:: [StatQuest — The Normal Distribution](https://www.youtube.com/watch?v=rzFX5NWojp0)

## Decision boundary

- ✅ Reason in σ-bands whenever data is roughly bell-shaped: thresholds, guard-bands, outlier fences (±2σ/±3σ), comparing readings across different scales (z-scores).
- ❌ NOT when the data is skewed/multi-modal (GC-stall latency tails!) — percentiles (P99) beat σ there, which is exactly why NVMe QoS specs quote percentiles, not σ.

## Traps I hit

![[trap-log#^sigma-fence]]

## Depth layers

- **2026-06-07 (F, first contact):** bell basics, 68-95-99.7 — anchored in the bell-curve HTML pages.
- **2026-06-30 (F, rebuild):** the bell re-derived FROM the σ drill (raw readings → mean → deviations → variance → σ → "what does σ LOOK like?" → the bell); the ±1σ-fence trap caught. → [[2026-06-28_linear-algebra-vectors-dot-cosine_F#16. The Bell Curve — σ drawn as a SHAPE]]

## Project brick

The thermal model's anomaly fence: **a die-temp reading beyond ±3σ of its recent window = thermal
event candidate** — and z-scoring every telemetry channel is the standardization step before any
[[covariance]]/[[pca]] compression feeds the forecaster.

## Formula

```
z = (x − μ) / σ            how many σ from the mean (comparable across drives/channels)
±1σ ≈ 68%   ±2σ ≈ 95%   ±3σ ≈ 99.7%
```

## Flashcards

#flashcards/normal-distribution

A read lands outside ±1σ. Alarm? :: No — ~1 in 3 readings falls outside ±1σ BY DESIGN. Outliers live beyond ±2σ/±3σ. (Drive B's 80 µs = −1.26σ = normal jitter.)
What does the area under a slice of the bell mean? :: The probability a reading lands in that slice — the bridge from statistics to probability and Bayes.
When do percentiles beat σ-bands? :: Skewed/multi-modal data — e.g. GC-stall latency tails; that's why NVMe QoS quotes P99, not σ.
