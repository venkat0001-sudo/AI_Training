---
title: Derivative-as-limit → chain rule → gradient descent (the what-if drill)
date: 2026-07-08
sessions: [F]
concepts: [calculus, gradient-descent]
type: scroll
up: "[[MOC-foundation-math]]"
recap: "Depth-gate self-study check. Rebuilt: derivative = the LIMIT (exact, not the 2.01 approximation), chain rule multiplies because rates are nested 'per' counts, and the training rule 2(P−T)x = error × input. Anchored with what-if tables: nudge one number, watch the step change."
tags: [calculus, gradient-descent, depth-gate]
---

# 🍥 Derivative-as-limit → chain rule → gradient descent

> **Recap (one breath):** A derivative is the **limit** a slope-ratio homes in on as the nudge
> shrinks to zero — *exact*, not the 2.01 approximation. The **chain rule multiplies** because
> rates are nested "per" counts (pizzas-per-box × slices-per-pizza). And the training rule
> `2(P−T)·x = error × input` steers a weight downhill: the error picks the **direction**, the
> input decides the **blame**.

**Concepts touched:** [[calculus|derivatives & chain rule]] · [[gradient-descent|the training rule]]

**The arc today:** self-study (3B1B Essence of Calculus ch 2–4 + a partial-derivative / gradient
intro), then a depth-gate check where I narrated and got corrected. I kept defaulting to
*approximate* three times; each time we forced it back to *exact*. That pattern **is** the lesson.

---

## §1 · The derivative is the LIMIT (not the approximation)

**Cold open:** on a straight line the slope is the same everywhere — easy. On a curve, two points
give you the slope of the line *between* them (the **secant** = an average), not the slope *at* a
point (the **tangent**). Zoom in until the curve looks pixelated-straight, and the tangent appears.

```
 y│           ,Q          secant P→Q = AVERAGE slope over the gap (an APPROXIMATION)
  │        ,·ˊ ╱
  │     ,·ˊ  ╱
  │  ,·˟P───╱────── tangent at P = the DERIVATIVE (Q slid onto P)
  │,·ˊ
  └─────────────── x
```

**The keystone: the derivative is the value the ratio *approaches* as the nudge shrinks to zero —
the LIMIT — and it is exact.** The measured 2.1, 2.01, 2.001 are *approximations*; the number they
chase is the derivative.

### The anchor numbers — `f(x)=x²` at `x=1`  ^limit-table

```
 nudge dx │  (f(1+dx) − f(1)) / dx           │ ratio
──────────┼──────────────────────────────────┼───────
   0.1    │  (1.21   − 1)/0.1   = 0.21/0.1    │ 2.1
   0.01   │  (1.0201 − 1)/0.01  = 0.0201/0.01 │ 2.01
   0.001  │  …                               │ 2.001
   0.0001 │  …                               │ 2.0001   → homing in on ● 2
```

Two different axes, do not confuse them: the **nudge → 0**, the **slope → 2**. (A parabola is not
flat at x=1, so its slope cannot be heading to 0.)

### Why we can't just set the nudge to 0 — and the trick that saves it

