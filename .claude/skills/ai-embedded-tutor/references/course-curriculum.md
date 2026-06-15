# Course curriculum — Executive PG Certificate in Applied AI & ML (IIT KGP + upGrad)

The full syllabus the learner is taking. Use it to **situate** every concept: where it sits in the
arc, what earlier session it builds on, and what later session will need it. He attends one class per
weekend and comes to Claude afterward for the in-depth version of what the professor covered.

How to use this file:
- When he names a session or concept, find it here and teach it *in context* — name the prior session
  it extends and the future session it feeds. That connection-web is his top priority.
- The "embedded bridge" notes per session are the strongest hardware hooks; combine with
  `embedded-analogy-bank.md`.
- Re-teach in depth, beyond the surface the lecture covered. Assume the prof gave breadth; you give
  depth + intuition + his-domain grounding.

Course runs **30-May-2026 → 10-Jan-2027**. Classes are weekend mornings (10am–1pm IST).

---

## Foundation Bridge — upGrad (Module Lead: Dr. Suresh Kumar)
*The math/Python runway. Everything else stands on this — invest heavily here, given his math rebuild.*

| Date | Session | Embedded bridge |
| --- | --- | --- |
| 30 May–3 Jun 2026 | Readiness Assessment Test | — |
| 6 Jun 2026 | Python Tool Proficiency | NumPy array = SRAM buffer; vectorization = SIMD/DMA vs byte-by-byte loop |
| 7 Jun 2026 | Probability & Statistics Foundations | NAND Vt curves = Gaussians; P99 QoS = percentiles; RBER = probability; LDPC = Bayes |
| 13 Jun 2026 | Linear Algebra Foundations | vectors = buffers; dot product = MAC; matmul = systolic array/NPU |
| 14 Jun 2026 | Calculus Foundations | derivative = thermal-loop slope; gradient descent = read-level Vref calibration |

*(The Notes.md he shared maps to the 7-Jun Probability & Statistics session.)*

## Module 1: Machine Learning Fundamentals — 6 weeks (Lead: Prof. Adway Mitra)
*From raw data to working predictors. The vocabulary every later module reuses.*

| # | Date | Session | Builds on / feeds | Embedded bridge |
| --- | --- | --- | --- | --- |
| 1 | 20 Jun 2026 | Data analysis, preprocessing, visualization; ML workflow; cross-validation; error types & performance metrics | uses Foundation stats; feeds everything | EDA = bringing up a board with a logic analyzer before trusting it; metrics = pass/fail screening criteria |
| 2 | 27 Jun 2026 | Supervised learning: linear & logistic regression | uses calculus/gradient descent; feeds neural nets (a neuron = logistic regression) | linear fit = ADC calibration curve; logistic = a soft Vref decision boundary |
| 3 | 4 Jul 2026 | Supervised learning: decision trees & SVMs | alt to regression; feeds ensembles | decision tree = nested if/else firmware state machine; SVM margin = guard-band between Vt curves |
| 4 | 11 Jul 2026 | Ensemble methods: bagging, random forests, AdaBoost, gradient boosting | combines Session 3 trees | RAID-like redundancy: many weak voters beat one; voting = ECC majority logic |
| 5 | 18 Jul 2026 | Unsupervised learning: K-means clustering & PCA | uses linear algebra; PCA feeds dim-reduction everywhere | PCA = lossy compression / keeping dominant signal components; clustering = wear-level grouping |
| 6 | 19 Jul 2026 | Assignment & doubt-clearing | — | — |

## Module 2: Deep Learning, Computer Vision, Deployment — 6 weeks (Lead: Prof. Somdyuti Paul)
*Where it becomes "AI." Neurons stack into networks; CNNs see, RNNs remember; then deploy.*

| # | Date | Session | Builds on / feeds | Embedded bridge |
| --- | --- | --- | --- | --- |
| 7 | 25 Jul 2026 | Feedforward neural networks & backpropagation | logistic regression × many layers; backprop = chain-rule calculus | a layer = a pipeline stage; backprop = error propagation back through stages |
| 8 | 1 Aug 2026 | Gradient-based optimizers & regularization | extends gradient descent (Foundation) | optimizer = the throttle/PID tuning; regularization = guard-band/margin |
| 9 | 8 Aug 2026 | Convolutional neural networks (CNNs) | feedforward + weight sharing | convolution = a FIR/DSP filter sliding over a signal |
| 10 | 16 Aug 2026 | Recurrent neural networks (RNNs) | adds state/memory; feeds Transformers | RNN hidden state = a state machine's persistent register across cycles |
| 11 | 22 Aug 2026 | Transfer learning & deployment | reuses pretrained nets; **first real Edge-AI session** | porting a validated IP block to a new chip; deployment = flashing firmware to constrained silicon |
| 12 | 23 Aug 2026 | Assignment & doubt-clearing | — | — |

## Module 3: NLP, Transformers, Speech AI — 5 weeks (Lead: Prof. Plaban Bhowmick)
*Sequences and language. Attention replaces recurrence; the Transformer is born.*

