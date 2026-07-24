---
title: Module 2 battle plan — IIT KGP + CampusX unified (Jul 25 → Aug 23)
date: 2026-07-25
sessions: [s7, s8, s9, s10, s11, s12]
concepts: [neural-nets]
type: plan
recap: 30 days, three sources, one machine — CampusX pre-teaches each Saturday, PyTorch builds the R2 forecaster, every week ends in a deliverable + teach-back.
up: "[[MOC-m2-deep-learning]]"
---

# 🗺️ Module 2 battle plan — 30 days (Jul 25 → Aug 23)

> **The one sentence:** unite IIT KGP (Saturdays) + CampusX 100-Days (concepts) + CampusX PyTorch
> (practice) into ONE schedule, so that by **Aug 23** a working **PyTorch MLP→LSTM thermal
> forecaster (R2)** exists — the resume-grade artifact.

**Sources (all local, nothing to buy):**
- IIT KGP sessions s7–s12 — Saturdays, the certifying course
- `CampusX/Deep_Learning/100_days_DL_book.pdf` (1,125 pp) — concept depth, read AFTER each video
- `CampusX/Deep_Learning/PyTorch_Complete_Course_CampusX_OCR%20%281%29.pdf` (304 pp) — the job stack

**The operating rule — a concept is DONE only when:**
1. rebuilt in a PyTorch/numpy cell (predict-before-run),
2. its Obsidian atom exists,
3. it survives a Friday voice teach-back.
Videos alone count as **zero**.

---

## Week-by-week

### Week 1 · Jul 25–31 — the neuron learns · [s7 today]
- [ ] CampusX: Perceptron block (perceptron, trick, loss fn, problem-with-perceptron) — book Part II
- [ ] CampusX: MLP block (notation, intuition, forward prop) — book Part III
- [ ] CampusX: Backprop Part 1/2/3 + loss functions — book Part V ⭐⭐⭐
- [ ] PyTorch lessons 1–4: Intro · Tensors · Autograd · Training Pipeline
- [ ] **DELIVERABLE:** capstone `temp = w·load + b` retrained in raw PyTorch autograd →
      `labs/2026-07-25_pytorch-week1.ipynb` — must converge to **w≈15, b≈25** on `[1,2,3]→[40,55,70]`,
      the exact hand-built numbers. Proof both layers agree.
- [ ] 30-min recall sprint: overdue foundation rows (probability, bayes, vectors, EV, calculus) —
      backprop needs the chain rule HOT
- [ ] Fri voice teach-back: backprop in NVMe terms + artifacts (atoms: perceptron, backprop)

### Week 2 · Aug 1–7 — training that actually works · [s8 Aug 1]
- [ ] CampusX: GD variants (batch/SGD/mini-batch), vanishing/exploding gradients — book Part VI
- [ ] CampusX: activations (sigmoid/tanh/ReLU + variants), weight init (Xavier/He) — book Part VII
- [ ] CampusX: dropout, L2/regularization, early stopping, scaling, batch-norm — book Part VII ⭐⭐⭐
- [ ] PyTorch lessons 5–7: nn.Module · Dataset & DataLoader · Building an ANN
- [ ] **DELIVERABLE:** MLP classifier *"throttle in next N s?"* on R0/R1 telemetry, fed via DataLoader
- [ ] Fri teach-back + atoms (activation-functions, optimizers, regularization)

### Week 3 · Aug 8–14 — budget week · [s9 CNN Aug 8]
- [ ] CampusX CNN block — ⭐ **exam-level pass ONLY** (convolution = FIR filter; off project path)
- [ ] PyTorch lessons 8–10: GPU training · Optimizing the NN · Optuna tuning
- [ ] **DELIVERABLE:** MLP temperature **regressor** on telemetry + Optuna tuning → **R2 part 1**
- [ ] Fri teach-back + atom (cnn — recognition level)

### Week 4 · Aug 15–21 — memory · [s10 RNN Aug 16]
- [ ] CampusX: RNN, backprop-through-time, **LSTM/GRU** ⭐⭐⭐ (the forecaster family)
- [ ] PyTorch lessons 13–14: RNN mechanism · **LSTM**
- [ ] **DELIVERABLE:** LSTM transient forecaster v0 on telemetry windows → **R2 part 2**
- [ ] Fri teach-back + atoms (rnn-lstm)

### Week 5 · Aug 22–23 — close the module · [s11 deploy Aug 22 · s12 doubts Aug 23]
- [ ] s11: transfer learning & deployment — first real Edge-AI session; INT8 *awareness* read
- [ ] **DELIVERABLE:** benchmark MLP vs LSTM (MAE · params · latency) + R2 summary write-up
- [ ] Module-boundary ritual: consolidated doc, next rung, queue INT8 hands-on for s20

**Skipped on purpose (no guilt):** book Part IV Keras projects (Keras ≠ our stack), PyTorch
lessons 11–12 (CNN/transfer — image-domain, off the R2 path). Revisit only if a session demands.

---

## The weekly rhythm (8–12 h)

```
Mon–Thu  ~1.5h  2–3 videos → book chapter AFTER (revision, not substitute) → 1 predict-before-run cell
Fri      ~1h    PyTorch lesson + VOICE teach-back  (doubles as Saturday primer)
Sat             IIT KGP class — confirmation, not first contact · due recall cards
Sun      ~2h    WEEK DELIVERABLE + artifact routine (atoms → scroll → ledger → hub → commit)
Tue+Thu  10min  recall-ledger due cards
```

## s7 — the 3 questions to hold in today's lecture

