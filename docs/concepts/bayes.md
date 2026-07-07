---
title: Bayes' theorem — flip the conditional
aliases: [bayes-theorem, posterior, prior, base-rate, bayes-rule]
date: 2026-06-25
sessions: [s1]
lane: f
edge: 2
status: due
type: concept
up: "[[MOC-foundation-math]]"
recap: "The datasheet gives P(HOT|Real); the field moment needs P(Real|HOT). Bayes is the bridge — and with rare events, a 90% sensor earns only 50% trust (the base-rate trap)."
---

# Bayes' theorem — flip the conditional

> **Recap:** The datasheet gives P(HOT|Real); the field moment needs P(Real|HOT). **Bayes is the
> bridge — and with rare events, a 90% sensor earns only 50% trust (the base-rate trap).**

**Chain:** [[probability]] ──► **Bayes** ──► [[ml-taxonomy]] (classifier outputs ARE posteriors; thresholds are Bayes decisions) ──► [[naive-bayes]]

## What it is (plain words)

You know how often the sensor catches a real event (the spec). You want the reverse: **the alarm
just fired — how likely is it real?** Bayes flips the conditional by counting bodies: the one
real-alarm bucket, divided by every way the alarm could fire.

## The anchor numbers — the 200-cycle table  ^anchor

```
                Real Event   No Event   Total
Sensor HOT          18          18        36     ← equal buckets = the punchline
Sensor NORMAL        2         162       164
Total               20         180       200

base rate P(Real) = 10%   detection P(HOT|Real) = 90%   false-alarm P(HOT|NoEvent) = 10%

P(Real|HOT) = 0.90×0.10 / (0.90×0.10 + 0.10×0.90) = 0.09/0.18 = 0.50  →  50% trust. Coin flip.
```

**Rarity is the villain:** 9× more calm cycles means even 10% noise produces as many false alarms
as the 90% sensor produces real catches. Make real events rarer → trust collapses further (~22%).

## Numpy twin

```python
p_real, p_hot_given_real, p_hot_given_calm = 0.10, 0.90, 0.10
top = p_hot_given_real * p_real
bottom = top + p_hot_given_calm * (1 - p_real)
print(f"P(Real|HOT) = {top/bottom:.2f}")        # 0.50 — the 90% sensor is a coin flip
for p_real in (0.10, 0.03, 0.01):               # watch trust collapse as events get rarer
    t = 0.9*p_real; print(f"base {p_real:.0%} → trust {t/(t+0.1*(1-p_real)):.0%}")
```

## Where it came from / where it goes

builds-on:: [[probability]] — Bayes IS conditional probability, rearranged
builds-on:: [[normal-distribution]] — the likelihoods it multiplies are often areas under bells
feeds:: [[ml-taxonomy]] — classifier outputs are posteriors; a decision threshold is a Bayes decision
feeds:: [[naive-bayes]] — the classifier built directly on this theorem
feeds:: evaluation metrics (s1) — precision vs recall IS the base-rate story wearing a confusion matrix
scroll:: [[2026-06-25_bayes-and-ml-taxonomy_s1]] — §①, the full bucket walk
twin-page:: [Bayes & taxonomy page](../html/2026-06-25_bayes-and-ml-taxonomy_s1.html)

## Decision boundary

- ✅ Bayes wins when real events are RARE and the detector is imperfect — exactly when "HOT ⇒ throttle" drowns in false alarms.
- ❌ Fixed threshold wins when the rule is simple, known, and hard (datasheet says 95°C is a hard limit — don't compute a posterior for a certainty).

## Traps I hit

![[trap-log#^base-rate]]

## Depth layers

- **2026-06-25 (s1 prep):** the flip, the 200-cycle table, the base-rate trap, the shape (one real bucket ÷ all alarm buckets). → [[2026-06-25_bayes-and-ml-taxonomy_s1]]

## Project brick

**The R1 throttle predictor must carry the base rate:** a controller that ignores how rare real
thermal events are will throttle on noise and tank performance. (And he ships Bayes already —
LDPC soft-decision decoding is prior → evidence → posterior in silicon.)

## Formula

```
P(Real|HOT) = P(HOT|Real)·P(Real) / [ P(HOT|Real)·P(Real) + P(HOT|NoEvent)·P(NoEvent) ]
shape: posterior = (the one real-alarm bucket) ÷ (every alarm bucket summed)
```

## Flashcards

#flashcards/bayes

A 90%-accurate sensor fires on a 10%-base-rate event. Trust? :: 50% — 18 real alarms vs 18 false alarms out of 200 cycles. Rarity manufactures false alarms faster than accuracy kills them.
The datasheet gives you P(HOT|Real)=0.9. Why isn't that your answer in the field? :: That's hardware-direction (given real, does it fire?). The field needs P(Real|HOT) — given it fired, is it real? Bayes flips it, and the base rate decides.
When should you NOT bother with a posterior? :: When the rule is known and hard — 95°C datasheet hard-limit. Bayes earns its keep only under rarity + imperfect detection.
