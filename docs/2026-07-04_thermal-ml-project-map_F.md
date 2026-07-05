---
title: Thermal-ML project map — the course, mapped onto MY rung-1 project
date: 2026-07-04
sessions: []
concepts: [thermal-project]
type: map
recap: The daily north-star. Dated readiness milestones (by DATE X, own skills Y) + every course concept mapped to a piece of the in-storage thermal-throttle ML project. Read the top strip before every session.
---

# 🎯 Thermal-ML Project Map — the course, assembling MY project

> **This is the daily compass.** Before any session, read §0 (where am I, what must I own by the next
> dated checkpoint) and find today's concept in §2 (which piece of the thermal project it builds).
> The abstract course becomes *"every module ships a part of the predictive-thermal-throttle engine
> I will put inside SSD firmware."* Grounded in `2026-07-04_ssd-thermal-ml-research.md` (40 papers).

---

## 0. ⭐ THE READINESS TIMELINE — future dates → skills I must have in hand

> Read this like a firmware release schedule: each date is a **gate**; by that gate these skills must
> be *owned* (not "seen"), and this project rung must be *buildable*. Check it daily. "We are HERE."

```
 ══ FOUNDATION ══════ M1 ════════════ M2 ═══════════ M3 ═════ M4 ═══════ M5 ════ M6 ══ 🏁
 Jun          ▲Jul 5           Jul25         Aug22       Sep      Oct10      Nov21    Jan10
              you are here
```

| Gate (date) | Course point | Skills I MUST own by then | Project rung ready | Prep status |
|---|---|---|---|---|
| **Jul 11** (s4) | Ensembles | shared math cluster — **chain rule · cross-entropy · MSE · gradient descent**; trees/entropy | R0: rule-based throttle **simulator** + synthetic telemetry (temp/IOPS/QD) — the baseline to beat | ⏳ in progress |
| **Jul 18** (s5, M1 end) | K-means & PCA | regression, trees, ensembles, **k-means, PCA** (own); sklearn fluency | **R1:** classical "throttle in next N s?" classifier + k-means data-hotness + PCA on 20 channels | ⬜ |
| **Jul 25** (s7, M2 start) | Neural nets | **dev board in hand** (order before this); perceptron→sigmoid, backprop = chain rule ×layers | — (buy + first-inference lab) | ⬜ |
| **Aug 22** (s11) | Transfer & deploy | **CNN, RNN/LSTM**, matmul-as-layers; INT8 quantization basics | **R2:** MLP→LSTM temperature **forecaster**, INT8-quantized, timed on the board | ⬜ |
| **Aug 29** (M2→M3) | — | tail-latency/p99 thinking applied to ML | **R3:** 18-gear granular control demo **vs** bang-bang baseline (jitter/p99 plots) | ⬜ |
| **Oct 10** (s20) | LoRA/QLoRA | **4–8-bit quantization deep** (PTQ vs QAT), model-size/latency budgeting | **R4:** quantization deep-dive + public write-up; MPC bridge reading | ⬜ |
| **Nov 21** (s24, M5) | RAG & vectors | embeddings, vector search, LLM-over-structured-data | **R5:** KORAL-style LLM+telemetry mini (fleet reasoning) | ⬜ |
| **Jan 10 2027** (🏁) | Course end | full loop: data→model→INT8→real-time/thermal budget | **R6 CAPSTONE:** thermal predictor architected for SSD-controller constraints — portfolio + resume line | ⬜ |

**The one sentence to say daily:** *"I am at `<gate>`; to be ready for `<next date>` I must own
`<skills>`, and today's concept is a brick in `<project rung>`."*

---

## 1. The problem — in MY language (why this project exists)

Today's firmware ships **reactive bang-bang throttling** — hard temperature gates:

```
   temp ──►  85°C → Level-1 (clock down a bit)
             95°C → Level-2 (slash R/W 20–30%: 2.0 → 1.5 GB/s)
            100°C → emergency shutdown
```

What it costs (I live these):
- **Latency jitter / QoS blown** — a 5 s op spikes to 20 s mid-throttle → cascading pipeline stalls.
- **One hotspot throttles the whole drive** — up to **15°C chip-to-chip** delta, yet a single hot NAND
  package triggers a *global* throttle, starving cool parallel chips.
- **Thermal cycling** — the heat→throttle→cool swing fatigues solder joints, shortening device life.

**The ML shift:** stop reacting, start **forecasting** — predict the thermal trajectory and taper
*smoothly* across ~18 gears *before* the gate is hit. That predictor is R1–R6 above.

---

## 2. ⭐ Every course concept → its piece of the thermal project

> This is the map to consult when a session starts: *what part of the engine am I building today?*

