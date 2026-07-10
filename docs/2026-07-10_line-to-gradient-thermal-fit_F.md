---
title: The whole R1 story — a line, two knobs, and gradient descent that fits the thermal predictor
date: 2026-07-10
sessions: [F]
concepts: [gradient-descent, linear-equation, calculus]
type: scroll
up: "[[MOC-foundation-math]]"
recap: "Start-to-end teaching-book walk of R1: the SSD heats under load → model it as a LINE temp = w·load + b → the two knobs w (climb rate) and b (floor) are IDENTICAL to m and c → measure each guess's miss (residual → loss bowl) → the gradient is the uphill compass, so walk DOWNHILL to the best fit → predict temp ≈ observed. Fixes four live cracks: knobs vs partial derivatives, prediction vs residual, what w actually measures, and 'downhill = less error not more'. Loaded with what-if numeric tables."
tags: [gradient-descent, linear-equation, thermal-project, depth-gate, teaching-book]
---

# 🍥 The whole R1 story — a line, two knobs, and the gradient that fits it

> **Recap (one breath):** Your SSD heats under load. Model that as a **line** `temp = w·load + b`
> — the *same* `y = m·x + c`, just wearing work clothes. `w` is the **climb rate** (°C per unit
> load, = the slope `m`), `b` is the **floor** (idle/room temp, = the intercept `c`). To *fit* the
> line: guess the two knobs, measure the **miss** on every reading (residual → squared → the
> **loss**), then read the **gradient** — the uphill compass — and step the two knobs the opposite
> way, **downhill**, until `predicted temp ≈ observed temp`. That downhill walk is **gradient
> descent**, and it is the literal training engine of R1.

**Chain:** [[linear-equation|line y=mx+c]] ──► two knobs (slope, intercept) ──► [[calculus|partial derivatives]] of the loss ──► the **gradient** ──► **[[gradient-descent]]** ──► best-fit line ──► R1 thermal predictor

---

## §0 · Daily compass — where this sits

- **Edge chain:** `line y=w·load+b ──► loss bowl ──► gradient ──► fit the two knobs ──► on-device temp prediction ──► throttle EARLY`
- **Project hook:** this *is* **R1** — the throttle predictor. Everything below builds the exact model firmware will ship.
- **Grade:** [[gradient-descent]] is **⭐⭐⭐ (edge 3, critical path)** → the depth bar is *rebuild from scratch*. This scroll is that rebuild, told as a story.

---

## §1 · The problem statement (why R1 exists at all)

An SSD heats up when it works hard. Cross a thermal limit and the controller **throttles** (slows
itself to cool) or, worse, risks data integrity. Reacting *after* the sensor screams is already too
late — the heat is here.

**R1's job: PREDICT the temperature from the workload, so firmware acts *before* the drive cooks.**

> 😄 **The funny version.** It's a toddler in a bath. React-mode = you wait for the scream, *then*
> check the water — kid's already par-boiled. Predict-mode = you know "hot tap + 8 seconds = ouch,"
> so you cut it at second 6. R1 is the parent who learned the *hot-tap-to-ouch line* and never lets
> it get to the scream.

> 🔧 **The SSD version.** You already live this: read-retry and Vref calibration don't wait for an
> ECC blow-up — they walk toward the safe point *ahead* of failure. R1 is the same reflex for heat:
> load telemetry in, predicted temperature out, throttle decision *early*.

We need a **rule** that turns a load number into a temperature number. The simplest honest rule is a
straight line.

---

## §2 · The model — a line (and the mapping that killed the confusion)

```
   temp = w · load + b
   ▲      ▲      ▲
   │      │      └── b = the FLOOR   : temperature when load = 0 (drive idle ≈ room temp)
   │      └───────── w = the CLIMB RATE : °C added per one unit of load
   └──────────────── temp = what we predict
```

**This is `y = m·x + c` with new names — nothing more.** That was the whole knot; here it is untied:

