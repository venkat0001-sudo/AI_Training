---
title: Chain rule → the training gradient (self-study, depth-gated)
date: 2026-07-05
sessions: [F]
concepts: [calculus, gradient-descent]
type: notes
recap: The chain rule, drilled from "I get it" to "I can build it" — 3 worked examples (with my real traps), the ∂p/∂w=x apple analogy, and deriving 2(P−T)·x = my thermal model's training rule, ending in a full 2-sensor thermal cycle.
tags: [calculus, chain-rule, gradient-descent, thermal-project]
---

# Chain rule → the training gradient

> [!abstract] What this doc holds
> Self-study session (3B1B *Essence of Calculus* ch 2–4) run through the **Depth Gate**: pushed from
> "conceptual understanding" to *deriving my thermal model's training rule by hand*. The traps I fell
> into ARE the value — they're the recall hooks. Related: [[2026-06-14_calculus-foundations_F]] ·
> [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]] (slide 52) · [[2026-07-04_thermal-ml-project-map_F]] · [[trap-log]]

## 0. Revision ladder (recall, don't re-read)

1. Chain rule = **rates MULTIPLY along a chain**. `y←u←x` ⇒ `dy/dx = dy/du · du/dx`. → §2
2. Method: **u-substitution** — name the inner `u`, peel outer × peel inner. Don't expand. → §2
3. Three layers of "knowing": **SEE → SOLVE → BUILD**. Intuition alone (3B1B) is layer 1 only. → §1
4. `∂p/∂w = x` — the **coefficient of the variable is the rate**. Apple analogy. → §4
5. `∂L/∂w = 2(P−T)·x` — the **training rule**, = gradient. error × input. → §5
6. `x` in the gradient = **credit assignment** (silent sensor x=0 → zero correction). → §6
7. Full **thermal cycle**: sensors → predict → loss → gradient → update → repeat. → §7
8. Sanity checks: **degree-check** + **numerical gradient-check**. → §3

## Why are we learning this?

Gradient descent trains every model by asking *"if I nudge this weight, how does the loss move?"* —
`∂Loss/∂weight`. But the loss doesn't touch the weight directly; it sees the prediction, which sees
the weight. That's a **chain**. The chain rule is the only tool that computes a rate through a chain,
so it is **the literal training engine** of my thermal predictor (edge grade **⭐⭐⭐**).

---

## 1. The three layers of "knowing" (the honest map)

```
   LAYER 1: SEE it     ← 3B1B ch 2–4 — intuition, no computation
   LAYER 2: SOLVE it   ← compute a derivative by hand   ← project needs THIS
   LAYER 3: BUILD it   ← the numpy twin / training loop
```

> [!warning] The trap I started in
> I watched 3B1B and said "I get it." But 3B1B *deliberately* stops at layer 1 (intuition). For a
> ⭐⭐⭐ concept, recognition ≠ ready. Backprop is *numerical* chain rule computed thousands of times —
> you can't debug a computation you can only visualize. **Conceptual is necessary, not sufficient.**

---

## 2. The method — u-substitution (peel outer × peel inner)

`y = (5x−2)³` → let `u = 5x−2`:
```
   du/dx = 5           (inner)
   dy/du = 3u²         (outer — the exponent comes from THIS problem)
   dy/dx = 3u² · 5 = 15u² = 15(5x−2)²      ← leave it factored. done.
```

> [!quote] The analogies that made the chain rule stick (humor-first)
> **😄 Funny — sleep → coffee → mood:** how much does mood improve per hour of sleep? Not direct —
> sleep buys coffee, coffee buys mood. Each hour of sleep → **2** cups; each cup → **+3** mood ⇒
> **6 mood/hour**. The link-rates (3 and 2) **multiply**. That's the entire chain rule in one image.
> **🔧 SSD — temp → resistance → latency:** `d(latency)/d(temp) = d(latency)/d(resistance) · d(resistance)/d(temp)`.
> A sensor chain — I already reason this way in firmware.
> **🎯 The ML chain:** `∂L/∂w = ∂L/∂p · ∂p/∂w` — loss ← prediction ← weight. Same shape, always.

