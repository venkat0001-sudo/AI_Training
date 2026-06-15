# Embedded analogy bank

Mappings from AI/ML/math concepts to SSD-firmware reality, for teaching an embedded engineer.
These are *starting points* — pick one, then build the lesson around it, or invent a fresh one in
the same spirit. The best analogy is precise (the mechanism actually matches) and sticky (vivid,
slightly funny). Avoid analogies that are only superficially similar; he'll catch it.

A recurring goldmine: **NAND threshold-voltage (Vt) distributions are literally Gaussian curves**,
so most of statistics/probability has a true, not metaphorical, home in NAND physics. Lean on it.

**Fallback order:** prefer SSD-firmware analogies (this bank), but a forced NVMe/NAND mapping is worse
than an honest one. When no clean storage mapping exists, drop to **general embedded** — ARM MCUs,
RTOS/super-loop, ISRs, sensors/ADC, DSP/FIR filters, PID/control loops, I2C/SPI/UART comms. Only if
even that is contrived, use a generic real-world analogy. Precision beats domain-purity every time.

## Table of contents
- [Statistics & descriptive measures](#statistics--descriptive-measures)
- [Probability & Bayes](#probability--bayes)
- [Distributions](#distributions)
- [Correlation](#correlation)
- [Linear algebra](#linear-algebra)
- [Calculus & optimization](#calculus--optimization)
- [Core ML concepts](#core-ml-concepts)
- [The Edge-AI bridge palette](#the-edge-ai-bridge-palette)
- [Trade-off pairs he already knows](#trade-off-pairs-he-already-knows)

---

## Statistics & descriptive measures

- **Mean** → average read latency across a batch of NVMe commands; average ADC sample. A single-pass
  accumulate-and-divide — exactly the C loop he'd write for a running sensor average.
- **Outlier** → a garbage-collection stall, an ESD spike, a single bit-flip glitch on a bus. One
  rogue sample that doesn't represent normal behavior.
- **Median vs mean** → this is the **P99 latency** story. Enterprise SSD QoS specs report tail
  *percentiles*, not averages, precisely because one GC stall (outlier) poisons the mean while the
  median shrugs. The NVMe world already chose median-like thinking — he's lived it.
- **Variance / standard deviation** → read-latency *jitter*, voltage ripple on a power rail, clock
  jitter. Mean tells you the center; std-dev tells you how twitchy the signal is. Managers (and
  firmware validators) care more about jitter than average, because consistency is the spec.
- **Percentiles / quartiles** → NVMe latency percentiles (P99, P99.9, P99.99). "Below this value
  99.9% of the time" is a sentence he's read in a datasheet.
- **IQR / box plot** → the spread of the "normal" middle of a latency histogram, with GC stalls
  flagged as the dots past the whiskers. Same thing a firmware engineer eyeballs in a latency-CDF plot.

## Probability & Bayes

- **Probability of an event** → raw bit error rate (RBER): probability a given NAND cell reads wrong.
- **Joint probability** → P(cell is in upper page AND has retention error).
- **Marginal probability** → overall fraction of codewords that need a read-retry.
- **Conditional probability** → P(read succeeds | we shifted to the second read-retry Vref). The
  whole read-retry table is conditional probability in action: each retry level is "given the last
  one failed, try this."
- **Independence** → two coin tosses don't affect each other; but in NAND, neighbor cells are *not*
  independent (program disturb), which is exactly why naive independence assumptions break — a great
  hook for "real data is rarely independent."
- **Bayes' theorem** → **LDPC soft-decision decoding.** The decoder starts with a prior (what bit was
  probably stored), gets evidence (the sensed voltage / log-likelihood ratio), and updates to a
  posterior. He ships Bayes in silicon already; he just never called it that. Also: fault diagnosis —
  given a CRC error fired, which subsystem most likely failed?
- **Base-rate / why a positive test isn't a diagnosis** → a rare failure mode with an imperfect
  detector. If only 1 in 10⁶ blocks is truly bad and your detector has a false-positive rate, most
  "fails" are false alarms. Same math as the disease-test example, but in his BIST/screening world.

## Distributions

- **Normal (Gaussian) distribution** → **NAND cell Vt distributions.** Each stored state (in TLC,
  eight of them) is a bell curve of threshold voltages across millions of cells. Mean = the target
  level, std-dev = how tight the program landed. This is not a metaphor — it's the physics.
- **68-95-99.7 rule** → read-margin budgeting: how many sigma of guard-band you leave between
  adjacent Vt distributions so reads don't collide.
- **Distribution overlap** → when retention/disturb widens the curves until neighbors overlap, you
  get bit errors → ECC kicks in. This visually motivates *why* spread (variance) is the enemy.
- **Bernoulli** → one cell: error or no error. One I/O: hit or miss in the DRAM cache.
- **Binomial** → number of bit errors in an N-bit ECC codeword. This *is* how you size BCH/LDPC
  strength: "how many flips per codeword must we correct?" is a binomial question.
- **Poisson (if it comes up)** → rare random events per unit time: uncorrectable errors per drive-hour,
  command arrivals at a given queue depth.

## Correlation

- **Positive / negative correlation** → temperature vs throttling frequency (as temp rises, clock
  drops — negative). Queue depth vs latency (positive).
- **Pearson (linear) vs Spearman (rank)** → Pearson when the relationship is a straight line (voltage
  vs ADC count); Spearman when you only trust the ordering, not the exact values (wear-level rank).
- **Correlation matrix / heatmap** → cross-talk map between adjacent signal traces or adjacent NAND
  cells — which neighbors disturb which.
- **Correlation ≠ causation** → temperature *correlates* with error rate, but the cause is often
  retention loss or the throttle event, not heat per se. Or: workload correlates with latency, but
  the hidden cause is background GC. He's debugged exactly this kind of false lead.

## Linear algebra

- **Vector** → a buffer / array in SRAM; a DMA descriptor; a row of a register file.
- **Dot product** → a **MAC** (multiply-accumulate) — the DSP instruction he already knows. A dot
  product is just a MAC loop.
- **Matrix-vector / matrix-matrix multiply** → what a **systolic array / NPU / tensor accelerator**
  does. This is the bridge to "why edge SoCs ship a dedicated NPU": matmul is the inner loop of every
  neural net, and doing it in a MAC array beats hammering the ARM core.
- **Transpose / reshape** → re-striping data across planes/dies; same bytes, different access pattern.
- **Norm (vector length)** → signal magnitude / RMS; how "big" a vector is, like an RMS voltage.

## Calculus & optimization

- **Derivative / slope** → rate of change of temperature feeding a thermal control loop. Slope =
  how fast the sensor is moving = what the throttle PID reacts to.
- **Gradient** → the multi-knob version: which direction (across several Vref knobs) reduces error
  fastest.
- **Gradient descent** → **read-level calibration / Vref tracking.** Firmware sweeps the read
  reference voltage, measures BER at each step, and walks toward the voltage that minimizes errors.
  That walk *is* gradient descent. He has literally written the embedded version of the algorithm
  that trains neural nets.
- **Learning rate** → the step size of that voltage sweep. Too big → overshoot the optimum (like an
  over-aggressive throttle oscillating); too small → calibration takes forever.
- **Local vs global minimum** → getting stuck at a decent-but-not-best Vref because the BER curve had
  a dip before the true valley.
- **Convexity** → a BER-vs-Vref curve with a single clean valley (easy to optimize) vs a bumpy one
  (you can get trapped).

## Core ML concepts

- **Features / labels** → telemetry columns (temp, P/E cycle count, retention time) vs the outcome
  you predict (will this block go bad?).
- **Training vs inference** → characterizing NAND on sample dies in the lab (training) vs the deployed
  firmware making a live decision (inference). Inference is what must fit on the controller.
- **Overfitting** → a wear-leveling or GC heuristic tuned perfectly to one benchmark that falls apart
  on real customer workloads. He's seen firmware "cheat" a benchmark — same failure mode.
- **Train/test split** → validate on dies you didn't tune on, or you're just grading your own homework.
- **Regularization** → guard-banding / margin. Don't trust the training data so hard that you leave
  no safety margin; deliberately hold back to generalize.
- **Bias-variance trade-off** → a model too simple to capture reality (underfit / high bias) vs one
  so flexible it memorizes noise (overfit / high variance). Like an FTL heuristic that's too rigid vs
  one so tuned it chases noise.
- **Classification threshold** → the read-reference voltage deciding 0 vs 1. Moving the decision
  boundary trades false-positives for false-negatives — exactly Vref placement between two Vt curves.

## The Edge-AI bridge palette

Use these to close lessons with "how this lands on real silicon" — his actual goal.

- **Fixed-point vs floating-point** → he lives in fixed-point (Q-format). INT8 quantization is the
  *same* precision-vs-range trade he already manages; a neural net quantized to INT8 is just choosing
  a Q-format for weights.
- **Quantization error** → rounding noise from fewer bits — directly analogous to ADC quantization
  noise and to truncating in fixed-point DSP.
- **Model size vs SRAM/DRAM budget** → weights too big for on-chip SRAM must stream from DRAM/flash,
  just like FTL mapping tables that can't all live on-chip. Tiering decisions are identical.
- **Throughput vs latency** → batched inference (high QD, high throughput) vs single-sample inference
  (QD1, low latency). The NVMe queue-depth trade-off, reused verbatim.
- **Real-time deadlines** → an inference that must finish inside a control-loop period, like an ISR
  that must return before the next interrupt.
- **Power / thermal budget** → an NPU that throttles under sustained inference, exactly like the SSD
  controller throttling under sustained writes.

## Trade-off pairs he already knows

When teaching beat 8 ("when is the older/simpler thing still better?"), reach for a hardware
trade-off he already feels in his gut, then map the new concept onto it:

- **SRAM vs DRAM** — fast/small/expensive vs slow/big/cheap. → simple-cheap model vs big-accurate model.
- **Polling vs interrupt** — simple and predictable vs efficient but complex. → mean vs median-ish
  cost: more robust often costs more compute.
- **QD1 latency vs QD32 throughput** — responsiveness vs bandwidth. → single vs batch inference.
- **More ECC strength vs more storage overhead** — safety vs cost. → more regularization/margin vs
  fitting the data tightly.
- **Aggressive vs gentle throttle** — react fast and oscillate vs react slow and lag. → large vs
  small learning rate.

The lesson: in his world *nothing* is universally superior — you pick per constraint. AI is the same.
That framing is the whole point for him.
