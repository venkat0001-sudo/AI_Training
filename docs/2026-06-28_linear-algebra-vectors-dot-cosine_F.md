---
title: Linear algebra — vectors → dot → cosine → covariance → eigen → PCA
date: 2026-06-28
sessions: [F]
concepts: [vectors, covariance, eigenvectors, pca]
type: notes
recap: The 860-line spine: walk 3E-4N=5 → dot's two lies → cosine → covariance votes → eigen stretch → the two weights (§21)
---

# Linear Algebra Foundations — Vectors, Magnitude, Dot Product & Cosine Similarity

> Revision notes for the **2026-06-28 hands-on lab** — a NumPy practical built on top of the earlier Foundation classes (hence the `_F` tag, not a session number). Spine = **dot product + cosine similarity**; everything else (matrices, covariance, eigen) is recognition-level. This doc captures the magnitude → dot → cosine arc and the A/D/C recommendation example that shows *when each tool wins*.

---

## Why are we learning this?

Every ML model compares things — users to users, documents to documents, feature vectors to each other.
To compare two vectors you need to measure how "similar" they are, and the wrong tool gives the wrong answer.
This session builds the three tools (magnitude, dot product, cosine similarity) and shows exactly when each one wins — which feeds directly into recommendation systems, embeddings, PCA, and gradient descent.

---

## 0. Revision ladder (walk this in 2 minutes — recall, don't re-read)

Step through these in order; each builds on the last. If a rung is fuzzy, jump to the section noted.

1. **A vector has two separable properties: direction (which way) and magnitude (how far / how big).** → §1
2. **Magnitude = length of the arrow** = `sqrt(sum of squares)` = `np.linalg.norm`. Anchors: walk 3-east-4-north → 5; TV diagonal; drone speed. → §1
3. **Dot product = `a1·b1 + a2·b2 + …`** — measures alignment, *but it's contaminated by magnitude.* A high score can mean *aligned* OR *just loud*. → §2
4. **The trap:** same direction + different size → wildly different dot scores; and different directions → can give the *same* dot score. Dot can't tell direction from size. → §2
5. **Cosine fixes it: `(A·B) / (|A|·|B|)`** — divides out both magnitudes, leaving only direction. Range −1…+1. → §3
6. **Cosine = the cosine of the angle between the two vectors.** 0°→1, 90°→0, 180°→−1. → §4b
7. **Proof it matters:** a far-walking / heavy-rating *wrong*-direction vector can out-score a perfect match on raw dot product — cosine ranks them correctly. → §4 (Netflix), §4b (walking)
8. **Decision boundary:** dot product is fine *only when all vectors are ~same length*; use **cosine the moment magnitudes vary** (always, in real data). → §5
9. **NumPy:** `a @ b` · `np.linalg.norm(a)` · `(a @ b)/(norm(a)*norm(b))`. → §6

---

## 1. Magnitude — "how big", stripped of direction

A vector has two separable properties:
- **Direction** = which way it points (the *shape* of the signal / the *heading* you walked).
- **Magnitude** = how long it is (the *amplitude* / how far you walked), regardless of direction.

```
|v| = sqrt(v1² + v2² + ... + vn²)        # NumPy: np.linalg.norm(v)
```

**Intuition anchors (all the same move — square the parts, add, square-root):**
- Walk **3 east, 4 north** → straight-line distance from start = `sqrt(9+16) = 5`.
- TV screen **3 wide, 4 tall** → diagonal = `5` (why a "55-inch TV" quotes the diagonal).
- Drone at **6 m/s east, 8 m/s up** → true speed = `sqrt(36+64) = 10 m/s`.

**Where magnitude is actively used:**
- **Normalization:** `v / |v|` → unit vector (length 1, pure direction). Engine inside cosine; how embeddings get normalized.
- **Distance / error:** `|A − B|` = Euclidean (L2) distance. In regression, the error-vector magnitude squared & averaged = **MSE loss**.
- **Gradient descent:** gradient is a vector; its magnitude = slope steepness = step size. "Gradient clipping" = cap that magnitude.
- **Edge-AI:** INT8 quantization scaling is driven by the **max magnitude** of a weight tensor.

✅ Use magnitude when you need a single number for "how big / how far / how steep" — size, not direction.
❌ Do NOT use magnitude alone when you care about similarity between two vectors — it tells you nothing about alignment.

> **ML destination:** magnitude feeds gradient clipping (training stability), MSE loss (regression), and INT8 quantization scaling — all in Modules 1–2.

---

## 2. Dot product — alignment, but blind to size

```
A·B = a1·b1 + a2·b2 + ... + an·bn        # NumPy: A @ B  or  np.dot(A, B)
```

Result is a single number measuring how much two vectors align. **But it's contaminated by magnitude:** a high score can mean *aligned* OR *just loud*. It can't tell those apart.

**The two lies of the raw dot product:**
1. Same direction, different volume → wildly different scores. `[1,1]·[1,1]=2` but `[10,10]·[10,10]=200` — same perfect alignment, 100× the score, purely from loudness.
2. Different directions → can give the *same* score. `[1,0]·[5,0]=5` (identical heading) and `[5,5]·[1,0]=5` (45° apart) — dot product can't distinguish them.

✅ Use dot product when all vectors you are comparing are already the **same length** (e.g. all unit-normalized, or you only care about absolute activation strength).
❌ Do NOT use dot product when vectors vary in magnitude — volume will drown out direction, and you will rank the wrong item first.

> **ML destination:** dot product = the MAC (multiply-accumulate) inside every layer of a neural net (`score = w·x`). It powers the linear classifier from the Jun-20 notebook and is the raw operation inside attention heads (Sess 14). Where magnitudes matter, cosine or normalization wraps around it.

---

## 3. Cosine similarity — chop off the length, keep the heading

```
cosine(A,B) = (A·B) / (|A| × |B|)        # divide out BOTH magnitudes
```

Range `−1 … +1`: **+1** = same direction, **0** = unrelated, **−1** = opposite. It normalizes out the gain on both sides, leaving only direction.

✅ Use cosine whenever magnitudes vary across vectors — recommendation engines, NLP embeddings, document similarity, user-taste comparison.
❌ Do NOT use cosine when direction is meaningless and you genuinely want size (e.g. comparing amplitudes of two signals; here magnitude is the point).

> **ML destination:** cosine similarity is the backbone of vector/embedding search in RAG pipelines (Sess 24) and the similarity metric in k-NN (Module 1). It also shows up in attention — query·key dot products are often scaled (divided by √d) to prevent magnitude from dominating, which is the same fix cosine makes explicit.

---

## 4. ⭐ Worked example — A / D / C users (why cosine, not dot product)

Netflix users rating genres `[Action, Comedy, Romance]`:

```
A = [5, 4, 1]      reference (casual rater, loves Action)
D = [10, 8, 2]     IDENTICAL taste to A (A doubled) — same heading
C = [2, 8, 100]    OPPOSITE taste (Romance fanatic) — but a very heavy rater
```

D is A's perfect twin; C is A's opposite. So **D must win "most similar."**

**Magnitudes:**
```
|A| = sqrt(25+16+1)    = sqrt(42)    ≈ 6.48
|D| = sqrt(100+64+4)   = sqrt(168)   ≈ 12.96
|C| = sqrt(4+64+10000) = sqrt(10068) ≈ 100.3
```

**Dot product (gets it WRONG):**
```
A·D = (5×10)+(4×8)+(1×2)   = 50+32+2   = 84
A·C = (5×2)+(4×8)+(1×100)  = 10+32+100 = 142
```
→ Dot product says **A·C (142) > A·D (84)** → "C is more similar than the perfect twin D!" Fooled because C's `×100` Romance rating bulldozed the score. **Volume beat taste.**

**Cosine (gets it RIGHT):**
```
cosine(A,D) = 84  / (6.48 × 12.96) ≈ 84  / 84  = 1.00   ← perfect twin ✓
cosine(A,C) = 142 / (6.48 × 100.3) ≈ 142 / 650 = 0.22   ← opposite ✓
```
→ Cosine ranks **D (1.0) >> C (0.22)** — correct. It stripped C's heavy-rater volume and read the actual taste.

---

## 4b. ⭐ Same idea, walking-direction version (cosine = cosine of the angle)

Three walkers from the same spot; each vector = where they walked to:

```
Person A:  [5, 4]      short stroll, east-northeast
Person D:  [50, 40]    SAME bearing as A — just hiked 10× farther
Person C:  [0, 120]    walked due NORTH — different bearing, but a very long way
```

D copied A's heading; C went a totally different way. So **D is the true match.**

**Magnitudes (how far each walked):**
```
|A| = sqrt(25+16)     = sqrt(41)   ≈ 6.40
|D| = sqrt(2500+1600) = sqrt(4100) ≈ 64.0   (exactly 10×|A|)
|C| = sqrt(0+14400)   = 120
```

**Dot product (FOOLED):**
```
A·D = (5×50)+(4×40) = 250+160 = 410
A·C = (5×0)+(4×120) =   0+480 = 480
```
→ Dot says **A·C (480) > A·D (410)** → "C walked more like A than D!" Wrong — C went due north; dot got bought off because C walked *so far* (120). Distance inflated the score.

**Cosine (CORRECT):**
```
cosine(A,D) = 410 / (6.40 × 64.0) ≈ 410 / 410 = 1.00     ← same bearing ✓
cosine(A,C) = 480 / (6.40 × 120)  = 480 / 768  = 0.625    ← 51° apart ✓
```
→ Cosine ranks **D (1.0) >> C (0.625)** — right. Threw away *how far*, kept *which way*.

**Why it's called cosine — it IS the cosine of the angle between the headings:**
```
angle = 0°    → cos = 1.00    same direction
angle ≈ 51°   → cos = 0.625   51° apart
angle = 90°   → cos = 0       perpendicular / unrelated
angle = 180°  → cos = −1      opposite directions
```
Dot product blends heading *and* distance into one number; cosine isolates heading alone.

---

## 5. When to use what (the decision boundary)

- **Dot product is enough ONLY when all vectors are roughly the same length.** Then magnitude can't distort the ranking.
- **Use cosine whenever magnitudes vary** — and in real recommendation data they always do (some users rate 5 items, some rate 5,000). Dot product confuses *"rates a lot"* with *"similar taste"* and can rank the wrong item first.
- **Firmware echo:** comparing two signals' raw correlation without normalizing — a high-amplitude noisy channel can out-score a clean low-amplitude match. Normalize first, *then* compare.

---

## 6. NumPy you'll type today

```python
import numpy as np
a = np.array([5, 4, 1])
b = np.array([10, 8, 2])

a @ b                      # dot product
np.linalg.norm(a)          # magnitude
(a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))   # cosine similarity
np.cov(data.T)             # covariance matrix
np.linalg.eig(cov_matrix)  # eigenvalues, eigenvectors
```

---

## 7. Variance & Covariance (the full walk — how we actually built it)

> This section is the narrative, not just the formula. It captures the exact misconception → correction → "vote" intuition → 4 cases → matrix arc we walked, so a re-read reconstructs the *understanding*, not just the answer.

**Variance** = how spread out a single variable is around its mean.
**Std dev** = sqrt(variance) — same idea, back in original units (easier to read).

```
variance(X)     = avg of (xi − x̄)²           # one variable vs itself
std dev(X)      = sqrt(variance(X))
covariance(X,Y) = avg of (xi − x̄)(yi − ȳ)    # two variables, paired
```

Covariance is variance's sibling — variance asks "how much does *one* thing spread?", covariance asks "do *two* things spread *together*?"

### 7a. The misconception that had to die first

The trap I fell into: *"take the mean of each vector, multiply the two means together, then sum."* **WRONG.** Covariance never touches the product of the means.

The mean's ONLY job is to be a **reference line** — a zero-point you measure *against*. You never multiply the two means.

```
WRONG:  product of (mean_X) and (mean_Y), then sum
RIGHT:  for each point, how far it sits FROM its own mean,
        multiply those two paired distances, THEN average
```

### 7b. The "vote" intuition (this is the whole engine)

Each data **row casts a vote**:
- above/above or below/below → `(+)(+)` or `(−)(−)` → **positive vote** ("they move together")
- above/below or below/above → `(+)(−)` → **negative vote** ("they move opposite")

**Covariance = the average of all the votes.**
- mostly positive votes win → covariance positive → rise & fall together
- mostly negative votes win → covariance negative → one up, the other down
- votes cancel → ≈ 0 → no relationship

A single negative vote (one feature above its mean while the other is below) *drags the whole sum down* — that's the mechanism, not a rule to memorize.

😄 **Analogy — the office gossip chart:** covariance is a "who's secretly synced with whom" detector. When the tall guy is *also* the heavy guy, and the short guy *also* the light guy → height & weight **gossip together** → **positive** covariance. If tall guys were always light → they move opposite → **negative**. And the full covariance **matrix** is the whole office chart: the **diagonal** is "how moody is each person alone" (their own variance), the **off-diagonal** is "who's synced with who."

### 7c. ⭐ The four cases, side by side (the keystone table)

Same machine every time. The ONLY thing that changes is the **sign-pairing of the deviation rows**.

```
 ┌──── POSITIVE ────┐  ┌──── NEGATIVE ────┐  ┌──── NEUTRAL (≈0) ────┐  ┌──── cov(X,X) = VARIANCE ────┐
 Temp↑ → Latency↑      Temp↑ → Clock↓        Temp vs random            Temp paired with ITSELF

 X:  40, 50, 60        X:  40, 50, 60        X:  40,  50,  60          X:  40, 50, 60
 Y: 100,120,140        Y: 900,850,800        Y: 140,  80, 140          X:  40, 50, 60   (same col)
 X̄=50  Ȳ=120           X̄=50  Ȳ=850           X̄=50   Ȳ=120              X̄=50

 X−X̄: −10, 0,+10       X−X̄: −10, 0,+10       X−X̄: −10,  0, +10        X−X̄: −10,  0, +10
 Y−Ȳ: −20, 0,+20       Y−Ȳ: +50, 0,−50       Y−Ȳ: +20,−40, +20        X−X̄: −10,  0, +10

 votes:                votes:                votes:                   votes:
  (−10)(−20)=+200       (−10)(+50)=−500       (−10)(+20)=−200          (−10)(−10)=+100
  (  0)(  0)=  0        (  0)(  0)=  0        (  0)(−40)=   0          (  0)(  0)=   0
  (+10)(+20)=+200       (+10)(−50)=−500       (+10)(+20)=+200          (+10)(+10)=+100
 sum = +400            sum = −1000           sum =    0               sum = +200
 cov = +200  ✓         cov = −500  ✓         cov =   0  ✓             cov = +100  ✓
  "rise together"       "one up,one down"     "votes cancel"          "ALWAYS positive"
```

Read the **two deviation rows** in each column — that's where the whole story lives:
- **Positive:** deviation rows share the same sign → votes pile up positive.
- **Negative:** deviation rows are flipped → votes pile up negative.
- **Neutral:** Y just *wiggles on its own* (`+20, −40, +20`) — ignores X completely → votes cancel → 0.
- **cov(X,X):** X paired with its own column → every vote is a number **times itself** → can NEVER be negative. **This is variance.**

| pairing | what it measures | sign possible |
|---|---|---|
| X with Y (related, same way) | covariance | **+** |
| X with Y (related, opposite) | covariance | **−** |
| X with Y (unrelated) | covariance | **≈ 0** |
| X with X (itself) | **variance** | **+ only** |

**The bridge unlocked here:** *variance is just covariance of a feature with itself.* That's exactly why variances sit on the **diagonal** of the covariance matrix.

### 7d. The formula (now that the intuition is owned)

```
                1
cov(X,Y) =  ─────── · Σ (xᵢ − X̄)(yᵢ − Ȳ)
             n − 1
```
- `Σ (xᵢ − X̄)(yᵢ − Ȳ)` = add up all the **votes** (paired deviations)
- `1/(n−1)` = **average** them. The `−1` is a sample-size correction (a sample is "shyer" than the full population, so we slightly inflate). Ignore it for intuition.

No product-of-means anywhere. ✓

---

## 8. The Covariance Matrix (assembling the grid)

With many features, store **every pairwise covariance** in a grid. For 2 features there are only 4 pairings → a 2×2:

```
              Temp            Latency
         ┌─────────────┬─────────────┐
  Temp   │  cov(T,T)   │  cov(T,L)   │   diagonal  = variance (always +)
         ├─────────────┼─────────────┤
 Latency │  cov(L,T)   │  cov(L,L)   │   off-diag  = covariance (signed)
         └─────────────┴─────────────┘
```