```
   y    = m · x    + c          the math-class line
   temp = w · load + b          the same line in firmware clothes
   │      │   │      │
   y↔temp   m↔w    x↔load    c↔b
```

| math name | firmware name | role | on the graph |
|---|---|---|---|
| `x` | `load` | the **input** you feed in | horizontal axis |
| `m` | `w` (weight) | the **slope / climb rate** | how steeply the line tilts |
| `c` | `b` (bias) | the **intercept / floor** | where the line crosses at load 0 |
| `y` | `temp` | the **output** you predict | vertical axis |

> **Lock it:** `w·load` *is* `m·x`. Same multiply, same slope-times-input. The letters changed; the
> machine did not.

---

## §3 · What the two knobs FEEL like (with what-if tables)

Two independent dials. `w` **tilts** the line; `b` **lifts** it. They never touch each other.

```
   temp
    │              ╱   ← big w  : this drive heats FAST
 54 │           ╱
    │        ╱        w = 3  →  every +1 load adds +3 °C
 42 │     ╱
    │  ╱
 30 │╱  ← b = 30  : the FLOOR — idle drive already sits at room temp
    └────────────────── load
    0   2   4   6   8
```

### What-if A — turn only the CLIMB-RATE knob `w` (hold floor b = 30)

*"What if this drive heats twice as fast? What if it barely heats at all?"*

| load | w = 1 → `1·load+30` | w = 3 → `3·load+30` | w = 5 → `5·load+30` |
|---|---|---|---|
| 0 | 30 | 30 | 30 |
| 2 | 32 | 36 | 40 |
| 4 | 34 | 42 | 50 |
| 6 | 36 | 48 | 60 |
| 8 | 38 | 54 | 70 |

**Read it:** every line *starts* at 30 (same floor) but **fans out** — bigger `w` = steeper climb =
hotter at the same load. `w` is the drive's *thermal sensitivity*.

### What-if B — turn only the FLOOR knob `b` (hold climb w = 3)

*"What if the ambient is a cold server room vs a hot rack?"*

| load | b = 20 → `3·load+20` | b = 30 → `3·load+30` | b = 45 → `3·load+45` |
|---|---|---|---|
| 0 | 20 | 30 | 45 |
| 2 | 26 | 36 | 51 |
| 4 | 32 | 42 | 57 |
| 6 | 38 | 48 | 63 |
| 8 | 44 | 54 | 69 |
| gap vs middle | −10 everywhere | — | +15 everywhere |

**Read it:** the three lines are **parallel** — identical tilt, shifted straight up/down by the
floor. `b` moves the *whole* line without rotating it. Change the room temperature, the line lifts;
its steepness is untouched. **Tilt and lift are separate knobs.**

> **Your own instinct, confirmed:** you said *"b can't really be 0 — even off, the drive sits at
> room temp."* Exactly right. `b` **is** that idle temperature. Setting `b = 0` would claim a drive
> at 0 °C when idle (unphysical); real `b ≈ 30`. We only ever set `b = 0` as a teaching simplification.

---

## §4 · Three cracks fixed (the exact spots the story wobbled)

### Crack 1 — the two knobs are **parameters**, NOT the partial derivatives

The word **slope** wears *two different hats*, and mixing them is the whole confusion:

```
   m      = slope of THE LINE        (tilt of the prediction — lives on the data plot)
   ∂L/∂m  = slope of THE LOSS w.r.t. m   (how the ERROR changes as you nudge m — lives on the loss bowl)
```

So `w` and `b` are the **two dials you turn** (the parameters). The **partial derivatives**
`∂L/∂w` and `∂L/∂b` are a *different* thing — they are the slopes of the *error* with respect to
each dial, and **stacked together they form the gradient**.

> **Corrected sentence:** *"Slope and intercept are the two **knobs**; `∂L/∂slope` and
> `∂L/∂intercept` are the two **partial derivatives** whose vector — the gradient — I follow
> downhill to the best-fit line."* (Not "slope and intercept ARE the partial derivatives.")

