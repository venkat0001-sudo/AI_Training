---
title: The ML workflow — data → model → loss → optimize
aliases: [eda, preprocessing, imputation, outlier-handling, curse-of-dimensionality, overfitting, underfitting, inductive-bias, workflow]
date: 2026-06-27
sessions: [s1]
lane: m1
edge: 2
status: learning
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "Y = F(X, W): fix F (the architecture), then the whole ML problem is 'from the data, find W — then freeze it.' Four steps: collect labelled data → design model → define loss → optimize. Fit on training data ≠ fit on test data."
---

# The ML workflow — data → model → loss → optimize

> **Recap:** **Y = F(X, W): fix F (the architecture), then the whole ML problem is "from the
> data, find W — then freeze it."** Four steps: collect labelled data → design model → define
> loss → optimize. Fit on training data ≠ fit on test data.

**Chain:** [[ml-taxonomy]] ──► **the workflow** ──► loss ([[cross-entropy]]/MSE) ──► [[gradient-descent]] ──► [[metrics]] + [[cross-validation]]

## What it is (plain words)

Every ML project is the same four-step cycle: **(1) collect a labelled dataset, (2) design the
model, (3) define the loss, (4) optimize the weights.** The professor's framing that locks it:
a model is a mathematical function `Y = F(X, W)` — ChatGPT included: "they optimized W on huge
data, froze W, gave you the model; you just supply your input."

## The anchor numbers  ^anchor

```
The three fits (S58 — the punchline of the section):
Case 1: 1st-order poly  → UNDERFIT   (too simple, misses the trend)
Case 2: 10th-order poly → GOOD FIT   (captures trend, ignores noise)  ← the professor's green "Good"
Case 3: 40th-order poly → OVERFIT    (threads every training point, "Bad o/p" on anything new)

"With four parameters I can fit an elephant, and with five I can make him wiggle his trunk." — von Neumann
(Fermi had used 20. A 2010 paper literally drew the elephant with 4 complex parameters.)
```

**Data challenges (the messy-reality checklist):** never drop missing rows — data is precious,
**impute** (mean/median/model); **errors destroy information, artifacts CREATE false information**
(the fintech team merging $/€/₹ without converting); **outliers are interesting, not noise** — a
different mechanism generated them, but Σ-losses have no discrimination so one "HERE I AM" point
drags the whole fit; **curse of dimensionality** — the points that cover a 1-D line become sparse
blind-spots in 2-D, so more dimensions demand explosively more data AND a more complex model
(prefer [[pca|dimensionality reduction]]; "3×income" adds zero information). ^anchor-datachallenges

**Inductive bias (the squirrel parable):** the squirrel is brilliant at trees, hopeless at water;
the duck is the reverse. **Every model has built-in strengths — CNNs see, Transformers sequence —
so for every new problem ask: does this model's strength match?** No amount of optimization saves
a mismatched F.

## Numpy twin

```python
import numpy as np, matplotlib.pyplot as plt
rng = np.random.default_rng(0)
x = np.linspace(0, 1, 15); y = np.sin(2*np.pi*x) + rng.normal(0, .25, 15)
xs = np.linspace(0, 1, 200)
for deg, style in ((1,'--'), (10,'-'), (14,':')):
    c = np.polyfit(x, y, deg)
    plt.plot(xs, np.polyval(c, xs), style, label=f'degree {deg}')
plt.scatter(x, y, c='k', zorder=3); plt.ylim(-2, 2); plt.legend()
plt.title('underfit / good / overfit — the elephant lives at high degree'); plt.show()
```

## Where it came from / where it goes

builds-on:: [[ml-taxonomy]] — the workflow is what "machine learns from data" actually means, step by step
feeds:: [[cross-entropy]] — step 3 for classifiers (and MSE for regression)
feeds:: [[gradient-descent]] — step 4 IS gradient descent
feeds:: [[cross-validation]] — the overfitting alarm: training error keeps falling, validation error turns back up
feeds:: [[metrics]] — evaluation closes the loop, and "your loss must be consistent with the metric you care about"
used-by:: every session after this one — s1 is the vocabulary lesson for the whole course
scroll:: [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]] — the 77-slide master walk

## Decision boundary

- ✅ The 4-step cycle fits ANY learning problem — it's the checklist for framing new work (incl. the thermal project).
- ❌ "Fits the training data" is NOT the goal — fit on train ≠ fit on test; the real aim is unseen examples.
- ❌ Don't add dimensions casually — redundant features (3×income) add zero information and inflate the data requirement.

## Depth layers

- **2026-06-27 (s1):** the full deck — 4-step cycle, Y=F(X,W), loss functions, data challenges, elephant, complexity, inductive bias, evaluation. → [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]]

## Project brick

**The thermal project IS this workflow instantiated:** collect telemetry ticks + throttle labels →
choose F (logistic vs tree, per [[ml-taxonomy]]) → loss = [[cross-entropy]] → optimize with
[[gradient-descent]] → validate against drives it never trained on ([[cross-validation]]) — or
it's a benchmark-cheating heuristic, the firmware failure mode he already knows.

## Formula

```
Y = F(X, W)      fix F → learn W from data → freeze W → deploy
the four steps:  data → model → loss → optimize     (then evaluate, honestly)
```

## Flashcards

#flashcards/ml-workflow

The professor's one-line definition of a model? :: A mathematical function from input to output, parameterized by weights: Y = F(X,W). Fix F, learn W from data, freeze W, ship.
Errors vs artifacts — the chat-poll answer that won? :: "Errors DESTROY information (unavoidable acquisition noise); artifacts CREATE false information (you made it — like merging $/€/₹ unconverted — so you can remove it)."
Why does one outlier drag the whole fitted line? :: The loss is an aggregate Σ over all points with no discrimination — the far-off point's huge squared error shouts "consider me too!" and tilts the fit.
