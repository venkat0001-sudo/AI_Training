# Linear Algebra Foundations — Vectors, Magnitude, Dot Product & Cosine Similarity

> Revision notes for the **2026-06-28 hands-on lab** — a NumPy practical built on top of the earlier Foundation classes (hence the `_F` tag, not a session number). Spine = **dot product + cosine similarity**; everything else (matrices, covariance, eigen) is recognition-level. This doc captures the magnitude → dot → cosine arc and the A/D/C recommendation example that shows *when each tool wins*.

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

---

## 2. Dot product — alignment, but blind to size

```
A·B = a1·b1 + a2·b2 + ... + an·bn        # NumPy: A @ B  or  np.dot(A, B)
```

Result is a single number measuring how much two vectors align. **But it's contaminated by magnitude:** a high score can mean *aligned* OR *just loud*. It can't tell those apart.

**The two lies of the raw dot product:**
1. Same direction, different volume → wildly different scores. `[1,1]·[1,1]=2` but `[10,10]·[10,10]=200` — same perfect alignment, 100× the score, purely from loudness.
2. Different directions → can give the *same* score. `[1,0]·[5,0]=5` (identical heading) and `[5,5]·[1,0]=5` (45° apart) — dot product can't distinguish them.

---

## 3. Cosine similarity — chop off the length, keep the heading

```
cosine(A,B) = (A·B) / (|A| × |B|)        # divide out BOTH magnitudes
```

Range `−1 … +1`: **+1** = same direction, **0** = unrelated, **−1** = opposite. It normalizes out the gain on both sides, leaving only direction.

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

## 7. Variance & Covariance

**Variance** = how spread out a single variable is around its mean.
**Std dev** = sqrt(variance) — same idea, back in original units (easier to read).

```
variance(X)     = avg of (xi − x̄)²           # one variable vs itself
std dev(X)      = sqrt(variance(X))
covariance(X,Y) = avg of (xi − x̄)(yi − ȳ)    # two variables, paired
```

Covariance is variance's sibling — variance asks "how much does *one* thing spread?", covariance asks "do *two* things spread *together*?"

**Sign tells the whole story:**
- **Positive** → both rise together (temp ↑, latency ↑ due to throttling)
- **Negative** → one rises, other falls (price ↑, sales ↓)
- **≈ Zero** → no relationship (shoe size vs exam score)

**Numeric example — controller temp vs read latency:**

```
Temp X:      40,  50,  60      mean X̄ = 50
Latency Y:  100, 120, 140      mean Ȳ = 120

X − X̄:   −10,   0,  +10
Y − Ȳ:   −20,   0,  +20

products: (−10)(−20)=+200,  (0)(0)=0,  (+10)(+20)=+200
covariance = 400 / (3−1) = 200   → positive: both rise together ✓
```

**Covariance matrix** — when you have many features, store all pairwise covariances in a grid:

```
           Temp   Latency
Temp     [[ 1.0,   0.7 ],
Latency   [ 0.7,   1.0 ]]
```
Diagonal = each variable vs itself (= its own variance). Off-diagonal = pairwise covariance.
`np.cov(data.T)` computes this for the whole dataset at once.

---

## 8. Eigenvectors & Eigenvalues

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
