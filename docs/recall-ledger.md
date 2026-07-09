---
title: Recall ledger — spaced-repetition tracker
date: 2026-07-02
sessions: []
concepts: [meta]
type: ledger
recap: What is due when — the interval-ladder table the daily deck builds from
up: "[[HOME]]"
---

# Recall ledger — spaced-repetition tracker

> One row per topic. Ladder: learn → +1d → +3d → +7d → +16d → +35d → +60d → graduated.
> Pass = advance a step. Stumble = drop back one step. A topic *used* inside a newer lesson counts as a pass.
> Maintained by Claude at every session (check due topics → open with a recall sprint → update rows).

| Topic | Anchor artifacts | Learned | Last recalled | Ladder step | Next due |
|---|---|---|---|---|---|
| [[normal-distribution\|Normal distribution, μ/σ, z-score]] | `html/normal_distribution.html`, `html/2026-06-30_bell-curve-sigma-latency_F.html` | 2026-06-07 | 2026-06-30 (bell-curve rebuild) | +7d | 2026-07-07 |
| [[probability\|Probability basics (marginal/joint/conditional, base-rate trap)]] | `docs/2026-06-25_bayes-and-ml-taxonomy_s1.md` | ~2026-06-17 | 2026-06-25 (used in Bayes) | +7d | **2026-07-02 — DUE** |
| [[bayes\|Bayes' theorem (bucket-counting posterior)]] | `docs/2026-06-25_bayes-and-ml-taxonomy_s1.md`, `html/2026-06-25_bayes-and-ml-taxonomy_s1.html` | 2026-06-25 | 2026-06-25 | +7d | **2026-07-02 — DUE** |
| [[ml-taxonomy\|AI→ML taxonomy, classic-vs-deep, features-vs-weights]] | same as Bayes docs | 2026-06-25 | 2026-06-25 | +7d | **2026-07-02 — DUE** |
| [[vectors\|Magnitude, dot product, cosine similarity]] | `docs/2026-06-28_linear-algebra-vectors-dot-cosine_F.md` §1–§6, its HTML twin | 2026-06-28 | 2026-06-29 (+1d pass) | +3d | **2026-07-02 — DUE (overdue 1d)** |
| [[covariance\|Covariance + covariance matrix (votes, 4-case, 3×3 read)]] | notes doc §7–§8, `html/2026-06-30_covariance-eigen-capstone_F.html` | 2026-06-28 | 2026-06-30 (used in capstone) | +3d | 2026-07-03 |
| [[eigenvectors\|Eigenvectors/eigenvalues (matrix = rotate+stretch machine)]] | notes doc §10–§11, capstone HTML | 2026-06-29 | 2026-06-30 (capstone) | +3d | 2026-07-03 |
| [[pca\|Covariance→eigen→PCA bridge (20 sensors → 3 numbers)]] | `html/2026-06-28_pca-20-sensors-walkthrough_F.html`, notebook cells 4.1b/4.6 | 2026-06-29 | 2026-06-30 | +3d | 2026-07-03 |
| [[mcu-deployment\|MCU deployment + decision-tree geometry]] | `html/2026-06-26_mcu-deployment-flashcards_s1.html` | 2026-06-26 | 2026-06-26 | +3d | **2026-07-02 — DUE (overdue)** |
| [[gradient-descent\|Gradient descent (numeric loss-shrinking example)]] | `docs/2026-06-25_bayes-and-ml-taxonomy_s1.md` (GD example), `docs/2026-07-08_derivative-limit-to-gradient-descent_F.md` §7 | 2026-06-28 | 2026-07-09 (built the gradient vector: two-knob partials ∂L/∂w=2·err·x & ∂L/∂b=2·err, bias absorbs raw error; reconciled with StatQuest linear-regression fit — slope=weight, intercept=bias) | +7d | 2026-07-16 |
| [[calculus\|Derivative=limit → chain rule → training gradient 2(P−T)·x (credit assignment, thermal cycle)]] | `docs/2026-07-05_chain-rule-to-gradient_F.md`, `docs/2026-07-08_derivative-limit-to-gradient-descent_F.md` | 2026-07-05 | 2026-07-09 (partial derivatives owned: freeze-all-but-one = a 1-D slice through the loss bowl) | +7d | 2026-07-16 |

**Legend:** DUE items are batched into the next recall sprint / due-cards deck. Snap a due date to a
pre-class Saturday slot when the weekend session builds on that topic.
