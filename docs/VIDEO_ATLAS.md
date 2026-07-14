---
title: 🎬 VIDEO ATLAS — the learning-to-teaching content system
date: 2026-07-11
type: map
recap: "The zoomed-out channel story, six seasons mapped to course modules, the video-ready rubric, the scored candidate slate, and the per-video pipeline. Claude curates; you approve, voice, and face."
up: "[[HOME]]"
---

# 🎬 VIDEO ATLAS — from a straight line to a drive that manages itself

> **The one-breath story the whole channel tells:**
> *"A Samsung SSD-firmware engineer teaches himself AI — from a straight line to a drive that manages itself."*
> Every video is one brick. Every video ends with the **Atlas beat**: the same map, one more node lit.
> Finale: **Jan 2027 — the capstone film: ML running inside the SSD controller (R6).**

## 0 · Operating agreement (who does what)

- **Claude curates.** Any session touching `AI_Training/` scans `html/` + `docs/` (HUB JSON + frontmatter), scores new artifacts on the rubric below, and *prompts you*: "X is video-ready → proposed title, hook, season slot."
- **You approve, then record** (voice per timed script, 10-s face hook + 8-s outro PiP, music per design map).
- **Claude builds everything else**: schematic → Manim scenes (validated skill) → animatic → final render → Short cut spec → carousel prompts → Atlas node update in this file.
- Cadence is **readiness-driven, not calendar-driven** — a video ships when a note passes the rubric, not because a week elapsed. (Exam weeks Sep 20 / Jan 10: no builds.)

## 1 · The video-ready rubric (all five = green light)

| # | Gate | Why it exists |
|---|---|---|
| ① | **Field-tested** — taught to your friend (or in a live session) and it landed | pedagogy proven before production |
| ② | **Universal analogy** — staircase/checkout-lane class, no fandom, no SSD-required | reaches strangers, not just engineers |
| ③ | **Numbers-in-motion story** — something must MOVE to explain it | if it's only text, it's a carousel, not a video |
| ④ | **Atlas slot** — advances the season arc; the map gains a node | serialization = binge + subscribe |
| ⑤ | **Trap/payoff beat** — a misconception from [[trap-log]] to spring | the hook writes itself |

## 2 · The six seasons (course modules → story arcs)

| Season | Window | Arc | Anchor build-log |
|---|---|---|---|
| **S1 · The Math That Moves Machines** | now – Jul | line → slope → derivative → gradient → GD · vectors/dot · σ/bell · covariance → eigen → PCA · Bayes · entropy/EV | — |
| **S2 · Machines That Learn** | M1, – Jul 19 | CV & metrics · regression · trees/SVM · ensembles · k-means/PCA | **BL#1** — R1 first throttle predictor (~Jul 18) |
| **S3 · Deep Learning** | M2, Jul 25–Aug 23 | neuron = dot product · backprop · optimizers · CNN · RNN | **BL#2** — R2 LSTM forecaster + INT8 on dev board |
| **S4 · Language & Attention** | M3, Aug 29–Sep 20 | tokens · attention · Transformer variants | — (exam Sep 20) |
| **S5 · The LLM Era** | M4, Sep 26–Nov 1 | GenAI · LLM archs · LoRA/QLoRA · multimodal · alignment | **BL#3** — R4 quantization deep-dive (public write-up) |
| **S6 · Systems That Think** | M5–M6, Nov–Jan | RAG · agents · MLOps | **CAPSTONE FILM** — R6, the finale |

**Pillars (only four, per retention research):** ① math-in-motion explainers ② ML-concept explainers ③ SSD×AI build-logs ④ Shorts. Same structure inside each pillar every time — familiar segments retain.

## 3 · Candidate slate — scored 2026-07-11

**GREEN (production-ready or one step away):**

