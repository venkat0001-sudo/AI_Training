---
title: Perceptron arc — revision scroll (CampusX videos 1–7)
date: 2026-08-05
sessions: [s7]
concepts: [neural-nets, regression]
type: notes
recap: One neuron = w·x+b + activation = a line. Trick nudges it per-point; loss+GD slides it globally. Swap the activation+loss and it BECOMES logistic/linear/softmax regression. XOR proves one line is not enough → MLP.
up: "[[MOC-m2-deep-learning]]"
---

# Perceptron arc — revision scroll (videos 1–7)

> **Read this before s8, before any MLP work, and any time the notation goes fuzzy.**
> Source: CampusX *100 Days of DL* Part II (ch 4–7, pp. 61–98) + our sessions 2026-07-28 → 07-30.

---

## ⭐ THE SPINE — recite this first, it holds all 7 videos

**A perceptron is a line that learns where to stand.**

Everything else is detail on three questions:
1. **What is it?** → a weighted sum + a threshold (videos 1–4)
2. **How does it learn?** → nudge per misclassified point (trick, v5), or shrink a global loss with gradient descent (v6)
3. **Where does it break?** → data that no single line can split — XOR (v7) → **that failure is why MLPs exist**

---

## 1 · What a perceptron IS

```
inputs        weights                    activation      output
 x₁ ──w₁──┐
 x₂ ──w₂──┼──▶  z = w₁x₁ + w₂x₂ + b  ──▶  step(z)  ──▶  ŷ ∈ {0,1}
 x₃ ──w₃──┘         (weighted sum)        (z≥0 →1)
                                          (z<0  →0)
```

- **Weights = feature importance.** If `w₂ > w₁`, feature 2 matters more to the decision.
- **Bias = the threshold shifter** (the `w₀` with a permanent `x₀=1`).
- Weakly inspired by a biological neuron — *weakly*. It's a math object, not biology.

**The anchor numbers (book ch 4 — keep these, they are the memory hook):**  ^anchor
Student placement: `x₁ = IQ = 117.5`, `x₂ = CGPA = 8.67`, weights `w₁=1, w₂=2, b=3`

```
z = 117.5×1 + 8.67×2 + 3 = 117.5 + 17.34 + 3 = 137.84
z ≥ 0  →  PLACED ✓
```

**The geometric truth — the one thing to never forget:**

| Dimensions | The perceptron is a… | Equation |
|---|---|---|
| 2D | **line** | `Ax + By + C = 0` |
| 3D | **plane** | `Ax + By + Cz + d = 0` |
| n-D | **hyperplane** | `w·x + b = 0` |

`w·x + b = 0` **is the decision boundary itself.** Points where it's ≥0 = positive region; <0 = negative region.

---

## 2 · How it learns — TWO different machines (don't blur them)

### (a) The perceptron trick — per-point nudging (v5)

Pick a misclassified point, move the line toward/away from it. Repeat.

| Misclassification | Update | Visual effect |
|---|---|---|
| positive point in negative region | `w ← w + η·x` | **pull** boundary toward it |
| negative point in positive region | `w ← w − η·x` | **push** boundary away |

- Changing the bias → **shifts** the line. Changing `w₁,w₂` → **rotates** it. `η` sets how hard.
- Sees **one point at a time.** No global score — it never knows if the overall situation improved.

### (b) Loss function + gradient descent — global (v6)

```
L = (1/n) Σ max(0, −yᵢ·f(xᵢ))        where f(xᵢ) = w₁xᵢ₁ + w₂xᵢ₂ + b
```

**The `y·f(x)` trick — this is the whole idea.** The sign of `f(x)` alone only says *which side*;
correctness needs the label. Multiply them: ^yfx

| label y | side f(x) | y·f(x) | verdict |
|---|---|---|---|
| +1 | +2 | **+2** | ✓ correct |
| +1 | −2 | **−2** | ✗ misclassified |
| −1 | −2 | **+2** | ✓ correct (negative side is RIGHT for y=−1) |
| −1 | +2 | **−2** | ✗ misclassified (f>0 yet WRONG) |

**`y·f(x) > 0` = correct · `y·f(x) < 0` = misclassified.**
And `max(0, ·)` is a gate: **correct points contribute exactly 0 — only the criminals pay.**

**The gradient (and the sign confusion, resolved):**

