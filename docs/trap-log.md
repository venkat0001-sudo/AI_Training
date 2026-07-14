---
title: Trap log — the misconception ledger
date: 2026-07-04
sessions: []
concepts: [meta]
type: ledger
up: "[[HOME]]"
recap: Every trap I fell into, one line each — the strongest recall hooks I own. Read before exams.
---

# 🪤 Trap Log — my greatest hits of wrong turns

> One line per trap: the wrong belief → the correction, with a link to the full story.
> These are **exam gold**: each one marks a spot where intuition misfires — mine did, so will half the cohort's.
> Maintained at every session (new trap → new line, newest on top).
> Format note (2026-07-07 Atlas migration): converted from a table to one-trap-per-line so each
> trap carries a block ID (`^id`) — concept atoms EMBED these lines (`![[trap-log#^id]]`) instead
> of copying them. The trap lives once, here.

- **2026-07-13** · I believed *"prediction = regression; regression needs gradient descent"* → Prediction = regression (a **number**) OR classification (a **class**). **GD trains both** — MSE for regression, cross-entropy for classification; logistic regression is classification-by-GD. Entropy/info-gain is the split rule for classification **trees**, not "the classification method." Full story: [[2026-06-25_bayes-and-ml-taxonomy_s1]] ^gd-trains-both

- **2026-07-13** · I believed *"non-parametric model = zero parameters"* → It means the param count **grows with the data** (not fixed), not zero. Trees/KNN are non-parametric → can grow **unbounded** and eat memory; parametric (linear/logistic/NN) has a fixed, bounded count. Full story: [[2026-06-25_bayes-and-ml-taxonomy_s1]] ^nonparam-zero

- **2026-07-10** · I believed *"the slope and intercept ARE the two partial derivatives"* → No — `w`/`b` are the two **knobs (parameters)** you turn. The partial derivatives `∂L/∂w`, `∂L/∂b` are a *different* object: the slope of the **loss** w.r.t. each knob. The word "slope" wears two hats — `m` = slope of the *line*; `∂L/∂m` = slope of the *loss bowl*. Full story: [[2026-07-10_line-to-gradient-thermal-fit_F]] §4 ^knob-vs-gradient

- **2026-07-10** · I believed *"prediction = mx + c − observed"* → That subtracted thing is the **residual (the miss)**, not the prediction. Prediction = `w·load+b`; residual = `pred − observed`; loss = `Σ residual²`. Three ordered objects, not one. Full story: [[2026-07-10_line-to-gradient-thermal-fit_F]] §4 ^predict-vs-residual

- **2026-07-10** · I believed *"w tells how much the load varies / load is how fast"* → `w` **never measures load**. Load is the input you read; `w` answers *"when load rises by 1, how much does TEMP rise?"* — it measures the **output's** response. The temp-change ÷ load-change ratio is `w`, and it reports temp. Full story: [[2026-07-10_line-to-gradient-thermal-fit_F]] §4 ^w-measures-load

- **2026-07-10** · I believed *"if you go downhill you end up in MORE error"* → Flat backwards: **downhill = LESS error** — the bottom of the loss bowl is the goal. The gradient points **uphill** (toward more loss); you step the **opposite** way (the minus in `w ← w − η·∂L/∂w`). Read a negative `∂L/∂w` as "floor's to the right → step right → w increases." Full story: [[2026-07-10_line-to-gradient-thermal-fit_F]] §6 ^downhill-more-error

- **2026-07-09** · I believed *"for y = 5x + 7, from 7 the line moves by 35"* → The slope and the intercept **never multiply**: per step y rises by the slope **5**, not 5×7. The `+7` is the *lift* (start height), the `5` is the *tilt* — and the `+7` **vanishes** when you differentiate (`d/dx(5x+7)=5`). Full story: [[linear-equation]] ^tilt-times-lift

- **2026-07-09** · I believed *"subbing 5x+7 into (f(x+h)−f(x))/h gives −14"* → The minus hits the **whole** second bracket, but only `f(x)`'s `+7` flips: `+7 − 7 = 0`, **not** `−7 − 7 = −14`. `f(x+h)`'s `+7` stays positive. Result is `5h/h = 5`. Full story: [[linear-equation]] ^minus-distribute

- **2026-07-08** · I believed *"the derivative IS the approximate value dy/dx reaches (2.01…)"* → No — 2.01 is the **approximation**; the derivative is the **limit** those approximations home in on, and it's **exact** (=2). Cancel `dx` first, *then* send `dx→0`. Full story: [[calculus]] ^deriv-is-limit

- **2026-07-08** · I believed *"0/0 is infinite"* → **0/0 is indeterminate**, not infinite. `1/0` blows up; `0/0` leaves room for a real finite answer — which is *why* a slope can come out to a clean 2. Full story: [[calculus]] ^zero-over-zero

