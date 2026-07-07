---
title: Calculus Foundations — Derivatives, Gradients & Backpropagation
date: 2026-06-14
session: Session 4 (3-hour block)
sessions: [F]
concepts: [calculus, gradient-descent]
type: notes
up: "[[MOC-foundation-math]]"
recap: "The 3-hour foundation walk: slope → derivative → gradient-as-GPS → gradient descent + learning rate → chain rule → backprop preview."
tags: [calculus, derivatives, gradient-descent, chain-rule, backpropagation, optimization]
---

# Calculus Foundations — Derivatives, Gradients & Backpropagation

> Foundation notes (_F) for Session 4. Three hours: Hour 1 = what a derivative is; Hour 2 = gradients + optimization + gradient descent; Hour 3 = chain rule + computational graphs + backpropagation. These are the mathematical tools that let an ML model learn from its mistakes.
>
> **Permanent homes (Atlas concept atoms):** [[calculus]] · [[gradient-descent]] — the atoms hold the distilled anchors + typed links; this scroll stays the full walk.

---

## Why are we learning this?

Before this session we knew how to represent data (vectors, matrices) and measure uncertainty (statistics).
But we still could not answer: when a model makes a mistake, how does it know which way to improve?
Calculus is the answer. Derivatives measure "which direction reduces error," and gradient descent follows that direction until the model converges.
Without calculus there is no learning — just guessing.

---

## §0 Revision ladder (walk this in 2 minutes — recall, don't re-read)