| # | Video | Source | Rubric | Note |
|---|---|---|---|---|
| 1 | ✅ **Lines READ. Curves DERIVE.** | line-vs-curve HTML | ①②③④⑤ | SHIPPED — video 1 |
| 2 | **Gradient Descent: the bowl** | ✅ HTML BUILT `html/2026-07-14_gradient-descent-thermal-capstone_F.html`; docs: derivative-limit-to-GD, line-to-gradient-thermal-fit | ①②③④⑤ | HTML done 2026-07-14: temp=w·load+b — 3 objects, bowl, hand-step, live scrubber 0→180 converging onto target (15,25), η-divergence + threshold. Ready to schematic → carousel Post 11 + video 2. |
| 3 | **PCA: 20 sensors → 3 numbers** | pca-20-sensors HTML | ②③④⑤ (① self-tested) | Banger title; 11-step story; scree keep/drop; "when PCA betrays you" = trap. Ready to schematic TODAY. |
| 4 | **The bell curve & σ** | bell-curve-sigma + normal_distribution HTMLs (merge) | ②③④⑤ | σ-slider bends the bell; 68-95-99.7; latency grounding as a case study, not the analogy. |
| 5 | **Eigen, fully by hand** | eigen-by-hand + covariance-eigen-capstone HTMLs | ②③④⑤ | 2×2 vs 3×3 in parallel; the stretch IS the motion story. Feeds #3 — release BEFORE PCA if sequencing strictly. |
| 6 | **Vectors, dot & cosine** | vectors-dot-cosine HTML | ②③④⑤ | Drag-B playground → motion; sets up "the same sum-of-products everywhere" (dot = EV = neuron) — the S3 bridge. |
| 7 | **Why one split lies** | cross-validation HTML | ②③④⑤ | k-fold rotation animation; skeptical hook ("your model aced a test it wrote itself"). |
| 8 | **Bayes with buckets** | bayes-taxonomy HTML | ②③④⑤ | Bucket-counting Bayes — no formula until the end. |
| 9 | **BL#1: Teaching my SSD to fear heat** | R0/R1 (thermal-project-map) | ④⑤ + demo footage | First build-log; record R1 work ~Jul 18. Different pillar, different structure (screen + face + plots). |

**YELLOW (not videos yet):**
- ✅ entropy / expected-value / info-gain — HTMLs BUILT 2026-07-13 (`html/2026-07-11_entropy-expected-value-info-gain_s4.html`, `html/2026-07-13_decision-tree-growing-iterations_s4.html`); now video-ready (EV→surprise→entropy→tree; ties to #6's dot-product thread). Promote to GREEN at next scoring.
- mcu-deployment flashcards — no motion story → carousel material
- linear-algebra-trainer-deck — a 14-chapter MINE for future videos, not one video
- rasengan theme mockup — meta, N/A

**Suggested S1 release order:** 1 ✅ → 2 (GD bowl) → 6 (vectors/dot) → 5 (eigen) → 3 (PCA) → 4 (bell) → 7 (CV) → 8 (Bayes) → BL#1 whenever R1 lands (interleave).

## 4 · Per-video pipeline (the proven loop)

1. Teaching HTML exists + friend-tested → rubric check
2. Claude: scene schematic (hook ≤5 s → preview ≤15 s → beats with pattern-interrupts every 30–60 s → trap → reveal → side-by-side → Atlas beat → outro)
3. Claude: Manim build via `manim-video-style` skill (-ql frame-verified loop → animatic to you → 1080p60)
4. You: narration (timed script provided) + 10-s face hook / 8-s outro clips + 4 music tracks (design map provided)
5. Claude: PiP composite, music cut/duck to hit-points, mux, SRT captions
6. Derivatives: 1 Short (the trap OR the reveal, 45–60 s vertical re-layout) + 1 LinkedIn carousel (Post-7 blueprint JSON) + Atlas node lit in §5
7. Publish: YouTube (video + Short), LinkedIn (carousel links video), title/thumbnail per pillar style

**Retention checkpoints (2026 research):** target 40–55 % avg-view for 5–15 min; review each video's retention curve before building the next — steep early drop = hook problem, mid-sag = pacing problem.

## 5 · The Atlas map (the serialization glue)

A single reusable end-scene (Manim, ~10 s): a constellation of nodes left→right through six season clusters on the dark brand background; shipped videos glow cyan, the current video's node pulses orange, unlit nodes stay faint. Same closing music sting every time. The map IS the channel trailer once all nodes are lit.

```
S1 ○─○─○─○─○─○─○─○   S2 ○─○─○─○─◆BL1   S3 ○─○─○─○─◆BL2   S4 ○─○─○   S5 ○─○─○─○─◆BL3   S6 ○─○─○─★CAPSTONE
   line GD vec eig PCA bell CV bayes
```

Nodes update in this file with each ship. Claude renders the updated AtlasBeat scene per video.

## 6 · Live status

- **Shipped:** #1 Lines READ. Curves DERIVE. (awaiting your voice/face/music for the full-audio master)
- **Next up (your pick):** #2 GD Bowl (do the owed teaching HTML first — two birds) **or** #3 PCA (schematic can start today)
- **Waiting on:** narration + clips + music for video 1 · R1 build (~Jul 18) for BL#1
