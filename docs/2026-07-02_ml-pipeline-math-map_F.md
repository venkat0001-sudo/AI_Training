---
title: The ML pipeline × math map
date: 2026-07-02
sessions: [F]
concepts: [ml-pipeline]
type: map
recap: 6-box pipeline; which math powers which box; house-price flow with the label-entry line
---

# The Whole Picture — Where Each Math Piece Plugs Into Machine Learning

> The master map. One page that answers: *"I'm learning linear algebra / calculus / probability /
> statistics — where EXACTLY does each one work inside an ML system?"* Every future topic gets placed
> on this map ("we are HERE"). `_F` = Foundation-bridging doc, 2026-07-02.

---

## Why are we learning this?

Concepts learned in isolation are trading cards — impressive, useless.
This map is the *board* they get played on.

Once you see the one pipeline every ML system follows, each math tool stops being "chapter 3"
and becomes "the part that makes step 4 work." That changes how deeply you need to learn it, and
what "understanding it" even means.

---

## 1. The movie in one strip (read left to right)

```
 RAW DATA ──► PREP the data ──► MODEL ──► TRAINING LOOP ──► EVALUATE ──► DEPLOY & PREDICT
              (linear algebra)  (linear    (calculus         (statistics   (probability +
               "extract the      algebra:   drives the        judges it)     statistics at
               cream of the      weights    weight updates)                  runtime — on the
               data"             ARE                                         edge, quantized)
                                 matrices)
```

One sentence per stage — the whole of ML:

1. **Raw data** — sensor readings, text, images… reality, messy.
2. **Prep** — turn reality into clean vectors/matrices; drop redundant channels; scale things fairly.
3. **Model** — a box of adjustable numbers (**weights**) that maps input → prediction.
4. **Training loop** — compare prediction vs truth (**loss**), compute which way to nudge every
   weight (**gradient**), nudge, repeat until the loss stops shrinking.
5. **Evaluate** — on data the model never saw: is it actually good, or did it memorize?
6. **Deploy & predict** — run it on new inputs; outputs come with confidence; watch for inputs
   the model has never seen the likes of.

That's it. Everything in the course is a zoom-in on one of these six boxes.

---

## 1b. The same strip, made CONCRETE — house-price prediction (non-SSD, for teaching a stranger)

> The abstract strip above, walked as one real regression example. Use this one when explaining to
> someone who has no firmware background. The star annotation: the **⬇ LABEL ENTERS HERE ⬇** line —
> everything above it is *unsupervised* (never sees the price), everything below is *supervised*.
> This flowchart is exactly what makes the **PCA-vs-gradient-descent** split click.

```
                🏠 HOUSE-PRICE PREDICTION  (a regression pipeline)

  [1] RAW DATA            20 features/house: school? hospital? metro? traffic?
      ───────────         sqft, floor, age … (Bangalore)                        math: —
                                    │                                           label seen? NO
                                    ▼
  [2] PCA  (PREP)         covariance matrix → eigenvectors/eigenvalues          math: LINEAR ALGEBRA
      ──────────────      "which 4 blended directions hold the most spread?"    label seen? NO  ← unsupervised
      squeeze 20 → 4      OUTPUT = 4 clean, perpendicular ingredients           weight born? RECIPE weights
                          (recipe weights / loadings — how to BLEND features)      (loadings)
                                    │
        ════════════════════ ⬇  LABEL (the price) ENTERS HERE  ⬇ ════════════════════
                                    │
  [3] MODEL              price_guess = w₁·c₁ + w₂·c₂ + w₃·c₃ + w₄·c₄ + b        math: LINEAR ALGEBRA
      ─────             (the w's start as random junk)                          label seen? about to
                                    │
                                    ▼
  [4] LOSS              how wrong?  (guess − real price)²                       math: CALCULUS + PROB
      ────                                                                       label seen? YES ← supervised
                                    │
                                    ▼
  [5] GRADIENT DESCENT  nudge each w downhill on the loss bowl, repeat          math: CALCULUS
      ────────────────  thousands of times                                      weight born? PREDICTION weights
                                    │
                                    ▼
  [6] TRAINED WEIGHTS   w₁..w₄, b  →  the model is now built                    math: —
      ──────────────    (THESE are the price-prediction weights)
```

**Two different "weights" born in two different boxes** (this is the whole confusion, solved by the picture):
- **Box [2]** makes **recipe weights** (loadings) — *how to blend* 20 features into 4. Price never seen. Unsupervised.
- **Box [5]** makes **prediction weights** — *how hard each ingredient pushes the price.* Price drives them. Supervised.

**PCA vs gradient descent, side by side:** PCA (box 2) *reshapes features* using covariance — no label, no loss. Gradient descent (box 5) *minimizes a loss* using the label. They are **not** two flavors of the same machine; they live on opposite sides of the label line. Full untangling: `2026-06-28_linear-algebra-vectors-dot-cosine_F.md` §21.

**Box [2] is optional.** You can feed all 20 features straight to box [3] and let gradient descent sort them out. PCA earns its seat only when features are many / noisy / redundant — it's an *upstream convenience*, not a mandatory link.

---

## 2. The journey note (the misconception this doc kills)

**The trap:** *"Probability and statistics are used at the end, in the production phase."*

**The correction:** they're not the last stage — they're **load-bearing in every stage.**
Three surprises:

- **The loss function IS probability.** Cross-entropy (the standard classification loss) is just
  "maximize the probability the model assigns to the right answer." Training literally minimizes
  a probability formula. So probability sits at the *heart of training*, not after it.
- **A classifier's output IS a probability.** Logistic regression / softmax don't say "HOT" —
  they say "P(HOT) = 0.83." Deciding what to *do* at 0.83 is your threshold call (Bayes!).
- **Evaluation IS statistics.** Accuracy, precision/recall, confidence in the metrics — all
  statistics on the errors.

And the idea you were reaching for — *"input arrives in a range that was never in the training
data"* — that's a real, named thing: **out-of-distribution (OOD) detection.** The model was trained
inside a bell curve of familiar inputs; a new input far out in the tail (huge z-score) means "don't
trust my prediction here." Your SSD instinct is exactly right: it's an anomaly fence around the
model itself. Models **interpolate** well (between seen examples) and **extrapolate** badly (beyond
them) — probability is how you *know which one you're doing*.

---

## 3. Phase × math — the master table

Running example throughout: **your thermal-throttle model** (inputs: temp, clock, queue depth,
latency… → predict: throttle in the next N seconds?).

| Pipeline phase | Math doing the work | On the thermal model, concretely |
|---|---|---|
| **Prep** | **Linear algebra:** vectors, norms, dot/cosine, covariance → PCA. **Statistics:** mean/σ for scaling (z-score normalization) | 20 sensor channels → covariance matrix → eigen → keep 3 directions (99% of the signal). Scale °C and MHz to comparable units so neither bullies the model |
| **Model itself** | **Linear algebra:** the forward pass is matrix × vector, layer after layer | `prediction = W₂·f(W₁·x)` — weights ARE matrices; inference is matmul |
| **Training loop** | **Calculus:** loss function, derivatives, chain rule → gradient descent. **Probability:** the loss (cross-entropy = max-likelihood). **Linear algebra:** gradients computed as matrix ops | Loss says "you predicted no-throttle, it throttled — wrong by this much"; chain rule traces blame back through every weight; each weight takes a small step downhill |
| **Evaluate** | **Statistics:** metrics (accuracy, precision/recall), variance across folds (cross-validation), confidence intervals | "Catches 92% of throttle events, 3% false alarms — measured on days it never trained on" |
| **Deploy & predict** | **Probability:** output = P(throttle), threshold choice, Bayes reasoning on alarms. **Statistics:** OOD/anomaly fences (z-scores), drift monitoring. | Fires at P > 0.7; a reading at z = +4 on temp → "outside my training world, flag don't guess"; monthly drift check: has the input distribution moved? |
| **Edge deployment** | **Statistics of the weights:** INT8 quantization uses each tensor's min/max/distribution. **Norms:** clipping. | Weight matrix's spread decides the INT8 scale factor; model must fit SRAM + latency budget |

**How to read this:** no math topic owns one box. Linear algebra dominates *data-shaping and the
model's body*; calculus owns *learning*; probability/statistics own *judging and trusting* — at
every stage, not just the end.

---

## 4. Your zoom-out, cleaned (supervised learning as a loop)

Your own broad view, tightened into six numbered beats — this is the paragraph to be able to say
out loud:

1. Input arrives as **vectors/matrices** (linear algebra territory).
2. Linear algebra **extracts the cream** — PCA/covariance drop redundant channels; normalization
   puts features on one scale.
3. The model makes a guess: **matrix multiplication** through the weights.
4. The **loss function** measures how wrong (its formula usually comes from probability).
5. **Calculus** (derivative + chain rule = gradient) finds which way each weight should move;
   **gradient descent** moves them a small step.
6. Loop 3→5 until loss flattens: weights are now "tightened to match input to target."
   Then **statistics** judges it on unseen data, and in production **probability** rides along
   with every prediction (confidence + OOD fences).

---

## 5. Concept → algorithm cheat-table (what powers what)

| Math concept you learned | Powers these ML pieces |
|---|---|
| Dot product | similarity scores, every neuron's core op (weights · inputs), attention in Transformers |
| Cosine similarity | recommendations, embeddings/vector search (RAG, Module 5) |
| Magnitude / norms | distances, MSE loss, gradient size, gradient clipping, quantization scaling |
| Covariance matrix | PCA, feature-redundancy detection, multivariate Gaussians, anomaly detection |
| Eigenvectors / eigenvalues | PCA (Session 5), spectral methods, "where does the variance live" |
| Mean / variance / σ | normalization, z-scores, drift & anomaly fences, initialization scales |
| Normal distribution | noise models, OOD detection, confidence, weight-init assumptions |
| Conditional probability + Bayes | classifier outputs, threshold decisions, Naive Bayes, uncertainty |
| Derivative + chain rule | backpropagation (Session 7) — the entire training loop |
| Gradient descent | training literally everything, incl. LoRA finetuning (Module 4) |

---

## Key takeaways

- **One pipeline, six boxes** — every course topic is a zoom-in on one box. Ask "which box am I in?"
- **Linear algebra** = the data's shape and the model's body. **Calculus** = how it learns.
  **Probability/statistics** = how it's judged and trusted — *in every phase, not just production.*
- The loss function is probability in disguise; the output is a probability, not a verdict.
- "Input outside the training bell" = OOD — the model's own anomaly fence. Your firmware instinct
  maps 1:1.
- On the edge, one more math layer appears at the END: quantization = statistics of the weights.