**Two cells, two rules — burn this in:**
- **Diagonal** = each feature with **itself** = variance → **always ≥ 0, never changes sign.** "How much does this feature wiggle on its own."
- **Off-diagonal** = two features **with each other** = covariance → **can flip sign.** "Do they wiggle together (+) or against (−)."
- **Symmetry:** `cov(T,L) = cov(L,T)` (order doesn't matter in multiplication) → the matrix is always a **mirror across the diagonal.** If it isn't, you computed wrong.

Positive scenario → `var_T=100, var_L=400, cov=+200`:
```
        Temp   Latency
Temp   [ 100  ,  200 ]
Lat    [ 200  ,  400 ]
```
Throttling (negative) scenario → only the **off-diagonal** flips; diagonal stays positive:
```
        Temp   Clock
Temp   [ 100  , −200 ]
Clock  [ −200  , 400 ]
```

### 8a. ⭐ Full 3×3 worked read (Temp, Clock, Latency)

```
Temp  T:   40,  50,  60      T̄ = 50    dev: −10,  0, +10
Clock C:  900, 850, 800      C̄ = 850   dev: +50,  0, −50   (throttles as it heats)
Lat   L:  100, 120, 140      L̄ = 120   dev: −20,  0, +20   (slows as it heats)

Diagonal (variance, always +):
  var_T = (100+0+100)/2   = 100
  var_C = (2500+0+2500)/2 = 2500
  var_L = (400+0+400)/2   = 400

Off-diagonal (signed):
  cov(T,C): (−10·+50)+(+10·−50) = −1000 → /2 = −500    T↑ C↓  NEGATIVE
  cov(T,L): (−10·−20)+(+10·+20) = +400  → /2 = +200    T↑ L↑  POSITIVE
  cov(C,L): (+50·−20)+(−50·+20) = −2000 → /2 = −1000   C↑ L↓  NEGATIVE

          Temp    Clock    Lat
 Temp   [  100    −500    +200 ]
 Clock  [ −500    2500   −1000 ]
 Lat    [ +200   −1000    +400 ]
```

**The analysis checklist (how to READ any covariance matrix):**
1. **Diagonal → who spreads most?** Clock (2500) is the wild one; Temp (100) barely moves. Magnitude of variance = how much that feature wiggles.
2. **Off-diagonal signs → the relationships:** T–C = − (heat→throttle), T–L = + (heat→slower), C–L = − (faster clock→lower latency).
3. **Symmetry check** → top-right triangle must mirror bottom-left.

```python
np.cov(data.T)   # spits out this whole grid in one call
```

---

## 9. Why this matters in ML (the syllabus payoff — don't skip)

This whole covariance-matrix → eigen machine is **not abstract math** — it's the literal engine of one upcoming class and a recurring tool everywhere after.

```
covariance matrix → eigenvectors/eigenvalues  ═══►  Module 1, Session 5 (18 Jul 2026): PCA
```

**PCA *is* "take the covariance matrix, find its eigenvectors/eigenvalues, keep the biggest ones."** That's the entire algorithm. We're pre-building that lecture from the floor up.

| Where it shows up | What eigen-of-covariance does | Importance (Edge-AI goal) |
|---|---|---|
| **PCA / dim-reduction** (Sess 5, 18 Jul) | Squeeze 20 sensor channels → 2–3 that hold the real signal | ⭐⭐⭐ the edge compression trick — fewer features = less SRAM, fewer MACs, lower power |
| **Embeddings / vector search** (Sess 24, RAG) | Same math shrinks a 768-dim embedding to fit on-device | ⭐⭐⭐ |
| **Feature correlation** (Sess 1, 20 Jun) | Off-diagonal ≠ 0 → two features redundant → drop one | ⭐⭐ why log temp *and* clock if they're locked? |
| **Multivariate Gaussian / anomaly detect** | Covariance matrix = the shape of the bell in N-D; eigenvectors = its axes | ⭐⭐ SSD acting "off-distribution" = anomaly |
| **Whitening / normalization** | Use eigenvectors to de-correlate inputs before training | ⭐ |

**One-line stake:** every feature fed to an edge model costs RAM, MACs, milliwatts. PCA uses eigen-of-covariance to throw away the directions where the data *doesn't move* (low eigenvalue = low variance = no info) and keep only where it does. **It's lossy compression for features — and you already think in lossy compression.**

---

## 10. Matrix as a machine (the door to eigenvectors)

Step out of covariance. Forget what the numbers *mean*; watch what a matrix *does* mechanically.

**Core picture:** a matrix is a machine that eats a vector and spits out a different vector. Generally it does TWO things to the arrow — **rotates it** (changes direction) and **stretches it** (changes length).

😄 **Analogy — the pasta press:** feed a *random* arrow through the matrix like a noodle through a pasta press — it comes out **bent (rotated) AND longer (stretched)**. But a few **special arrows** slide through **without bending** — they come out pointing the exact same way, just longer or shorter. Those un-bendable arrows are the **eigenvectors**.

```
A = [ 2  0 ]
    [ 0  3 ]

Feed it a "random" arrow v = [1,1]  (clean 45°, x=y):
A · [1,1] = [2, 3]        2 ≠ 3  → arrow TILTED steeper than 45° → ROTATED + stretched

Feed it a "special" arrow v = [1,0]  (pure east, 0°):
A · [1,0] = [2, 0]        same direction, just 2× longer → NOT rotated, only STRETCHED
```

That second arrow is the teaser for the next rung: some arrows a given matrix **cannot rotate** — it can only lengthen/shorten them. Those are **eigenvectors**, and the stretch factor is the **eigenvalue**. (continued in §11)

😄 **Analogy — gym-bro gains:** push a normal arrow through the matrix and it **twists like a noodle** (new angle). Push an *eigenvector* through and it just gets **taller — same direction, pure gains, no twist.** 💪 The amount it bulked up = the eigenvalue.

✅ Think "matrix as a machine" whenever you reason about what a linear transformation does to a vector — rotation, stretching, projecting.
❌ This framing is conceptual scaffolding, not a computation shortcut — use NumPy for actual multiplies.

> **ML destination:** the matrix-as-machine picture is the mental model for every neural network layer (`output = A·x`), convolution, and PCA — where the covariance matrix is the machine and eigenvectors are its special non-rotating arrows (Sess 5, 18 Jul).

---

## 11. Eigenvectors & Eigenvalues (continues §10)

**One-line definition:**
> Apply a matrix to a vector. If the direction doesn't change — only the length — that vector is an **eigenvector.** The stretch factor is the **eigenvalue (λ, "lambda").**

```
A · v = λ · v
```

**3×3 numeric example — diagonal matrix:**

```
A = [[ 3, 0, 0 ],
     [ 0, 1, 0 ],
     [ 0, 0, 2 ]]

A · [1,0,0] = [3,0,0] = 3 × [1,0,0]   → eigenvector, λ=3  (stretched 3×)
A · [0,1,0] = [0,1,0] = 1 × [0,1,0]   → eigenvector, λ=1  (unchanged)
A · [0,0,1] = [0,0,2] = 2 × [0,0,1]   → eigenvector, λ=2  (stretched 2×)

A · [1,1,0] = [3,1,0]  ≠  λ × [1,1,0]  → direction CHANGED — NOT an eigenvector
```

**Firmware hook:** the matrix is a gain block. Eigenvectors = signal channels that pass through without rotating — only scaled. Eigenvalue = gain on that channel. Non-eigenvectors = cross-talk, direction rotates.

**Connection to covariance & PCA:**

```
Data: [1,2], [2,4], [3,6]   (all on line y = 2x)

Covariance matrix → eigenvalues: λ1=5 (direction [1,2]), λ2=0 (direction [2,−1])

λ1=5 → eigenvector [1,2] = the line y=2x → ALL the spread lives here (high variance)
λ2=0 → perpendicular direction → zero spread, zero information
```

**The bridge:**
- Eigenvector = *direction* of a stretch in your data
- Eigenvalue = *how much* variance (spread) lives in that direction
- **Biggest eigenvalue = most information = what PCA keeps**

```python
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
# largest eigenvalue index → most important direction
```

✅ Eigenvalues/vectors are the right tool when you want to find the "natural axes" of a dataset — directions of maximum spread or minimum redundancy.
❌ Do NOT interpret eigenvalue magnitude as "feature importance" in a raw model — it measures variance in the data, not predictive power; a feature with high variance can still be uninformative for a specific label.

> **ML destination:** this is the direct prerequisite for PCA (Sess 5, 18 Jul). The same eigen-decomposition appears in Multivariate Gaussians, anomaly detection, whitening, and embedding compression (Sess 24, RAG). Understanding it here means Session 5 is revision, not new material.

---

## 12. 🧭 The learning flow — how we actually built this (the journey, wrong turns included)

> **🖥️ Session environment:** this section was learned inside the **VS Code extension of Claude Code** (not the usual Claude Code desktop app) — which is why we could read & edit the Jupyter notebook live (added cell **4.1b**) and run cells in the project `.venv`.
>
> Written as a **journey, not a summary** — the struggles are the memory hooks. When future-me reopens this, *this* section is the one that replays "oh right, this is how it clicked." We did it by hand against the matrix `A = [[2,0],[0,3]]` (stretches EAST ×2, NORTH ×3 — **unequal**, which is the whole point). Live in notebook cell **4.1b**.

**Step 1 — Reframe: a matrix is a machine that moves an arrow.**
Arrow in → new arrow out. It can do two things: **rotate** (change heading) and/or **stretch** (change length). The only question we kept asking: *did the arrow's direction survive?*

**Step 2 — Fed the axis arrows by hand:**
```
A · [1,0]:  (2×1)+(0×0)=2 ,  (0×1)+(3×0)=0  →  [2,0]   still EAST,  just ×2 longer
A · [0,1]:  (2×0)+(0×1)=0 ,  (0×0)+(3×1)=3  →  [0,3]   still NORTH, just ×3 longer
```
Both **held heading** → both are **eigenvectors**. Stretch factor (×2, ×3) = **eigenvalue λ**.

**Step 3 — 💭 The dimension snag (worth remembering).**
I objected: "A has 2 columns but `[1,0]` has 1 row — multiplication needs *cols of first = rows of second*, so this shouldn't fit!"
**Fix:** a vector is a **column**, standing up. `[1,0]` is really `[[1],[0]]` = **2×1** (two rows, one column), not a flat 1×2.
```
A (2×2) · v (2×1)  →  inner dims 2 = 2 ✅  →  result (2×1), another arrow
```
*My rule was right — I'd just drawn the arrow lying down instead of standing up.* (Same `.T` trick the notebook uses in `np.cov(X.T)` / `X @ X.T`: flip rows↔cols so inner dims line up.)

**Step 4 — Fed the diagonal `[1,1]`, and hit the 💭 big misconception.**
```
A · [1,1]:  (2×1)+(0×1)=2 ,  (0×1)+(3×1)=3  →  [2,3]
in:  [1,1] = 45°  (equal east & north)
out: [2,3] ≈ 56°  (more north than east)   →  it ROTATED  →  NOT an eigenvector
```
**My wrong belief:** "`[1,1]` always grows along 45° and never rotates."
**Why wrong:** rotation isn't about the *arrow* — it's about the *matrix*:
```
matrix pulls both legs EQUALLY (×2, ×2)  →  [1,1] HOLDS 45°  (eigenvector)
matrix pulls legs UNEQUALLY    (×2, ×3)  →  [1,1] ROTATES toward the stronger leg
```
I was picturing an equal-stretch machine; *this* one is unequal, so the diagonal tips.

**Step 5 — ✅ Corrected myself with my own rule.**
I'd already said: *"whichever leg is pulled harder, the arrow rotates that way."* Apply to `[1,1]`: north ×3 beats east ×2 → arrow rotates **toward north** → `[2,3]`. My own two statements finally agreed.

**The takeaway that locked it:**
> **An eigenvector is an arrow the matrix can only STRETCH, never ROTATE.**
> - **Axis arrows have one leg** → nothing to tip them → always eigenvectors; stretch = eigenvalue.
> - **The diagonal `[1,1]` has two legs** → survives only if the matrix pulls both legs equally; unequal pull → it rotates.
> - `np.linalg.eig(A)` just *finds* these survivor-arrows automatically (no guessing by hand).

**Step 6 — Started the bridge to covariance (where we headed next).**
A covariance matrix doesn't move arrows — it **describes the shape of a data cloud** (Math vs Physics dots = a tilted cigar). Diagonal = spread per axis; off-diagonal = how much it leans. Off-diagonal ≈ diagonal → tight tilted cigar → features strongly related. The cloud's **eigenvector** = its long axis (max-spread direction); its **eigenvalue** = how much variance lives there. Biggest eigenvalue = what **PCA keeps** → §9's ML payoff. *(continue here next session.)*

---

## 13. ⭐ Temp/Latency eigen — the full chain BY HAND (2×2, paper-ready)

> The one example where *every* step is hand-computable (2×2 → eigenvalues are a quadratic, solvable without a computer). Raw values → covariance → eigenvalue → eigenvector → feature meaning → PCA. Verified against `np.linalg.eig`.

**Data — 3 readings, 2 features (Temp & Latency rise together):**
```
reading   Temp T   Latency L
  #1        40        100
  #2        50        120
  #3        60        140
```
2 features → covariance is **2×2** (features set the size, not the 3 readings).

**Step 1 — means:** `T̄ = 50`, `L̄ = 120`

**Step 2 — deviations:**
```
T − T̄ :  −10,  0, +10
L − L̄ :  −20,  0, +20
```

**Step 3 — the three covariance numbers (÷ n−1 = 2):**
```
var(T)   = [100 + 0 + 100]/2 = 100
var(L)   = [400 + 0 + 400]/2 = 400
cov(T,L) = [(−10)(−20)+0+(10)(20)]/2 = [200+0+200]/2 = 200
```

**Step 4 — the 2×2 covariance matrix:**
```
        T      L
   T [ 100    200 ]
   L [ 200    400 ]
```

**Step 5 — eigenvalues via det(C − λI) = 0:**
```
det [ 100−λ   200  ]  = (100−λ)(400−λ) − 200·200 = 0
    [  200  400−λ  ]
  → λ² − 500λ = 0  →  λ(λ−500) = 0  →  λ₁ = 500 (100%),  λ₂ = 0 (0%)
```
All spread on ONE direction (data sits perfectly on L = 2T+20).

**Step 6 — eigenvector v1 via (C − 500I)v = 0:**
```
[ −400   200 ] [x]        −400x + 200y = 0  →  y = 2x
[  200  −100 ] [y] = 0  →  v1 = [1, 2]   (numpy normalizes → [0.447, 0.894])
```

**Step 7 — verify C·v1 = λ₁·v1:**
```
[100 200][1]   [500]        [1]
[200 400][2] = [1000] = 500·[2]  ✓  stretched ×500, not rotated
```

**Step 8 — how v1 ties to the features (the key read):**
```
v1 = [1]  ← Temp weight
     [2]  ← Latency weight
```
v1's components are **weights on each feature** *(⚠️ these are RECIPE weights / loadings — a blend, NOT the model's prediction weights; see §21 for the full untangling)*: the main axis is "1 part Temp, 2 parts Latency" → Latency swings **2× per unit Temp** — exactly the built-in `L = 2T+20`. **The eigenvector recovered the feature relationship.** Both weights positive → features rise together (matches +200 cov).

