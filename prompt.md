# Prompt: generate my sanitized "work-context profile" for an AI/ML tutor

**How to use this file (on the office laptop):**
1. Open this repo's Claude Code CLI in your work environment (the one that already knows your code).
2. Tell it: *"Read `prompt.md` and follow it. Produce `work-context.md`."*
3. **Review the output yourself, line by line, for anything confidential** (see the sanitization rules — they are strict and non-negotiable).
4. Copy the cleaned `work-context.md` back into this repo, commit, and push. The tutor will read it.

---

## Role and goal (for the office Claude reading this)

You are helping me build a **portable, sanitized profile of my day-to-day engineering work**. A
*separate* AI tutor — running on my personal account — uses it to teach me AI / ML / math by framing
**every example, analogy, and exercise around what I actually build at work**, instead of generic
textbook scenarios.

You know my codebase and what I work on. Your job is to distill the **shape** of that work — the
domain, subsystems, vocabulary, data structures, constraints, and recurring problems — into a single
markdown file the tutor can map machine-learning concepts onto.

You are **not** exporting my work. You are writing a high-level, industry-generic description of the
*kind* of engineering I do. Think "what I'd be allowed to say about my job at a public conference,"
not "what's in the repo."

---

## ⚠️ Sanitization rules — strict, non-negotiable

This file will leave the work machine and live in a personal (private) repo. Therefore, **exclude
absolutely**:

- **No source code** — not even snippets, function names, or file paths from the work repo.
- **No proprietary or secret algorithms** — describe the *category* ("a wear-leveling heuristic"),
  never the actual method or any detail that constitutes the "secret sauce."
- **No internal codenames** — project names, chip names, product names, internal tool names. Replace
  with generic industry terms ("the controller," "the host interface," "the mapping layer").
- **No customer, partner, or vendor names.**
- **No unreleased-product or roadmap information.**
- **No performance numbers that are confidential** — use relative/qualitative phrasing ("tight
  latency budget") rather than exact specs if the exact figure is sensitive.
- **No credentials, configs, infrastructure details, or internal URLs.**

**Rule of thumb:** if a competitor reading this line would learn something they couldn't find in a
public datasheet, textbook, or standard spec — cut it or generalize it. When unsure, omit. A thinner
but safe profile is far better than a rich but leaky one.

---

## About me (so you frame the analogy hooks at the right target)

- I'm an **embedded / firmware engineer** rebuilding math from fundamentals and learning AI/ML.
- My **end goal is Edge / Physical AI** — running models on constrained hardware.
- I think fluently in **C, registers, interrupts, state machines, buffers, memory hierarchies,
  signal integrity, and hardware tradeoffs**. I am *not* a strong math person — intuition must come
  before symbols.
- I learn best when a new concept is **mapped onto something I already do in firmware**, then bridged
  to how it lands on real silicon (fixed-point/quantization, RAM/flash budget, latency vs throughput,
  power/thermal limits).

So the most valuable thing you can give me is **a list of my real work concepts paired with the
AI/ML/math idea each one naturally illuminates.**

---

## Output: produce `work-context.md` with these sections

Write clean, scannable markdown. Be concrete but sanitized. Aim for depth in sections 6 and 7 — they
are the payoff.

### 1. Domain in one paragraph
What kind of systems I work on, at an architecture level. The 5-sentence version I'd give another
engineer outside my company.

### 2. Subsystems & components I touch regularly
A bulleted list of the modules / layers / blocks I work in (generic terms only). For each, one line
on what it does and how often I'm in it.

### 3. Daily vocabulary & mental models
The concepts, abstractions, and patterns I reason with every day (e.g., state machines, queues,
pipelines, scheduling, arbitration, error handling, caching, DMA). These are the building blocks the
tutor will reuse as analogy material — be generous and specific here.

### 4. Data structures & algorithms I actually use
The recurring data structures (tables, ring buffers, trees, bitmaps, queues…) and algorithm classes
(search, sort, hashing, scheduling, calibration loops, error correction…) in my work — generically
described. No proprietary specifics.

### 5. Constraints I live under
The real engineering pressures: latency targets, memory/footprint limits, power/thermal budgets,
real-time deadlines, throughput-vs-latency tradeoffs, reliability/endurance, determinism. Qualitative
where exact numbers are sensitive.

### 6. Recurring problems, tradeoffs & optimizations
The kinds of bugs I chase, the tradeoffs I tune, and the optimizations I repeatedly make. The tutor
uses these to build "you've debugged exactly this" moments. (e.g., "balancing responsiveness against
throughput," "deciding what lives in fast memory vs slow," "tracking a drifting parameter over time.")

### 7. Analogy hooks → AI/ML/math (the most important section)
A two-column mapping. **Left:** a real concept/pattern/problem from my work (sanitized). **Right:**
the AI/ML/math concept it naturally explains, with one sentence on *why* the mechanism matches.
Cover as many genuine matches as you can find. Target these tutor topics on the right side:

- **Statistics:** mean, median, variance/std-dev, percentiles, outliers, distributions
- **Probability:** conditional probability, Bayes' theorem, independence, base rates
- **Distributions:** normal/Gaussian, Bernoulli, binomial, Poisson
- **Linear algebra:** vectors, dot product, matrix multiply, norms
- **Calculus / optimization:** derivatives, gradients, gradient descent, learning rate, local vs
  global minima, convexity
- **Core ML:** features/labels, training vs inference, overfitting, regularization, bias-variance,
  classification thresholds
- **Neural nets & beyond:** layers/backprop, CNNs (filters), RNNs (state/memory), attention/
  Transformers, LLMs
- **Edge AI:** fixed-point vs float, INT8 quantization, model size vs memory budget, throughput vs
  latency, real-time deadlines, power/thermal throttling

Only include a row when the mechanism **genuinely** matches — a forced analogy is worse than none.
Flag the strongest 5–10 hooks with a ⭐ so the tutor leans on them first.

### 8. Things to avoid in analogies
Any area where a hardware-to-AI mapping would actually mislead me, or any topic you deliberately kept
vague for confidentiality (so the tutor doesn't probe there).

---

## Quality bar
- Concrete over abstract; sanitized over detailed when they conflict.
- Generous in sections 3, 6, 7; tight everywhere else.
- Output **only** the contents of `work-context.md` — no preamble, no explanation of what you did.
- End with a one-line self-check: *"Confidentiality review: confirm no code, codenames, customers,
  secret methods, or sensitive specs are present."* — and make sure that's true before you finish.
