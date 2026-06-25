---
title: Bayes' Theorem & The ML Bloodline
date: 2026-06-25
session: Sage Scroll II
domain: SSD thermal throttling
tags: [bayes, probability, machine-learning, taxonomy, decision-tree, edge-ai]
goal: on-device predictive thermal-throttle ML model (Edge AI)
---

# 🐸 Sage Scroll II — Bayes' Theorem & The ML Bloodline

> Running example throughout: **SSD thermal throttling** — a sensor reads temperature, fires HOT, and firmware must decide whether to throttle.

**Concepts mastered today:** [[Bayes' Theorem]] · [[AI vs ML vs Deep Learning]] · [[Classic ML vs Deep Learning Models]] · [[Decision Tree]] · [[Features vs Weights]]

---

## ① Bayes' Theorem

**Why it matters:** A sensor screams HOT. Do you trust it? Bayes answers *"given the alarm fired, how likely is it real?"* by combining the sensor's spec with how rare real events actually are.

### The core move — flip the conditional

| Direction | Reads as | Where it lives |
|---|---|---|
| **KNOWN** — `P(HOT \| Real)` | "given it's truly real, how often does the sensor catch it?" | the **datasheet** (hardware, fixed) |
| **WANT** — `P(Real \| HOT)` | "the alarm just fired — should I trust it?" | this **field moment** (depends on base rate) |

> Known is about the **hardware**. Want is about **this moment in the field**. Bayes is the bridge.

### The four numbers (200-cycle table)

|                | Real Event | No Event | Total |
|----------------|-----------|----------|-------|
| **Sensor HOT**    | 18        | 18       | 36    |
| **Sensor NORMAL** | 2         | 162      | 164   |
| **Total**         | 20        | 180      | 200   |

- **Base rate** `P(Real)` = 20/200 = **10%** — the piece the datasheet can't give you
- **Detection rate** `P(HOT|Real)` = 18/20 = **90%** — the sensor's spec
- **False-alarm rate** `P(HOT|No Event)` = 18/180 = **10%** — the sensor's noise
- **Prior calm** `P(No Event)` = 180/200 = **90%**

### The formula = body-counting, written out

```
P(Real | HOT) =          P(HOT|Real)·P(Real)
              ──────────────────────────────────────────────
              P(HOT|Real)·P(Real) + P(HOT|NoEvent)·P(NoEvent)

              =        0.90 × 0.10            0.09
                ──────────────────────────  = ──────  = 0.50  (50%)
                0.90×0.10  +  0.10×0.90        0.18
```

> **Shape to remember:** posterior = (one real-alarm bucket) ÷ (all alarm buckets summed). The bottom is "every way the sensor could fire HOT." The top is "the one way that's actually real."

### The base-rate trap
Out of 200 cycles: **18 real alarms** (from 20 real events × 90% caught) vs **18 false alarms** (from 180 calm cycles × 10% noise). Equal → only 50% trust. **Rarity is the villain:** there are 9× more calm cycles, so even a small false-alarm rate produces enough junk to drown the real catches. Make real events rarer → trust collapses further (~22% in the rare case).

### Decision boundary
- ✅ **Bayes wins** when real events are rare and the detector is imperfect — exactly when a naive "HOT ⇒ throttle" rule drowns in false alarms.
- ❌ **Fixed threshold wins** when the rule is simple, known & hard — e.g. datasheet says 95°C is a hard limit. Don't compute a posterior for what you already know for certain.

> 🔌 **Edge-AI bridge:** the base rate is exactly what your on-device predictive throttle must carry. A controller that ignores how rare real events are will throttle on noise and tank performance.

---

## ② AI → ML → Classic / Deep — the bloodline

The nesting is right; the trap is thinking *"classic ML = rule-based."* It isn't. Rule-based sits **outside** ML.

```
AI ───────────────────────────────────────────────┐
│  Rule-based / expert systems                     │
│     hand-coded if/else — NO learning             │
│     (your  if(temp>90) throttle;  firmware)      │
│                                                  │
│  Machine Learning — learns weights FROM DATA ──┐ │
│  │   Classic ML            Deep Learning       │ │
│  │   (you pick features)   (network finds them)│ │
│  └────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────┘
```

### The two dividing lines

| Boundary | Question | Answer A | Answer B |
|---|---|---|---|
| Rule-based vs ML | **Who writes the logic?** | Human writes `if(temp>90)` → rule-based | Machine learns thresholds from data → ML |
| Classic vs Deep | **Who finds the features?** | You hand-pick → classic | Network discovers them in layers → deep |

> **Anchor:** the Jun-20 linear classifier *learned* its weights via gradient descent → it's classic ML, **not** rule-based. If "classic = rule-based" were true, that notebook would need no training at all.

### The bridge between the clans
A single neuron = **logistic regression**. Stack it into many feeding-forward **layers**, let it learn its own features → you cross from classic ML into deep learning.
⚠️ Only logistic regression is "the neuron." A **decision tree is a sibling model** — stacking trees gives a *random forest* (still classic ML), never a neural net.

---

## ③ Classic ML vs Deep Learning — the two clans

### 🍃 Classic ML *(you curate features, model learns weights)*

| Model | What it does | Course |
|---|---|---|
| Linear regression | fit a line → predict a number | Sess 2 · Jun 27 |
| Logistic regression | soft yes/no boundary → classify **(= the neuron)** | Sess 2 · Jun 27 |
| Decision tree | nested if/else, but *learned* | Sess 3 · Jul 4 |
| SVM | widest margin between classes | Sess 3 · Jul 4 |
| Random forest / boosting | many weak voters → one strong call | Sess 4 · Jul 11 |
| k-NN | "what do my nearest neighbors look like?" | — |
| Naive Bayes | classify using Bayes' theorem (①!) | — |
| k-means / PCA | cluster / squeeze features | Sess 5 · Jul 18 |

### 🌀 Deep Learning *(network finds its own features)*

| Model | What it does | Course |
|---|---|---|
| Feedforward NN / MLP | stacked neurons — the base net | Sess 7 · Jul 25 |
| CNN | sees images; convolution = sliding FIR filter | Sess 9 · Aug 8 |
| RNN / LSTM | remembers sequences; hidden state = persistent register | Sess 10 · Aug 16 |
| Transformer | attention replaces recurrence — powers all LLMs | Sess 14 · Sep 5 |
| LLMs / GANs / diffusion | scaled transformers; generate data | Modules 4+ |

> 🔌 For your **on-device SSD throttle**: classic ML (small tree or logistic model) likely wins — fits in SRAM, runs in nanoseconds, explainable. Deep learning earns its cost only on huge *unstructured* data (images, audio, text).

---

## ④ Decision Trees — firmware whose constants were learned

Not a knowledge tree — a flowchart of yes/no questions. You've written hundreds in C. The only difference: the machine **learns the branch values from data**.

```
[ temp > 85°C ? ]
 ├─ no  ─→ DON'T THROTTLE
 └─ yes ─→ [ P/E cycles > 50k ? ]
            ├─ no  ─→ [ retention > 30d ? ] ─→ NO / THROTTLE
            └─ yes ─→ THROTTLE
```

**Vocab:** Node = a question · Branch = yes/no path · Leaf = final answer · Depth = questions before deciding.

### Trained tree vs your actual firmware
At **runtime they're twins** — both nested `if` comparisons. The difference is upstream:

|  | Hand-coded firmware | Trained decision tree |
|---|---|---|
| Who picks thresholds | your gut / datasheet (`90°C`) | algorithm proves `85°C` best separates the data |
| How many signals at once | 2–3 you can reason about | finds 4-way interactions automatically |
| When data changes | engineer rewrites & revalidates | feed fresh telemetry → regenerate → reflash |

> A trained tree **is** firmware — just firmware whose constants were learned from the field instead of written by you.
> ↩ Hand-code when the rule is simple/known/hard (95°C hard-limit). Learn a tree when thresholds are unknown, drift across lots, and depend on several signals at once.

---

## ⑤ Features vs Weights — the vocabulary that bites in class

| Word | What it is | Who sets it |
|---|---|---|
| **Feature** | an input column (workload, temp, P/E cycles) | **human**, in classic ML |
| **Weight** = **parameter** | how much each feature counts | **always learned** from data |

> **Feature = the question you feed in. Parameter/weight = what the model learns.** Parameters are never hand-set — if a human set them, it wouldn't be learning.

### Your SSD model, concretely
```
Predict: THROTTLE or NOT

features (you curated):    temp   P/E   retention   workload
weights  (model learned):  0.7    0.2     0.05         0.4
                            ↑ temp matters most — the model figured that out

score = 0.7·temp + 0.2·cycles + 0.05·retention + 0.4·workload
```

> That `score = Σ wᵢ·featureᵢ` is a **dot product** — your MAC loop. The linear algebra you learned IS the engine inside the linear classifier. Full circle. 🐸

|  | What you feed in | Who engineers features | Who learns weights |
|---|---|---|---|
| **Classic ML** | clean hand-built features | **you** | data |
| **Deep Learning** | raw messy data | **the network** | data |

---

## 🚦 Bonus — Bangalore Traffic (transfer test, passed)

Same two clans, new domain.

- **Classic ML:** hand-curate features (`time of day`, `8am rush flag`, `bus timings`, `school open/close`) + 2–3 yrs of traffic history → model learns weights.
- **Deep Learning:** feed raw data (live GPS pings, raw timestamps, weather) → network builds its own features, finding patterns you'd never hand-code, e.g. *"rain + Friday evening + a match at Chinnaswamy = total gridlock."*

**Which to pick?** Classic ML when you have clean tabular history and know which signals matter (cheaper, explainable). Deep learning when raw feeds are massive and hand-engineering is hopeless. Same "when is the simpler tool still right?" call you make on hardware.

---

## ⑥ Intuitions from this session (learner-derived)

### ML = a *learned mathematical function*

An ML model is a mathematical function: `output = f(features, parameters)`. Not magic — arithmetic.

- **Everything in the world boils down to numbers**, and math only plays with numbers. Image = grid of RGB values (each pixel = 3 numbers, 0–255). Audio = samples. Text = token IDs. "Modulated into a number" — like sampling an analog signal into ADC counts.
- The numbers aren't a loose pile — they're **structured into vectors / matrices / tensors** (linear algebra). An image is a tensor `H × W × 3`; that structure is *why* CNNs exist.

> **Physics models are math functions too** (`F = ma`). The difference isn't math-vs-physics — it's *where the numbers come from*: physics derives them from **laws**; ML **fits them from data**. Same math universe, different origin of the constants.

```
raw world → numbers → arranged into tensors → fed to a math function → prediction
```

> 🔌 **Why this unlocks Edge-AI:** if the model is just arithmetic (multiply each feature by a weight, add them up = a dot product / MAC), it can run on the controller. Inference = MAC loops on integers → that's why INT8 quantization works and a tiny model fits in SRAM.

### Algorithm vs Model — the trainer and the bodybuilder

**The algorithm doesn't *become* the model — it *produces* it.**

| Term | What it is | Example |
|---|---|---|
| **Algorithm** | the *procedure* that adjusts parameters from data | gradient descent; CART tree-builder |
| **Model (architecture)** | the *shape* of the function, params not yet set | "a logistic regression," "a decision tree" |
| **Trained model** | shape **+ learned parameters** — the deployable artifact | the fitted weights; the tree with split values |

```
untrained model + data
       │  (the ALGORITHM runs)
       ▼
  TRAINED MODEL  ← function with learned parameters, ready to predict
```

> **Algorithm = how it learns. Model = what it learned.** You don't train an algorithm; the algorithm is what *does* the training. (Library caveat: sklearn loosely calls both "estimators.")
> Embedded anchor: algorithm = the **Vref-calibration sweep routine**; model = the **calibration table** it produces. You ship the table, not the sweep.

**The bodybuilder analogy (learner's own — it's a complete, correct picture of supervised training):**

| Bodybuilder world | ML world |
|---|---|
| the trainer's method | the **algorithm** (e.g. gradient descent) |
| the bodybuilder | the **model** |
| muscles built (emerge from training, not chosen) | **parameters / weights** |
| height, weight (inputs) | **features** |
| target physique (sprinter vs lifter) | **label / target** |
| workouts & meals trained on | **training data** |
| how hard each session pushes | **learning rate** |
| one workout session | one **iteration** |
| gap between his body and the goal | the **loss** (shrinking it = training) |

> Key line: **features go IN, the target is what you aim AT.** The goal is not a feature — it's the target. The trainer adjusts muscles (parameters) until output matches the goal (target).

---

## ⚡ Key Takeaways

- **Bayes** = flip `P(evidence|cause)` into `P(cause|evidence)`. Posterior = one real bucket ÷ all buckets. **Rarity is the villain.**
- **Rule-based ≠ classic ML.** Rule-based hand-codes logic (no learning), sits outside ML.
- **Classic vs Deep** = who finds the features. Classic: you. Deep: the network, via stacked layers.
- **The neuron** = logistic regression. Stack in layers → deep learning. A decision tree is a sibling, not a neuron.
- **Decision tree** = learned nested if/else. Runtime-twin of firmware; difference is constants came from data.
- **Feature** = input you feed. **Weight/parameter** = what the model learns. Never confuse them.
- **Edge-AI line:** small classic models fit constrained silicon; deep nets only earn their cost on huge unstructured data.
- **ML = a learned math function.** Everything → numbers → tensors → arithmetic → prediction. Physics derives constants from laws; ML fits them from data.
- **Algorithm ≠ model.** Algorithm = how it learns (the trainer); model = what it learned (the bodybuilder + his muscles). The algorithm produces the model.

### 📐 Formula sheet
```
z-score (standardize a feature)   z = (x − μ) / σ
linear score (a "neuron")         score = Σ wᵢ·xᵢ   (= dot product = MAC)
Bayes posterior                   P(A|B) = P(B|A)·P(A) / P(B)
   where  P(B) = P(B|A)·P(A) + P(B|¬A)·P(¬A)   ← all the buckets summed
```

---

## 🍥 Active Recall (answer before checking)

1. A HOT alarm is 90% accurate at catching real events. So if it fires, is it 90% likely real?
   → **No.** That confuses `P(HOT|Real)` with `P(Real|HOT)`. Rare events + huge calm population → trust drops to ~50% or less. Base-rate trap.
2. Is a decision tree a kind of neural network?
   → **No.** The neuron is logistic regression. Stacked trees = random forest (classic ML), never a net.
3. `if(temp>90) throttle;` — is that machine learning?
   → **No**, rule-based. You hand-coded the threshold. ML = the machine *learns* it from data.
4. In `score = 0.7·temp + 0.2·cycles`, which are features, which are weights?
   → temp, cycles = features. 0.7, 0.2 = weights/parameters. The sum is a dot product.
5. On-device SSD throttle predictor — classic ML or deep learning, why?
   → **Classic ML.** Tabular telemetry, small feature set, must fit SRAM, run in ns, be explainable.

---

*Next: watch the Jun-20 recording → walk the linear-classifier notebook as your thermal model.*
