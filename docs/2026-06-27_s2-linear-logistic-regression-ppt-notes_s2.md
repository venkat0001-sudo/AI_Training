---
title: Session 2 — Linear & Logistic Regression (deck + transcript master notes)
date: 2026-06-27
sessions: [s2]
concepts: [regression, gradient-descent, neural-nets]
type: notes
recap: The full 62-slide deck (incl. every handwritten annotation) + transcript — perceptron→dot product→linear/logistic regression→regularization→gradient descent (batch/SGD/mini-batch)
---

# Session 2 — Supervised Learning: Linear & Logistic Regression

> **Master notes, aggressively extracted from the slide deck (all 62 slides, including the
> professor's live handwritten ink) + the class transcript.** Lecturer: **Mahesh Mohan M R, Dept of
> AI, IIT Kharagpur**, 27 Jun 2026. This is the faithful capture (the s1-style "PPT notes"); the
> deep-dive teaching + numpy twins happen separately. Slide numbers are marked `[Sxx]` so you can
> jump back to the deck. Handwriting = what he wrote *live*, which is where the real intuition lives.

## Table of contents (section → slides)

| Section | Slides |
|---|---|
| 0. The one-line story of the session | — |
| 1. From biological neuron to artificial neuron | 2–7 |
| 2. The historic neurons: McCulloch–Pitts, Hebb, Perceptron | 8–13 |
| 3. The dot product IS the neuron's core operation | 14–16 |
| 4. Geometric view: the decision boundary is wᵀx = 0 | 17–20 |
| 5. Linear regression & the bias term | 21–23 |
| 6. The XOR problem — why one line isn't enough (AI winter) | 24 |
| 7. Polynomial regression + regularization (Ridge/Lasso, L1/L2) | 25–29 |
| 8. Logistic regression: sigmoid, odds, log-odds, boundaries | 30–39 |
| 9. Optimization I: calculus review, loss, minima | 40–46 |
| 10. Optimization II: gradient descent (the update rule) | 47–52 |
| 11. Logistic-regression training: likelihood → cross-entropy | 53–56 |
| 12. Batch vs SGD vs Mini-batch; epochs & iterations | 57–62 |
| 13. Formula sheet | — |
| 14. Where this sits in the web + edge-AI grades | — |
| 15. Traps & things to re-check | — |

---

## 0. The one-line story of the session

A single artificial neuron computes a **dot product** of inputs with weights, then applies a
threshold. Stack that idea two ways: keep the raw number → **linear regression** (predict a value);
squash it through a **sigmoid** → **logistic regression** (predict a class *probability*). A single
neuron can only draw ONE straight boundary (the **XOR** counterexample → first AI winter), which
motivates polynomial features and, later, multi-layer networks. To *learn* the weights you
**minimize a loss** by **gradient descent** — step every weight downhill by `−λ·(gradient)` — and in
practice you do it on **mini-batches**. That's the whole session.

**The 4-step ML workflow from Session 1 is the spine** `[S40]`: (1) collect labelled data,
(2) design the model, (3) define a loss, (4) **optimize the weights** ← this session finally does step 4.

---

## 1. From biological neuron to artificial neuron `[S2–S7]`

- `[S2]` **Artificial Neural Network** — the apps you use (Claude, ChatGPT, DeepSeek, Grok) are ANNs
  under the hood: input nodes → hidden layers (all-to-all arrows) → output nodes.
- `[S3]` **Biological neuron** — presynaptic cell → axon (myelin segments) → presynaptic terminal →
  **synapses** → postsynaptic cell. *"Synapses = the points of contact where information passes from
  one neuron to the next."*
- `[S4]` **Biological neuron → neural network** — sensory neuron (Receptor→Axon→Synapse). Santiago
  Ramón y Cajal (1906 Nobel) and his historic hand-drawing of cortical neurons.
- `[S5]` **The parallel that drives the whole field:** biology (Sensory Neuron → Neural Network) is
  mimicked by engineering (Artificial Sensory System: Sensor→Pathway→Memory → Artificial NN).
- `[S6]` **The neuron-count-vs-year plot** (log scale, 10⁻²…10¹¹ neurons, 1950…2056). Biological
  scales on the right (Sponge → Roundworm → … → Bee → Frog → Octopus → **Human**); numbered AI
  systems (1–20) climb the rising blue line toward human-scale (~2056 extrapolation). *Artificial
  nets are steadily climbing biological neuron counts.*
- `[S7]` **Zoom into one artificial neuron** (one hidden node boxed) → the next slides open it up.

---

## 2. The historic neurons `[S8–S13]`

### McCulloch–Pitts neuron, 1943 `[S8–S10]`
The first *mathematical* neuron (1943 paper "A Logical Calculus of Ideas Immanent in Nervous
Activity"). Inputs x₁,x₂ → weights w₁,w₂ → **"Neurode"** → output y. The firing rule:

> **Σ xᵢwᵢ ≥ θ  ⇒  output = 1  ;  else  ⇒  output = 0.**   (θ = threshold)

- `[S9]` **AND logic (handwritten):** w₁=1, w₂=1, **θ=2**. Truth table output is 1 only for (1,1):
  worked live as **1×1 + 1×1 = 2 ≥ 2 ⇒ 1**. Excitatory weight = +1, inhibitory = −1.
- `[S10]` **OR logic (handwritten):** *same neuron, just* **θ=1**. Now (0,1),(1,0),(1,1) all fire:
  **1×1 + 1×1 = 2 ≥ 1 ⇒ 1**. ⭐ **Key idea:** AND vs OR is the *same machine* — only the threshold θ changed.

### Hebbian cell, 1949 `[S11]`
Donald Hebb, *The Organization of Behavior*. "Cells that fire together wire together." Handwriting
notes the shift to real-valued signals: **i/p ∈ ℝⁿ, o/p ∈ ℝ, weights ∈ ℝ** ("input binary, output
analog"; excitatory/inhibitory ±1). Chemical neurotransmitters set the weights.

### Perceptron, 1958 (Rosenblatt) `[S12–S13]`
- `[S12]` Frank Rosenblatt built the first **perceptron** on the Mark-I machine — "the first machine
  capable of having an original idea." Inputs a₁…a₅ → weights wⱼ₁…wⱼ₅ → summation (j/S) → threshold
  step → output. **Handwritten and crucial: the weights are learned "from the data"** (not hand-set
  like McCulloch–Pitts). "Engineered", "θ?", "Th?".
- `[S13]` **Perceptron Convergence Theorem (teaser):** "Given an elementary α-perceptron, a stimulus
  world W, and any classification C(W) for which a solution exists…" → if the data IS linearly
  separable, the perceptron **will** find a separating line. This launched the *first AI wave*.

---

## 3. The dot product IS the neuron's core operation `[S14–S16]` ⭐⭐⭐

- `[S14]` **Dot / inner product:** `(x₁ x₂ … x_N)·(y₁ … y_N)ᵀ = x₁y₁ + x₂y₂ + … + x_Ny_N`.
  Dimensions: **1×N · N×1 = 1×1** ("outer dimensions give the size of the result" → a single number).
  Handwriting ties it to the neuron: **y = w₁x₁ + w₂x₂ + … + w_Nx_N − θ**, then **o/p = threshold(y)**.
  → **This weighted sum is "perceptron step ①".** (Callback to your Linear-Algebra_F dot-product notes.)
- `[S15]` **Biological reading:** `(r₁…r_N)·(w₁…w_N)ᵀ = Σ rᵢwᵢ` where **r = input neurons' firing
  rates**, **w = synaptic weights**, result = the **output neuron's firing rate**. The dot product =
  a weighted vote of the inputs.
- `[S16]` **Geometric reading (the cosine):** **r⃗·w⃗ = |r⃗| |w⃗| cos(θ)**. Handwriting: **⟨r,w⟩**;
  **cos θ = 1 when θ=0** (input aligned with the weight → fires hardest), θ=90° → 0, θ=180° →
  opposite. → A neuron **fires most strongly when the input points the same way as its weight
  vector.** (Direct callback to your dot/cosine session.)

---

## 4. Geometric view: the decision boundary is wᵀx = 0 `[S17–S20]` ⭐⭐

- `[S17]` A weight vector **W = [0,0,1]** defines a **plane**. The **signum function** turns the sign
  of the score into a class: score > 0 → **Class 1**, score < 0 → **Class 2**, threshold at 0.
  Handwriting: **y = x₁w₁+x₂w₂+x₃w₃**, **o/p = threshold(y, 0)**.
- `[S18]` Four points A,B (above the plane) and C,D (below). Classify by the sign of **⟨point, w⟩**
  "compared with Th=0": positive → Class 1 (above), negative → Class 2 (below).
- `[S19]` ⭐ **The learning goal (handwritten): "Find the optimal W & threshold."** And the **bias-fold
  trick**: `w₁x₁+w₂x₂+w₃x₃ ≥ w₀`  ≡  `w₁x₁+w₂x₂+w₃x₃ − w₀ ≥ 0` — the threshold w₀ becomes just
  another weight (the **bias**).
- `[S20]` ⭐ **Punchline:** **wᵀx = 0 is the decision boundary** (a hyperplane). **wᵀx ≥ 0** = one
  class, **wᵀx < 0** = the other. The weight vector **W is the normal (perpendicular) to the plane**;
  the vectors in the plane (a=(1,0,0), b=(0,1,0)) satisfy wᵀx=0. **A linear classifier = a hyperplane;
  the sign of wᵀx = which side = the class.**

---

## 5. Linear regression & the bias term `[S21–S23]` ⭐

- `[S21]` **Pivot from classify → predict.** Instead of taking the *sign* of the score, output the
  **raw line value**. Fit a **line of regression** through the datapoints. Handwriting: **y = mx + c
  → "line"**; with vs without bias: `Y = mx − θ` (no bias) vs `Y = mx + c` (bias).
  Live Zoom chat (Abhinav Murli) nails the bias role: *"allows the output to be non-zero if all
  inputs are zero."*
- `[S22]` **Bias = intercept.** Model **W·x + b**. Handwriting: `Y = mx + c`; "**if x=0 → Y = c**".
  Without bias the line is forced through the origin.
- `[S23]` ⭐ **Anatomy of a linear model:** **y′ = b + w₁x₁**, where **y′ = Prediction**, **b = Bias**,
  **w₁ = Weight**, **x₁ = Feature value**. **b and w₁ are *calculated from training*** (learned); x is
  *given* (input). Handwriting shows a feature vector [x₁ x₂ … x_N] with a real data row
  [0.9, 0.001, 1.3 … 2.8].

---

## 6. The XOR problem — why one line isn't enough `[S24]` ⭐

Three truth tables + their 2-D plots:
- **AND** — the single `1` is separable from the `0`s by **one straight line**. ✅
- **OR** — also separable by one line. ✅
- **XOR** — the two `1`s sit on **opposite corners**; **NO single straight line** can separate them
  (handwriting draws **two lines c1, c2** needed). ❌

**1969, Minsky & Papert, *Perceptrons: An Introduction to Computational Geometry*** proved this
limit → funding froze → the **"AI winter"** (handwritten bump on a 1950→1969 timeline). ⭐ **A single
perceptron can only draw ONE straight boundary.** (The fix — stacking neurons into multi-layer nets
for curved boundaries — comes in Module 2.)

---

## 7. Polynomial regression + regularization `[S25–S29]` ⭐⭐

### Polynomial regression `[S25–S26]`
- `[S25]` **Simple linear model** `y = w₀ + w₁x` (straight) vs **polynomial model**
  `y = w₀ + w₁x + w₂x²` (curved — "uses input AND powers of the input"). Adding powers (x², x³…) lets
  the curve **bend** to fit non-linear data (green 🙂 "solves the non-linear problem") — but too much
  flexibility → **overfit** (red ☹).
- `[S26]` 😄 **The overfitting fable — von Neumann on Fermi:** *"With four parameters I can fit an
  elephant, and with five I can make him wiggle his trunk."* (A real elephant outline is drawn from 4
  complex parameters; the 5th wiggles the trunk. Mayer et al. 2010.) → Enough free parameters fit
  *anything* — which is exactly the danger.

### Regularization (Ridge & Lasso) `[S27–S29]`
Both add a **penalty on weight size** to the fit error:
- **Ridge (L2):** `J(θ) = MSE(θ) + α·½ Σ θᵢ²`   ·   **L2: R(θ) = ‖θ‖₂² = Σ θᵢ²**
- **Lasso (L1):** `J(θ) = MSE(θ) + α· Σ |θᵢ|`   ·   **L1: R(θ) = ‖θ‖₁ = Σ |θᵢ|`
- θ = the model's bias & coefficients; **α = the regularization weight** (how hard you penalize).
  Worked example for θ=[1,−2,−3]: **L2 = √(1²+2²+3²)**, **L1 = |1|+|2|+|3|**.
- `[S28]` ⭐ **Why L1 zeros weights (1-D picture):** L2 = x² (parabola), L1 = |x| (V). Near zero,
  **L2's slope → 0** (keeps shrinking but never fully to zero), while **L1 keeps a constant slope**
  and drives weights to **exactly 0** → **L1 = sparsity / feature selection**; L2 = smooth shrinkage.
  (Zoom chat: "A is L2 and B is L1.")
- `[S29]` **Effect of α:** α=0 → wild overfit wiggle; larger α → smoother, simpler fit (α=1 nearly
  flat). Left = Ridge(L2), right = Lasso(L1).

---

## 8. Logistic regression `[S30–S39]` ⭐⭐⭐

### Why not just linear? `[S30]`
Linear regression outputs a straight line that **goes beyond 0 and 1** — useless for a probability.
**Logistic regression uses an S-curve that stays inside [0,1]** → it can output "P(class) = 0.9" etc.

### The sigmoid `[S31–S33]`
- **LR(x) = eˣ / (1 + eˣ)**, domain x ∈ (−∞, ∞).
- **Max = 1** (as x→∞: e^∞/(1+e^∞)→1); **Min = 0** (as x→−∞: rewrite as e^(−x)/(1+e^(−x)) → 0).
- `[S33]` Crosses **0.5 at x=0** (`e⁰/(1+e⁰) = 1/2`). P=0 "impossible", P=1 "certain", P=0.5 "50/50".
  Other names: **Sigmoid function · S-curve**. → Squashes any real number into a probability in (0,1).

### Odds & log-odds — the definition of the model `[S34–S36]`
- `[S34]` Logistic regression is a **2-class, probabilistic classifier**: it returns **P(y=1|x)** —
  not just "class 1", but *how sure*.
- `[S35]` **Odds = P / (1−P)** — "probability it happens vs probability it doesn't." Always positive;
  ranges **0 to ∞**. (e.g. 50/50 → odds 1.) Stretches a bounded probability into an unbounded ratio.
- `[S36]` ⭐⭐⭐ **THE MODEL — "the log of the odds is a LINEAR function of the features":**
  > **log( P(y=1|x) / (1−P(y=1|x)) ) = θ₀ + θ₁x₁ + … + θₙxₙ = Z**
  Rearranged: **P(y=1|x) = e^Z / (1 + e^Z)** = **sigmoid(Z)**. So logistic regression = *run the
  linear score Z through the sigmoid to get a class-1 probability.*

### What boundary can it draw? `[S37–S39]`
- `[S37]` With `Z = θ₀+θ₁x₁+…`, the boundary is **Z = 0** (where P=0.5): a **straight line**. Z<0 →
  Class 0 (P<0.5), Z>0 → Class 1 (P>0.5).
- `[S38]` Class Q&A: how to get a curved boundary? → "use a polynomial function of the inputs."
- `[S39]` **"Z determines the boundary; make Z quadratic/polynomial ⇒ a curved boundary."** Same
  sigmoid, non-linear Z → non-linear decision surface.

---

## 9. Optimization I: calculus, loss, minima `[S40–S46]` ⭐

- `[S40]` **Recap of the 4-step workflow** — steps 1–3 ticked; **step 4 "Optimize weights" is
  today's job** (MNIST digits, 784-input ANN, loss-surface bowl).
- `[S42]` **Derivative = rate of change.** For y=f(x) (e.g. x²): **dy/dx < 0 → decreasing**,
  **dy/dx > 0 → increasing**, dy/dx = 0 at the bottom. **The derivative's sign points downhill** —
  the seed of gradient descent.
- `[S43]` **Partial derivatives** (multivariate y = x²+z²+w²): vary one variable, hold the rest →
  ∂y/∂x=2x, ∂y/∂z=2z, ∂y/∂w=2w. A model's **gradient = the stack of partials, one per weight.**
- `[S44]` **Local vs global minima** — gradient descent walks downhill but can get **trapped in a
  local minimum** instead of the global one.
- `[S45]` **The loss:** **E = Σᵢ (y⁽ⁱ⁾ − F(x⁽ⁱ⁾))²** (sum of squared errors, F = the model). Two
  objectives — we want (2) *the parameter values* that minimize E, not just the minimum value.
- `[S46]` **Calculus min/max test:** necessary `dy/dx = 0`; sufficient adds `d²y/dx² > 0` (min) or
  `< 0` (max). You *could* solve `dy/dx=0` in closed form — but for big models that's impossible, so
  we **iterate** instead.

---

## 10. Optimization II: Gradient Descent `[S47–S52]` ⭐⭐⭐

### The update rule, derived `[S47–S50]`
Derivative: `f'(a) = lim_{h→0} [f(a+h) − f(a)] / h`. **Question:** what if we set the weight step
**h = −λ f'(a)** (λ > 0)? Then `f(a+h) − f(a) ≈ f'(a)·h = −λ (f'(a))² ≤ 0` → **the loss goes down.**

> ⭐ **THE RULE:  a ← a − λ·f'(a)   (λ = learning rate).**
> Update every weight by stepping *opposite* the gradient. The sign of the derivative auto-picks the
> downhill direction (works from either wall of the bowl).

- `[S50]` **The algorithm:** (1) randomly initialise θ's; (2) repeat until convergence:
  **θⱼ ← θⱼ − r·(∂L/∂θⱼ)** for all j. **Convergence check:** fixed #iterations, or stop when params
  barely change.

### Applied to linear regression `[S51–S52]`
- Loss = MSE = `Σ (F(x⁽ⁱ⁾) − y⁽ⁱ⁾)²`. Gradient via **chain rule**:
  **∂E/∂θⱼ = 2 Σ (F(x⁽ⁱ⁾) − y⁽ⁱ⁾)·xⱼⁱ** (with x₀ⁱ=1 for the bias).
- Update: **θⱼ ← θⱼ − r·2 Σ (F(x⁽ⁱ⁾) − y⁽ⁱ⁾)·xⱼⁱ**. ⭐ **Gradient = 2 × error × input** — the error
  itself tells each weight which way to move. *(Prime numpy-twin candidate.)*

---

## 11. Logistic-regression training: likelihood → cross-entropy `[S53–S56]` ⭐⭐

- `[S53]` **One formula for both classes:** P(y=1|x)=LR(x), P(y=0|x)=1−LR(x), combined as
  **P(y|x;θ) = LR(x)^y · (1−LR(x))^(1−y)** (y=1 picks the first term, y=0 the second).
- `[S54]` **Likelihood** of the whole dataset, assuming examples are **independent** (so the joint =
  product): **L(θ) = ∏ᵢ LR(xⁱ)^yⁱ · (1−LR(xⁱ))^(1−yⁱ)**.
- `[S55]` ⭐⭐⭐ **Maximize the likelihood (MLE).** The product is awkward, so **maximize log L**
  (monotonic; `log(a·b)=log a+log b` turns product → sum):
  > **log L(θ) = Σᵢ [ yⁱ·log LR(xⁱ) + (1−yⁱ)·log(1−LR(xⁱ)) ]**
  This is exactly the **cross-entropy / log-loss** — the standard classification loss, *derived from
  maximum likelihood.* (Ties straight to the S1 "the loss function IS probability" note.)
- `[S56]` **Stochastic gradient ASCENT** (one sample at a time): **θⱼ ← θⱼ + r·(∂logL/∂θⱼ)** — note
  the **+** (we climb the likelihood). Clean gradient: **∂logL/∂θⱼ = (yⁱ − LR(xⁱ))·xⱼⁱ** =
  **(label − predicted probability) × input** — same shape as the linear-regression gradient.
  (Equivalently: *descend* on −logL, the cross-entropy.)

---

## 12. Batch vs SGD vs Mini-batch `[S57–S62]` ⭐⭐

| Flavour | Gradient computed on | Pros | Cons |
|---|---|---|---|
| **Batch GD** `[S57]` | **ALL** training samples | accurate gradient | slow, memory-hungry (1M rows!), not GPU-friendly, can stick in local minima |
| **SGD** `[S58]` | **ONE** sample at a time | fast, tiny memory | noisy path, under-uses GPU, hard to converge |
| **Mini-batch GD** `[S59]` ⭐ | **a small batch (say 100)** | smooths noise, fills the GPU, converges — "Better" on all 3 | pick batch size |

**Mini-batch is stamped "PRACTICAL AND USEFUL"** `[S61]` — it's what real training uses.

**Epochs vs iterations `[S60]` (memorize this):**
- **1 iteration** = one weight update on one batch.
- **1 epoch** = one full pass over ALL the data = **(dataset size ÷ batch size) iterations**.
- For 1000 rows: batch 1000 → 1 iter/epoch (= Batch GD); batch 500 → 2; batch 100 → 10.

---

## 13. Formula sheet

```
Neuron / perceptron:   o/p = threshold( Σ xᵢwᵢ − θ )         (θ = bias/threshold)
Dot product:           x·y = Σ xᵢyᵢ = |x||y|cos(θ)           (1×N · N×1 = 1×1)
Decision boundary:     wᵀx = 0     (wᵀx>0 → class 1, <0 → class 0)
Linear model:          y′ = b + Σ wⱼxⱼ                         (b,w learned from training)
Ridge (L2):            J = MSE + α·½ Σ θᵢ²
Lasso (L1):            J = MSE + α·  Σ |θᵢ|
Sigmoid:               LR(x) = eˣ/(1+eˣ) ∈ (0,1)
Logistic model:        log( P/(1−P) ) = Z = θ₀+Σθⱼxⱼ  ⇒  P(y=1|x) = e^Z/(1+e^Z)
Odds:                  P/(1−P) ∈ (0,∞)
GD update:             a ← a − λ f'(a)      θⱼ ← θⱼ − r ∂L/∂θⱼ
Linear-reg gradient:   ∂E/∂θⱼ = 2 Σ (F(xⁱ) − yⁱ)·xⱼⁱ
Cross-entropy (logL):  Σ [ yⁱ log LR(xⁱ) + (1−yⁱ) log(1−LR(xⁱ)) ]
Logistic gradient:     ∂logL/∂θⱼ = (yⁱ − LR(xⁱ))·xⱼⁱ
Epoch:                 iters/epoch = dataset_size ÷ batch_size
```

---

## 14. Where this sits in the web + edge-AI grades

- **Builds on:** dot/cosine (Linear-Algebra_F), derivatives & gradient descent (Calculus_F),
  the 4-step workflow + loss idea (S1). **Feeds:** neural nets = stacked logistic units (S7, Module 2),
  cross-entropy everywhere, optimizers (S8), and QLoRA/quantization on the edge (Module 4).
- **Edge-AI relevance grades** (attention budget):
  - ⭐⭐⭐ **regression** (a neuron IS logistic regression), **gradient descent** (trains everything),
    **mini-batch/SGD** (how real training fits constrained memory).
  - ⭐⭐ **sigmoid/logistic**, **L1/L2 regularization** (L1 sparsity = smaller models = fewer weights
    on-device), **decision boundary wᵀx=0**.
  - ⭐ perceptron/McCulloch–Pitts history, the XOR/AI-winter story (context, not exam-heavy math).

---

## 15. Traps & things to re-check (candidates for the trap log)

- **"AND vs OR need different neurons"** → ❌ *same* neuron, only θ changes (2 vs 1) `[S9–S10]`.
- **"The threshold is separate from the weights"** → the **bias-fold** makes θ just another weight
  `[S19]`; that's why the bias b appears inside the model.
- **"Logistic regression outputs a class"** → it outputs a **probability** P(y=1|x); the class comes
  from thresholding at 0.5 `[S34]`.
- **"Logistic regression can only do straight boundaries"** → straight *if Z is linear*; make Z
  polynomial → curved boundary `[S39]`.
- **"L1 and L2 both just shrink weights"** → L1 drives weights to **exactly 0** (sparsity), L2 only
  shrinks them smoothly `[S28]`.
- **"We minimize the logistic loss"** → we **maximize the likelihood** (gradient *ascent*, +sign),
  equivalently minimize the negative log-likelihood = cross-entropy `[S55–S56]`.
- **"Epoch = iteration"** → epoch = a full pass = (dataset ÷ batch) iterations `[S60]`.