1. **Calculus = mathematics of change.** Slope over two points → derivative at one point. → [§H1-2](#2-functions)
2. **A function maps one input to one output.** `y = 2x`, `y = x²`. ML models are complex functions. → [§H1-2](#2-functions)
3. **Slope = change-in-output ÷ change-in-input.** Hours→marks example: 10/1 = 10. → [§H1-3](#3-understanding-slope)
4. **Derivative = instantaneous slope at one point.** Speedometer analogy: 60 km/h right now. → [§H1-4](#4-from-slope-to-derivative)
5. **Large derivative = rapid change. Zero derivative = flat (at a minimum or maximum).** → [§H1-5](#5-understanding-derivatives-intuitively)
6. **Derivatives tell the model which direction reduces error** — the fog + mountain analogy. → [§H1-6](#6-why-do-derivatives-matter-in-ml)
7. **Partial derivative = change when ONLY ONE variable moves.** All others held fixed. → [§H2-2](#2-partial-derivatives)
8. **Gradient = vector of ALL partial derivatives.** Points toward steepest ascent. → [§H2-3](#3-what-is-a-gradient)
9. **Gradient Descent = repeatedly step OPPOSITE to the gradient.** Predict → loss → gradient → update → repeat. → [§H2-7](#7-what-is-gradient-descent)
10. **Learning rate controls step size.** Too small = slow; too large = overshoot. → [§H2-8](#8-learning-rate)
11. **Chain Rule = how to differentiate a function-inside-a-function.** Study → knowledge → score. → [§H3-2](#2-what-is-the-chain-rule)
12. **Backpropagation = chain rule applied backward through the network to assign blame.** → [§H3-6](#6-what-is-backpropagation)

---

# Hour 1 — Calculus Intuition, Functions, Slope & Derivatives

---

## 1. What is Calculus?

Calculus is the mathematics of change.
Whenever something changes, calculus measures and describes that change.

Examples of change:
- Stock prices rising and falling
- Temperature shifting over the day
- Model error decreasing during training ← the one we care about

---

### Real World Example

Driving a car:

```
10:00 AM  →  0 km
11:00 AM  →  60 km
12:00 PM  →  120 km
```

Distance is changing over time.
Calculus asks: how fast is it changing?
That question leads directly to derivatives.

**ML Connection:** during training, a model's error changes with every parameter update. Calculus measures those changes and guides the learning process.

---

## 2. Functions

A function is a rule that maps one input to one output.

```
y = 2x      if x = 3,  then y = 6
y = x²      if x = 4,  then y = 16
```

**Real World Example:** an employee earns ₹500 per hour.
- Input `x` = hours worked
- Output `y = 500x` = salary

**ML Connection:** an ML model IS a function.

```
Input:   House Size, Bedrooms, Location
   ↓
 Function (the model)
   ↓
Output:  Predicted House Price
```

The model is a sophisticated function that learns its own internal shape from data.

✅ Think "function" whenever something maps inputs to outputs — whether it is a simple formula or a 100-layer neural network.
❌ Do NOT confuse the function (the shape) with its parameters — the shape is fixed at design time; the parameters are learned.

> **ML destination:** the function view is used in every session. Session 1 (Jun 20) defined a model as `Y = F(X, W)`. Everything after that — logistic regression, trees, neural nets — is a different choice of F.

---

## 3. Understanding Slope

Imagine two roads:
- Road A: almost flat
- Road B: very steep

Road B climbs faster. The steepness is called **slope**.

**Formula:**
```
Slope = Change in Output / Change in Input
```

**Example — hours studied vs marks:**

| Hours | Marks |
|-------|-------|
| 1     | 50    |
| 2     | 60    |

Marks increased by 10. Hours increased by 1.
```
Slope = 10 / 1 = 10
```
For every extra hour studied, marks go up by 10.

Slope tells us: **how sensitive the output is to changes in the input.**

**ML Connection:** the slope measures how strongly house price responds to changes in house size. Many ML models learn these relationships from data.

---

## 4. From Slope to Derivative

Slope works between two points.
But what if you want to know the slope **at one exact point**?

That is a **derivative**.

A derivative measures the rate of change of a function at a specific point.
It is an **instantaneous slope**.

**Real World Example — Speedometer:**
Your speedometer reads 60 km/h.
That value tells you exactly how quickly your position is changing RIGHT NOW — not over the last hour, not tomorrow. Right now.

Speed = the derivative of position.

**Another Example:**
A company's revenue is increasing.
A derivative tells you how fast revenue is growing **at this moment**.

---

## 5. Understanding Derivatives Intuitively

Consider `y = x²`:

| x | y  |
|---|----|
| 1 | 1  |
| 2 | 4  |
| 3 | 9  |
| 4 | 16 |

As x grows, y grows **faster and faster**.
The rate of change is not constant.
A derivative measures this changing growth rate.

**Three cases:**

| Derivative | Meaning |
|---|---|
| Large | Output changing rapidly |
| Small | Output changing slowly |
| Zero | Output not changing (flat — at a peak or trough) |

---

## 6. Why Do Derivatives Matter in ML?

This is the most important idea of Hour 1.

A model predicts ₹9,00,000 but the actual value is ₹10,00,000.
The model made a mistake.
**Which direction should it adjust?**

If the model changes a parameter slightly:
- Does error increase? → move the other way.
- Does error decrease? → keep moving this way.

Derivatives answer that question.
Without derivatives, the model cannot know how to improve.

**Fog + Mountain Analogy:**
You are hiking down a mountain in heavy fog.
You cannot see the bottom.
You feel the ground and move in the direction that goes downhill.
Derivatives provide exactly this information: **"go this way — error decreases."**

✅ Derivatives are necessary any time a model adjusts its own parameters during training.
❌ You do not need to compute derivatives by hand in practice — frameworks like PyTorch and TensorFlow do it automatically via autograd. Understand the concept, not the arithmetic.

> **ML destination:** derivatives are the engine of gradient descent, which is the engine of ALL modern ML training (logistic regression, trees via boosting, neural networks, LLMs). First appeared in the Jun-20 notebook; revisited in every model session after.

---

## 7. Basic Differentiation Rules (High Level)

You do not need to memorize these rules today.
Just understand that derivatives can be computed systematically.

**Power Rule:**
```
y = x²   →   derivative = 2x
y = x³   →   derivative = 3x²
```

**Sum Rule:**
Derivative of `f(x) + g(x)` = derivative of each part added together.

**Product Rule:**
Used when two functions are multiplied together.

**Chain Rule:**
Used when one function is nested inside another.
This rule becomes extremely important for neural networks — see Hour 3.

> **ML destination:** the power rule + chain rule are the only two you truly need to understand gradient descent. Every other rule is built on top.

---

# Hour 2 — Partial Derivatives, Gradients & Optimization

---

## 1. Functions with Multiple Variables

Earlier we saw `y = f(x)` — one input, one output.

Real ML models have many inputs:
```
Price = f(Size, Bedrooms, Distance)
Score = f(Study Hours, Attendance)
```

Multiple inputs influence the output.
We need a way to measure the impact of **each variable individually**.

---

## 2. Partial Derivatives

A **partial derivative** measures:
> How does the output change if I change **only one variable** and keep everything else fixed?

**Example — Salary:**
```
Salary = f(Experience, Education)
```
How much does salary change when experience increases, while education is held constant?
That is the partial derivative of Salary with respect to Experience.

**Why this matters in ML:**
A model may have thousands of parameters.
We need to know:
- Which parameter is causing the error?
- Which direction should it move?
- By how much?

Partial derivatives answer all three questions simultaneously.

**ML Connection:** a house-price model predicts ₹90 Lakhs but the actual is ₹1 Crore. The model contains many parameters. Partial derivatives tell us which parameter contributed to the error and which direction it should move.

✅ Use a partial derivative when you want to know the effect of ONE specific input in isolation, while freezing all others.
❌ Do not confuse a partial derivative with a full derivative — changing two variables at once requires the gradient (see §3 below).

> **ML destination:** every weight in a neural network is updated using its own partial derivative of the loss — its individual "blame" for the error. This is the foundation of backpropagation (Hour 3).

---

## 3. What is a Gradient?

A **gradient** is a **collection of all partial derivatives** packed into a vector.

If a function has two variables:
```
f(x, y)

Gradient = [ ∂f/∂x,  ∂f/∂y ]
```

**Simple meaning:** the gradient tells you **which direction causes the fastest increase** in the output.

**Mountain Analogy:**
Imagine standing on a mountain.
The gradient points toward the steepest uphill direction.
ML usually wants the opposite — we move **downhill** to reduce error.

✅ Gradient = the direction of steepest ascent. For ML (minimizing loss), move opposite to the gradient.
❌ The gradient is not a fixed number — it changes at every point on the loss surface.

> **ML destination:** the gradient is what gradient descent follows (in reverse) every training step. In deep networks, computing the gradient of the loss across millions of parameters is what backpropagation (Hour 3) makes efficient.

---

## 4. Gradient = GPS for Learning

The gradient acts as a GPS for the model during training.

Your phone's GPS says: "Turn left. Walk 200 m. Turn right."
The gradient says: "Move this way. Error decreases in this direction."

The model follows this guidance step by step.
Over many steps, predictions improve.

---

## 5. Understanding Optimization

**Optimization** means finding the best possible solution.

Everyday examples:
- Cheapest flight
- Fastest route
- Maximum profit

In ML, optimization means finding the **lowest prediction error**.
The model wants its predictions as close as possible to reality.

---

## 6. Loss Function

A **loss function** measures prediction error.
It converts a mistake into a single number.

**Example:**
```
Actual House Price:    ₹1,00,00,000
Predicted Price:         ₹90,00,000
```

The loss function turns that gap into a number.

```
Large mistake  →  Large Loss
Small mistake  →  Small Loss
Perfect match  →  Loss = 0
```

During training, the goal is always: **Reduce Loss**.

✅ Choose a loss function that matches the task: MSE for regression (continuous output), cross-entropy for classification (discrete classes).
❌ Never use MSE for a classification task — its gradients are poorly shaped for probabilities.

> **ML destination:** Jun-20 deck covers MSE and cross-entropy explicitly. Both appear in every model session afterward.

---

## 7. What is Gradient Descent?

**Gradient Descent** is an optimization algorithm.
Its job: find parameter values that minimize the loss function.

**Mountain Analogy (revisited):**
Blindfolded on a mountain. Cannot see the bottom.
Only know: ground slopes up here, ground slopes down there.
Action: take a small step downhill. Check again. Take another step.
Eventually reach the bottom.
That is exactly Gradient Descent.

**The 5-step training loop:**
```
Step 1: Make a prediction   (forward pass)
Step 2: Calculate loss
Step 3: Compute gradient    (partial derivatives of loss w.r.t. every parameter)
Step 4: Move opposite to gradient
Step 5: Repeat
```

Over time, error decreases.

✅ Gradient descent works whenever the loss function is differentiable — i.e., you can compute a slope at each point.
❌ Gradient descent is NOT a one-shot solver. It is iterative. It finds a local minimum, which may or may not be the global minimum.

> **ML destination:** gradient descent (or its variants Adam, SGD, RMSProp) is the optimizer used in every trained ML model. Jun-20 notebook implements both closed-form (one-shot) and gradient-descent solutions for the same linear classifier to show the trade-off.

---

## 8. Learning Rate

A **learning rate** controls how big each step is during an update.

| Learning Rate | Effect |
|---|---|
| Very small | Tiny steps — stable but very slow |
| Very large | Huge steps — fast but may overshoot the minimum |

**Analogy — searching for a key in a dark room:**
- Tiny steps: safe but slow.
- Huge jumps: fast but risky (you might step past the key).

A good learning rate balances speed and stability.

✅ Start with a small learning rate (e.g. 0.01) and increase only if training is too slow.
❌ Do NOT use a fixed large learning rate for long training — it destabilizes; use a scheduler (learning-rate decay) after a warm-up period.

> **ML destination:** learning rate is the most impactful hyperparameter you tune. Learning-rate schedules (cosine decay, step decay) are introduced in later sessions. Bayes-scroll §⑥ showed a concrete gradient-descent walkthrough: `w=3.0 → 3.80 → 4.28 → ... → 5` with λ=0.05.

---

## 9. Local Minima (High Level)

Sometimes the loss landscape is not a simple bowl.
There may be many valleys — each a local low point.
But the deepest valley is the **global minimum**.

Gradient descent may get stuck in a local minimum.
Modern optimization algorithms have techniques to handle this (momentum, Adam, etc.).

For now: just understand that optimization can be difficult when the landscape is complex.

---

# Hour 3 — Chain Rule, Computational Graphs & Backpropagation

---

## 1. Functions Inside Functions

Real ML models are chains of functions, each feeding the next:

```
Input → Feature Transformation → Prediction → Loss
```

Each stage depends on the one before it.

**Coffee Analogy:**
```
Coffee Beans → Grinding → Brewing → Coffee
```
The final coffee depends on every step.
A change at the beginning (bad beans) affects everything after.
The Chain Rule helps measure this.

---

## 2. What is the Chain Rule?

The **Chain Rule** is used when one function is nested inside another.

```
y = f(g(x))

x  affects  g(x)
g(x)  affects  f(g(x))
f(g(x))  affects  y
```

Everything is connected.

**Study → Score Analogy:**
```
Hours Studied → Knowledge Gained → Exam Score
```

If study hours increase → knowledge changes → exam score changes.
The chain rule measures how a change at the start ripples through to the final result.

**Chain Rule — the worked example (Tab 5):**
```
Study Hours → Exam Score:    +5 points per hour
Exam Score  → Scholarship:   +₹100 per point

Study Hours → Scholarship:   5 × 100 = +₹500 per hour
```
The chain rule multiplies the rates: **the overall rate = product of all the individual rates along the path**.

✅ Chain rule is needed any time your quantity of interest goes through multiple intermediate steps.
❌ Chain rule is not needed when there is only a single step — a direct function with no nesting.

> **ML destination:** backpropagation IS the chain rule applied repeatedly backward through every layer of a neural network. Without the chain rule, training a deep network is computationally impossible. This appears in every neural network session (Sess 7 onward).

---

## 3. Computational Graphs

A **computational graph** is a visual map of the calculations.

Example: `z = x² + 3`
```
x  →  x²  →  +3  →  z
```

Instead of one large formula, calculations are broken into small steps.

In large neural networks with millions of operations, computational graphs help:
- Calculate outputs (forward direction)
- Track which calculation depends on which
- Compute gradients efficiently (backward direction)

**Manufacturing Analogy:**
```
Raw Material → Component A → Assembly → Final Product
```
If a defect appears in the final product, we trace backwards through the production steps.
Computational graphs do the same thing mathematically.

---

## 4. Forward Pass

The **forward pass** computes the prediction.

```
Input: House Size = 1500 sq ft
   ↓
 Model
   ↓
Output: Predicted Price = ₹95 Lakhs
```

Data moves from input to output.
Every neural network begins with a forward pass.

---

## 5. Backward Pass

After the forward pass, error is calculated.

```
Actual Price:    ₹1 Crore
Predicted Price: ₹95 Lakhs
Error exists.
```

Now we must determine: **which parameters caused this error?**

This is the **backward pass**.

**Student Analogy:**
A student gets a poor exam score.
The teacher investigates: attendance? practice? preparation?
The teacher traces the problem backward.
Backpropagation works the same way.

---

## 6. What is Backpropagation?

**Backpropagation** propagates error backward through the network.

Starting from the final error, it works backward to determine:
- Which parameters contributed most
- Which direction they should change
- How much they should change

Without backpropagation:
The model knows it made a mistake.
But it does not know how to fix it.
Backpropagation provides that information.

✅ Use backpropagation (automatic differentiation) any time you train a neural network.
❌ Backpropagation does NOT tell you whether a model is overfit or well-generalized — it only tells each parameter which direction to move.

> **ML destination:** backpropagation is the heart of neural-network training (Sess 7 onward). Understanding it here means when you see `loss.backward()` in PyTorch, you know it is running the chain rule backward through the computational graph, computing each parameter's partial derivative automatically.

---

## 7. Chain Rule + Backpropagation

Everything comes together here.

Backpropagation **repeatedly applies the Chain Rule**.

```
Input → Layer 1 → Layer 2 → Prediction → Loss
```

A change in Layer 1 affects Layer 2, which affects Prediction, which affects Loss.
The Chain Rule measures that effect.

**Key intuition:**
> If I slightly change this parameter, how much will the final loss change?
> That is exactly what machine learning needs to know.

---

## 8. The Full Training Loop

```
Step 1: Forward Pass          Input → Prediction
Step 2: Calculate Loss        Prediction vs Actual
Step 3: Backpropagation       Chain Rule → gradients for every parameter
Step 4: Gradient Descent      Update parameters: w ← w − λ · gradient
Step 5: Repeat                thousands of times → loss decreases → predictions improve
```

**Basketball Free-Throw Analogy:**
```
Attempt 1:   Missed left   → adjust
Attempt 2:   Missed right  → adjust
Attempt 3:   Closer
Attempt 100: Much better
```

ML training works the same way.
The model predicts, measures the mistake, and learns from it.

---

## Session Big Picture

```
Hour 1 → Derivatives       → How change is measured at a point
Hour 2 → Gradients + GD    → How the model knows which direction to move
Hour 3 → Chain Rule + Back  → How the model learns efficiently across many layers
```

**Final One-Line Summary:**
Calculus gives ML models a way to measure mistakes, understand how those mistakes were created, and continuously improve their predictions.

---

## Vocabulary Clarification (Q&A from session)

A question came up: "Do Parameters / Input / Variables / Features all mean the same thing?"

| Word | What it is |
|---|---|
| **Input** | the raw data fed into the model |
| **Features** | individual attributes / columns of the input data |
| **Variables** | a general term — can refer to features, parameters, or any quantity that takes values |
| **Parameters** | the model's learned weights and biases, adjusted during training |

They are NOT the same. Features go IN. Parameters are what the model LEARNS.

---

## Key Takeaways

**Hour 1 — Derivatives:**
- Calculus = mathematics of change.
- Functions map inputs to outputs; ML models are functions.
- Slope = change-in-output / change-in-input.
- Derivative = instantaneous slope at one point.
- Large derivative = rapid change. Zero derivative = flat.
- Derivatives tell a model which direction reduces error.

**Hour 2 — Gradients & Optimization:**
- Real ML models depend on many variables.
- Partial derivative = effect of changing one variable while others are fixed.
- Gradient = vector of all partial derivatives.
- Gradients point toward fastest increase; ML moves the opposite way.
- Loss function = measure of prediction error (lower is better).
- Gradient Descent reduces loss step by step.
- Learning rate controls step size — balance speed and stability.

**Hour 3 — Chain Rule & Backpropagation:**
- Real ML models are chains of functions — one output feeds the next.
- Chain Rule = how a change ripples through a chain of functions (multiply the rates).
- Computational graph = visual map of every calculation; enables efficient gradient computation.
- Forward pass = compute prediction; backward pass = trace error backward to each parameter.
- Backpropagation = chain rule applied backward; assigns gradient (blame) to every parameter.
- Modern AI (ChatGPT, image models, all LLMs) learns through this loop: forward → loss → backprop → gradient descent → repeat.

---

## Formula Sheet

```
Slope (two points)         m = Δy / Δx = (y2 − y1) / (x2 − x1)

Derivative (power rule)    d/dx [xⁿ] = n · xⁿ⁻¹

Partial derivative         ∂f/∂x   (hold all other variables fixed)

Gradient                   ∇f = [ ∂f/∂x₁,  ∂f/∂x₂,  ...,  ∂f/∂xₙ ]

MSE Loss                   L = (1/n) · Σ (yᵢ − ŷᵢ)²

Gradient Descent update    w  ←  w − λ · (∂L/∂w)
                           λ = learning rate

Chain Rule                 dy/dx = (dy/du) · (du/dx)
                           (multiply rates along the path)
```