> [!example] Warm-up (the first gut-check): `y = u²`, `u = 3x`
> Two links: `dy/du = 2u`, `du/dx = 3` ⇒ `dy/dx = 2u·3 = 6u = 18x`; at **x=1 → 18**.
> Recognize the two links first, then tackle the harder reps below.

> [!note] "The recipe, not the dish."
> Naming the two links out loud is *describing* the method. The Depth Gate needs me to **execute** it —
> produce the actual expressions, not say "calculate them separately." Describing ≠ solving.

### The three worked examples + the exact traps I hit (the journey)

> [!example] `y = (3x+1)²`  → answer `18x+6`
> I tried to *expand* instead of chain-rule it: wrote `(3x+1)² = 3x²+6x+2`. **Wrong twice:**
> `(3x)² = 9x²` (not `3x²`) and `1² = 1` (not `2`). Correct expansion `9x²+6x+1 → 18x+6`.
> Chain-rule way: `2(3x+1)·3 = 6(3x+1) = 18x+6`. ✅ Both agree — when the algebra's right.

> [!example] `y = (5x−2)³`  → answer `15(5x−2)²`
> I **dropped the cube** — used `u²` instead of `u³` (the `²` hitched a ride from the previous
> problem). Got a *linear* `20x−4`. **Degree-check caught it:** derivative of a cubic must be a
> quadratic; I got a line ⇒ an exponent got lost. Correct: `dy/du = 3u² → 15(5x−2)²`.

> [!example] `y = (2x+1)⁴`  → answer `8(2x+1)³`
> Chain rule perfect this time (`4u³·2 = 8u³`). But I *over-simplified*: `8(2x+1)³ → 8(4x+2)³`.
> **You can't slide a coefficient into a power:** `(4x+2)³ = [2(2x+1)]³ = 2³(2x+1)³ = 8(2x+1)³` — the
> 2 gets **cubed** inside. So `8(4x+2)³` is 8× too big. **Lesson: leave it factored, stop.**

> [!tip] Two free sanity-checks (both are real ML tools)
> - **Degree-check:** deg(derivative) = deg(function) − 1. A collapsed degree = a dropped exponent.
> - **Numerical gradient-check:** plug a number, compare to `[f(x+h)−f(x−h)]/2h`. This is *literally*
>   the backprop debugging technique called **gradient checking**.

---

## 3. Numpy twin — see the chain rule verify itself

```python
import numpy as np
f  = lambda x: (2*x+1)**4
df = lambda x: 8*(2*x+1)**3          # my factored answer
h  = 1e-5
for x in [0, 1, 2]:
    num = (f(x+h)-f(x-h))/(2*h)      # numerical gradient-check
    print(f"x={x}:  formula={df(x):.2f}   numeric={num:.2f}   match={np.isclose(df(x),num,rtol=1e-3)}")
# x=0: formula=8  numeric=8   ✓   (the wrong 8(4x+2)³ would give 64 — mismatch flags it)
```

---

## 4. `∂p/∂w = x` — the exchange-rate (where I kept getting trapped)

Prediction of a linear neuron: `p = w·x + b`. Differentiate w.r.t. the weight `w`:

> [!warning] My trap: I wrote `∂p/∂w = w`. It's `x`.
> `w` is the **knob training turns**; `x` is the **fixed input (data)**. `d/dw(x·w) = x` — the
> **coefficient of the variable is the rate** (same as `d/dx(6x)=6`).
> 😄 **Knob vs dial:** `w` is the **knob you turn**; `x` is the **reading on the dial** — you can't
> "turn the reading." Differentiating w.r.t. the knob leaves you the dial value `x`.