| Course concept (session) | Owns which project piece | Research anchor |
|---|---|---|
| **Linear/logistic regression** (s2) | the **baseline** throttle predictor: `P(throttle in next N s)` | — |
| **Decision trees / SVM** (s3) | non-linear throttle rules; margin = thermal guard-band | — |
| **Ensembles / boosting** (s4) | ⭐ **XGBoost = the exact thermal-forecaster family** in the papers | refs 19, 25, 27 |
| **K-means** (s5) | **data-hotness clustering** → group same-frequency data, cut write-amp heat | HAML-SSD (ref 5) |
| **PCA** (s5) | compress **20 telemetry channels → 3** for a controller-sized model | — |
| **Neural nets / backprop** (s7) | the MLP temperature predictor; backprop trains it | ref 21 |
| **Optimizers / regularization** (s8) | stable training; L1 = smaller (fewer-weight) on-controller model | — |
| **CNNs** (s9) | spatial thermal-map reasoning across the PCB (stretch) | ref 19 |
| **RNN / LSTM** (s10) | ⭐ **LSTM transient forecaster** — "heat now → die-temp in 10 s" | refs 25, 27 |
| **Transfer & deployment** (s11) | **INT8 quantize + run on constrained silicon** — the whole point | ref 21 |
| **LoRA / QLoRA** (s20) | 4–8-bit quantized weights, NPU-style; DPB-stabilized in V-NAND | refs 21, 22 |
| **RAG / vector search** (s24) | **KORAL**: LLM reasoning over telemetry knowledge-graph, fleet-scale | KORAL (ref 38) |
| **Agents / MLOps** (s29–31) | DRL channel/GC scheduler (research-stage); drift monitoring in the field | refs 20, 21 |

**Beyond the course (bridges from what I already know):**
- **MPC** (Model Predictive Control) — a step up from the PID/bang-bang I already ship; forecasts over
  a horizon, solves for optimal IOPS. Bridge reading after s8. (ref 17)
- **Waltz** — cross-layer: offload compression host↔drive by thermal telemetry (391%/627% throughput).
  Systems reading, M2+. (arXiv 2509.05365)

---

## 3. Numbers-as-anchors (the hard figures — interview ammunition)

| Anchor | Value | Source |
|---|---|---|
| Throttle gates | 85 / 95 / 100 °C (L1 / L2 / shutdown) | ref 8 |
| Temp rise rate under load | up to **12 °C/hour** | ref 8 |
| NAND lifespan decay at 85°C | **5× faster**; leakage +300% at extremes | ref 8 |
| Chip-to-chip delta in one drive | up to **15 °C** | ref 19 |
| L2 throttle throughput hit | **20–30%** (2.0 → 1.5 GB/s) | ref 18 |
| Granular gears (vs 2–3 stages) | up to **18** | ref 11 (AceTT) |
| CSD overheats to shutdown | **~8 min** of heavy compressible load | Waltz (34) |
| Waltz gains | **+391.5%** write / **+627%** read throughput | Waltz (34) |
| DPB weight stabilization | **+10.5 pp** NN accuracy in hot V-NAND | ref 22 |
| Self-healing (heat-accelerated trap recovery) | **~10× lifetime** | ref 19 |

---

## 4. Reading ladder — WHICH paper, WHEN (one per checkpoint, never a pile)

- **Now (skim):** *Toward Smarter SSDs* survey (ref 3) — the landscape.
- **After s4:** *SSD Thermal Throttling Prediction / Fast Prediction Model* (refs 19, 27) — the forecaster.
- **M2 (Aug):** *Waltz* (arXiv 2509.05365) — cross-layer thermal cooperation.
- **After s8:** *Thermal Throttling by MPC in Flash Memory* (ref 17) — the control bridge.
- **M5 (Nov):** *KORAL* (arXiv 2602.10246) — LLM+KG fleet reasoning.

---

## 5. Decision boundary — what rung-1 IS and is NOT

- ✅ **IS:** a *supervised* model that reads telemetry (temp, IOPS, queue-depth, P/E counts) and
  **predicts** an imminent throttle / future die-temp, so firmware tapers early. Trainable on
  synthetic or bench logs, laptop-first, deployable INT8.
- ❌ **IS NOT (yet):** a deep-RL agent rewriting GC/channel policy inside live firmware. That's
  research-stage (refs 20, 21) — a Module-6+ stretch, not the first build.

## 6. Honest caveats (so I don't over-claim)

- The research doc is a **synthesized survey** — some numbers are vendor-flavored; a few claims are
  breathless. **Verify a primary source before quoting** in interviews or a write-up.
- DRL-in-firmware and self-healing NAND are **frontier**, not shipping product — inspiring direction,
  not the near-term deliverable. The practical order is **predict first, control later** — which is
  exactly the order the course teaches. Good.

---

**🎯 The thread:** the course is not 32 disconnected classes — it is the **parts list for one engine**
I already have the hardware intuition to build. Every session, ask: *which brick, which gate, how
long until I can build the next rung?*
