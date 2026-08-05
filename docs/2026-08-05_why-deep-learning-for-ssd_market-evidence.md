---
title: Why deep learning (not just LLMs) for SSD firmware — the 2026 market evidence
date: 2026-08-05
sessions: []
concepts: [thermal-project, mcu-deployment]
type: research
recap: Neural nets are already shipping INSIDE SSD controllers (Marvell+NVDLA, ANN co-processors for wearout/QoS). LLMs can't fit on the controller; a small MLP/LSTM can. The intersection is the moat.
up: "[[MOC-thermal-project]]"
---

# Why deep learning for SSD firmware — the motivation, with receipts

> **Read this whenever the "why am I doing this?" fog rolls in.** Written 2026-08-05, mid-Module-2,
> six CampusX videos deep, when the notation started feeling like alphabet soup.

---

## 1 · Why not skip straight to LLMs?

**① LLMs are BUILT from what Module 2 teaches.** A transformer is matrix-multiply → activation →
[[calculus|backprop]]. Nothing else. Skipping ahead means learning *API calls*, not the machine.
Prompt engineers are a commodity; people who can modify a model are not.

**② An LLM will never fit in an SSD controller.** Controller SRAM is hundreds of KB; the smallest
useful LLM is ~1 GB. What actually runs on his silicon is a small MLP/LSTM — exactly Module 2.
LLM-only work makes you a *user* of somebody's cloud endpoint; DL makes you the person who puts
intelligence **inside the device**. See [[mcu-deployment]].

**③ The moat is the intersection.** Thousands can call an OpenAI endpoint. The set of people who
own *both* backprop *and* NAND read-retry timing is tiny. That intersection is where 6 years of
firmware becomes an unfair advantage — going LLM-only throws the moat away.

---

## 2 · What is actually shipping (2026) — not speculation

**Neural accelerators are already IN controllers**
- **Marvell integrates NVIDIA's NVDLA** (Deep Learning Accelerator) into data-center and client SSD
  controllers — ML inference on-drive, no host CPU, minimal network bandwidth.
- Published designs put an **ANN accelerator as a programmable co-processor in the SSD SoC**, used to
  *measure wearout*, *drive error-recovery decisions*, and *hold down QoS*. Neural-net-inside-firmware,
  in real silicon.

**His exact project category is a live, patented field** — this is the important one for
[[thermal-project|R2]]:
- ML framework for **NAND flash lifetime extension** (research)
- **US patent 11934696: "Machine learning assisted quality of service (QoS) for SSDs"**
- Published work on **AI-powered SSD firmware optimizing write amplification**

→ The R2 thermal/QoS forecaster is not a toy exercise; it sits inside a domain that is *patenting
and shipping right now*.

**The industry pivot is enormous**
- **NVIDIA + SK hynix "Storage Next"** — an AI SSD targeting **100M IOPS**, reframing flash as an
  *inference-optimized layer*; prototype due end-2026
- **Samsung PM1763** (his employer) — PCIe 6.0, 4 nm controller, mass production, AI-infrastructure targeted
- **SK hynix IMTE** tiering claims **+35.7 % inference efficiency**; FMS/CFMS 2026 agendas dominated
  by AI-inference SSDs

**The read:** storage is being redefined from *the thing that stores* to *the thing that computes*.
Firmware engineers who can't speak ML will maintain legacy drives. The ones who can will architect
the next ones. ^the-read

---

## 3 · Depth budget — what to go deep on

| Priority | Topic | Why for HIM |
|---|---|---|
| ⭐⭐⭐ | backprop + training loop | can't optimize what you can't build |
| ⭐⭐⭐ | MLP | the on-controller model *is* a small MLP |
| ⭐⭐⭐ | LSTM / time-series | telemetry is sequential; wearout & thermal are forecasts |
| ⭐⭐⭐ | **quantization / INT8** (s20) | makes it fit in SRAM — **highest-value single skill** |
| ⭐⭐ | optimizers, regularization | training quality |
| ⭐ | CNN | images; recognition-level only |
| ⭐ | LLM / transformers | literacy at M3, not a career bet |

**The one-line motivation:** *the market is putting neural nets inside storage controllers — and it
needs people who own both sides. He is already half-qualified; Module 2 is the other half.*

---

## Sources

- [Marvell / NVDLA in SSD controllers](https://www.electronicspecifier.com/products/artificial-intelligence/artificial-intelligence-ssd-controller-architecture-solution/)
- [FADU — AI inference SSDs at CFMS 2026](https://blogs.fadu.io/ai-inference-ssd-data-centers/)
- [ML framework for NAND flash lifetime extension](https://www.researchgate.net/publication/327138546_A_Machine_Learning_Framework_for_NAND_Flash_Lifetime_Extension)
- [US patent 11934696 — ML-assisted QoS for SSDs](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11934696)
- [AI-powered SSD firmware — write amplification](https://eudoxuspress.com/index.php/pub/article/download/4168/3044/8304)
- [NVIDIA + SK hynix "Storage Next" AI SSD](https://www.techspot.com/news/110674-nvidia-sk-hynix-building-ai-ssd-could-10x.html)
- [Samsung PM1763 mass production](https://www.storagenewsletter.com/2026/07/09/samsung-begins-mass-production-of-pm1763-ssd-optimized-for-next-generation-ai-infrastructure/)
- [FMS 2026 opening coverage](https://www.techtimes.com/articles/322686/20260802/fms-2026-opens-tuesday-liquid-cooled-pcie-60-ssds-debate-ai-memory-tiers.htm)

**Reading-ladder note:** the NAND-lifetime paper and the QoS patent are strong candidates for the
project-map §4 reading ladder — closer to his project than the generic smarter-SSDs survey.