> [!tip] The other half of the trap I need to watch
> I once phrased it "p changes as much as x changes." But **`x` doesn't change** — only `w` moves.
> Say it precisely: **"`w` moves 1 unit, `p` moves `x` units."** `x` is the fixed exchange rate, never
> a thing that moves. (Mixing up variable-vs-constant is the exact `w`↔`x` slip.)

😄 **Apple-bill analogy (this is what made it concrete):**
```
   p   =   x   ·   w   +   b
   bill = price · quantity + delivery
   w = how many apples (the knob YOU turn) · x = price/apple (FIXED — a tag doesn't change)
```
Micro-numbers (`x`=₹30, `b`=₹20): bill goes `50 →+30→ 80 →+30→ 110 …` — **every apple adds ₹30**.
That constant step **is** the slope: `∂p/∂w = 30 = x`. A price tag can't move; only quantity does.

> [!note] The punchline that kills the trap forever
> Same `p = w·x`, but the derivative depends on **which one is the knob**:
> `∂p/∂w = x` (turn the weight) · `∂p/∂x = w` (turn the input). It's always *"the other one"*, because
> they're multiplied. In training, `w` is the knob → `∂p/∂w = x`.

```python
import numpy as np
x, b = 30, 20; w = np.arange(0,6); p = w*x + b
print(np.diff(p))   # [30 30 30 30 30]  == x == ∂p/∂w, for ANY quantity
```

---

## 5. Deriving the training rule `∂L/∂w = 2(P−T)·x`

One neuron: `w → p = w·x + b → L = (p − T)²`  (T = actual temp, constant). Two-link chain:

```
   link ①  ∂p/∂w = x                    (coefficient of w)
   link ②  ∂L/∂p = 2(p − T)             (chain rule inside: outer u², inner (p−T), du/dp=1)
   ────────────────────────────────────────────────
   ∂L/∂w = ② · ① = 2(p − T) · x
```

> [!success] This IS Session-2 Slide 52: `2(F − y)·x`.
> I derived my thermal model's training rule **by hand, from scratch.** See [[2026-06-27_s2-linear-logistic-regression-ppt-notes_s2]] §10.

Read the meaning (not just symbols):
```
   ∂L/∂w = 2 · (P − T) · x
               └error┘  └input┘
```
- **Prediction too hot** (`P>T`) → gradient **positive** → descent **lowers** `w`. Self-correcting.
- Correction **scales with the input `x`** → §6.

---

## 6. Why `x` is in the gradient — CREDIT ASSIGNMENT

> [!example] Two sensors, one wrong (too-hot) prediction. error = 2(P−T), shared.
> ```
>   Sensor A: xₐ=100 (loud)   → correction 2(P−T)·100  = BIG
>   Sensor B: x_b=0  (silent) → correction 2(P−T)·0    = ZERO, automatically
> ```
> The `×x` term assigns blame **in proportion to how much each input actually contributed.** The
> sleeping sensor's weight is *innocent until it fires* — no `if(asleep)skip`, the math zeroes it for
> free. Drop `x` and you'd punish a weight for a mistake it had no hand in → training thrashes.

✅ **Decision boundary — when NOT to expand / when the chain matters:** for a bare polynomial you
*can* expand and use the power rule. But the moment the function is a **composition you can't expand**
(`sigmoid(w·x+b)`, a neural layer, a loss over a prediction) the chain rule is the **only** way —
that's every ML gradient. So: learn the chain method, not the expand crutch.

---

## 7. ⭐ The full runtime thermal cycle (one concrete tick)

**Job:** predict controller temperature 10 s ahead from 2 sensors. Sensors are **INPUTS**; the model
makes **ONE prediction** compared to **ONE actual**.