### Crack 2 — what `w` actually measures

You said *"load is how fast"* and *"w tells how much the load varies."* **Flip it.**

```
   load  = the INPUT you feed in / read off the telemetry.  (w never measures this)
   w     = the ANSWER to "when load goes up by 1, how much does TEMP go up?"
```

**`w` measures the *temperature's* response, never the load's variation.** Numeric proof with
`w = 3`:

| load steps by | temp steps by | that step ÷ load step |
|---|---|---|
| 0 → 1 | 30 → 33 (+3) | 3 |
| 1 → 2 | 33 → 36 (+3) | 3 |
| 5 → 6 | 45 → 48 (+3) | 3 |

The ratio (temp-change ÷ load-change) is **always `w = 3`**. That *is* the slope — rise over run —
and it reports **temp**, not load.

### Crack 3 — prediction vs residual

You said *"prediction = mx + c − observed."* That subtracted thing is not the prediction — it's the
**residual (the miss)**.

```
   prediction  =  w·load + b                       ← what the line SAYS
   residual    =  prediction − observed            ← how far the line MISSED (can be ±)
   loss        =  Σ residual²                       ← total badness of THIS line (one number)
```

Three different objects, in order: guess a temp → see how wrong it was → add up all the wrongness.

---

## §5 · Fitting the line — the miss, the residual, the loss

Real sensors jitter, so no straight line hits every dot. We want the line that **misses least.**

**The data (five noisy readings, floor b, climb w unknown):**

```
   load :  0    2    4    6    8
   temp :  31   35   43   47   55      ← wobbles around a slope-3, floor-30 line
```

**Start with a deliberately WRONG guess:** `w = 1, b = 20`. Predict each point, take the miss:

| load | observed | prediction `1·load+20` | residual = pred − obs | residual² |
|---|---|---|---|---|
| 0 | 31 | 20 | −11 | 121 |
| 2 | 35 | 22 | −13 | 169 |
| 4 | 43 | 24 | −19 | 361 |
| 6 | 47 | 26 | −21 | 441 |
| 8 | 55 | 28 | −27 | 729 |
| | | | | **loss = 1821** |

Every residual is **negative** → the line sits **too low** (predicting cooler than reality). Loss is
huge. This one number, **1821**, is the height on the loss bowl for the knob-pair `(w=1, b=20)`.

> **What-if C — a better guess drops the loss.** Try `w = 3, b = 30`:

| load | observed | prediction `3·load+30` | residual | residual² |
|---|---|---|---|---|
| 0 | 31 | 30 | −1 | 1 |
| 2 | 35 | 36 | +1 | 1 |
| 4 | 43 | 42 | −1 | 1 |
| 6 | 47 | 48 | +1 | 1 |
| 8 | 55 | 54 | −1 | 1 |
| | | | | **loss = 5** |

**1821 → 5.** Residuals now tiny and *mixed sign* (some over, some under) — the signature of a line
threading the cloud instead of sitting beside it. `(w=3, b=30)` is deep in the bowl's valley.

---

## §6 · The loss bowl, the two partials, and the direction rule

Plot the loss for **every** possible `(w, b)` and you get a **bowl**. The best line sits at the
**bottom**. Gradient descent is: *feel the slope of the bowl under your feet, step downhill, repeat.*

```
  Loss
   │╲                          ╱
   │ ╲   ● ← you are HERE      ╱
   │  ╲  (a wrong guess)      ╱
   │   ╲                     ╱
   │    ╲___             ___╱
   │        ╲___     ___╱
   │            ╲_●_╱  ← the FLOOR of the bowl = least loss = best (w, b)
   └──────────────────────────── w  (one knob; b has its own identical axis)
```

**The two partial derivatives** = the slope of the bowl along each knob's direction:

```
   ∂L/∂w  =  "if I raise w, does the loss grow or shrink?"     (from the training rule = 2·err·x)
   ∂L/∂b  =  "if I raise b, does the loss grow or shrink?"     (= 2·err ; blind to load, absorbs raw error)

   gradient  ∇L = [∂L/∂w, ∂L/∂b]     ← the two stacked = the compass
```

### The direction rule — the one that flipped, nailed with the bowl

**The gradient always points UPHILL (toward MORE loss). You always step the OPPOSITE way, downhill.**
That opposite-step is the minus sign in the update:

```
   w ← w − η·∂L/∂w        b ← b − η·∂L/∂b        η = learning rate (stride)
        ▲                        ▲
        └── the minus IS "walk downhill"; downhill = LESS loss (never more)
```

> **Corrected belief:** *"downhill = more error"* → **NO. Downhill = LESS error. That's the entire
> point of the walk.** The bottom of the bowl is the goal.

### What-if D — read the sign, know the step (no up/down confusion needed)

Stand on the bowl and just read where the floor is:

| `∂L/∂w` sign | where's the floor? | step direction | `w` does what | line does what |
|---|---|---|---|---|
| **negative** | to your **right** (bigger w) | step right | `w` **increases** | gets **steeper** |
| **positive** | to your **left** (smaller w) | step left | `w` **decreases** | gets **flatter** |
| **zero** | you're **on** the floor | don't move | `w` stays | best fit reached |

> Worked: `∂L/∂w = −22.4` (negative) → floor is to the right → `w ← w − η·(−22.4) = w + …` → `w`
> **increases** → line **steepens** toward the dots. (This is exactly the live self-correction from
> the session.) The gradient is just *a compass pointing away from the floor; you walk the other way.*

---

## §7 · The full loop → best fit → prediction ≈ observed

Put it together — this is the whole training loop, one tick:

```
   ① PREDICT   p = w·load + b                 (run the current line)
   ② MEASURE   compare p to the real temp     (residual = p − observed)
   ③ LOSS      L = Σ residual²                 (one badness number)
   ④ GRADIENT  ∂L/∂w = 2·err·load ,  ∂L/∂b = 2·err   (the uphill compass)
   ⑤ STEP      w ← w − η·∂L/∂w ,  b ← b − η·∂L/∂b     (walk downhill)
   ⑥ REPEAT    until the loss stops shrinking  (bottom of the bowl)
```

Each pass shrinks the loss; `w` drifts toward ~3, `b` toward ~30; the line snaps into the cloud.
When the bowl bottoms out, **predicted temp ≈ observed temp** — *that* is "best fit."

