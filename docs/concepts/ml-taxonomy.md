---
title: The ML bloodline — AI → ML → classic/deep
aliases: [ai-vs-ml, classic-vs-deep, ml-bloodline, rule-based, features-vs-weights, ml-family-tree]
date: 2026-06-25
sessions: [s1]
lane: m1
edge: 1
status: due
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "Two dividing lines: WHO WRITES THE LOGIC (human → rule-based, machine → ML) and WHO FINDS THE FEATURES (you → classic, the network → deep). Rule-based sits OUTSIDE ML."
---

# The ML bloodline — AI → ML → classic/deep

> **Recap:** Two dividing lines: **WHO WRITES THE LOGIC** (human → rule-based, machine → ML) and
> **WHO FINDS THE FEATURES** (you → classic, the network → deep). Rule-based sits OUTSIDE ML.

**Chain:** rule-based `if(temp>90)` ──► **ML** (learns weights from data) ──► classic ([[regression]], [[trees-svm]], [[ensembles]], [[kmeans]]/[[pca]]) ──► deep ([[neural-nets]], CNN, RNN, [[attention]])

*(⭐ course-only grade — keep this atom lean; it's the map, not a destination.)*

## What it is (plain words)

The family tree the whole course walks. **The trap: "classic ML = rule-based." It isn't** —
rule-based (hand-coded if/else, no learning) sits outside ML entirely. The Jun-20 linear
classifier *learned* its weights via [[gradient-descent]] → classic ML, not rule-based.

## The anchor  ^anchor

```
AI ────────────────────────────────────────────────┐
│  Rule-based: hand-coded if/else — NO learning    │
│  ML — learns weights FROM DATA ────────────────┐ │
│  │  Classic ML             Deep Learning       │ │
│  │  (you pick features)    (network finds them)│ │
│  └─────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘

Boundary 1: WHO WRITES THE LOGIC?    human → rule-based · machine → ML
Boundary 2: WHO FINDS THE FEATURES?  you → classic · the network, in layers → deep
```

**Features vs weights (the vocab that bites in class):** feature = the input column you feed in
(temp, P/E, workload); weight/parameter = how much each counts — **always learned**, never
hand-set. Anchor: `score = 0.7·temp + 0.2·cycles + 0.05·retention + 0.4·workload` — the 0.7 is
the model discovering temp matters most.

## Where it came from / where it goes

builds-on:: [[bayes]] — classifier outputs are posteriors; thresholds are Bayes decisions
feeds:: [[regression]] — the first ML citizens (s2); a single neuron IS logistic regression
feeds:: [[trees-svm]] — the sibling clan: a trained tree is firmware whose constants were learned
feeds:: [[neural-nets]] — cross the classic→deep line by stacking the neuron into layers
contrasts-with:: rule-based firmware — same runtime if/else, but thresholds came from data, not the datasheet
scroll:: [[2026-06-25_bayes-and-ml-taxonomy_s1]] — §②–§⑤

## Decision boundary

- ✅ **Classic ML:** clean tabular features, limited memory/compute, explainability, small-to-medium data — *the likely winner for the on-device throttle (SRAM-sized tree or logistic model)*.
- ✅ **Rule-based:** logic fully known, fixed, small (`if(temp>95) shutdown` — the datasheet already told you).
- ❌ **Deep learning** only earns its cost on massive RAW data (images/audio/text) where hand-engineering features is hopeless.

## Depth layers

- **2026-06-25 (s1 prep):** the bloodline, two dividing lines, trained-tree-vs-firmware, features-vs-weights. → [[2026-06-25_bayes-and-ml-taxonomy_s1]]

## Project brick

The throttle predictor's family decision, made on day one: **classic ML first (R1 = tree/logistic
in SRAM, nanosecond inference, explainable to a firmware reviewer); deep (R2 LSTM) only when the
sequence signal demands it.**

## Flashcards

#flashcards/ml-taxonomy

Your trained decision tree compiles to nested if/else — so is it rule-based? :: No. The runtime LOOK is identical; the dividing line is who set the thresholds — the algorithm proved 85°C separates the data; the datasheet didn't.
Name the two dividing lines of the bloodline. :: (1) Who writes the logic? human→rule-based, machine→ML. (2) Who finds the features? you→classic, network→deep.
Feature vs weight, one breath each. :: Feature = the input column you feed (temp, P/E). Weight = how much it counts — always LEARNED; if a human set it, it isn't learning.