**Step 9 — PCA payoff:** λ₁ = 100% → keep only v1 → each reading becomes one number `1·T + 2·L` → 2 features → 1, zero loss.

**Paper caveat:** real data is never *perfectly* collinear, so λ₂ would be small-but-nonzero; here it's a clean 0 only because the numbers are perfectly correlated (keeps the hand-math clean).

---

## 14. 🧭 Deep-dive journey — HOW eigenvectors are computed + every "wait, why?" (2026-06-29/30, VS Code session)

> The flow, wrong turns and questions included. §12 built *what* an eigenvector is (stretch-not-rotate). This section is the next climb: *how you actually compute one*, the intuition under the formula, and the misconceptions cleared along the way. Destination: PCA (syllabus Module 1, Session 5, 18 Jul).

### A. The recipe for finding eigenvectors (works at any size)
```
1. Eigenvalues:  solve  det(C − λI) = 0      ← "characteristic equation"
2. Eigenvectors: for each λ, solve  (C − λI)v = 0
```
**Honest limit:** a 5×5 makes step 1 a degree-5 polynomial → no hand formula exists (nothing past degree 4 does). So 5×5 is *computer-solved* (`np.linalg.eig`, QR algorithm). We learn the mechanics on a **2×2** (hand-solvable), then trust the machine for big ones.

