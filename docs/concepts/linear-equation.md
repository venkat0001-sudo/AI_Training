---
title: Line equation y = mx + c (and where a curve's slope diverges)
aliases: [line, linear-equation, y=mx+c, slope-intercept, mx+c, straight-line, tilt-and-lift, constant-slope]
date: 2026-07-09
sessions: [F]
lane: f
edge: 2
status: learning
type: concept
up: "[[MOC-foundation-math]]"
recap: "A line's slope is ONE constant you read straight off m in y=mx+c (the tilt); a curve's slope changes at every point, so it can only be DERIVED as a function (x²→2x). That gap is exactly where calculus begins."
---

# Line equation y = mx + c — and where a curve's slope diverges

> **Recap:** A line's slope is **one constant you read straight off `m`** in `y = mx + c` (the
> *tilt*); a curve's slope **changes at every point**, so it can only be **DERIVED** as a function
> (`x² → 2x`). That gap — read-off vs derive — is exactly where **calculus begins**.

**Chain:** rise/run (slope) ──► **line `y = mx + c`** ──► [[calculus|the derivative]] *(when the slope stops being constant)* ──► [[gradient-descent]] ──► [[regression]] *(fit the line to data)*

## What it is (plain words)

A **line** is the one shape whose slope **never changes**. Its equation `y = mx + c` has two knobs
that never touch each other:

- **`m` = slope = the TILT** — how fast it climbs. *Same everywhere.* This is the line's derivative.
- **`c` = intercept = the LIFT** — the starting height (where it sits at `x = 0`).

**A line advertises its slope** — `m` is printed right there as the coefficient of `x`. A curve
hides its slope, so you have to dig it out. That single difference is the whole story below.

## The two worlds, side by side — constant vs derived  ^side-by-side

|  | **LINE** `y = 2x` | **CURVE** `y = x²` |
|---|---|---|
| slope | **2** — one constant | **2x** — changes with x |
| how you get it | **READ** off the coefficient `m` | **DERIVE** it (first principles) |
| slope at `x = 1` | 2 | 2 |
| slope at `x = 3` | 2 | 6 |
| slope at `x = 5` | 2 | 10 |
| the derivative is… | a **constant** (`2`) | a **function** (`2x`) |
| needs a "zoom"? | **no** — read the label | **yes** — shrink a nudge to a point |

**Why the asymmetry?** `y = 2x` is already in `mx + c` form, so the slope *is* the coefficient —
printed on the label. `y = x²` is a **power**, not `mx + c`; there's no coefficient of `x` to read,
so the slope is hidden and must be extracted with the limit machine.

## Where it originated → how it went further (the narrative)

### ① Origin — a line, derived from rise-over-run

A line means "slope stays constant `= m`". Anchor at the y-axis crossing `(0, c)`; take any other
point `(x, y)` and drop a right triangle:

```
 y
 7┤                  ●(2, 7)   ← any point (x, y)
  │                ╱ ┆
  │              ╱   ┆  RISE = y − c = 7 − 3 = 4   (finish − start, vertical)
  │            ╱     ┆
 3┤ ●┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
  │(0, 3) anchor   RUN = x − 0 = 2   (finish − start, horizontal)
  └──┬───────────────┬──── x
     0               2
```

```
   slope = RISE / RUN = (y − c) / (x − 0) = 4 / 2 = 2      ← same everywhere = a line
   (y − c)/x = m   →   y − c = m·x   →   y = m·x + c        ← the equation IS rise/run rearranged
```

### ② Reading the slope straight off

```
   y = 2x       →  m = 2, c = 0   →  slope 2, through the origin
   y = 5x + 7   →  m = 5, c = 7   →  slope 5, starts at height 7
```

### ③ What the intercept does — tilt vs lift (parallel lines)

`y = 2x` vs `y = 2x + 3`: same tilt, different lift. The `+3` **lifts the whole line up by 3
without rotating it** — they stay **parallel**, exactly 3 apart at every x.

```
   x:        0    1    2    3    4
   y = 2x:   0    2    4    6    8
   y = 2x+3: 3    5    7    9   11
   gap:     +3   +3   +3   +3   +3     ← always 3  (the lift never touches the tilt)
```