```
∂L/∂w₁ = 0            if yᵢ·f(xᵢ) ≥ 0
       = −yᵢ·xᵢ₁      if yᵢ·f(xᵢ) < 0

update:  w₁ ← w₁ − η·(∂L/∂w₁) = w₁ − η·(−yᵢxᵢ₁) = w₁ + η·yᵢ·xᵢ₁   ← the code's "+"
```
**Two minuses cancel** — the derivative is negative, descent walks the opposite way. That's why the
code says `w1 = w1 + lr*y[i]*X[i][0]`.

> ⚠️ `|f(x)|` is only *proportional* to distance from the line — the true distance is `f(x)/‖w‖`.
> This loss skips the `÷‖w‖` (a "functional margin"). SVM is the algorithm that cares about the division.

---

## 3 · ⭐⭐⭐ THE BIG IDEA — the perceptron is a SOCKET

Same `w·x + b` body. Swap the activation + loss pair and it **becomes** a classical model:

| Activation | Loss | It IS… | Output |
|---|---|---|---|
| step | perceptron / hinge | classic perceptron (binary classifier) | 0 or 1 |
| **sigmoid** | binary cross-entropy | **logistic regression** | a probability |
| **softmax** | categorical cross-entropy | softmax regression (multi-class) | a probability vector |
| **linear (none)** | MSE | **linear regression** | a number |

**This is the most valuable single table in the arc.** Four "different" models = one skeleton with
different sockets filled. And it explains the naming scandal: *logistic regression is a regression of
**probabilities**, used as a classifier* — it regresses a continuous 0→1 value, then a threshold
turns it into a class.

**Regression vs classification:** regression → a continuous **number** (judged by *how far off*).
Classification → a **category** (judged by *right or wrong*).

---

## 4 · Where it breaks — XOR, proved (v7)

```
XOR:  (0,0)→0   (1,1)→0        ● class 0
      (1,0)→1   (0,1)→1        ✕ class 1

  x₂
  1 ✕         ●     the ✕'s sit on one diagonal,
    |               the ●'s on the other.
  0 ●─────────✕     No single straight line separates them.
    0         1
```

**The proof by contradiction** (class 1 → positive side, class 0 → negative):

```
(0,0)→0 :  b < 0                    …(A)
(1,0)→1 :  w₁ + b > 0               …(B)
(0,1)→1 :  w₂ + b > 0               …(C)
(1,1)→0 :  w₁ + w₂ + b < 0          …(D)

(B)+(C):  w₁ + w₂ + 2b > 0   ⟹   w₁ + w₂ + b > −b
(A) says −b > 0             ⟹   w₁ + w₂ + b > 0     ✗ contradicts (D)
```

**No (w₁,w₂,b) exists.** Not "hard to find" — mathematically nonexistent. A million epochs will
circle forever. Contrast AND, which *does* have a line — `w₁=1, w₂=1, b=−1.5` classifies all four ✓.

**This impossibility is the arrest warrant that summoned deep learning:** one line can't carve XOR,
but **two lines can** — and a hidden layer is exactly "several perceptrons drawing several lines,
combined." → [[neural-nets]]

---

## 5 · Where this goes (the thread forward)

```
perceptron ──► MLP (stack them, hidden layer invents features) ──► backprop (chain rule
   assigns blame across layers) ──► optimizers/regularization (s8) ──► LSTM (s10)
   ──► the R2 thermal forecaster ──► INT8 quantization ──► runs on the controller
```

**Project brick:** every hidden neuron in the R2 forecaster is one of these — `w·x+b` over
telemetry channels. Master this and the forecaster is just many of them wired together.
See [[thermal-project]].

---

## 🎤 RECITE-BACK CHECKLIST (the exam on yourself)

Cover the note. Answer aloud. A stumble = re-read only that section.

1. Write `z` for a 2-feature perceptron and say what each symbol means.
2. In 2D/3D/n-D, what *shape* is a perceptron? What equation *is* the decision boundary?
3. The trick: a positive point sits in the negative region — what happens to `w`, and what does
   the line visibly do?
4. Why does `y·f(x)` beat just checking the sign of `f(x)`? Give the `y=−1, f=+2` case.
5. What does `max(0, ·)` do to correctly-classified points, and why is that the whole point?
6. The gradient is `−y·x` but the code writes `+`. Explain in one sentence.
7. Recite the socket table: 4 activations → 4 losses → 4 model names.
8. Why is logistic regression called *regression* when it classifies?
9. Prove XOR is impossible using (A)(B)(C)(D). Then say what (B)+(C) vs (D) means *geometrically*.
10. Finish the sentence: "a hidden layer works because…"

**Pass = 8/10 fluent.** Then advance the [[recall-ledger]] row and move to MLP.