```
 INPUTS (now)                    WEIGHTS (guess)     bias
   xA = 0.8 (IOPS load)            wA = 20            b = 20
   xB = 0.6 (norm. current temp)  wB = 50

 ① PREDICT   p = wA·xA + wB·xB + b = 20(0.8)+50(0.6)+20 = 16+30+20 = 66°C
 ② MEASURE   actual T = 80°C   (waited 10 s)
 ③ LOSS      L = (p−T)² = (66−80)² = (−14)² = 196     ⚠️ under-called by 14° → throttle too LATE
 ④ GRADIENTS error=2(p−T)=−28;  ∂L/∂wA=−28·0.8=−22.4;  ∂L/∂wB=−28·0.6=−16.8
 ⑤ UPDATE   (λ=0.1, w←w−λ·grad)  wA→22.24 (↑)   wB→51.68 (↑)   → next tick predicts hotter, closer to 80
```

> [!note] Read it in firmware terms
> Under-prediction → negative gradients → weights pushed **up** → predicts hotter next tick → throttles
> **earlier**. And **sensor A's weight moved more than B's** (−22.4 vs −16.8) *because its input was
> louder* (0.8 > 0.6) — credit assignment, live.

```python
# numpy twin — watch the 2-sensor neuron learn to predict 80°C
import numpy as np
xA,xB,T,lr = 0.8,0.6,80.0,0.1
wA,wB,b = 20.0,50.0,20.0
for t in range(25):
    p = wA*xA + wB*xB + b
    e = 2*(p-T)
    wA -= lr*e*xA;  wB -= lr*e*xB;  b -= lr*e
    if t in (0,1,24): print(f"tick {t:2d}: pred={p:6.2f}  loss={(p-T)**2:7.2f}")
# tick 0 pred≈66 loss≈196   →   tick 24 pred≈80 loss≈0   (it learned the true temp)
```

---

## Key takeaways

- Chain rule = **rates multiply**; method = **u-sub, leave factored**.
- **Conceptual ≠ ready** for a ⭐⭐⭐ brick — you must SOLVE and BUILD, not just SEE.
- `∂p/∂w = x`: coefficient of the variable is the rate (`w` moves, `x` is the fixed multiplier).
- **`∂L/∂w = 2(P−T)·x` = error × input = the training rule** (Slide 52), and `x` = credit assignment.
- Sanity-checks: **degree-check** + **numerical gradient-check** (a real backprop tool).
- **The journey (recall hook):** my errors *walked backwards* — `no method (expanded)` → `wrong exponent`
  → `over-simplified` → `variable-vs-constant slip`. Each rep the mistake got smaller and more downstream.
  That regression from "can't start" to "just tidy-up" IS what learning something for real looks like.
- **λ (learning rate)** = step size on each update `w ← w − λ·grad`. Too big overshoots; too small crawls.

## Formula sheet

```
chain rule:        dy/dx = dy/du · du/dx          (rates multiply)
power (inner u):   d/dx uⁿ = n·uⁿ⁻¹ · du/dx
neuron:            p = w·x + b     ∂p/∂w = x     ∂p/∂b = 1     ∂p/∂x = w
squared loss:      L = (p−T)²      ∂L/∂p = 2(p−T)
TRAINING RULE:     ∂L/∂w = 2(p−T)·x       w ← w − λ·∂L/∂w
degree-check:      deg(f′) = deg(f) − 1
grad-check:        f′(x) ≈ [f(x+h) − f(x−h)] / 2h
```

## Traps banked (→ [[trap-log]])

1. Expanded instead of chain-ruling (crutch that fails on `sigmoid` etc.).
2. Dropped the exponent (`u²` vs `u³`) — degree-check catches it.
3. Slid a coefficient into a power (`8(2x+1)³ → 8(4x+2)³`) — leave it factored.
4. `∂p/∂w = w` instead of `x` — variable (knob) vs constant (input) confusion.

## ML / project destination

This is the **training engine** of R1 (throttle predictor) and R2 (LSTM forecaster) in
[[2026-07-04_thermal-ml-project-map_F]]. Every gradient in backprop (Session 7+) is this chain rule
stacked across layers. **Owned = R1 becomes buildable.**