Set `dx = 0` directly and you get `0/0`, which is **indeterminate** (not infinite — that's `1/0`).
The escape is algebra *first*, limit *second*:

```
Step 1 — CANCEL first          Step 2 — THEN send dx → 0
  (2x·dx + dx²) / dx             2x + dx  →  2x        (the +dx becomes EXACTLY 0)
  = dx(2x + dx) / dx
  = 2x + dx                     at x=1 → the derivative is exactly 2
```

Keep `dx` alive so you're *allowed* to cancel it (legal only because `dx ≠ 0`), then send it to
zero at the very end. The **cancellation** — not the smallness — is what escapes the `0/0`.
"Very small" only ever gives 2.0001; the limit gives exactly 2.

### Numpy twin — watch the ratio home in on 2

```python
import numpy as np, matplotlib.pyplot as plt
f  = lambda x: x**2
x0 = 1.0
dxs    = np.array([1, 0.5, 0.1, 0.01, 0.001, 1e-4, 1e-5])
ratios = (f(x0 + dxs) - f(x0)) / dxs          # the approximations
plt.axhline(2, color='green', ls='--', label='the LIMIT = derivative = 2')
plt.plot(dxs, ratios, 'o-', label='(f(1+dx) − f(1)) / dx')
plt.xscale('log'); plt.xlabel('nudge dx  (→ 0 toward the left)')
plt.ylabel('measured slope'); plt.legend(); plt.grid(True, alpha=.3); plt.show()
for dx, r in zip(dxs, ratios):
    print(f'dx = {dx:<8g}  ratio = {r:.6f}')  # 3, 2.5, 2.1, 2.01 ... → 2
```

---

## §2 · The chain rule multiplies because rates are nested "per" counts

**Cold open:** functions nest — `x → u → y`. A nudge in `x` pokes `u`, which pokes `y`. The two
link-rates **multiply**: `dy/dx = dy/du · du/dx`. The question is *why multiply, not add*.

### The picture — nested containers  ^pizza

```
   1 box ──► 3 pizzas ──► 8 slices per pizza     slices per box = 8 × 3 = 24
```

Not `3 + 8 = 11`. Each of the 3 pizzas brings its **own** 8 slices — **3 groups of 8**, not 3
*plus* 8. A derivative is just a **"per" rate** ("how many of the next thing per one of this
thing"); chaining "per" rates multiplies the group-sizes:

```
   pizzas per box   = 3    ← du/dx
   slices per pizza = 8    ← dy/du
   slices per box   = 8 × 3 = 24   ← dy/dx
```

**Pure-math twin (no toppings):** hours → minutes → seconds = `60 × 60 = 3600` sec/hour. Adding
would say an hour is 120 seconds — an hour of your life says no.

**The absurd check that kills the add-instinct:** ten `×1` gears in a chain give `1×1×…= 1`
(unchanged), not `1+1+…= 10`. Multiply is right; add is nonsense.

> ⚠️ **The trap I hit:** I first "explained" the chain rule as *"the du's cancel."* That's the
> **mnemonic, not the mechanism** — and it strands you the moment the `du`'s don't line up
> (partial derivatives, matrices). The real why is the nested-groups picture above.

---

## §3 · The training gradient `2(P−T)·x` = error × input

Now aim the chain rule at a loss. The chain that matters for training:

```
   weight w ──► prediction P=w·x ──► error e=(P−T) ──► loss L=e²
```

Training asks one question: *"if I nudge `w`, how does the loss `L` move?"* = `dL/dw`. Walk the
chain, multiply the three link-rates:

```
   dL/dw =  dL/de   ·  de/dP  ·  dP/dw
        =  2(P−T)   ·   1     ·   x     =  2(P−T)·x
```

Each link, decoded:
- `dP/dw = x` — nudging `w` moves `P` by `x` (since `P = w·x`, `x` fixed).
- `de/dP = 1` — error `e = P − T`; the constant `T` just **shifts** the curve, never **tilts**
  it, so it contributes 0 to the rate. (Derivative of any constant = 0.)
- `dL/de = 2e = 2(P−T)` — power rule on `L = e²`.

**The two meaningful pieces do two different jobs:**

```
   dL/dw  =   2 · (P − T) · x
                  └──┬──┘   └─ WHICH INPUT is to blame  (credit assignment)
                     └────── HOW WRONG & which way      (the error signal)
```

---

## §4 · One gradient-descent step — the thermostat + the blame

**The rule:** `w ← w − λ · dL/dw`. The **minus** means we step **opposite** the gradient — the
gradient points *uphill* (toward more loss); we want less, so we go the other way.

### Worked example — a pizza-party predictor  ^pizza-step

One knob `w` = "pizzas per guest". True appetite = **1.5 pizzas/guest**.

```
   input       x = 2 guests
   weight      w = 1            (naïve: one whole pizza each)
   prediction  P = w·x = 1×2 = 2 pizzas
   truth       T = 3            (they demolished three)
   error       P − T = 2 − 3 = −1        (negative = ordered too FEW)
   gradient    2·(−1)·2 = −4
   update      w ← 1 − 0.1·(−4) = 1 + 0.4 = 1.4   (λ = 0.1)
   next time   P = 1.4×2 = 2.8   → creeping toward 3 ✓
```

- **Direction (the thermostat 🌡️):** error negative (too few) → gradient negative →
  `w − (negative)` pushes the knob **UP** → order more. Too cold, heat up; too hot, cool down.
  It always shoves the prediction toward the truth.
- **Blame (the input `x`):** the `−4` is `2·(−1)·2`; that last `2` is `x`. A louder input earns a
  bigger correction, because via `P = w·x` a loud input gives that weight a bigger say in the
  answer — so a bigger share of the mistake.

---

## §5 · The what-if tables (nudge one number, watch the step)

The whole point of `2(P−T)·x` and `w ← w − λ·g` is that every lever has a *predictable* effect.
Base case throughout: pizza-party, `x = 2`, `w = 1` → `P = 2`, `λ = 0.1`.

### Table A · vary the TRUTH `T` (how hungry the crowd is) — the SIGN behaviour

| truth `T` | error `P−T` | gradient `2·err·x` | `w ← w − λg` | reading |
|---|---|---|---|---|
| `T = 3` (hungry) | `−1` | `−4` | `1.0 − 0.1·(−4)` = **1.4 ↑** | ordered too few → bump the knob UP |
| `T = 2` (spot on) | `0` | `0` | **1.0** (frozen) | perfect prediction → don't touch it |
| `T = 1` (light eaters) | `+1` | `+4` | `1.0 − 0.1·(4)` = **0.6 ↓** | ordered too many → cut the knob DOWN |

**Read it:** the error's sign is the steering wheel. `T` above → step up, `T` below → step down,
`T` equal → the weight stops moving (that's what *converged* means: zero error → zero gradient).

### Table B · vary the INPUT `x` (loud vs quiet sensor) — credit assignment

Hold the error fixed at `−1` so only `x` changes the story.

| input `x` | gradient `2·(−1)·x` | step `−λg` (λ=0.1) | reading |
|---|---|---|---|
| `x = 0.5` (quiet) | `−1` | `+0.05` | barely nudged — this knob hardly mattered |
| `x = 2` | `−4` | `+0.40` | moderate correction |
| `x = 10` (loud) | `−20` | `+2.00` | slammed hard — this knob drove the answer |

**Read it:** same mistake, correction scales with `x`. A silent input (`x = 0`) → gradient 0 →
weight **untouched** — no `if(asleep) skip`, the math zeroes the blame for free.

### Table C · vary the LEARNING RATE `λ` (stride length) — speed vs overshoot

Hold `g = −4` (the base error). True target `w = 1.5`.

| `λ` | step `−λg` | new `w` | reading |
|---|---|---|---|
| `0.01` | `+0.04` | `1.04` | tiny crawl — safe but slow |
| `0.1` | `+0.40` | `1.40` | healthy step toward 1.5 |
| `0.5` | `+2.00` | `3.00` | **overshoots past 1.5** → next step flips sign → oscillation |

**Read it:** `λ` too small = forever; too big = leap past the bottom and bounce. The decision
boundary of the stride.

### Table D · vary the NUDGE `dx` (from §1) — approximation → exact

| nudge `dx` | ratio `(f(1+dx)−f(1))/dx` | reading |
|---|---|---|
| `1` | `3.0` | crude — a wide secant |
| `0.1` | `2.1` | closer |
| `0.01` | `2.01` | closer still |
| `→ 0` (limit) | **`2` (exact)** | the derivative — after cancelling, not after shrinking |

---

## §6 · Numpy twin — the pizza knob learns

```python
import numpy as np, matplotlib.pyplot as plt
x, T, w, lr = 2.0, 3.0, 1.0, 0.1        # 2 guests, they ate 3, start naive, small step
hist = []
for step in range(15):
    P = w * x
    grad = 2 * (P - T) * x
    w -= lr * grad                       # step DOWNHILL (minus the gradient)
    hist.append(w)
plt.axhline(1.5, ls='--', color='green', label='true appetite = 1.5 pizzas/guest')
plt.plot(hist, 'o-', label='w (what the model believes)')
plt.xlabel('training step'); plt.ylabel('pizzas per guest'); plt.legend(); plt.grid(alpha=.3); plt.show()
print('final w =', round(w, 4), '  final prediction =', round(w*x, 4))   # → 1.5 , → 3
```

`w` climbs **up** to 1.5 (it started too low, so the fix pushes it up), and the prediction settles
on 3. Change `T` to 1 and it descends to 0.5 instead — Table A, live.

---

## Traps I hit today

![[trap-log#^deriv-is-limit]]
![[trap-log#^zero-over-zero]]
![[trap-log#^nudge-vs-slope]]
![[trap-log#^chain-cancel-mnemonic]]

---

## Decision boundary

- ✅ **Derivative-as-limit** — reach for it whenever "how fast is this changing *right here*". The
  cancel-then-limit method is the honest one; the numerical `(f(x+h)−f(x−h))/2h` is the debug tool.
- ✅ **Chain rule** — any nested "if I nudge this, how does that move" — and it's the *only* tool
  for a composition (every ML gradient is a composition).
- ✅ **`2(P−T)·x` + descent** — differentiable loss, weights to tune.
- ❌ **NOT** a one-shot solver — it's iterative and finds a *local* minimum; tiny linear problems
  belong to closed-form. And `λ` must be tuned (Table C).

---

## Project brick

This is the literal training engine of the **R1 throttle predictor** and **R2 LSTM forecaster**
([[gradient-descent]] project brick). Read the thermostat in firmware terms: under-predict the
temperature → negative gradient → weights pushed up → predicts hotter next tick → throttles
earlier. The what-if tables are the knobs I'll actually turn when the forecaster mis-calibrates.

**Still owed before this is fully owned (depth-gate honesty):** the jump from ONE weight to MANY
— **partial derivatives → the gradient vector** (each knob's partial, stacked into the downhill
compass). Watched it today; not yet rebuilt. Next brick.

---

## Key takeaways

1. The derivative is the **limit** (exact), not the small-nudge **approximation**.
2. `0/0` is **indeterminate**, not infinite — which is *why* a slope can be a clean finite number.
3. **Cancel first, then take the limit** — the cancellation escapes the `0/0`, not the smallness.
4. The chain rule **multiplies** because rates are **nested "per" counts** — not because "du's cancel".
5. `2(P−T)·x` = **error × input**: the error steers the **direction**, the input sets the **blame**.
6. Descent **subtracts** the gradient — step *opposite* the uphill arrow.

## Formula sheet

```
derivative   f'(x) = lim(dx→0) [f(x+dx) − f(x)] / dx      (cancel dx, THEN dx→0)
chain rule   dy/dx = dy/du · du/dx                        (nested "per" rates multiply)
training     dL/dw = 2(P−T)·x = error × input
update       w ← w − λ·dL/dw                              (minus = step downhill)
```
