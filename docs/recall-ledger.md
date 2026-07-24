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
| [[normal-distribution\|Normal distribution, μ/σ, z-score]] | `html/normal_distribution.html`, `html/2026-06-30_bell-curve-sigma-latency_F.html` | 2026-06-07 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[probability\|Probability basics (marginal/joint/conditional, base-rate trap)]] | `docs/2026-06-25_bayes-and-ml-taxonomy_s1.md` | ~2026-06-17 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[bayes\|Bayes' theorem (bucket-counting posterior)]] | `docs/2026-06-25_bayes-and-ml-taxonomy_s1.md`, `html/2026-06-25_bayes-and-ml-taxonomy_s1.html` | 2026-06-25 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[ml-taxonomy\|AI→ML taxonomy, classic-vs-deep, features-vs-weights]] | same as Bayes docs | 2026-06-25 | 2026-07-13 (recall sprint — untangled regression vs classification, GD trains both, parametric vs non-parametric) | +16d | 2026-07-29 |
| [[vectors\|Magnitude, dot product, cosine similarity]] | `docs/2026-06-28_linear-algebra-vectors-dot-cosine_F.md` §1–§6, its HTML twin | 2026-06-28 | 2026-07-21 (recall sprint) | +7d | 2026-07-28 |
| [[covariance\|Covariance + covariance matrix (votes, 4-case, 3×3 read)]] | notes doc §7–§8, `html/2026-06-30_covariance-eigen-capstone_F.html` | 2026-06-28 | 2026-07-21 (recall sprint) | +7d | 2026-07-28 |
| [[eigenvectors\|Eigenvectors/eigenvalues (matrix = rotate+stretch machine)]] | notes doc §10–§11, capstone HTML | 2026-06-29 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[pca\|Covariance→eigen→PCA bridge (20 sensors → 3 numbers)]] | `html/2026-06-28_pca-20-sensors-walkthrough_F.html`, notebook cells 4.1b/4.6 | 2026-06-29 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[mcu-deployment\|MCU deployment + decision-tree geometry]] | `html/2026-06-26_mcu-deployment-flashcards_s1.html` | 2026-06-26 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[gradient-descent\|Gradient descent (numeric loss-shrinking example)]] | `docs/2026-06-25_bayes-and-ml-taxonomy_s1.md` (GD example), `docs/2026-07-08_derivative-limit-to-gradient-descent_F.md` §7, `docs/2026-07-10_line-to-gradient-thermal-fit_F.md` (full R1 story), `html/2026-07-14_gradient-descent-thermal-capstone_F.html` (capstone) | 2026-06-28 | 2026-07-14 (capstone HTML built + owned: temp=w·load+b — 3 objects, bowl, gradient (why 2/3 = 2 from square × 1/3 from mean), hand-step, 60→180-iter convergence to (15,25) w/ target line, η knob. DIVERGENCE owned: too-big η overshoots to a steeper wall → gradient bigger → compounds exponentially past threshold ≈0.21; "fix becomes the failure", NAND = read-retry Vref overshoot) | +16d | 2026-07-30 |
| [[calculus\|Derivative=limit → chain rule → training gradient 2(P−T)·x (credit assignment, thermal cycle)]] | `docs/2026-07-05_chain-rule-to-gradient_F.md`, `docs/2026-07-08_derivative-limit-to-gradient-descent_F.md`, `html/2026-07-09_line-vs-curve-slope_F.html` | 2026-07-05 | 2026-07-21 (recall sprint) | +16d | 2026-08-06 |
| [[expected-value\|Expected value (EV = Σ p·v; loss is an EV)]] | `docs/concepts/expected-value.md`, `docs/2026-07-10_line-to-gradient-thermal-fit_F.md` | 2026-07-10 | 2026-07-24 (due-cards deck) | +7d | 2026-07-31 |

| [[kmeans\|K-means clustering (elbow, assign/mean loop, WCSS, local-minima restarts)]] | `docs/concepts/kmeans.md`, `html/2026-07-18_kmeans-clustering-walkthrough_s5.html`, `docs/2026-07-18_kmeans-clustering-walkthrough_s5.md` | 2026-07-18 | 2026-07-24 (due-cards deck) | +7d | 2026-07-31 |

**Legend:** DUE items are batched into the next recall sprint / due-cards deck. Snap a due date to a
pre-class Saturday slot when the weekend session builds on that topic.
