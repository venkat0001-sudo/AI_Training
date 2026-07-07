---
title: MCU deployment — what survives on a microcontroller
aliases: [edge-deployment, on-device, tinyml, sram-budget]
date: 2026-06-26
sessions: [s1]
lane: m1
edge: 3
status: due
type: concept
tags: [incomplete]
up: "[[MOC-m1-ml-fundamentals]]"
recap: "The deployment gate every model must pass: does it fit SRAM, run inside the deadline, survive fixed-point? Decision-tree geometry (axis-aligned cuts) is MCU-native. STUB — anchors live in the flashcard deck; a written atom-grade treatment is owed."
---

# MCU deployment — what survives on a microcontroller

> **Recap:** The deployment gate every model must pass: **does it fit SRAM, run inside the
> deadline, survive fixed-point?** Decision-tree geometry (axis-aligned cuts) is MCU-native.
> STUB — a written atom-grade treatment is owed.

> [!warning] ⚠️ STUB atom — learned 2026-06-26 via the flashcard deck; no markdown scroll exists.
> Owed: the written treatment (SRAM/flash/MACs budget table, INT8 quantization bridge, tree-vs-net
> inference cost numbers) — natural slot: alongside s5 [[pca]] (compression) or M2 deployment (s11).

**Chain:** [[ml-taxonomy]] (classic = SRAM-sized) ──► **MCU deployment** ──► the [[thermal-project]] gate ──► TinyML (post-M1: Warden book, dev board)

## What is owned so far

- **The gate questions:** RAM/flash footprint? real-time deadline? fixed-point-safe? explainable to a firmware reviewer?
- **Decision-tree geometry:** a trained tree = axis-aligned cuts = nested compares — no multiplies, MCU-native inference.
- [[pca]]'s whole edge-value: fewer features = fewer MACs = less SRAM = lower power.

## Where it came from / where it goes

builds-on:: [[ml-taxonomy]] — the classic-vs-deep cost line IS this gate
feeds:: [[thermal-project]] — every rung must pass through it
twin-page:: [MCU deployment flashcards](../html/2026-06-26_mcu-deployment-flashcards_s1.html)

## 📋 Still owed

- [ ] Written treatment with budget numbers (SRAM/flash/MACs per model family)
- [ ] INT8/fixed-point quantization bridge (his Q-format home turf)
- [ ] Then clear `tags: [incomplete]`

## Flashcards

#flashcards/mcu-deployment

Why is a decision tree the most MCU-native model? :: Inference = nested axis-aligned compares — no multiplies, no float, tiny code; a trained tree is firmware whose constants were learned.
Name the four gate questions for any on-device model. :: Fits SRAM/flash? Meets the real-time deadline? Survives fixed-point? Explainable to the reviewer?