### B. 💭 "Why subtract λI — why not just C − λ?"
Because `C` is a **matrix** and `λ` is a **single number** — you can't subtract a scalar from a matrix (shapes clash, his own dimension-rule). So rewrite the scaling `λv` as `(λI)v` — `λI` is just **λ sitting down the diagonal**. Now it's matrix − matrix, legal:
```
Cv = λv  →  Cv − λv = 0  →  Cv − (λI)v = 0  →  (C − λI)v = 0
```
The `I` is the **adapter** that turns scalar λ into a matrix so it can be subtracted. That's its whole job.

### C. 💭 "Why set the determinant to zero?"
`(C − λI)v = 0` says: *a NONZERO arrow v gets crushed to the zero vector.* Only a **collapsing** matrix can crush a live arrow to nothing — and the fingerprint of a collapsing matrix is **det = 0**.
- **det = area-scaling factor.** det=2 doubles areas; det=0 squashes the plane flat onto a line (kills a dimension).
- Worked the singular beast `B = [[1,2],[2,4]]` (row2 = 2×row1): feeds *every* arrow onto the line y=2x. `det = 1·4 − 2·2 = 0`. And `B·[2,−1] = [0,0]` — a real arrow crushed to the origin (walked the row-by-column multiply by hand).
```
det(C − λI) = 0  ⟺  C − λI collapses  ⟺  some nonzero arrow → 0  ⟺  an eigenvector exists
```
So step 1 hunts the **λ values that MAKE C − λI collapse** — those λ are the eigenvalues. (Note: he had NOT seen the notebook §2.4 — taught the collapse idea from scratch.)

### D. The 2×2 mechanics, fully by hand (the template)
`C = [[4,1],[1,4]]`: `det([[4−λ,1],[1,4−λ]]) = (4−λ)²−1 = 0 → λ = 3, 5`. Then `(C−5I)v=0 → −x+y=0 → v=[1,1]`; λ=3 → `[1,−1]`. **Each matrix has its OWN eigenvectors** (see §12: the diagonal `[[2,0],[0,3]]` gave the *axes* [1,0],[0,1], NOT [1,1]).

### E. The 5×5 covariance run (eigenvalue = importance, eigenvector = direction)
5 SSD sensors (S1S2 linked, S3S4 linked, S5 a blend) → 5×5 covariance → `np.linalg.eig`:
```
λ1 = 2.70 (64.9%), λ2 = 1.44 (34.4%), λ3..λ5 ≈ 0   → data really lives in 2 directions
top eigenvector v1 ≈ [−0.46,−0.46,−0.45,−0.45,−0.42]  (all ≈ equal → "all sensors rise together")
C·v1 = 2.70·v1  ✓ (stretch-not-rotate, now in 5-D)
```
**The split he locked:** the **eigenVALUE (λ) = HOW important** a direction is (how much variance); the **eigenVECTOR (v) = WHICH direction** it is. Most-important direction = eigenvector of the **biggest λ** = PCA's 1st principal component.

### F. ✅ Misconceptions cleared this session
- 💭 *"Is v1 the most-frequent reading, picked out of the data matrix?"* → **No.** v1 is NOT a row/reading and NOT about frequency. It's a **direction = a recipe/blend of the features** (e.g. `1·Temp + 2·Latency`), the long axis of the data cloud. PCA is about **spread (variance)**, not how often a value appears. It's *distilled from* all readings (via covariance), not *lifted whole* from them.
- 💭 *"Is the eigenvector always [1,1]?"* → **No.** `[1,1]` was special to ONE matrix. The matrix decides its own eigenvectors. Also: **length doesn't matter** — numpy normalizes to length 1, so `[1,1]` prints as `[0.707,0.707]`; `[1,1]`, `[2,2]`, `[0.46,0.46…]` are the *same direction*. Sign doesn't matter either (arrow can point either way).

### G. 💭 "Where does 500/(500+0) = 100% come from?" — the pizza
Total variance = **sum of ALL eigenvalues** (the whole pizza 🍕). Each direction's share = its λ ÷ the total:
```
λ1 share = 500/(500+0) = 100% ;  λ2 share = 0/500 = 0%
```
**Slick fact:** sum of eigenvalues = sum of the covariance diagonal (trace) = total variance. Eig just **re-slices the same total** along the cigar instead of the axes: `100+400 (axes) → 500+0 (eigen)`, same 500.

### H. 💭 "Why square the deviations for variance?"
Average the *raw* deviations and you always get **0** — the mean is the balance point, below cancels above (`−10+0+10 = 0`), every dataset, rigged. **Square first** → all positive → no cancellation → a real spread number. Bonus: squaring **punishes big deviations harder** (dev 10 → 100; dev 2 → 4) — the **L2 flavor** from the norms section (absolute-value would be L1: kills signs but treats all gaps evenly).