`y = 2x` values also read as the rule *"y is always twice x"*: (0,0) (1,2) (2,4) (3,6) (4,8).

### ④ First principles even on a line — the slope falls out with no zoom

Run the limit machine on `f(x) = 5x + 7`. Substitute = "every `x` becomes `(x+h)`"; the `+7` has no
`x`, so it's untouched:

```
   f(x+h) = 5(x+h) + 7 = 5x + 5h + 7
   f(x+h) − f(x) = (5x + 5h + 7) − (5x + 7) = 5h        ← 5x cancels, +7 − 7 = 0  (NOT −14)
   ÷ h  = 5h / h = 5                                     ← the h is GONE before the limit
   h → 0  = 5
```

The `h` vanished *before* taking the limit — that's the algebra proof of "a line needs no zoom".
And the `+7` cancelled itself out → *why* the lift never reaches the derivative.

### ⑤ Going further — the curve, where the slope won't sit still

`y = x²` has a different slope at every point, so first principles must keep `x` **symbolic** (never
plug a number) — that's what turns a point-slope into a slope-*function*:

```
   f(x+h) − f(x) = (x+h)² − x² = x² + 2xh + h² − x² = 2xh + h²
   ÷ h  = 2x + h
   h → 0  = 2x                     ← a FORMULA, because x stayed a letter
```

```
   keep x a letter →  2x   (a function: slope everywhere)
   plug x=1 first  →  2    (a number: slope at one spot)
```

### ⑥ Using the slope-function + watching the limit converge

```
   slope 2x  at x=1 → 2 · at x=3 → 6 · at x=5 → 10     (different at every point)

   convergence of the difference quotient at x=1 (nudge h shrinking):
      h=0.1   → 2.1     h=0.01  → 2.01     h=0.001 → 2.001   → 2  (exact, after cancelling)
```

### ⑦ The trap to keep straight — "2x" wears two hats

| "2x" as… | what it is | its own slope |
|---|---|---|
| `y = 2x` | a **line** (a shape) | **2** (constant) |
| `f'(x) = 2x` | the **derivative of x²** (a slope-reporter) | reports `2·x` per point |

Same algebra by coincidence — a parabola's slope just *happens* to grow linearly. And the line
`y = 2x` has its own derivative `d/dx(2x) = 2`, flat, because it's a line.

## The anchor numbers  ^anchor

```
LINE   y = 2x       slope 2 everywhere            points (0,0)(1,2)(2,4)(3,6)(4,8)
       y = 2x + 3   slope 2, lifted +3            gap = +3 at every x  (parallel)
       triangle     anchor (0,3) → point (2,7):   run 2, rise 4, slope 4/2 = 2
CURVE  y = x²        slope = 2x (derived)          2x → 2,6,10 at x=1,3,5
       first princ.  (x+h)²−x² = 2xh+h² → 2x+h → 2x
```

## Numpy twin

```python
import numpy as np, matplotlib.pyplot as plt
x = np.linspace(-1, 4, 100)
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4))

# LEFT — LINES: slope is a constant you read straight off m
for m, c, lbl in [(2, 0, 'y = 2x'), (2, 3, 'y = 2x + 3'), (3, 0, 'y = 3x')]:
    axL.plot(x, m*x + c, label=f'{lbl}  (slope {m} everywhere)')
axL.set_title('LINES — constant slope (READ off m)')
axL.axhline(0, color='k', lw=.5); axL.axvline(0, color='k', lw=.5)
axL.legend(); axL.grid(alpha=.3)

# RIGHT — CURVE: slope CHANGES, derived as 2x (draw tangents to prove it)
axR.plot(x, x**2, 'b', label='y = x²')
for pt in (1, 3):
    s = 2*pt                                     # the slope-function 2x
    axR.plot(x, s*(x - pt) + pt**2, '--', label=f'tangent at x={pt}: slope {s}')
axR.set_title('CURVE — slope is a FUNCTION 2x (DERIVED)')
axR.axhline(0, color='k', lw=.5); axR.axvline(0, color='k', lw=.5)
axR.set_ylim(-2, 16); axR.legend(); axR.grid(alpha=.3)
plt.tight_layout(); plt.show()

print('LINE  y=2x   slope at x=1,3,5 :', [2, 2, 2])            # constant
print('CURVE y=x²   slope 2x at 1,3,5:', [2*1, 2*3, 2*5])      # 2, 6, 10
for h in [0.1, 0.01, 0.001]:                                    # first principles at x=1 → 2
    print(f'  diff-quotient(x=1, h={h}) = {((1+h)**2 - 1)/h:.4f}')
```

