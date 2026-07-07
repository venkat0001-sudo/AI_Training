---
title: Probability basics — marginal · joint · conditional
aliases: [conditional-probability, joint-probability, marginal-probability, independence]
date: 2026-06-17
sessions: [F]
lane: f
edge: 2
status: due
type: concept
tags: [incomplete]
up: "[[MOC-foundation-math]]"
recap: "P(A) = the fraction of the world where A happens; conditional P(A|B) = the fraction of B-world where A happens. STUB — sourced from the Bayes table; its own worked doc is owed."
---

# Probability basics — marginal · joint · conditional

> **Recap:** P(A) = the fraction of the world where A happens; **conditional P(A|B) = the
> fraction of B-world where A happens.** STUB — sourced from the Bayes 200-cycle table; a full
> worked doc of its own is owed.

> [!warning] ⚠️ STUB atom — the concept was taught (~2026-06-17, Foundation stats) but never got
> its own scroll; the anchors below are borrowed from [[bayes]]'s 200-cycle table. Owed: its own
> worked examples (dice/NAND RBER), independence + program-disturb counterexample, numpy twin.

**Chain:** counting ──► **probability** ──► [[normal-distribution]] (areas ARE probabilities) ──► [[bayes]] ──► [[entropy]] (expected surprise)

## The anchor numbers (borrowed from the Bayes table)  ^anchor

Read every probability flavor off ONE table ([[bayes#^anchor]]):

```
marginal     P(Real)        = 20/200  = 10%      one variable, ignore the rest (the row/col totals)
joint        P(Real ∧ HOT)  = 18/200  = 9%       both at once (one inner cell)
conditional  P(HOT | Real)  = 18/20   = 90%      shrink the world to the Real column FIRST
```

**The move that matters: conditioning = shrinking the world.** P(HOT|Real) lives inside the
20-cycle Real column, not the 200-cycle world.

## Where it came from / where it goes

feeds:: [[normal-distribution]] — the area under a slice of the bell IS a probability
feeds:: [[bayes]] — conditional probability, rearranged
feeds:: [[entropy]] — entropy = expected surprise, computed FROM the p's
used-by:: RBER thinking — P(a NAND cell reads wrong) is a probability he already quotes
scroll:: [[2026-06-25_bayes-and-ml-taxonomy_s1]] — the table it's read from

## Decision boundary

- ✅ Marginal for "how common overall"; joint for "both at once"; conditional the moment you have partial knowledge (an alarm fired, a test came back).
- ❌ NEVER assume independence by default — NAND neighbours program-disturb each other; real data is rarely independent. (Full counterexample owed.)

## 📋 Still owed (resume checklist)

- [ ] Own worked example set (dice + RBER), fully hand-computed
- [ ] Independence: definition + the program-disturb counterexample with numbers
- [ ] Numpy twin (simulate the 200-cycle table, verify the three flavors converge)
- [ ] Then clear `tags: [incomplete]` and advance the recall ladder

## Flashcards

#flashcards/probability

P(HOT|Real) = 90% but P(Real|HOT) = 50%. How can both be true? :: Different worlds: the first lives in the 20-cycle Real column, the second in the 36-cycle alarm row. Conditioning = shrinking the world; direction matters.
Joint vs conditional in one move? :: Joint = an inner cell over the WHOLE world (18/200). Conditional = same cell over a SHRUNK world (18/20).
