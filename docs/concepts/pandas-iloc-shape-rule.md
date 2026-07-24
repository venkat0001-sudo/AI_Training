---
title: pandas .iloc shape rule (scalar vs slice vs list)
aliases: [iloc, iloc shape, 1D vs 2D pandas, iloc dimension rule, why 0:1]
date: 2026-07-21
sessions: [python-journey]
lane: f
edge: 1
status: owned
type: concept
up: "[[HOME]]"
recap: How you index with .iloc decides the DIMENSION you get back; the number decides the POSITION — two independent knobs.
---

# pandas .iloc shape rule (scalar vs slice vs list)

> **Recap:** `.iloc` gives back **1-D or 2-D depending on HOW you index, not which column** — a
> scalar drops the dimension, a slice or a list keeps it. Two independent knobs: *scalar/slice/list*
> sets the **shape**, the *number* sets the **position**.

## What it is (plain words)

`df.iloc[rows, cols]` = integer-location indexing into a DataFrame. The surprise for a C brain:
selecting "one column" can give you either a flat vector **or** a one-column table — and *which one*
is decided purely by the punctuation you use, not by the data.

## The anchor rule  ^rule

```
scalar  0     → drop the dimension  → 1-D   shape (200,)
slice   0:1   → keep it (contiguous) → 2-D   shape (200, 1)
list    [0]   → keep it (cherry-pick)→ 2-D   shape (200, 1)
```

Same numbers, different **container**:

```
df.iloc[:, 0]         df.iloc[:, 0:1]
  6.89                  [6.89]
  5.12                  [5.12]
  7.82        vs        [7.82]
  ...                    ...
bare column of values  each row is still a "row" (holding 1 value)
1-D vector             2-D matrix (200×1)
```

Like `int x[200]` vs `int x[200][1]` in C — identical data, but the second has an extra wrapper
dimension.

**Position is a separate knob.** The number picks the column; negative counts from the end:

```
df.iloc[:, 0]    # first column   (scalar → 1-D)
df.iloc[:, -1]   # LAST column    (scalar → 1-D)   -1 always = last, however many columns
df.iloc[:, 0:1]  # first column   (slice  → 2-D)
```

`df.iloc[:, [0, 3, 1]]` — a **list** cherry-picks any columns in any order (a slice can only grab a
contiguous run `0:3` = 0,1,2). This is why real multi-feature X is written `df[['cgpa','attendance']]`
— a list of names → 2-D feature matrix.

## Why it matters (the .fit() trap)

sklearn's `.fit(X, y)` wants **X as 2-D** (a matrix, one row per sample, one column per feature) and
**y as 1-D** (one answer per row). So in the placement notebook:

```python
X = df.iloc[:, 0:1]   # 2-D on purpose — the slice keeps X a table
y = df.iloc[:, -1]     # 1-D on purpose — the scalar collapses y to a vector
```

Feed `.fit()` a 1-D X (`df.iloc[:, 0]`) and it throws:
`ValueError: Expected 2D array, got 1D array instead... Reshape your data using array.reshape(-1, 1)`.
So `0:1` (or `[0]`) is the lazy way to stay 2-D without a separate `.reshape(-1, 1)`.

## Decision boundary

- ✅ **scalar** (`0`, `-1`) when you want a **1-D Series** — the target `y`, or any single column to plot/compute on.
- ✅ **slice `0:1` or list `[0]`** when something demands **2-D** — sklearn's `X`, one feature but must stay a matrix.
- ✅ **list `[0,3,1]`** when you want **multiple / reordered** columns as 2-D.
- ❌ don't hand a scalar-indexed 1-D column to `.fit()` as X — shape error.

## Numpy twin

```python
import pandas as pd
df = pd.DataFrame({'cgpa':[6.89,5.12,7.82], 'package':[3.26,1.98,3.25]})
print(df.iloc[:, 0].shape)    # (3,)    scalar → 1-D
print(df.iloc[:, 0:1].shape)  # (3, 1)  slice  → 2-D
print(df.iloc[:, [0]].shape)  # (3, 1)  list   → 2-D
print(df.iloc[:, -1].shape)   # (3,)    scalar, last column → 1-D
```

## Where it goes (typed links)

used-by:: [[regression]] — sklearn `LinearRegression.fit(X, y)` is what forces the 2-D-X / 1-D-y shape rule
builds-on:: [[vectors]] — 1-D Series is a vector; 2-D is the feature matrix that holds many

## Formula

No formula — it's an API shape rule. Mnemonic: **scalar drops, slice/list keeps.**