## Where it came from / where it goes

builds-on:: rise-over-run — the line equation IS constant rise/run rearranged; `(y−c)/(x−0)=m → y=mx+c`
feeds:: [[calculus]] — the derivative generalizes a line's *constant* slope `m` to a curve's *varying* slope, a function like `2x`; first principles is the machine that extracts it
feeds:: [[regression]] — linear regression **is** `y = mx + c` fit to data: **slope = weight, intercept = bias**
feeds:: [[gradient-descent]] — GD tunes the line's slope & intercept (`w`, `b`) to cut the loss; the §7 reconciliation (slope=weight, intercept=bias, SSR=loss) is this same line
contrasts-with:: [[calculus|the derivative]] — line: slope **read off**, constant; curve: slope **derived**, a function of x
scroll:: [[2026-07-08_derivative-limit-to-gradient-descent_F]] — §0 (line-vs-curve on-ramp) + §7 (the gradient-vector close)

## Decision boundary

- ✅ **Read the slope straight off `m`** whenever the equation is in `y = mx + c` form — a line's
  slope is advertised, constant, no calculus needed.
- ❌ **You cannot read a slope off a power or curve** (`x²`, `sin`, `sigmoid`) — there's no single
  `m`; you must use first principles or the derivative rules (power/chain).
- **A line is the special case** where the slope-function is a flat constant that ignores `x`. Every
  other function's slope is a genuine function of `x`.

## Traps I hit

![[trap-log#^tilt-times-lift]]
![[trap-log#^minus-distribute]]

## Depth layers

- **2026-07-09 (F, first contact):** built lines from the ground up in a long Socratic thread —
  derived `y = mx + c` from rise/run (the anchor triangle), separated **tilt** (slope) from **lift**
  (intercept), saw `y = 2x + 3` sit **parallel** to `y = 2x` (+3 at every x), ran first principles on
  **both** a line (`5x+7 → 5`, the `h` vanishes early) and a curve (`x² → 2x`, keep `x` symbolic → a
  function), and untangled the **two hats of "2x"**. → [[2026-07-08_derivative-limit-to-gradient-descent_F]] §0/§7

## Project brick

The line `y = w·x + b` **is** the R1 throttle predictor's model — **slope = weight** (each sensor's
sensitivity), **intercept = bias** (the idle/ambient temperature offset). Reading a line's slope
straight off `m` is why a linear model is *cheap* on an MCU: its sensitivity is known without
iterating. The curve/derivative machinery ([[calculus]] → [[gradient-descent]]) is what *trains* it.

## Formula

```
line:            y = m·x + c          m = slope (tilt, constant)   c = intercept (lift, start height)
from rise/run:   (y − c)/(x − 0) = m  →  y = m·x + c
slope of a line: constant m           (read off; d/dx(m·x + c) = m — the c vanishes)
slope of a curve: a function          (derive; d/dx x² = 2x)
first principles: f'(x) = lim(h→0) [f(x+h) − f(x)] / h    (cancel h, THEN h → 0)
```

## Flashcards

#flashcards/linear-equation

For `y = 5x + 7`, what is the slope, and does the `+7` change it? :: Slope is **5** — read straight off `m`. The `+7` is the *lift* (start height); it never touches the *tilt*, so `d/dx(5x+7) = 5`. The `+7` vanishes. (Trap: 5 and 7 don't multiply — per step y rises 5, not 35.)
Why can you read a line's slope off but must derive a curve's? :: A line is in `mx + c` form — the slope is the coefficient, printed on the label, constant. `x²` is a power with no visible slope; first principles digs out `2x`, a **function**.
What is `x²`'s slope at x = 1, 3, 5? :: 2, 6, 10 — from the slope-function `2x`. Different at every point, which is *why* it's a function, not a number.