1. Where exactly does the **non-linearity** enter — and what does a 10-layer net collapse into without it?
2. What is backprop computing for each weight, and how is it **just the chain rule** I already own?
3. A neuron is logistic regression with one extra thing — **what's the extra thing?**

## Notes → HTML pipeline (per week, not per video)

Atom per concept (anchor numbers · twin · decision boundary · project brick) → scroll per week →
**one HTML teaching page per week built FROM the atoms** → ledger rows → `atlas_audit.py` clean →
`build_hub.py` → commit.

---

# 🤖 OPERATOR MANUAL — instructions for ANY assistant driving this plan

> **Purpose of this section:** the learner may open a future session with a smaller model and zero
> conversation history. Everything needed to guide him is written HERE, explicitly. Follow it
> literally; do not improvise the system.

## Who the learner is (5 lines)

- SSD-firmware engineer (Samsung), thinks in C/registers/NVMe; **not** yet fluent in math — intuition
  before symbols, always.
- Taking IIT KGP+upGrad AI course; Saturdays are class days. This doc covers Module 2 (Jul 25–Aug 23).
- Goal: edge-AI engineer. Flagship project: **R2 = PyTorch MLP→LSTM thermal forecaster** on SSD
  telemetry (see `docs/2026-07-04_thermal-ml-project-map_F.md`).
- Teaching style he needs: funny example first, then NVMe-level analogy (NVMe queues/commands/latency
  ONLY — never NAND/ECC/wear-leveling internals), tiny hand-computable numbers, then formula, then C view.
- He answers teach-backs by voice; make him PRODUCE answers, never accept "I understood it."

## The daily loop (Mon–Thu) — run these steps in order

1. Ask: "which CampusX videos did you watch since last time, and what did you learn?" (He reports;
   you probe — 1–2 retrieval questions per concept. Wrong-tool questions are best.)
2. Check this doc's current week checklist; tick items he completed (edit this file, `- [ ]` → `- [x]`).
3. Have him run ONE predict-before-run cell in the week's `labs/` notebook: he states the expected
   output aloud/typed BEFORE running. If prediction wrong → that's the day's re-teach target.
4. If a NEW concept was learned: create/extend its atom in `docs/concepts/<slug>.md` (follow
   `.claude/skills/obsidian-notes/SKILL.md`), add a node to `tools/web.json` (lane `"m2"`), and add a
   recall-ledger row (see template below).
5. End with tomorrow's 3-video assignment from the current week's block.

## Friday loop

1. Voice teach-back of the week's ⭐⭐⭐ concept. PASS = he can state intuition + the anchor numbers +
   one "when NOT to use it". FAIL = re-ground only the broken link, retest Monday.
2. Preview tomorrow's IIT KGP session (per the table above) + give 3 questions to hold in lecture.

## Sunday loop (deliverable day)

1. Build the week's DELIVERABLE (listed per week above) in `labs/`.
2. Artifact routine, exact commands from repo root:
   ```
   python3 tools/atlas_audit.py        # must print clean; fix problems before proceeding
   python3 tools/build_hub.py          # regenerates /index.html
   git add -A && git commit -m "M2 week N: <what>" && git push
   ```
3. Update every touched recall-ledger row (advance/drop the ladder step).

## Recall-ledger row template (append to the table in `docs/recall-ledger.md`)

```
| [[<slug>\|<Display name>]] | `docs/concepts/<slug>.md`, labs notebook | <learn-date> | <learn-date> (first contact — <one line of what he built>) | +1d | <learn-date +1> |
```

Ladder: learn → +1d → +3d → +7d → +16d → +35d → +60d → graduated. Pass = advance. Stumble = drop one.

## Week-1 deliverable — exact spec (verified numbers)

Notebook `labs/2026-07-25_pytorch-week1.ipynb`. Data: `X=[1,2,3]`, `Y=[40,55,70]` (the hand-built
capstone's exact numbers, from `html/2026-07-14_gradient-descent-thermal-capstone_F.html`).
Model `temp = w·load + b`, MSE loss, lr=0.1. **Must converge: ~(15.08, 24.81) by iter 180, exactly
(15.0, 25.0) by iter 500.** If his run matches these, both his hand-math layer and the autograd layer
agree — that is the point of the exercise. Divergence demo: lr≥0.67 explodes (his capstone's
"fix becomes the failure" story; the 2/n=2/3 factor makes the threshold 3× the HTML page's 0.21).

## Decision rules when things slip

- Behind schedule → drop in THIS order: Keras content (already skipped) → CNN depth (Week 3) →
  Optuna → never drop backprop/optimizers/LSTM (project-critical path).
- He reports a concept "done" from video alone → NOT done; require the cell + atom + teach-back.
- He drifts to video-making/LinkedIn content → redirect to study; content is backlog (standing rule).
- A misconception surfaces → log it in `docs/trap-log.md` with a `^block-id`, embed from the atom.

## Where everything lives

| Thing | Path |
|---|---|
| This plan/tracker | `docs/2026-07-25_campusx-m2-plan.md` (tick the boxes!) |
| Concept notes (atoms) | `docs/concepts/<slug>.md` |
| Weekly notebooks | `labs/2026-07-25_pytorch-week1.ipynb`, then per week |
| Concept graph | `tools/web.json` (slugs immutable; lane `m2`) |
| Recall ledger / trap log | `docs/recall-ledger.md` · `docs/trap-log.md` |
| CampusX books | `CampusX/Deep_Learning/*.pdf` |
| Project map (R2 spec) | `docs/2026-07-04_thermal-ml-project-map_F.md` §2 |
| Vault/note rules | `.claude/skills/obsidian-notes/SKILL.md` |
| Tutor protocol | `~/.claude/skills/ai-embedded-tutor/SKILL.md` |