### I. The PCA payoff + the size rules (the 20-sensor capstone)
- **Flow:** raw `500×20` → `np.cov` → 20×20 → eig → scree shows **3 big λ, 17 ≈ 0** → cumulative hits 95% at **3** → keep 3 numbers, ~99% preserved. *That's PCA.* Edge-AI win: ⅞ less SRAM/MACs/power, same signal (lossy compression for features).
- **Grid size = (#channels)², NEVER #readings.** `500×20 → 20×20`; `1000×20 → 20×20` (more readings only steady the averages); `1000×8 → 8×8`. Mechanism: each cell = one channel-PAIR averaged over all readings; `Xc.T @ Xc` → inner dim (readings) cancels, outer (channels) survives.
- **Pair-counting:** n channels → n² cells, but symmetric mirror, so unique = `n(n+1)/2` (n variances on diagonal + `n(n−1)/2` distinct pairs). The `·` in `20·19` = "times", not a decimal point.
- **⚖️ When PCA BETRAYS you:** (1) the rare signal hides in a tiny-λ direction (anomaly/thermal-runaway spike) → PCA throws it away; (2) you lose interpretability (kept numbers are blends, not "temperature"); (3) the eig step itself costs compute — only worth it if reused. **PCA wins when channels are redundant & you want compact features; loses when every channel is independent or the rare event is the point.**

### J. Artifacts from this journey
Notebook cells **4.1b** + **4.6**; interactive **PCA 20-sensor HTML** (`html/2026-06-28_pca-20-sensors-walkthrough_F.html`, 11 baby-steps); notes **§12** (eigen basics flow), **§13** (Temp/Latency by-hand), this **§14** (the deep-dive). numpy/matplotlib/sympy installed into the project `.venv` so the notebook actually runs.

---

## 15. Variance & Standard Deviation — the FULL deep-dive (2026-06-30)

> This is the part we drilled hardest in the second half. Capture every rung.

### 15.1 — How deviations are calculated (locked, with the slip)
- **deviation = value − mean.** One per reading. No special formula — just subtraction.
- **N values → N deviations**, each measured against the **ONE single mean** (NOT against each other; it's value-vs-mean, never value-vs-neighbour). The mean is the one referee; all players measured against the referee.
- 😄 **Analogy — the "how weird am I" score:** deviation = how far you are from the room's average height. In a room averaging 5'9", **Shaq is +15 cm** (way above), **Danny DeVito is −10 cm** (below). Same room, opposite weird. The *sign* is which side of normal you're on.
- Convention is **value − mean** (not mean − value) so the **sign tells above/below**. For variance the sign vanishes anyway (we square), but keep value−mean so sign stays meaningful.
- **Built-in spell-check: deviations ALWAYS sum to 0** (the mean is the balance point — below cancels above). If yours don't sum to 0, the mean is wrong.
- **Slip caught (S3 = [10,20,30]):** he said mean=30. ❌ 30 is the **max value**, not the mean. mean = sum/count = 60/3 = **20**. With mean=30 the deviations were −20,−10,0 → summed to **−30 ≠ 0** → the alarm fired. Correct mean=20 → deviations −10, 0, +10 → sum 0 ✓. *His method was perfect; only the anchor was misplaced.*
- The **÷(n−1) "divide" lives in variance**, NOT in the deviations themselves.

### 15.2 — Why we SQUARE (variance)
- Average the **raw** deviations → **always 0** (they cancel; mean = balance point). Useless as a summary.
- **Square first** → all positive → no cancellation → a real spread number.
- **Bonus job of squaring:** it **punishes big misses extra** — a deviation of 20 → 400, a 10 → only 100. That's the **L2 flavour**. (Absolute value would be **L1**: also kills signs, but treats all gaps evenly.)
- 😄 **Analogy — the room of people:** a room of **clones** (everyone identical height) → variance **0**. A room with **Danny DeVito AND Shaq** in it → variance **huge**. Variance = "how much do the members disagree with the average?" Wide variance on a latency sensor = jittery QoS.
- `variance = (Σ squared deviations)/(n−1)` — one number, but in **squared units** (°C², µs²).

### 15.3 — Why STANDARD DEVIATION when we already have deviations / variance
- **Deviations** = a *list* (signed, sums to 0) → can't summarize spread in one number.
- **Variance** = one number, but **squared units** ("250 µs²" is meaningless to a human).
- **σ = √variance** → back to **real units** = "the typical distance a reading sits from the mean." The headline you can put on a datasheet or set a throttle threshold against.
- **Decision boundary (which tool when):**
  - **raw deviation** → you care about ONE specific point / how big an outlier is.
  - **σ (std dev)** → you want the typical spread, in real units (thresholds, ±, datasheets).
  - **variance (σ²)** → inside the MATH machinery (covariance, optimization) — squared form adds/combines cleanly.

### 15.4 — The "mean ± σ = typical range" statement (analogies)
- **Height:** "we're typically 5'9" ± 2"."
- **Pizza 🍕:** mean 30 min. Shop A = 30 ± 2 (reliable, plan dinner); Shop B = 30 ± 20 (chaos). Same mean, σ is the whole difference between trustworthy and gamble.
- **Latency:** "reads typically land at 100 ± 8 µs."

### 15.5 — ⭐ Two-drive latency example, FULL by hand (same mean, different σ)
```
Drive A (steady):  [98, 100, 102, 99, 101]      Drive B (jittery): [80, 120, 90, 110, 100]
mean A = 500/5 = 100                            mean B = 500/5 = 100        ← identical mean!
dev A:  −2, 0, +2, −1, +1                       dev B: −20, +20, −10, +10, 0
sq  A:   4, 0,  4,  1,  1  = 10                  sq  B: 400,400,100,100,0 = 1000
var A = 10/4   = 2.5                             var B = 1000/4 = 250
σ_A  = √2.5  ≈ 1.58 µs                           σ_B  = √250  ≈ 15.81 µs
→ 100 ± 1.6 (98–102): steady ✅                  → 100 ± 16 (84–116): jitter-bomb 🔥
```
**The mean said "identical drives." σ exposed the lie.** Drive B's fat σ = p99 tail blowout = QoS support ticket, even though the average looked perfect. *σ is the only number that caught it.*

---

## 16. The Bell Curve — σ drawn as a SHAPE

- The bell **is the picture of σ.** Peak sits at the **mean**; **width is set by σ**.
  - small σ → a **razor-thin spike** (steady drive, reads jammed near mean)
  - big σ → a **wide hill** (jittery drive, reads sprawl far)
- **68–95–99.7 rule:** `±1σ ≈ 68%`, `±2σ ≈ 95%`, `±3σ ≈ 99.7%` of readings.
- **⚠️ ±1σ is NOT the outlier fence.** ~**1 in 3 readings normally falls outside ±1σ** (by design). Outliers live beyond **±2σ / ±3σ**.
  - Drive B (σ=15.81): ±1σ = 84–116 (so 80 & 120 fall *outside* ±1σ) — but ±2σ = **68.4–131.6**, and 80 & 120 sit **inside** it → **normal jitter, NOT outliers.** A real outlier would be ~150+ µs (beyond 3σ), out in the dead tail → "go investigate" (ECC retry, read-disturb, throttle).
- **z-score = (value − mean)/σ** = how many σ from the mean. Drive B's 80 → (80−100)/15.81 = **−1.26σ**. It's the band-position turned into a number, and makes different drives comparable.
- **The journey into the bell:** raw readings → mean → deviations → variance → σ → *"but what does σ LOOK like?"* → **the bell.**
- **Where the bell leads (it's a hub):** **z-scores** (how-many-σ), **anomaly detection** (beyond ±3σ = off-distribution), **probability/Bayes** (area under a slice = probability a read lands there), **ML normalization** (standardize = subtract mean ÷ σ = z-score on every value → mean 0, σ 1; keeps °C and mV channels on equal footing, ties back to covariance/PCA scaling).

---

## 17. ⭐⭐ Variance: TRUST vs IMPORTANCE — the reconciliation (the hardest knot, now locked)

**The apparent contradiction he spotted:** the restaurant/latency lesson said *LOW variance = good (trust)*, but PCA said *HIGH variance = important.* Which is it?

**The resolution — variance is NEUTRAL. It only ever means SPREAD. Whether you WANT it high or low flips with the QUESTION:**

```
                       LOW variance            HIGH variance
reliability / trust →  GOOD (rely on it)       BAD (unpredictable)
information / PCA   →  USELESS (no info)        IMPORTANT (informative)
```

- **Reliability question** ("which do I trust?") → want **LOW** variance = consistency. Restaurant A (30±2) beats B (30±20). SSD: tight σ = good QoS.
- **Information question** ("which feature tells things apart?", PCA) → **HIGH** variance is "important" = **discriminating power**. A zero-variance feature ("has a roof?" = all yes) can't separate anyone → useless.

**⭐ Worked numbers — the two restaurants (same mean 30 min):**
```
Restaurant A:  [28, 30, 32, 29, 31]   mean=30   dev −2,0,+2,−1,+1        var=10/4=2.5      σ≈1.58  → 30 ± 1.6 (reliable ✅)
Restaurant B:  [10, 50, 30, 45, 15]   mean=30   dev −20,+20,0,+15,−15    var=1250/4=312.5  σ≈17.7  → 30 ± 18 (gamble ❌)
```
Same average delivery — σ is the entire difference between "plan your evening" and "order at your own risk."

- **KEY: "important" (PCA) ≠ "good/trustworthy."** It means *"this is where the differences / the information live."* The **same high variance** is simultaneously **BAD** (untrustworthy) and **IMPORTANT** (informative) — no contradiction, different questions.
- **The one-liner:** *variance is a **speedometer, not a judge.*** It tells you "how much spread," never "good or bad." 120 mph is both "important" (lots happening) and "dangerous" (don't trust) — same number, depends if you're the race analyst or the passenger.
- 😄 **Analogy — the yes-man sensor & the useless exam question:** a sensor that reads `3.30, 3.30, 3.30…` is a **yes-man** — says "all good" every time, so it can never *explain* why the drive throttled → variance ≈ 0 → deletable. Same as the **exam question everyone gets right** (`[10,10,10,10,10]`, variance 0): it can't rank a single student → zero information. The **high-variance** question (`[2,5,7,9,10]`) is the one that *tells students apart* → that's the "important" one PCA keeps. **Important = discriminating power, NOT quality.**

**⭐ Worked numbers — yes-man sensor vs storyteller sensor:**
```
Sensor A (voltage rail):  [3.30, 3.30, 3.31, 3.30, 3.30]   mean≈3.30   var≈0.00002   → FLAT, a yes-man → tells you nothing → drop it
Sensor B (die temp):      [42, 55, 71, 63, 88]             mean=63.8   var≈297.7 (σ≈17.3)  → SWINGS → this is where the throttling story lives → keep it
```
For a thermal-throttle predictor, Sensor B (high variance) is gold; Sensor A is deletable dead weight. PCA keeps B's direction, drops A's.
- **Zero-variance feature `[50,50,50,50]`:** trust lens → **GOOD** (rock-steady); training lens → **DROP it** — it has zero predictive power by construction (every example looks identical on it → model gives it weight 0), yet still costs SRAM/MACs/mW. **Dropping near-zero-variance directions = exactly what PCA/feature-selection automates → smaller model, same accuracy = the Edge-AI win.** (His own words: "I would not keep this for training — it doesn't add any corner scenario.")

---

## 18. Why readings go in ROWS, features in COLUMNS

- It's a **convention**, but the sensible one:
  1. **Data streams in row-by-row over time** — each new reading appends a new **row** (table grows *downward*, unbounded). Features are **fixed-width**. Columns-as-readings would grow the table sideways off-screen forever.
  2. **A row = one complete record/snapshot = a C struct.** The whole log = an **array of structs** (`log[reading].field`) — which *is* rows-as-readings.
  3. **Every tool agrees** (pandas, scikit-learn): rows = samples, columns = features.
- **The `.T` wrinkle (why it kept appearing):** `np.cov` is the odd one out — it **defaults to rows = variables**. So with normal data (rows=readings) you write **`np.cov(X.T)`** to flip (readings×features) → (features×readings) for that one function. The math works either way; you'd just swap `Xᵀ X` ↔ `X Xᵀ`.
- **Quick check:** 1000 readings × 5 sensors → shape **1000 × 5**; the **1000 keeps growing** tomorrow, the **5 is fixed**.

---

## 19. ⭐ Clean 3×3 eigen — FULLY by hand (`[[2,1,1],[1,2,1],[1,1,2]]`)

> §13 walked a 2×2 by hand in 8 steps. This is the 3×3 twin — same 8-step chain, same "verified, hand-doable, PCA-payoff-at-the-end" flow. Two genuinely new things at 3×3: the eigenvalue step is a **cubic** (harder in general — clean only when the matrix is designed nicely), and one eigenvalue **repeats** (`λ = 1, 1`) which forces a small side-story about "flat leftover" directions. Verified against `np.linalg.eig`.

**Setup — 3 sensors, every pair equally linked (cov = 1):**
Not raw data this time — we start straight from the covariance matrix (as if the data-→cov steps of §13 already ran). Each diagonal `2` = each sensor's own variance; each off-diagonal `1` = each pair's covariance. The story: *whatever three sensors we're watching, they all move together the same amount.*
```
        S1  S2  S3
   S1 [ 2   1   1 ]
C = S2 [ 1   2   1 ]
   S3 [ 1   1   2 ]
```

**Step 1 — the characteristic equation, `det(C − λI) = 0`:**
Subtract λ down the diagonal, take the determinant, set it to zero.
```
       [ 2−λ   1     1  ]
C−λI = [  1   2−λ    1  ]
       [  1    1    2−λ ]
```

**Step 2 — expand the determinant (cofactor along row 1). Let `a = 2−λ` to keep it clean:**
```
det = a·(a·a − 1·1) − 1·(1·a − 1·1) + 1·(1·1 − a·1)
    = a(a²−1) − (a−1) + (1−a)
    = a³ − a − a + 1 + 1 − a
    = a³ − 3a + 2
```
That's the cubic. This is the *only* real wall past 2×2 — generic cubics have no clean formula. Ours factors.

**Step 3 — factor the cubic → eigenvalues:**
Try `a = 1`: `1 − 3 + 2 = 0` ✓ → `(a−1)` divides it. Long-divide:
```
a³ − 3a + 2 = (a − 1)(a² + a − 2) = (a − 1)(a − 1)(a + 2) = (a−1)²(a+2)
```
Roots: `a = 1` (double) or `a = −2`. Undo the substitution `λ = 2 − a`:
```
λ₁ = 4      (the "common-mode" tide — all sensors together)
λ₂ = 1      \_ the two "differential" leftovers
λ₃ = 1      /
```
**Sanity checks (do these EVERY time — cheap catch for arithmetic slips):**
- trace `= 2+2+2 = 6` should equal `Σλ = 4+1+1 = 6` ✓
- `det(C) = 2(4−1) − 1(2−1) + 1(1−2) = 6−1−1 = 4` should equal `Πλ = 4·1·1 = 4` ✓

**Step 4 — eigenvector for λ₁ = 4: solve `(C − 4I)v = 0`.**
Subtract 4 from the diagonal, then row-reduce.
```
[ −2   1   1 ][x]   [0]     Row1 − Row2 :  −3x + 3y +  0 = 0  →  x = y
[  1  −2   1 ][y] = [0]     Row2 − Row3 :    0 − 3y + 3z = 0  →  y = z
[  1   1  −2 ][z]   [0]     →  x = y = z   →   v₁ = [1, 1, 1]
```
Meaning: PC1 points along "**all three sensors rising together**" — the shared tide. (numpy normalizes → `[0.577, 0.577, 0.577]`.)

**Step 5 — eigenvectors for the REPEATED λ = 1 (the genuinely new bit): solve `(C − 1·I)v = 0`.**
```
[ 1  1  1 ]          all three rows collapse to ONE equation:
[ 1  1  1 ]  ⇒       x + y + z = 0
[ 1  1  1 ]
```
One equation in three unknowns → a **2-dimensional solution plane** (2 degrees of freedom), which is exactly why we get *two* eigenvectors here. Anything in that plane works; pick two independent arrows:
```
v₂ = [ 1, −1,  0 ]      "S1 up, S2 down, S3 idle"
v₃ = [ 1,  1, −2 ]      "S1 & S2 up, S3 twice down"
```
Both cancel to sum-zero → both live in that plane → both are eigenvectors with λ = 1. Every direction that *doesn't* move all three sensors together sits here.

> **💡 Why repeats give a plane, not a line (the intuition):** an eigenvalue's **multiplicity** = how many independent directions the matrix stretches by that same factor. λ = 1 appears twice → two independent directions get "stretched by 1" (i.e. left alone). A whole 2D plane of "leftover" is unchanged; only the common-mode direction is amplified (×4).

**Step 6 — verify each `C·v = λ·v` (must-do, catches all algebra bugs):**
```
C·v₁: [2+1+1, 1+2+1, 1+1+2] = [4,4,4] = 4·[1,1,1]        ✓  λ=4
C·v₂: [2−1+0, 1−2+0, 1−1+0] = [1,−1,0] = 1·[1,−1,0]      ✓  λ=1
C·v₃: [2+1−2, 1+2−2, 1+1−4] = [1,1,−2] = 1·[1,1,−2]      ✓  λ=1
```
All three land on `λv` exactly — matrix stretches, doesn't rotate. Chain verified end-to-end.

**Step 7 — how v₁ ties to the sensors (the key read):**
```
v₁ = [1]  ← S1 weight
     [1]  ← S2 weight
     [1]  ← S3 weight
```
Equal positive weights on all three sensors → PC1 is literally "**the average of the three sensors**" — the common tide.
That mirrors §13's read: there `v₁ = [1, 2]` meant "1 part Temp + 2 parts Latency"; here `v₁ = [1, 1, 1]` means "1 part each of S1, S2, S3."
The **SSD common-mode / differential-mode** analogy fits perfectly: PC1 = "all rails rise together" (bulk thermal drift); v₂ and v₃ = "one rail vs another" (differential jitter). Every good storage engineer already reasons this way about noise.

**Step 8 — PCA payoff:**
Fractions of total variance = `λ / Σλ`:
```
PC1 (v₁, λ=4):  4/6 = 66.7%   ← the shared tide
PC2 (λ=1):      1/6 = 16.7%   \_ the leftover differential plane
PC3 (λ=1):      1/6 = 16.7%   /
```
Keeping just PC1 compresses **3 sensors → 1 number** (the sum) and retains ⅔ of the variance. If we also cared about the differential jitter, we'd keep any *one* extra direction from the leftover plane and be at 83.3% with just 2 numbers. That's PCA: rank directions by λ, keep the top-K, drop the rest.

**Paper caveat:** this all works cleanly because the matrix is symmetric with a nice-shaped cubic. Real 3×3 covariances from field data will have ugly decimals and won't factor by inspection — that's when we hand it to `np.linalg.eig`. But the **mechanics** are the same eight steps.

**Side-by-side interactive twin:** `html/2026-07-02_eigen-by-hand-2x2-vs-3x3_F.html` walks both §13 (2×2) and §19 (3×3) in parallel, step-by-step, so you can see the exact same chain at two sizes.

---

## 21. ⭐ The two "weights", the label rule, + the perpendicularity drill (2026-07-03)

> **Why this section exists:** the word **"weights"** in §9/§13 (eigenvector components) got mixed up with the **prediction weights** a model learns. This was a high-value confusion — untangled here so it never recurs. Then a fresh 8-step drill re-revises covariance AND proves *why* the kept eigenvectors come out perpendicular.

### 21.0 — The picture first: WHERE each weight is born (house-price flow)

The whole confusion dissolves the moment you see the two weights born in **two different boxes**, on **two sides of the label line**:

```
  [1] 20 raw house features ─┐
                             │      math: —                 label? NO
  [2] PCA (covariance→eigen) │      math: LINEAR ALGEBRA    label? NO   ← UNSUPERVISED
      squeeze 20 → 4 clean   │      → makes RECIPE weights (loadings): how to BLEND features
      perpendicular axes     │
  ════════════ ⬇ LABEL (price) ENTERS HERE ⬇ ════════════
  [3] model: price = w₁c₁+…+b │     math: LINEAR ALGEBRA
  [4] loss = (guess − price)² │     math: CALCULUS+PROB    label? YES  ← SUPERVISED
  [5] gradient descent        │     → makes PREDICTION weights: how hard each ingredient pushes price
  [6] trained weights w₁..b  ─┘     the model is built
```

- **Box [2] → recipe weights** (the eigenvector components / loadings). Price never seen. Unsupervised.
- **Box [5] → prediction weights.** Price drives them. Supervised.
- **PCA reshapes features; gradient descent predicts.** Opposite sides of the label line — not two flavors of one machine.

*(Full 6-box version with per-box math annotations: `2026-07-02_ml-pipeline-math-map_F.md` §1b.)* Now the details:

### 21.1 — "Weights" means TWO different things (the overloaded word)

| | **Recipe weights** (aka *loadings*) | **Prediction weights** |
|---|---|---|
| What | eigenvector components — *how much of each feature to BLEND into a new axis* | how hard each ingredient *pushes the answer* |
| Formula | `PC1 = 0.71·School + 0.71·Metro` | `Price = w₁·PC1 + w₂·PC2 + b` |
| Comes from | **PCA** (eigen of covariance) | **gradient descent** (or least-squares) |
| Sees the label? | ❌ never | ✅ yes — the label drives them |
| Answers | *"what is this new axis made OF?"* | *"how important is it to the answer?"* |

- ✅ *"An eigenvector's components are weights on your features"* → **recipe weights.** True. (What §13 meant.)
- ❌ *"PCA gives me the price-prediction weights"* → **false.** Those are learned later, by the model.
- 😄 **Cooking split:** PCA is the **prep cook** writing a *recipe* ("2 parts school, 2 parts metro" = one clean ingredient). Gradient descent is the **head chef** deciding *how much of each ingredient makes the dish taste right* (predict the price). Same word "measure," two different jobs.

### 21.2 — The label rule: it's about the METHOD, not the PIPELINE

> A technique is supervised/unsupervised by **whether THAT technique looks at the label** — not whether the overall project has labels.

- House-price project = **supervised** (price = label). But **PCA as a step is unsupervised** — it never sees the price, it only studies how features co-move. Perfectly legal to bolt an unsupervised step onto the front of a supervised pipeline.
- 😄 **Kitchen:** the restaurant is "supervised" (serve the ordered dish). The **prep cook** who chops veg never sees the order → his step is "unsupervised." Still a supervised kitchen.
- **One-line test — has the label entered the math yet?**
  - **No** → any "weight" you see is a **recipe weight** (PCA loadings); the step is unsupervised.
  - **Yes** → "weight" now means **prediction weight** (gradient descent); the step is supervised.

### 21.3 — ⭐ The perpendicularity drill (8 steps, house features, fully by hand)

Same skeleton as the §13/§19 covariance drills, but the payoff is **orthogonality**. Non-SSD domain on purpose (for teaching a stranger). *All numbers verified vs `np.linalg.eig`.*

**Setup — 5 Bangalore houses, 2 amenity features** (score 0–10, higher = closer):
```
House:     H1    H2    H3    H4    H5
School :    3     4     6     6     6
Metro  :    4     7     5     7     7
```

**Step 1 — means:** School = 25/5 = **5**  ·  Metro = 30/5 = **6**

**Step 2 — deviations (value − mean):**
```
School dev:  −2   −1   +1   +1   +1
Metro  dev:  −2   +1   −1   +1   +1
```
(each row sums to 0 ✓ — the built-in spell-check)

**Step 3 — the two variances (÷ n−1 = ÷4):**
```
var(School) = (4+1+1+1+1)/4 = 8/4 = 2
var(Metro)  = (4+1+1+1+1)/4 = 8/4 = 2
```

**Step 4 — the covariance (average of the per-house "votes"):**
```
School·Metro dev products:  (−2)(−2)+(−1)(1)+(1)(−1)+(1)(1)+(1)(1)
                          =    4   −1    −1    +1    +1   = 4
cov = 4/4 = 1     (positive → school & metro proximity rise together)
```

**Step 5 — the covariance matrix:**
```
C = | 2  1 |     (diagonal = the two variances; off-diagonal = the shared lean)
    | 1  2 |
```

**Step 6 — eigenvalues via det(C − λI) = 0:**
```
det | 2−λ   1  | = (2−λ)² − 1 = 0  →  2−λ = ±1  →  λ₁ = 3,  λ₂ = 1
    |  1   2−λ |
```

**Step 7 — eigenvectors (the recipe weights):**
```
λ₁ = 3:  (2−3)x + y = 0  →  −x + y = 0  →  x = y   →  v₁ = [1, 1]   (the "both rise together" axis)
λ₂ = 1:  (2−1)x + y = 0  →   x + y = 0  →  y = −x  →  v₂ = [1, −1]  (the "one up, other down" axis)
```

**Step 8 — THE PUNCHLINE (perpendicularity + PCA):**
```
v₁ · v₂ = (1)(1) + (1)(−1) = 1 − 1 = 0   →  the two axes are at 90° (PERPENDICULAR) ✓
shares:  λ₁/Σλ = 3/4 = 75%   ·   λ₂/Σλ = 1/4 = 25%
PCA: keep v₁ (75%) → each house's 2 numbers → 1 number (1·School + 1·Metro). Drop v₂, lose only 25%.
```

### 21.4 — Why perpendicular, and why it matters

- **Guaranteed, not lucky.** *Every* covariance matrix is **symmetric** (`cov(A,B)=cov(B,A)`), and symmetric matrices *always* hand back eigenvectors at exactly 90°. Pick any dataset — the axes come out perpendicular. (That's why your earlier `[1,2]` + `[1,1]` guess couldn't both be real components — they're not at 90°; the true partner of `[1,2]` is `[2,−1]`.)
- **Why 90° = "clean":** perpendicular axes share **zero** information. Each new ingredient carries something the others don't — no double-counting. That's the whole point of PCA: turn 20 overlapping, gossiping features into a few **independent** ones.
- **Recipe-weight, not prediction-weight:** `v₁ = [1,1]` says *"blend one School + one Metro to make the strongest new axis."* It does **not** say what a house costs — the price never entered. (Label rule, §21.2.)

**🎯 The thread forward:** these perpendicular recipe axes are what you feed *into* a regression model on 18 Jul (Session 5). Only *there* does gradient descent look at the price and learn the **prediction weights**. PCA compresses; the model predicts. Two steps, two kinds of weight.

---

## 20. Study HTMLs built this session (all in `html/`)

1. **`2026-06-28_pca-20-sensors-walkthrough_F.html`** — 11 baby-steps: 20 SSD sensors → 3 numbers; raw → covariance → eigen → scree/cumulative; worked-by-hand covariance cell + channel-pair counting; "when PCA betrays you."
2. **`2026-06-30_covariance-eigen-capstone_F.html`** — full-width side-by-side **2×2 vs 3×3**, same pipeline in parallel rows: readings → mean (number-line + formula) → deviations (ladder showing value−mean) → variance (squared arithmetic) → std dev (+ per-sensor bell curves on slide 5) → covariance (vote-quadrant scatter) → covariance matrix (heatmap) → eigenvalues (`det(C−λI)=0`) → **eigenvectors (full matrix-grid derivation: C, λI, C−λI, the system, the solve + machine input→output stretch plot)** → stretch → takeaways.
3. **`2026-06-30_bell-curve-sigma-latency_F.html`** — interactive σ slider (bell goes skinny↔fat), Drive A/B presets, 68-95-99.7 bands, data points colored by band; **comprehensive narrative** top (the 7-rung road to the bell) + bottom (where the bell leads: z-score/anomaly/Bayes/normalization).
