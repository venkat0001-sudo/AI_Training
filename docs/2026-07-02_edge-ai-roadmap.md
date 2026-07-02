# Edge-AI Roadmap — from SSD-firmware engineer to exceptional Edge-AI engineer

> The north star doc. Goal → what the market wants → the unfair advantage → skill stack → project
> ladder tied to course modules. Drafted 2026-07-02 from live research; revisit ~quarterly (market
> moves fast).

---

## 1. The goal, stated precisely

**Become an exceptional Edge-AI engineer — one who designs, trains, compresses, and ships ML models
onto constrained hardware — with a specialization nobody can copy cheaply: AI inside storage
firmware.** Not "knows some AI." The bar: could own the full loop — data → model → quantized INT8
deployment → running under real-time/power/thermal budgets — on silicon he also understands at the
register level.

Why the goal matters: it sets learning depth. Concepts on the *deployment-critical path*
(quantization, model size, inference math, anomaly/OOD detection, time-series) get mastered;
concepts off-path (e.g. giant-scale distributed training) get recognition-level only.

---

## 2. What the market says (researched 2026-07)

- **Growth:** Edge-AI market growing at **30%+ CAGR toward 2030**; deployment-to-edge skills flagged
  as rising demand beyond 2026. Driven by IoT, autonomy, privacy, latency, and on-device LLMs.
- **The skills job posts actually name:** TensorFlow Lite (LiteRT) / TFLite-Micro, Edge Impulse,
  **embedded C/C++** (his native tongue!), Python for training, **quantization + pruning**, model
  optimization under memory/power budgets.
- **Salary signal (US bands):** ~$100–160k junior → $170–240k mid → **$250–350k senior** — edge-AI
  seniority pays because the intersection (ML *and* embedded) is rare.
- **Hiring industries:** automotive, healthcare, manufacturing/industrial IoT, consumer devices.
- **The rare-profile insight:** most candidates come from the ML side and can't do embedded;
  he comes from embedded and is adding ML. That direction is the scarcer, more valuable one.

---

## 3. The unfair advantage (storage × AI is a real, active field)

Live evidence that his exact home turf is an AI frontier:

- **ML-based SSD failure prediction** is an active research + production area: SMART-data models,
  multi-view/multidimensional feature models (FAST '23, IEEE), cloud-scale collaborative prediction.
- **Patents exist for firmware-level ML failure prediction** — ML modules running *inside the
  device*, combining block-level + device-level signals. This is literally "his job + this course."
- **SSD thermal management via ML** is called out as the field's most promising direction:
  closed-loop systems integrating sensors + algorithms + firmware, analyzing workload patterns to
  **preemptively throttle/cool** — which IS his planned capstone project.
- Datasets to practice on exist publicly (e.g. Backblaze drive-stats SMART data).

**Positioning statement (the resume line to grow into):** *"I put ML inside the SSD controller —
predictive thermal management and failure prediction running in firmware under real-time budgets."*

---

## 4. The skill stack (tiered)

| Tier | Skills | Status / source |
|---|---|---|
| **Already his** | Embedded C/C++, ARM multi-core, real-time constraints, power/thermal control loops, NVMe/PCIe, telemetry | 6 yrs on the job — the moat |
| **Course delivers** | Math foundations, classic ML, deep learning, CNNs/RNNs, deployment (Sess 11), quantization/LoRA (Sess 20), MLOps (Sess 31) | IIT KGP course, May 26–Jan 27 |
| **Add alongside course** | TFLite-Micro / LiteRT, Edge Impulse workflow, INT8 quantization hands-on (PTQ→QAT), CMSIS-NN awareness | Project ladder below |
| **Differentiators (later)** | ExecuTorch/ONNX Runtime, edge LLM runtimes (llama.cpp-class), NPU toolchains, time-series forecasting at the edge, OOD/anomaly detection discipline | Post-Module-2, as projects demand |

---

## 5. The project ladder (each rung unlocked by a course module)

```
Rung 0  NOW           → notebook fluency: NumPy pipelines (done: covariance→eigen→PCA capstone)
Rung 1  after Sess 2-3 → SMART-data failure prediction, classic ML (logistic regression / tree)
        (Jul 2026)       on the Backblaze public dataset — HIS domain, laptop-only, no hardware
Rung 2  after Sess 5   → PCA + anomaly detection on SSD telemetry (synthetic or bench logs):
        (Jul 2026)       20-channel → 3-feature pipeline he already built, now productionized
Rung 3  after Sess 7-8 → first neural net: thermal time-series → throttle-event predictor (Python)
        (Aug 2026)
Rung 4  after Sess 11  → DEPLOY IT: quantize to INT8, run on a Cortex-M dev board (TFLite-Micro
        (Aug 2026)       or Edge Impulse); classic starter alternatives: keyword spotting /
                         gesture recognition / anomaly detection on ESP32 or Arduino BLE33
Rung 5  Module 4-5     → compress smarter (QLoRA ideas), evaluate properly, drift monitoring
        (Oct-Dec 2026)
Rung 6  CAPSTONE       → predictive thermal-throttle model architected for SSD-controller
        (Jan 2027 →)     constraints (SRAM-size model, deterministic latency, INT8) — the
                         portfolio centerpiece + the work story
```

Free structured back-up tracks: HarvardX TinyML (edX), Edge Impulse university courseware (GitHub),
MLSysBook (Harvard's ML-systems textbook), awesome-tinyml list.

---

## 6. How this changes day-to-day learning

- Every concept gets the question: **"what does this cost on-device?"** (RAM, MACs, latency, power).
- Math on the deployment path (linear algebra, quantization statistics, time-series, probability
  fences) = **mastery depth**; everything else = recognition depth.
- Projects > certificates. The ladder above produces artifacts; the repo is the portfolio.
- Revisit this doc quarterly; the edge-LLM/NPU corner of the market is moving fastest.

---

**Sources:**
- [Edge AI Engineer Job Description: Key Roles & Skills (upGrad)](https://www.upgrad.com/blog/edge-ai-engineer-job-description/)
- [Top 10 Most In-Demand AI Engineering Skills and Salary Ranges in 2026 (Second Talent)](https://www.secondtalent.com/resources/most-in-demand-ai-engineering-skills-and-salary-ranges/)
- [AI/ML Engineering Jobs in 2026: Analyzing 10,000+ Posts (Axial Search)](https://axialsearch.com/insights/ai-ml-engineering-jobs/)
- [Edge Impulse embedded-ML courseware (GitHub)](https://github.com/edgeimpulse/courseware-embedded-machine-learning)
- [TinyMLedu free courses (Harvard)](http://tinyml.seas.harvard.edu/courses/)
- [ML Systems book — TinyML blueprint](https://mlsysbook.ai/instructors/tinyml-syllabus.html)
- [awesome-tinyml curated list (GitHub)](https://github.com/gauravfs-14/awesome-tinyml)
- [Multi-view Feature-based SSD Failure Prediction (USENIX FAST '23)](https://www.usenix.org/system/files/fast23-zhang-yuqi.pdf)
- [Multidimensional Features Helping Predict Failures in Production SSDs (IEEE)](https://ieeexplore.ieee.org/document/10137082/)
- [Industrial-Grade SSD Thermal Management: Status & Future (YANSEN)](https://www.yansen-ssd.com/blog/industrial-grade-ssd-thermal-management-current-status-challenges-and-future-evolution)
- [Firmware failure-prediction patent (USPTO)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11994934)
