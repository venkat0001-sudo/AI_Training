---
title: Evaluation metrics — confusion matrix, precision, recall, F1
aliases: [confusion-matrix, precision, recall, f1, f1-score, accuracy, false-positive, false-negative, type-1-error, type-2-error]
date: 2026-06-27
sessions: [s1]
lane: m1
edge: 2
status: learning
type: concept
up: "[[MOC-m1-ml-fundamentals]]"
recap: "Naming rule: the SECOND word is what the model said, the FIRST word is whether it was right. Which error costs more depends on the domain — cancer minimizes FN (recall), anti-missile minimizes FP (precision)."
---

# Evaluation metrics — confusion matrix, precision, recall, F1

> **Recap:** Naming rule: **the SECOND word is what the model said, the FIRST word is whether it
> was right.** Which error costs more depends on the domain — cancer minimizes FN (recall),
> anti-missile minimizes FP (precision).

**Chain:** [[bayes]] (base rates) ──► **metrics** ──► [[cross-validation]] (the score each fold reports) ──► model selection
**Chain:** [[cross-entropy]] ──► **metrics** — "your loss must be consistent with the metric you care about, or optimizing it fails YOUR objective"

## What it is (plain words)

Every prediction lands in one of four cells: the model said positive/negative (second word), and
it was true/false that it was right (first word). **TP and TN are the good diagonal; FP (Type 1)
and FN (Type 2) are the two DIFFERENT ways to be wrong — and they almost never cost the same.**

## The anchor  ^anchor

```
                Reality = True    Reality = False
ML says True    TP  (correct)     FP  (Type 1 error)
ML says False   FN  (Type 2)      TN  (correct)

Accuracy  = (tp+tn)/(tp+tn+fp+fn)        default — but LIES on imbalanced classes
Precision = tp/(tp+fp)     100% ⇔ FP = 0   → anti-missile (never fire on a civilian aircraft)
Recall    = tp/(tp+fn)     100% ⇔ FN = 0   → cancer (never send a sick patient home "clear")
F1        = 2·P·R/(P+R)    harmonic mean — the balanced default
```

**The sprint-vs-marathon rule:** both are "running," but you judge them differently — two
classifiers likewise need different metrics depending on which error is dangerous *in context*.

## Numpy twin

```python
tp, fp, fn, tn = 18, 18, 2, 162          # the SAME 200-cycle table from the Bayes atom!
acc  = (tp+tn)/(tp+tn+fp+fn)
prec = tp/(tp+fp); rec = tp/(tp+fn)
f1   = 2*prec*rec/(prec+rec)
print(f"accuracy {acc:.0%}  precision {prec:.0%}  recall {rec:.0%}  F1 {f1:.0%}")
# accuracy 90%  precision 50%  recall 90%  F1 64%
# ← 90% accurate, yet HALF its alarms are false — accuracy hid what precision exposed
```

## Where it came from / where it goes

builds-on:: [[bayes]] — the confusion matrix IS the 200-cycle table; precision = the posterior P(Real|HOT); imbalanced classes = the base-rate trap wearing a metrics hat
feeds:: [[cross-validation]] — CV averages one of these across folds; pick WHICH one before you tune
feeds:: threshold-setting on [[regression|logistic]] outputs — moving the 0.5 cut trades FP for FN along the same four cells
contrasts-with:: accuracy alone — 90% accuracy sounded great until precision said "coin flip"
scroll:: [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]] — §15–§16 (S64–66)

## Decision boundary

- ✅ **Recall** when a miss is catastrophic (cancer, incoming missile, thermal runaway).
- ✅ **Precision** when a false alarm is catastrophic (firing on civilian aircraft; throttling a healthy drive into a perf SLA breach).
- ✅ **F1** when both matter and classes are imbalanced.
- ❌ **Accuracy on imbalanced data** — predict "no event" always on a 1% base rate and score 99%.
- Closing rule from the professor: the LOSS you optimize must be consistent with the metric you care about.

## Depth layers

- **2026-06-27 (s1):** naming rule hand-decoded, the three case studies polled live, precision/recall knob-mapping. → [[2026-06-27_jun20-intro-to-ml-ppt-notes_s1]]

## Project brick

**The thermal classifier's metric decision is a real design choice:** miss a real thermal event
(FN) → cook the NAND; false-alarm (FP) → throttle a healthy drive and blow the latency SLA.
Enterprise storage usually prices the FN higher → weight recall — but the anchor's 50% precision
says exactly how many angry perf tickets that buys.

## Flashcards

#flashcards/metrics

Decode "False Negative" using the naming rule. :: Second word = model said NEGATIVE; first word = that was FALSE (wrong). So reality was positive and the model missed it — the Type 2 error, the cancer-case killer.
Your 200-cycle sensor: accuracy 90%, precision 50%. Which number do you show the boss, and why? :: Both — accuracy hides that HALF the alarms are false (base-rate trap); precision exposes it. Imbalanced classes make accuracy a liar.
Which metric hits 100% exactly when FP = 0, and which domain demands it? :: Precision — the anti-missile case: never fire on a civilian aircraft.