> **Credit assignment rides along for free** (the `·load` in `∂L/∂w`): a sensor that read a **loud**
> load earns a **bigger** weight correction than a quiet one, and a silent sensor (`load = 0`) gets
> **zero** correction automatically — no `if(asleep) skip`, the math zeroes it. See the two-sensor
> anchor in [[gradient-descent#^anchor]].

---

## §8 · Deploy — R1 doing its job in firmware

After training, firmware holds a tiny fixed rule, e.g. `temp ≈ 3·load + 30`. No iteration at
runtime — just **one multiply and one add per tick** (a single MAC), which is *why* a linear model
is cheap enough to live inside the controller:

```
   live load  ──►  temp̂ = 3·load + 30  ──►  temp̂ > danger?  ──►  throttle EARLY (before the real sensor gets there)
```

The **training** (the whole §5–§7 bowl-walk) happens **offline / once**; the **inference** (§8) is
the cheap part that ships. That split — expensive fit, cheap predict — is the heart of edge AI.

---

## §9 · Numpy twin — watch the two knobs walk to the fit

```python
import numpy as np, matplotlib.pyplot as plt

load = np.array([0., 2., 4., 6., 8.])          # the input (x)
temp = np.array([31., 35., 43., 47., 55.])     # the observed output (y)

w, b, lr = 1.0, 20.0, 0.002                    # the deliberately-wrong start guess
hist = []
for step in range(400):
    pred = w*load + b                          # ① predict  (the line)
    err  = pred - temp                         # ② residual (the miss)
    loss = np.sum(err**2)                       # ③ loss     (one number)
    dw   = np.sum(2*err*load)                   # ④ ∂L/∂w = 2·err·load   (uphill, tilt knob)
    db   = np.sum(2*err)                         #    ∂L/∂b = 2·err        (uphill, floor knob)
    w   -= lr*dw;  b -= lr*db                    # ⑤ step DOWNHILL (minus the gradient)
    hist.append(loss)
    if step in (0, 1, 399):
        print(f"step {step:3d}:  w={w:5.2f}  b={b:5.2f}  loss={loss:8.1f}")
# step   0: loss≈1821  →  step 399: w≈3, b≈30, loss≈5  (it found the line)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.scatter(load, temp, color='#ff9433', zorder=3, label='observed')     # the noisy dots
ax1.plot(load, w*load + b, color='#7fd4c0', label=f'fitted  temp={w:.1f}·load+{b:.1f}')
ax1.set_xlabel('load'); ax1.set_ylabel('temp'); ax1.set_title('best-fit line'); ax1.legend(); ax1.grid(alpha=.3)
ax2.plot(hist, color='#9fe8ff'); ax2.set_title('loss walking down the bowl')
ax2.set_xlabel('step'); ax2.set_ylabel('loss'); ax2.grid(alpha=.3)
plt.tight_layout(); plt.show()
```

The left plot proves the fit (line threads the dots); the right plot **is** the descent — loss
sliding down the bowl to its floor.

---

## §10 · When a LINE is the right model — and when it isn't

- ✅ **Use a line** when temperature rises roughly *proportionally* with load — cheap (1 MAC),
  interpretable (`w` = sensitivity, `b` = ambient), perfect for R1's first cut.
- ❌ **A line breaks** when heat *lags* load (thermal mass = temperature depends on the *history* of
  load, not just the current value) or saturates near a limit. That's the whole reason **R2 becomes
  an LSTM forecaster** — it remembers the recent load trajectory. Same gradient-descent engine,
  many more knobs.
- **Trade:** more knobs fit messier reality but cost MACs, SRAM, and training time. R1's line is the
  QD1-latency choice; R2's LSTM is the QD32-throughput choice. Pick per the thermal budget.

---

## §11 · Teach-back owed (seal it)

Explain to a junior firmware engineer at the next desk, in 4 sentences:
1. What R1 predicts and *why* (predict-not-react).
2. The two knobs — what `w` and `b` each mean physically.
3. How the gradient fits them (compass points uphill → step downhill → bottom of the bowl).
4. What the drive does with the prediction at runtime.

If all four flow without stumbling, R1 is **owned**, not just followed.

---

## Where it came from / where it goes

builds-on:: [[linear-equation]] — R1's model IS the line `y=mx+c`; `w↔m` (slope/climb-rate), `b↔c` (intercept/floor)
builds-on:: [[calculus]] — the two partials `∂L/∂w`, `∂L/∂b` are derivatives of the loss; the gradient is built by the chain rule
feeds:: [[gradient-descent]] — this whole story IS gradient descent grounded on a 2-knob line
feeds:: [[regression]] — fitting a line to data by minimizing squared residuals is linear regression
scroll:: [[2026-07-08_derivative-limit-to-gradient-descent_F]] — §7, the one→many jump + the earlier what-if tables
scroll:: [[2026-07-05_chain-rule-to-gradient_F]] — the training rule `2(P−T)·x` derived by hand
video:: StatQuest — Gradient Descent, https://www.youtube.com/watch?v=sDv4f4s2SB8 (the height/weight line fit = this same machine)
project-brick:: R1 throttle predictor — `temp = w·load + b` is the shipped model; this scroll is its full derivation

## Traps caught this session

![[trap-log#^knob-vs-gradient]]
![[trap-log#^predict-vs-residual]]
![[trap-log#^w-measures-load]]
![[trap-log#^downhill-more-error]]