- **2026-07-08** · I believed *"as dx→0, the slope also →0"* → Two different axes: the **nudge** →0, the **slope** →2 (the limit). A parabola isn't flat at x=1, so its slope can't be 0. Full story: [[calculus]] ^nudge-vs-slope

- **2026-07-08** · I believed *"the chain rule multiplies because the du's cancel"* → That's the **mnemonic, not the mechanism**. It multiplies because rates are nested "per" counts: pizzas-per-box × slices-per-pizza = slices-per-box. Series multipliers multiply. Full story: [[calculus]] ^chain-cancel-mnemonic

- **2026-07-05** · I believed *"∂p/∂w = w" (for p = w·x + b)* → It's **x** — the coefficient of the variable is the rate. `w` is the knob you turn, `x` is the fixed dial reading. Full story: [[2026-07-05_chain-rule-to-gradient_F]] §4 ^dpdw-w

- **2026-07-05** · I believed *"8(2x+1)³ simplifies to 8(4x+2)³"* → Can't slide a coefficient into a power: (4x+2)³ = 2³(2x+1)³ = 8(2x+1)³ (it gets **cubed**). **Leave it factored.** Full story: [[2026-07-05_chain-rule-to-gradient_F]] §2 ^coeff-power

- **2026-07-05** · I believed *"(5x−2)³ → derivative is 20x−4"* → Dropped the cube (used u² not u³). **Degree-check:** deriv of a cubic must be a quadratic — a line means an exponent was lost. Correct: 15(5x−2)². Full story: [[2026-07-05_chain-rule-to-gradient_F]] §2 ^degree-drop

- **2026-07-05** · I believed *"just expand it, then power-rule"* → Works for a bare polynomial, but you **can't expand** sigmoid(w·x+b) — the chain rule is the only way for compositions (= every ML gradient). Full story: [[2026-07-05_chain-rule-to-gradient_F]] §6 ^expand-everything

- **2026-07-03** · I believed *"PCA gives me the price-prediction weights"* → PCA gives **recipe weights (loadings)** — how to *blend* features. Prediction weights come later, from [[gradient-descent]], using the label. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §21 ^weights-overload

- **2026-07-03** · I believed *"PCA is like gradient descent — it also reduces a loss"* → PCA has **no loss and no label** — it reshapes features. They live on opposite sides of the label-entry line. Full story: [[2026-07-02_ml-pipeline-math-map_F]] §1b ^pca-loss

- **2026-07-03** · I believed *"PCA can't be used in my supervised project — it's unsupervised"* → The label rule is about the **method, not the pipeline**: PCA-the-step never sees the label, so it's unsupervised *even inside* a supervised project. Full story: [[2026-06-25_bayes-and-ml-taxonomy_s1]] ^pca-supervised

- **2026-06-30** · I believed *"±1σ is the outlier fence"* → ~1 in 3 readings falls outside ±1σ **by design**. Outliers live beyond ±2σ/±3σ. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §16 ^sigma-fence

- **2026-06-30** · I believed *"mean of `[10,20,30]` = 30"* (grabbed the max) → mean = sum/count = **20**. Spell-check: deviations must sum to 0 — mine summed to −30, alarm fired. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §15.1 ^mean-max

- **2026-06-29** · I believed *"v₁ is the most frequent reading in the data matrix"* → v₁ is a **direction (a blend of features)**, not a row; [[pca|PCA]] is about *spread*, not frequency. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §14.F ^v1-frequent

- **2026-06-29** · I believed *"the eigenvector is always `[1,1]`"* → Each matrix has its **own** eigenvectors; `[1,1]` was special to one matrix. Length & sign don't matter — direction does. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §14.F ^eig-always-11

- **2026-06-29** · I believed *"matrix × vector can't work — A has 2 columns but `[1,0]` has 1 row"* → A vector is a **column**, standing up: `[1,0]` is really 2×1. My cols-of-first = rows-of-second rule was right; I'd drawn the arrow lying down. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §12 step 3 ^vec-column

- **2026-06-28** · I believed *"covariance = multiply the two means together, then sum"* → Covariance **never touches the product of the means**. The mean's only job is the reference line; you multiply the paired *deviations*, then average. Full story: [[2026-06-28_linear-algebra-vectors-dot-cosine_F]] §7a ^cov-meanproduct

- **2026-06-25** · I believed *"a 99%-accurate alarm means 99% sure when it fires"* → Base rates rule: with rare events the posterior can be ~50% or worse — count the buckets. Full story: [[2026-06-25_bayes-and-ml-taxonomy_s1]] ^base-rate
