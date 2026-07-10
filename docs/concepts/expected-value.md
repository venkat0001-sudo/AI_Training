---
title: Expected value (EV)
aliases: [expectation, EV, expected-value, E[X], long-run-average, mean-of-a-distribution]
date: 2026-07-10
sessions: [F]
lane: f
edge: 2
status: learning
type: concept
up: "[[MOC-foundation-math]]"
recap: "EV = Σ (probability × payoff) — the long-run AVERAGE haul, not a promise about the next try. A big reward and a rare chance fight; the EV is the referee. It's a dot product, and the ML loss you minimize is one."
---

# Expected value (EV)

> **Recap:** EV = **Σ (probability × payoff)** — the **long-run average** haul over many tries, not
> a promise about the next one. How *big* a payoff is and how *often* it happens pull against each
> other; **EV is the referee.** Same sum-of-products shape as a dot product — and the ML **loss** you
> minimize is an expected value (average error).

**Chain:** [[probability]] (the weights) ──► **expected value** `Σ pᵢvᵢ` ──► the **loss** (average error) ──► [[gradient-descent]] (drive that average down)

## What it is (plain words)

Every outcome carries **two** separate numbers: **how often** it happens (probability) and **how
much** it pays (payoff, with a sign — money *to* you is `+`, *away* is `−`). Multiply the pair for
each outcome, add them all up: that's the average you'd land on if you played the game a thousand
times. **Big reward ≠ good bet** — a huge payoff on a rare event can still lose.

😄 **The dog-treat hustle.** A friend with a clumsy Labrador: *"₹200 to you if he catches this treat
first try, but ₹50 to me if he misses."* Sounds generous — 4× your money! But the dog catches 1-in-10,
so EV = −₹25: you bleed money every round. **The big prize was too rare.** Only the EV knew.

## The anchor numbers  ^anchor

```
TROLL 2 BET  — "get $10 if the next person heard of Troll 2, pay $1 if not"
  heard      p=0.17   payoff +10   →  +1.70
  not heard  p=0.83   payoff −1    →  −0.83
  EV = +0.87   ✅ good bet   (rare $10 beats the frequent $1 loss)

DOG-TREAT BET — "get ₹200 if he catches, pay ₹50 if he misses"
  catch 0.10  +200 → +20  ;  miss 0.90  −50 → −45  ;  EV = −25   ❌ walk away
  catch 0.33  +200 → +66  ;  miss 0.67  −50 → −33.5;  EV = +32.5 ✅ FLIPPED — only the odds changed

BREAK-EVEN  — what reward R makes the Troll 2 bet fair (EV = 0)?
  0.17·R + 0.83·(−1) = 0  →  R = 0.83/0.17 ≈ 4.88   (below ~$4.88 the bet turns bad)
```

**The lesson in one line:** the dog bet flipped from −25 to +32.5 with the payoffs *unchanged* — only
the catch probability rose 0.10 → 0.33. Rarity and size fight; shift either one and the verdict moves.

## Numpy twin

```python
import numpy as np, matplotlib.pyplot as plt
p = np.array([0.17, 0.83]); v = np.array([10.0, -1.0])   # Troll 2 bet
EV = np.dot(p, v)                                          # Σ pᵢvᵢ  — literally a DOT PRODUCT
print(f"EV = {EV:.2f}  (>0 → take it)")                    # EV = 0.87

rng = np.random.default_rng(0)                             # simulate 5000 plays, watch the average converge
draws = rng.choice(v, size=5000, p=p)
running = np.cumsum(draws) / np.arange(1, 5001)
plt.plot(running, color='#9fe8ff', label='running average')
plt.axhline(EV, color='#ff9433', ls='--', label=f'EV = {EV:.2f}')
plt.xlabel('plays'); plt.ylabel('avg $/play'); plt.legend(); plt.grid(alpha=.3); plt.show()
# early plays swing wildly; by ~thousands the average settles onto the EV line — that's what "expected" means
```

## Where it came from / where it goes

builds-on:: [[probability]] — the `pᵢ` weights ARE probabilities; they must sum to 1, so EV is a probability-weighted average
builds-on:: [[vectors]] — `Σ pᵢvᵢ = p · v` is a **dot product**; expectation is the probability vector dotted with the payoff vector
feeds:: [[gradient-descent]] — the **loss is an expected value** (average squared error over the data); "minimize the loss" = "make the expected miss small"
feeds:: [[regression]] — least-squares fits the line that minimizes the *expected* squared residual
contrasts-with:: single-trial thinking — EV says nothing about the NEXT play (you still win or lose that one); it's the average over many
scroll:: [[2026-07-10_line-to-gradient-thermal-fit_F]] — same session; the loss bowl that EV underlies
video:: StatQuest — Expected Values, Main Ideas (the Troll 2 example this atom anchors on)

## Decision boundary

- ✅ Use EV to judge any repeated gamble/decision with known odds & payoffs — bets, retries, speculative work.
- ✅ EV `> 0` → worth doing over the long run · `< 0` → skip · `= 0` → break-even.
- ❌ **Do NOT trust EV for a one-shot, ruin-or-nothing call** — a +EV bet that can bankrupt you on one bad draw is still reckless (variance/risk matter, not just the average).
- ❌ EV needs honest probabilities; garbage `pᵢ` → garbage EV.

## Traps I hit

- Wrote *both* outcomes as −1 in an asymmetric bet → each outcome has its **own** signed payoff; the "win" side of Troll 2 is **+10**, not −1. (Fixed live 2026-07-10.)
- "Big reward means good bet" → no; a big payoff on a rare event (dog at 0.10) still loses. Rarity and size fight.

## Depth layers

- **2026-07-10 (F, first contact):** built EV from three worked bets — Troll 2 (+0.87, good), the dog-treat hustle (−25 bad → +32.5 good when odds rose), and a break-even solve (R ≈ 4.88). Saw the sum-of-products = **dot product** shape, tying it back to [[vectors]] and forward to the **loss** as an average error. Self-drove the probability (1-in-3 = 0.33) and the EV arithmetic. → [[2026-07-10_line-to-gradient-thermal-fit_F]]

## Project brick

The **loss** that trains R1 is an expected value: the *average* squared gap between predicted and
observed temperature across every logged reading. Gradient descent's whole job is to shove that
expected miss downhill. So expectation isn't just betting math — it's the quantity the training loop
minimizes.

## Formula

```
EV = Σ pᵢ · vᵢ  =  p₁v₁ + p₂v₂ + … + pₙvₙ        (Σ pᵢ = 1 ; each vᵢ carries its own sign)
     = p · v                                       (a dot product)
verdict:  EV > 0 good · = 0 break-even · < 0 bad
```

## Flashcards

#flashcards/expected-value

What is expected value in one formula, and what does it actually tell you? :: EV = Σ (probability × payoff) = p·v. It's the **long-run average** haul over many tries — NOT a prediction of the next single play.
A bet pays +₹200 on a 10% event and −₹50 otherwise. Good bet? :: EV = 0.10·200 + 0.90·(−50) = 20 − 45 = **−25**. Bad — walk away. Big reward, but too rare to beat the frequent small loss.
Why is EV "a dot product," and where does that show up in ML? :: Σ pᵢvᵢ = p·v, the probability vector dotted with the payoff vector. The training **loss** is an EV — the average error over the data — which [[gradient-descent]] minimizes.
