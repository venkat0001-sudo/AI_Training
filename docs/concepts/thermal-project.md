---
title: 🎯 The thermal-ML project (rung ladder R0–R6)
aliases: [thermal-throttle, thermal-forecaster, rung-1, r1, thermal-ml, the-project]
date: 2026-07-04
sessions: []
lane: m2
edge: 3
status: learning
type: concept
up: "[[MOC-thermal-project]]"
recap: "The north-star: on-device predictive thermal-throttle ML inside SSD firmware. Rule-based step-throttling fails (oscillation, cliff drops); the fix is forecast-then-act — R1 classifier → R2 forecaster → MPC. Every course concept maps to one of its bricks."
---

# 🎯 The thermal-ML project (rung ladder R0–R6)

> **Recap:** The north-star: **on-device predictive thermal-throttle ML inside SSD firmware.**
> Rule-based step-throttling fails (oscillation, cliff drops); the fix is forecast-then-act —
> R1 classifier → R2 forecaster → MPC. Every course concept maps to one of its bricks.

**Chain:** every ⭐⭐⭐ concept ──► **a project brick** ──► R1 (M1 skills) ──► R2 (M2: LSTM) ──► MPC/DRL (papers) ──► exceptional edge-AI engineer

## The brick map (which concept builds what)

- [[variance-sigma]] → sensor triage (drop the yes-man rail, keep the storyteller die-temp)
- [[normal-distribution]] → the ±3σ anomaly fence + z-scored channels
- [[covariance]] → reading the telemetry relationships (the −500 "heats→throttles" cell)
- [[pca]] → 20 channels → 3, a controller-SRAM-sized front-end (with the small-λ runaway caveat)
- [[bayes]] + [[metrics]] → the FN-vs-FP pricing of throttle decisions (recall vs latency SLA)
- [[regression]] + [[cross-entropy]] → R1: the throttle/no-throttle classifier and its loss
- [[gradient-descent]] + [[calculus]] → the training engine (2(P−T)·x derived by hand)
- [[cross-validation]] → validate on drives never trained on, time-ordered folds
- [[entropy]] → tree splits (R1 alternative) + cross-entropy's foundation
- [[mcu-deployment]] → the deployment gate every model must pass

## Where the full detail lives

scroll:: [[2026-07-04_thermal-ml-project-map_F]] — §0 the DATED readiness timeline (the daily compass gate) · §2 the full concept→piece table · §3 numbers-as-anchors (interview ammunition) · §4 the paper reading ladder · §5 what rung-1 IS and IS NOT
scroll:: [[2026-07-04_ssd-thermal-ml-research]] — the 40-citation research base (LSTM/XGBoost forecasting, MPC, DRL, Waltz, KORAL)
scroll:: [[2026-07-02_edge-ai-roadmap]] — the market case + the 6-rung ladder + skill stack

## Decision boundary

- ✅ Every Daily Compass hook and every atom's "project brick" section points HERE.
- ❌ Rung-1 is NOT a product: it's a proof-of-skill on public/simulated telemetry (honest caveats in the map §6).

## Flashcards

#flashcards/thermal-project

Why does rule-based throttling fail, in one breath? :: Step-function thresholds react AFTER the heat arrives → oscillation around the trip point and performance cliff drops; forecasting acts before the cliff.
What gates R1, per the readiness timeline? :: Own k-means + PCA by Jul 18 (M1 boundary) — then R1's compression front-end and classifier are all owned skills.