| # | Date | Session | Builds on / feeds | Embedded bridge |
| --- | --- | --- | --- | --- |
| 13 | 29 Aug 2026 | Text preprocessing & representation | tokens → vectors (linear algebra) | parsing a byte stream / protocol framing before processing |
| 14 | 5 Sep 2026 | Attention mechanism & Transformer | replaces RNN (Session 10); core of all LLMs | attention = a crossbar/interconnect routing where each token "reads" relevant others (like PCIe fabric routing) |
| 15 | 12 Sep 2026 | Transformer variants: tokenization, encoder-only, decoder-only | extends Session 14; feeds LLMs | encoder vs decoder = read-path vs write-path engines, different jobs same fabric |
| 16 | 19 Sep 2026 | Speech/audio representations, ASR, TTS, voice cloning | applies Transformers to audio | audio framing = ADC sampling + windowing; spectrogram = FFT he already knows |
| 17 | 20 Sep 2026 | Exams | — | — |

## Module 4: Applications of Generative AI & LLMs — 6 weeks (Lead: Prof. Jiaul Paik)
*Scaling Transformers into generative systems; adapting and aligning them.*

| # | Date | Session | Builds on / feeds | Embedded bridge |
| --- | --- | --- | --- | --- |
| 18 | 26 Sep 2026 | Foundations of Generative AI | builds on Transformers | generating vs reading data — like a traffic generator vs a sniffer |
| 19 | 3 Oct 2026 | LLM concepts & architectures, pretraining at scale, prompt engineering | scales Session 15 | pretraining = mass characterization runs; prompt = a command opcode shaping behavior |
| 20 | 10 Oct 2026 | LLM adaptation & finetuning: PEFT, LoRA, QLoRA | adapts pretrained LLMs; **QLoRA = quantization, pure Edge-AI** | LoRA = a small patch/overlay instead of reflashing the whole image; QLoRA Q = your fixed-point Q-format |
| 21 | 24 Oct 2026 | Multimodal AI: audio/speech/vision Transformers, CLIP, fusion | unifies vision (CNN) + text (Transformer) | sensor fusion: combining multiple sensor streams into one decision |
| 22 | 31 Oct 2026 | LLM alignment + Responsible AI (hallucination, bias, PII leakage, prompt injection, governance) | safety layer over LLMs | input validation / threat model; prompt injection = untrusted input crossing a trust boundary |
| 23 | 1 Nov 2026 | Assignment & doubt-clearing | — | — |

## Module 5: RAG Systems, LangChain, Advanced Evaluation — 5 weeks (Lead: Prof. Koustav Rudra)
*Giving LLMs external memory and grounding; orchestrating and evaluating them.*

| # | Date | Session | Builds on / feeds | Embedded bridge |
| --- | --- | --- | --- | --- |
| 24 | 21 Nov 2026 | Foundations of RAG & vector search | uses embeddings (vectors) | vector search = content-addressable memory / a cache lookup by similarity |
| 25 | 28 Nov 2026 | LangChain & RAG orchestration | composes Session 24 | chaining = a driver stack / middleware layers passing buffers |
| 26 | 5 Dec 2026 | Advanced RAG techniques & system design | scales RAG | cache hierarchy + prefetch design for relevance |
| 27 | 12 Dec 2026 | Evaluation, debugging & optimization | evaluates the whole stack | regression test suite + perf profiling for firmware |
| 28 | 13 Dec 2026 | Assignment & doubt-clearing | — | — |

## Module 6: Agentic AI, MLOps, Responsible AI (Lead: Prof. Jiaul Paik)
*Autonomy, operations, and governance — shipping and running AI for real.*

| # | Date | Session | Builds on / feeds | Embedded bridge |
| --- | --- | --- | --- | --- |
| 29 | 19 Dec 2026 | Agentic AI: foundations, building blocks, architectures, orchestration | builds on LLMs + RAG | an agent loop = a firmware super-loop / RTOS scheduler calling tasks |
| 30 | 26 Dec 2026 | Building, evaluating, deploying agentic AI systems | extends Session 29 | system integration + HIL (hardware-in-the-loop) testing |
| 31 | 2 Jan 2027 | MLOps: operationalizing ML, monitoring, CI/CD | ops layer over everything | CI/CD = firmware build/flash/test automation; monitoring = telemetry/SMART logging |
| 32 | 9 Jan 2027 | Responsible Agentic AI & governance (guardrails, human-in-the-loop) | governs agents | safety interlocks / watchdog timers / fail-safe states |
| — | 10 Jan 2027 | Final Exam | — | — |

Holidays noted on the schedule: 17 Oct (Durga Saptami), 7 & 14 Nov (Diwali) — no classes.

---

## The course as one connected story (use this to keep the web alive)

Stats/probability → describe and reason under uncertainty →
linear algebra/calculus → the machinery to optimize →
regression → the first predictor; **a neuron is just logistic regression** →
stack neurons + backprop → neural nets →
specialize: CNN (space), RNN (time) →
replace recurrence with **attention → Transformer** →
scale the Transformer → **LLMs** →
adapt (LoRA/QLoRA) and align them →
give them memory (**RAG**) →
let them act (**agents**) →
operate and govern them (**MLOps, responsible AI**).

Every session is a link in that chain. When teaching any one link, point backward and forward along
it — that is exactly the "why is this better than the last thing, and when was the last thing fine?"
reasoning he asked for.
