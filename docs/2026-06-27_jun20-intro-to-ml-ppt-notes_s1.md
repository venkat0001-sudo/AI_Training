---
title: Jun 20 Session 1 — Intro to ML (PPT lecture notes)
date: 2026-06-27
source: session1_jun20 Session-PPT.pdf (77 slides)
tags: [ml-workflow, preprocessing, cross-validation, metrics, foundations]
---

# Jun 20 Session 1 — Introduction to Machine Learning (PPT lecture notes)

Lecturer: Mahesh Mohan M R, Department of AI, IIT Kharagpur.

## Table of Contents

| Section | Slides |
|---|---|
| 1. Motivation & Data Types | 1–11 |
| 2. Why ML Now (history of the field) | 12–14 |
| 3. Case Study: Reading a Postcode (rules vs learning) | 15–23 |
| 4. Outline / Supervised Learning intro | 24–27 |
| 5. The ML Workflow ("How to Solve It" — 4 steps) | 28–33 |
| 6. Loss Functions (Cross-entropy & MSE) | 34–39 |
| 7. Classification vs Regression | 36, 59 |
| 8. Optimization (closed-form & gradient descent, learning rate) | 40–44 |
| 9. Parametric vs Non-parametric Methods | 45–46 |
| 10. Data Challenges (missing data, errors/artifacts, outliers, curse of dimensionality) | 47–52 |
| 11. Model Building Story: Fitting an Elephant (over-parameterization) | 53–56 |
| 12. Model Challenge 1: Complexity (under/good/overfit) | 57–58 |
| 13. Train vs Validation; K-fold Cross-Validation | 60–62 |
| 14. Model Challenge 2: Inductive Bias | 63 |
| 15. Model Challenge 3: Evaluation — Confusion Matrix & Error Types | 64–65 |
| 16. Performance Metrics (Accuracy, Precision, Recall, F1) | 66 |
| 17. Unsupervised Learning (Clustering, Association) | 67–70 |
| 18. Reinforcement Learning | 71–76 |
| 19. Summary of "Intro to ML" | 77 |

## Overview

This is an end-to-end "Intro to ML" deck. It opens by motivating ML through applications and by classifying data by dimensionality (time-series 1-D, image 2-D/3-D, video 3-D). It uses handwritten-digit / postcode reading (the LeCun MNIST setup) to contrast brittle hand-written rules against a learned neural-network solution, and from that extracts a 4-step ML workflow: (1) collect labelled data, (2) design the model, (3) define a loss, (4) optimize weights. It then teaches the two core loss functions (cross-entropy for classification, MSE for regression), optimization via gradient descent (with learning-rate intuition), and the parametric/non-parametric distinction. The back half covers real-world data challenges (missing data, errors vs artifacts, outliers, curse of dimensionality), model complexity / under- vs over-fitting, validation and K-fold cross-validation, error types via the confusion matrix (Type 1 / Type 2), and the standard performance metrics. It closes by sketching unsupervised and reinforcement learning and a one-slide taxonomy summary.

---

## Revision ladder (skim these in 2 minutes — recall, don't re-read)

1. **Data dimensionality:** 1-D time series, 2-D grayscale image, 3-D color image / grayscale video, 4-D color video. → §1
2. **Why ML now? Two unlocks:** big data + GPU parallelism. Algorithms existed since the 1990s. → §2
3. **Rules vs Learning:** handwritten digit rules fail on real variation. "If a problem is hard to solve with rules, use a data-centric method." → §3
4. **4-step ML workflow:** Collect labelled data → Design model → Define loss → Optimize weights. → §5
5. **Cross-entropy loss (classification):** only the true class's probability matters; `L_CE = −log(p_true)`. Case 2 (0.095) < Case 1 (0.3677) = better. → §6
6. **MSE loss (regression):** pixel-wise squared difference; used when output ≈ input (e.g. deblurring). → §6
7. **Gradient descent vs closed-form:** GD = iterative, scales to big models; closed-form = one-shot, requires matrix inverse, breaks at large feature counts. → §8
8. **Overfitting vs underfitting:** high bias (underfit) vs high variance (overfit). K-fold cross-validation catches it. → §§12–13
9. **Confusion matrix:** TP / FP / FN / TN. Type 1 error = FP (false alarm). Type 2 error = FN (missed detection). → §15
10. **Accuracy / Precision / Recall / F1:** use F1 when classes are imbalanced; accuracy alone misleads. → §16
11. **Unsupervised learning:** no labels — find structure (clustering, association). → §17
12. **Reinforcement learning:** agent + environment + reward signal. No labelled dataset needed. → §18

---

## 1. Motivation & Data Types (Slides 1–11)

- **Slide 1 — Title:** "Introduction to Machine Learning." Mahesh Mohan M R, Department of AI, IIT Kharagpur.
  - ✍️ **Instructor ink (Slide 1):** a short red cursive scribble in the left margin below the title rule, best read as "**Chit**" (or initials). — **Intent:** a **stray pen-test / name-tag stroke** — the transcript's opening minute is pure setup chatter ("OK, rename… I need to put Mahesh, Mohan and Goa… I changed it") with **no teaching content yet**, so this is a warm-up mark while he renamed/labelled the session, not a concept. (Confirmed from the slide PNG; residual uncertainty on the exact word, but its *non-conceptual* nature is certain.)
- **Slide 2 — Applications montage:** AI is everywhere — Robotic Manufacturing, AI for Agriculture, Loan Approval, Smart Diagnosis, Depression Classification, Recommendations. (6 application images.)
- **Slide 3 — Time Series Data (1-dimensional):** a signal/sequence indexed by time; one value per timestep.
  - ✍️ **Instructor ink (Slide 3):** a large red **"2"** drawn on the black arrow (a step marker in his live walk-through), plus a tangle of red margin notes bottom-centre near "IoT device". With the spoken context the tangle now reads as the **windmill height-vs-power sketch**: "**pointing model by … windmill**", "**store data in memory**", and the axis label "**x → ht of its windmill**" (height of the windmill). — **Intent:** *(resolved via transcript)* he was drawing the **windmill example live** — plotting **windmill height (x) vs power (y)** to show a 1-D signal that varies across a *non-time* axis (distance/height), and noting the data is stored in memory. The earlier "polynomial / width of its window" reading was a misread of "**pointing … windmill … ht of its windmill**."
  - 🖼️ **Figure (Slide 3):** left = stacked red/black ECG-like 1-D signals from IoT sensors; right = two real time-series line charts (Variable-vs-Time, and two-city temperature over a week). **Takeaway:** time-series data is one scalar value indexed along a single time axis.
- **Slide 4 — Time Series Forecasting:** example "ESG Risk" forecasting. Citation: *Learning the ESG Geometry with Domain Aware Language Models, ICML 2026.*
  - ✍️ **Instructor ink (Slide 4):** red top-left box "**Profit**"; below it the ESG expansion "**E → Env(ironment)**", "**S → Soc(ial)**", "**G → Govern(ance)**"; a red "**A\***" with asterisk over the fan-out forecast region. — **Intent:** he spelled out what ESG stands for and tied the forecast to a business "profit"/risk motive; the "A\*"/asterisk flags the widening uncertainty cone as the key thing to notice.
  - 🖼️ **Figure (Slide 4):** a forecast chart — solid history line up to 2025, then a red→orange **fanning band** of predicted ESG-risk trajectories afterward. **Takeaway:** forecasting predicts future values *with growing uncertainty* the farther out you go (the widening cone).
- **Slide 5 — Image Data (2-dimensional):** a grayscale image is a 2-D grid of pixel intensities.
- **Slide 6 — Gray Scale Image Analysis:** example task. Citation: *Noise-aware Detail Enhancement in Scanning Electron Microscope imagery, KLA-Tencor's Neoterix, 2018.*
- **Slide 7 — Color Image (3-dimensional):** an RGB image is 3-D (height × width × 3 channels).
  - ✍️ **Instructor ink (Slide 7):** red labels "**R, G, B**" over the channel cube, and sample colour-coordinate tuples written by hand: "**(128,0,0)**", "**(0,255,0)**", "**(0,0,0)**", "**(255,255,255)**". — **Intent:** he made the 3-channel encoding concrete — each pixel is a triple, and specific tuples map to specific colours (e.g. (0,0,0)=black, (255,255,255)=white, (0,255,0)=pure green), driving home that a colour image is H×W×3 numbers.
  - 🖼️ **Figure (Slide 7):** a bird image overlaid with a pixel grid beside a stacked R/G/B matrix cube and a colour-name→RGB lookup table. **Takeaway:** a colour image is three stacked 2-D intensity planes (one per channel).
- **Slide 8 — Color Image Analysis:** deblurring example. Citation: *Deep Dynamic Scene Deblurring for Unconstrained Dual-lens Cameras, IEEE TIP, 2021.*
  - ✍️ **Instructor ink (Slide 8):** heavy red mark-up over the two example panels — labels "**Sharp**"/"**Blurred i/p**", "**Blurred**", "**Humans**", "**Reference (90%?)**", "**Bike**", arrows pointing input→output, and "**Background**" callouts (several words unclear). — **Intent:** he walked through two CV tasks live — **(1) Semantic Segmentation** and **(2) Object Detection** — annotating which region is input vs deblurred output and naming the objects (humans, bike, background) the model must separate.
- **Slide 9 — Grayscale Video Data (3-dimensional):** grayscale frames stacked over time → 3-D (H × W × Time).
  - ✍️ **Instructor ink (Slide 9):** red dimension annotations — "**2D**" / "**single image**", "**10 → time**", "**30**", "**3D**", "**a sequence of video frames**", "**time**", and on the frames "**RGB-2**", "**RGB-1**", "Frame". — **Intent:** he derived the dimensionality bookkeeping live: a single grayscale image is 2-D; stacking, say, 30 frames over 10 time-steps adds a **time axis → 3-D**. Makes the "video = images over time" idea explicit.
  - 🖼️ **Figure (Slide 9):** a single digit pixel-grid (2-D) → an arrow → a stack of video frames with X, Y and a time axis, ending in a "blob of connected pixels". **Takeaway:** video stacks 2-D frames along time, so grayscale video is a 3-D (H×W×T) volume.
- **Slide 10 — Grayscale Video Analysis:** IR motion-deblurring. Citation: *Fast Motion Deblurring of IR Images, IEEE Signal Processing Letters, 2022.*
  - ✍️ **Instructor ink (Slide 10):** small red carets/arrows ("‸") drawn above both the "Blurred" frame-stack and the deblurred output stack. — **Intent:** points the eye to the per-frame quality change (blurred → sharpened) across the video stack; emphasis mark rather than text.
- **Slide 11 — Color Video Analysis:** color video adds a channel dimension (4-D conceptually). Citation: *Barriers to Computer Vision Applications in Pig Production Facilities, Computers and Electronics in Agriculture, 2022.*
  - ✍️ **Instructor ink (Slide 11):** red dimension tags over the multi-frame pig-pen panels — "**5×8×30**" (top-left, green) and "**6×4×30**" (top-right). — **Intent:** *(now legible from the PNG)* he kept the running dimensionality bookkeeping going on the **pig-pen colour video** — H × W × frames (e.g. 30 frames) — to land that adding colour + time pushes the data to **4-D**. (Spoken context: this is the **University of Illinois pig-activity monitoring** clip, which he later said ran at **15 fps over 4 months**.)

**Takeaway of section:** data is categorized by dimensionality — 1-D time series, 2-D grayscale images, 3-D color images / grayscale video, higher for color video.

- 🎙️ **Spoken (Slides 2–4 — time series):** He opened by saying *data is what drives AI — it's the input, and it's also what the method gives out.* For 1-D he stressed that "1 dimension" need not be **time** — it can be any single axis (seasonal, monthly, **distance**). His concrete example: a **windmill company** plotting **height of the windmill (x) vs power generated (y)**. In a flat terrain like the **Sahara desert** you reach a given power at a *smaller* height; in **Mumbai city**, with tall buildings and trees blocking wind, you only get that same power at a *much larger* height — so the height-vs-power curve shifts by location. (This is the windmill story behind the slide-3 ink "x → ht of its windmill".) For the ESG slide he told the **real story of his PhD scholar Kunal** — a working professional (a company director doing a *part-time* PhD at IIT KGP, from a finance background) whose ESG-forecasting paper was just accepted at **ICML** (the top ML conference), and the whole team is flying to **South Korea (July first week)** to present it. He unpacked **ESG = Environment / Society / Governance** with the cigarette example: *invest in cigarettes and you may get profit, but it harms the environment AND society* — so you want profit *while* respecting these factors. Motivational aside to the class: "even though he's a working professional, he didn't reduce his expectations — try and do good in your own industry too."
- 🎙️ **Spoken (Slides 5–8 — images):** Grayscale concretely = "a bunch of numbers; 0 = black, 255 = white, everything between is a shade of grey" (he pointed at sample cells: "47 ≈ blackish, 255 = white"). The grayscale-analysis example is his group's collaboration with **KLA-Tencor**: they run a **scanning electron microscope (SEM)** over **fabricated chips** (the kind in mobiles, laptops, GPUs) to spot **microscopic defects** invisible to the human eye — SEM produces *grayscale* images by its imaging mechanism. His group's job: **denoise** the patches so structures become evident and the chip can pass **QC (quality check)**. For colour he made RGB concrete with tuples spoken aloud — (255,0,0)=brightest red, (128,0,0)=half-red, (0,255,0)=pure green, (0,0,0)=black, (255,255,255)=white. The colour-analysis example is **autonomous driving**: cars move and hit bumps, so the captured image is **blurred**; he walked through **semantic segmentation** (colour-code: pink=human, green=bicycle, blue=background) and **object detection** (bounding boxes with confidences, e.g. "person 69%", "bike 90%", "water dispenser 85%") — his group **deblurs blur→sharp first** so detection/segmentation actually work at deployment.
- 🎙️ **Spoken (Slides 9–11 — video):** "Video is nothing but images arranged across time." He explained **frames per second** ("30 fps = 30 images in succession per second; your eye can't resolve 1/30 s, so it looks smooth"), and derived dimensionality live: grayscale image = 2-D, arranged across 1-D time → **3-D grayscale video**; colour image = 3-D, across time → **4-D colour video**. The grayscale-video case study is for **DRDO (India's defence R&D org)**: a **submarine** surfaces and pops up an **infrared camera on a gimbal** that does a **360° rotation** to scan for enemy ships — but the **gimbal motion blurs** the footage, so his group recovers a **clean video from the blurred one** for human/machine analysis. The colour-video case study is from his **postdoc at University of Illinois Urbana-Champaign**: monitoring **pigs in pig-pens** via a 24/7 camera. Because a sick pig is **less active**, they **classify each pig and track its activity over time** ("this pig is lying lateral 5–7 hrs, rarely eats") to **flag/isolate sick animals early** before disease spreads through the pen. (He later clarified in Q&A: it ran at **15 fps over a 4-month period**, and time is essential because "a pig lying down for one instant isn't necessarily unwell — it'll stand up next moment.")

## 2. Why ML Now (Slides 12–14)

- **Slide 12 — "Why ML didn't take off in the 90s?"** Key point: *Most techniques for ML were already developed before the 1990s.* So the algorithms aren't new.
- **Slide 13 — Same question, the two reasons:**
  1. Limited big-data availability.
  2. Limited computational power to crunch the data.
  - ✍️ **Instructor ink (Slide 13):** red callouts on the two vintage room-sized-computer photos — "**stored disk**" with an arrow to the tape/disk unit, and "**20k**" + "**mobile phone**" pointing at the old machine. — **Intent:** dramatized the compute gap — that entire 1990s mainframe had less storage/power than a modern ~20k-rupee mobile phone, so the *bottleneck was hardware, not algorithms*.
- **Slide 14 — "Why ML is trending now?"** The two earlier limits are now solved:
  - **Big data availability:** one trillion images; 350 million images uploaded per day; 100 hrs of video uploaded per minute; 2.5 petabytes of data every minute.
  - **Computational power:** parallel processing units — **GPUs**.
  - ✍️ **Instructor ink (Slide 14):** red arithmetic over the GPU/core graphics — "**1 × 16**", "**10,000 × 16**", "**1,00,000**", "**10,000**" (Indian-notation, i.e. one lakh). — **Intent:** he quantified parallelism live: a CPU has ~16 cores but a GPU has tens of thousands, so multiplying cores (e.g. 10,000 × 16) gives the massive throughput that makes modern ML feasible.
  - 🖼️ **Figure (Slide 14):** left column = big-data logos (Google/Facebook/YouTube/Walmart with their per-minute volumes); right = a CPU chip (few cores) **vs** a GPU chip (thousands of cores) with NVIDIA cards. **Takeaway:** the two former blockers — data and compute — are now both abundant, which is *why* ML took off.

- 🎙️ **Spoken (Slides 12–14):** He told a **personal story**: during his own PhD at **IIT Madras** he had never heard of deep learning — *there was no course by that name* — until his 3rd/4th year (around **2015–16**) when it suddenly boomed; now IIT Madras and IIT KGP both have whole **AI departments** with separate ML and DL courses. He then ran a **live chat poll**: "the techniques existed before the 1990s — why didn't AI boom then?" and read out the class's answers approvingly: **"lack of data"** and **"computing power / hardware wasn't advanced."** He dramatized both bottlenecks: data used to be stored on **punched paper rolls read manually**; and the compute that today fits in **any ordinary ~₹20K mobile phone in your pocket** once needed a **whole room** of bulky **vacuum tubes** — which, like filament bulbs, kept failing and needing replacement (transistors later fixed that reliability). On *why* it succeeded now: "**you yourselves create the data** — browsing YouTube, asking Google, uploading WhatsApp/Facebook photos; multiply that by the whole globe." Plus the **digital footprint** of every industry (MRI scans saved to computer, IoT agriculture sensors) — and "computers want digital data, which is now abundant." On compute he worked a number live: if a **CPU has 16 cores** (16 parallel jobs) and you must process **10,00,000 (10 lakh) images** one-per-core, it takes **2–3 months**; a **GPU with thousands of cores** crunches the same in **a few minutes** — *that combination of big data + GPU is the enabler.* (He also caught himself getting "confused with the US notation" while writing 10,00,000 — the Indian-lakh vs comma convention.)

## 3. Case Study: Reading a Postcode (Slides 15–23)

The deck uses handwritten-digit recognition to contrast rule-based vs learned approaches.

- **Slide 15 — "A Case Study: Reading Postcode":** problem setup (read handwritten digits off an envelope).
  - ✍️ **Instructor ink (Slide 15):** handwritten "**695…**" pin-prefix on the postcard; the envelope PIN boxes filled in red as "**5 0 0 0 7 2**"; a small red circle/"**0**" over the printed digit-card "0" and a red "**2**" with an arrow over the "2". — **Intent:** he literally read a real Indian PIN code off the envelope and tied each handwritten digit on the card to its class label, motivating digit recognition as the running case study (695…/500072 are real PIN codes).
  - 🖼️ **Figure (Slide 15):** a scanned envelope with a region-code key (North 1,2 / West 3,4 / South 5,6 / East 7,8) and a strip of the ten digit templates 0–9. **Takeaway:** reading a postcode = classifying each handwritten glyph into one of 10 digit classes.
- **Slide 16 — Hand-crafted rules (attempt):** trying to describe a digit in words, e.g. "right bend curve with sleeping line bottom," "semi-circle joined to a horizontal line at the bottom, making a swan-like shape." Constraints invented: (1) should not contain any complete circle, (2) cannot be only straight lines, (3) the straight line should be horizontal.
  - ✍️ **Instructor ink (Slide 16):** red hand-drawn shape sketches — a "right-bend curve + sleeping line", a small arch (semicircle), and a boxed red word "**Good**" beside the swan-shape description. — **Intent:** he sketched the very strokes the verbal rules describe and ticked the "swan" rule as a **Good** characterization — but the whole exercise sets up how impossibly fiddly hand-rules are, the punchline of the next slide.
- **Slide 17 — Rules as pseudo-code:** the rules become brittle `if/else` logic, e.g. "if (semi-circle left→right, then straight line, then acute angle, then straight line) else if (semi-circle left→right, then a knot to make a semi-circle again)…" — illustrating how unmanageable hand rules become.
- **Slide 18 — Reading Postcode:** shows the rule approach failing on real handwriting variation.
- **Slide 19 — Image Representation in Computer:** a digit image is just a grid of pixel numbers (intensities) the computer sees.
  - ✍️ **Instructor ink (Slide 19):** red note top-right (best-effort: "**Matrix / elements / each cell …**") with an arrow to the number grid, plus a small red "**0.5%?**" / value annotation near one cell, and a red box around a pixel. — **Intent:** he underscored that the image IS a matrix of intensity numbers (0=black … 255=white) — the computer never "sees" a digit, only this number grid.
  - 🖼️ **Figure (Slide 19):** the same digit shown as a shaded pixel grid set equal (=) to its numeric intensity matrix (mostly 255s with darker values tracing the stroke). **Takeaway:** to a computer an image is literally a 2-D array of pixel intensities.
- **Slide 20 — AI-Based Solution: Reading Postcode:** the learning recipe is "Data and Labels" → "Neural Network and Training" (instead of hand rules).
- **Slide 21 — AI for Reading Postcode [LeCun et al.] (the MNIST setup):**
  - A multi-layer network (Input → Layer 1 → Layer 3 → Layer 5 shown).
  - **All images are 28×28 grayscale.**
  - **60k training examples; 10k test examples.**
  - **Output value is an integer 0–9** (10 classes).
- **Slide 22 — Why learning is hard / what invariances are needed:** the model must be robust to **translation invariance, rotation invariance, scale invariance, squeeze invariance, stroke-width invariance, noise invariance.**
- **Slide 23 — AI: Inference / Testing:** a test digit cropped from an envelope is fed to the **Artificial Neural Network (ANN)**; the output is a one-hot vector (here the "7" position = 1, all others 0). "Testing samples extracted from envelope" → ANN → O/p.

- 🎙️ **Spoken (Slides 15–23):** He framed the case study around **IIT Kharagpur's own post office**: it receives mail for many locations but "doesn't have the manpower" to sort it, so imagine a **conveyor belt with a camera** photographing each envelope; the task = **classify each digit image into one of 10 classes (0–9)**. He noted the PIN code is "a very definitive thing" — *South India starts with 5 or 6, East with 7 or 8* (his own Kerala PIN starts ~695). Then the **key live exercise**: he asked the class to **crowd-source hand-written rules to recognize the digit "2"** and read their chat answers aloud — "right-bend curve with a sleeping line at the bottom," "a semicircle joined to a horizontal line at the bottom making a **swan-like shape**." He praised the swan rule ("I can't break this one... good"), then **deliberately broke every rule** by showing real handwritten 2s with **no semicircle** or **no horizontal line** — yet "everyone agrees it's a 2." Punchline he repeated *twice* for emphasis: **"If a problem is hard to solve with rules/algorithms, the good solution is a data-centric (AI) method."** Contrast he drew: for **F = m·a** a physics-derived rule beats data — *use rules when a clean rule exists, use data when it doesn't.* He rebutted the "standard 2" idea live ("there's no standard 2 — everything here is a 2") and the "compare to a template vector" answer the same way. He explained the **MNIST scale**: 28×28 grayscale, **60,000 training (~6,000 per digit if balanced) and 10,000 test** images, and listed the real-world **invariances** the model must survive — *different size, rotation, stroke width, bold vs ink/fountain pen, even dust if the postcard fell on the ground.* He also stressed: once trained, **"you can forget the data — keep only the network,"** and gave the mining-style synonyms for ML: **pattern recognition, knowledge distillation, data mining** ("from a large ore you extract the precious bit").

- 🎙️ **Spoken (Slides 24–27 — supervised intro):** He motivated supervised learning with the **mother-and-kid analogy**: a child holds up a yellow block and says "yellow," the mother says "good"; the child holds a green block and says "yellow," the mother says "no, that's not yellow" — through this **constant reinforcement** (the mother is the **supervisor**) the kid learns the concept. He mapped this to neurons: "the kid's neurons have a **chemical composition** that changes with the mother's supervision until it locks in; in an ANN we instead **fix numbers (weights)** that respond a particular way to a given input." Hence the name: "our brain is a network of neurons; we want something brain-like, but artificial → **Artificial Neural Network**." Definition he gave for supervised data: "there's an **input** and there's a **label** (is it correct or not) — the mother gives the label."

## 4. Outline & Supervised Learning Intro (Slides 24–27)

- **Slide 24 — Outline.**
- **Slide 25 — "Introduction to Supervised Learning"** (section divider).
- **Slide 26 — "Yellow color":** intuition image (learning to recognize an attribute / class).
- **Slide 27 — Neurons (biological motivation):** diagram of presynaptic cell → synapses → postsynaptic cell. **Definition:** *Synapses refer to the points of contact between neurons where information is passed from one neuron to the next.* (Biological inspiration for the artificial neuron.)

## 5. The ML Workflow — "AI: How to Solve It?" (Slides 28–33)

This is the deck's core workflow, repeated as a 4-quadrant cycle on many slides:

> **The 4 steps:**
> 1. **Collect Labelled Dataset**
> 2. **Design the Machine Learning Model** (here: Design an Artificial Neural Network)
> 3. **Define the Loss Function**
> 4. **Optimize the weights**

- **Slide 28 / 29 — "AI: How to Solve it?":** the 4-step cycle diagram. Quadrants: (1) Collect labelled dataset (labelled digit images), (2) Design ANN (784 input neurons for a 28×28 image → hidden layers → output), (3) Loss function (shown as a loss-surface bowl), (4) Optimize weights.
- **Slide 30 — "Collect Labelled Dataset"** (step-1 divider).
- **Slide 31 — Workflow cycle** (re-shown, highlighting step 1).
  - ✍️ **Instructor ink (Slide 31):** a green **✓ tick on "1. Collect Labelled Dataset"**; the ANN annotated with "**x → i/p**" (input) and "**y → o/p**" (output) labels; a red note near the top "**??? Form data, Fn**" and red "**ML model**" / "**supply your o/p**" callouts with arrows from the network to the output side. — **Intent:** he checked off step 1 as done and overlaid the input→model→output framing (x in, y out) so students see the labelled data feeding the model.
- **Slide 32 — "Design ANN Architecture"** (step-2 divider).
  - ✍️ **Instructor ink (Slide 32):** key matrix-algebra annotations on the **Ax** decomposition — "**Linear o/p**" (top right), an up-arrow + "**A**" under the weight matrix, "**x**" + "**i/p**" under the input vector, "**Ax**" + "**o/p**" under the result; and the crucial margin note "**learnable parameter(s)**" / "**I need to learn**" pointing at the **A** matrix. Also handwritten digits 0–9 and a blue/red ring around "**8**". — **Intent:** he drove home that the network layer is just **output = A·x** (a matrix multiply), and that **A (the weights) is what the model learns** — the heart of "design the model."
  - 🖼️ **Figure (Slide 32):** a 3×3 weight matrix **A** times input vector **x**, expanded column-by-column into **Ax**, set beside the 784-input MNIST network. **Takeaway:** a layer = matrix multiply A·x; learning = finding the entries of A.
- **Slide 33 — Workflow cycle** (re-shown, highlighting step 2).
  - ✍️ **Instructor ink (Slide 33):** green **✓ ticks on steps 1 and 2** with both circled; "**f(x,ω)**" written above the network; "**step 1 / step 2**" labels; and right-side notes "**optimize w.r.t. data → step 1**" plus small worked numbers "**λ₁ → 7%**", "**λ₂ … → ŷ / 0.05%**". — **Intent:** he marked steps 1–2 complete and previewed step 3/4 — that the model f(x,ω) will be optimized over the data, with λ (learning rate / weights) driving the error down toward a tiny value.

Note on step 2: input layer for a 28×28 image = **784 input neurons** (flattened pixels).

- 🎙️ **Spoken (Slides 28–33):** He ran another **live chat poll on step 1 ("how do you collect a labelled dataset?")** and read out the answers: **manually label it** (Saurabh Gupta — "you're the best person to know the outcome you want for your own problem"), use a **public dataset** (Pranavjeet Mishra — Hugging Face / Kaggle), **surveys/forms**, and **outsource via Amazon Mechanical Turk** ("Turkers create the data and you pay them"). For step 2 he defined a model as **"a mathematical function from input to output, parameterized by weights"** and wrote it as **Y = F(X, W)** — "time series is a vector, image is a matrix, video is a 3-D matrix, so it's just a mapping from a high-dim input to some output dim." Key spoken framing: **once you fix F (CNN vs RNN vs Transformer — each is a different F), the whole ML problem becomes "from the data, find/freeze W."** Then "forget the data, keep the network." He grounded it in **ChatGPT/Claude**: "they had a dataset, a model, a loss, and they optimized W on huge data — then they froze W and gave you the model; you just **supply your input** and it gives the output." The linear-network case: **output = A·x where A is the learnable parameter** ("this is what I need to learn").

## 6. Loss Functions (Slides 34–39)

### Cross-entropy Loss (classification) — Slides 34–35

- **Slide 34 — "Cross-entropy Loss — What we want?":**
  - Pipeline: Input image → **NN Layers** → **Logits (L)** → **Softmax** → **Output probabilities (P)** → Classes.
  - **Softmax formula:**
    ```
    S(y)_i = exp(y_i) / Σ_{j=1..n} exp(y_j)
    ```
  - Worked example logits [3.2, 1.3, 0.2, 0.8] → softmax probabilities [0.775, 0.116, 0.039, 0.070] for classes {Dog, Cat, Horse, Cheetah}.
  - We compare the network's softmax output **S** (e.g. [0.775, 0.116, 0.039, 0.070]) against the one-hot **target T** (e.g. [1, 0, 0, 0]) via the loss `L_CE(S, T)`.
  - ✍️ **Instructor ink (Slide 34):** green labels "**network o/p**" (over the S box) and "**Target**" (over the T box), a curved green arrow joining S↔T, and green ticks/circles beside the class list (Dog/Cat/Horse/Cheetah). — **Intent:** he named the two things the loss compares — the network's predicted probability vector **S** vs the ground-truth one-hot **T** — so cross-entropy is understood as a *distance between prediction and target*.

- **Slide 35 — "Cross-entropy Loss?" (the formula + worked numbers):**
  - **Cross-entropy loss:**
    ```
    L_CE = − Σ_{i=1..n} t_i · log(p_i)      (for n classes)
    ```
    where `t_i` is the truth label and `p_i` is the softmax probability for the i-th class.
  - **Worked Case 1 (good-ish output):** with S = [0.775, 0.116, 0.039, 0.070], T = [1,0,0,0]:
    ```
    L_CE = − [ 1·log2(0.775) + 0·log2(0.116) + 0·log2(0.039) + 0·log2(0.070) ]
         = − log2(0.775)
         = 0.3677
    ```
  - **Worked Case 2 (better output):** with S = [0.938, 0.028, 0.013, 0.023], T = [1,0,0,0]:
    ```
    L_CE = − 1·log2(0.938) + 0 + 0 + 0
         = 0.095
    ```
  - **Intuition (from the log(x) plot):** only the probability assigned to the *true* class matters; the closer that probability is to 1, the closer `−log(p)` is to 0, so lower loss = better prediction.
  - ✍️ **Instructor ink (Slide 35):** a green boxed "**Good**" by the formula; hand-drawn brackets/loops over the `t_i·log(p_i)` term marking that the **0-target terms vanish**; "**Case 1**" / "**Case 2**" labels; "**NN o/p**" labels on the two S vectors; a red **circle around the result `0.3677`** and around "**= 0.095**" with a red **down-arrow**. — **Intent:** he visually isolated the only surviving term (the true class's `−log p`) and circled both numeric answers to show **Case 2's lower loss (0.095 < 0.3677) = the better prediction** — lower CE means a more confident-correct model.
  - 🖼️ **Figure (Slide 35):** the `log(x)` curve (negative for x<1, →0 as x→1) with a blue bar under the [0,1] region. **Takeaway:** since p∈[0,1], `−log(p)` is large when p is small and →0 as p→1, so CE punishes low confidence on the true class.

### MSE Loss (regression) — Slides 36–38

- **Slide 38 — "MSE Loss":**
  - **Mean Squared Error:**
    ```
    MSE = (1/n) · Σ_{i=1..n} (Y_i − Ŷ_i)^2
    ```
  - Where: **MSE** = mean squared error; **n** = number of data points; **Y_i** = observed (true) values; **Ŷ_i** = predicted values.
  - Diagram: scatter of points with a fitted line; the vertical gap between each point and the line is labelled "Error" — MSE averages the squares of those gaps.
- **Slide 37 — "A Real Life Application":** "Input and Output are similar" through an ML model (auto-encoder / reconstruction style example where MSE is used).
  - ✍️ **Instructor ink (Slide 37):** red "**ANPR**" (automatic number-plate recognition) label near the ML-model arrow, red boxes/arrows linking the blurred input plate to its reconstructed output, and the underline of "**Input and Output are similar**". — **Intent:** he tagged the example as a real number-plate-recognition / reconstruction task where the **target ≈ input**, which is exactly the regime where **MSE (pixel-wise squared difference) is the right loss**.
  - 🖼️ **Figure (Slide 37):** a traffic camera → blurred number-plate crop → ML model (gear/network icon) → cleaned-up plate, with a column of recovered plates. **Takeaway:** when the desired output resembles the input (reconstruction), error is measured pixel-by-pixel via MSE.
- **Slide 39 — Workflow cycle** (re-shown, highlighting step 3, Loss Function).
  - ✍️ **Instructor ink (Slide 39):** green **✓ ticks on steps 1, 2 and 3** (Collect / Design / Define Loss), with "Optimize weights" left unticked. — **Intent:** progress check — three of the four workflow steps are now done; only optimization remains, cueing the next section.

- 🎙️ **Spoken (Slides 34–39 — losses):** He defined the loss back through the **mother analogy**: "computers only understand numbers, so the loss *is* the mother's reinforcement — **small loss = doing well, high loss = doing badly**." For cross-entropy he ran a **live chat poll** ("Case 1 vs Case 2 — which output is better for the dog example?") and the class correctly chose **Case 2** because its softmax is closer to the one-hot target [1,0,0,0]; he then showed the CE numbers confirm it (**0.095 < 0.3677** → lower loss = better). Verbal rule: "a good loss is **low when prediction is close to target, high when far** — that's how the computer knows it's working." For the **MSE/regression** example he used the **traffic-violation "AI cameras" / e-challan** story: cars in motion give a **blurry number-plate** image (plus dirt), so you train on **blurry-input ↔ clean-plate label pairs**, and since images are 2-D matrices the loss is **element-wise (pixel-wise) subtract → square → mean** (MSE). He noted target ≈ a cleaned version of the input, the regime where MSE is right. (See also Appendix A slide 37 — he tagged this **ANPR**, automatic number-plate recognition.)

## 7. Classification vs Regression (Slides 36, 59)

- **Slide 36 — "Classification vs Regression":**
  - **Regression:** Weather Data → model → **continuous** output (e.g. tomorrow's temperature = 29.5 °C / 29.116 °C). Plot: points with a best-fit line.
  - **Classification:** Weather Data → model → **discrete/categorical** output (e.g. Hot vs Cold tomorrow). Plot: two colored point clusters separated by a decision boundary.
  - ✍️ **Instructor ink (Slide 36):** red annotations on the regression row — "**Temp tomorrow (unclear)**" over the arrow, a red **circle around "29°C"** on the thermometer with "**Feb like**" beside it, and the precise values "**29.5 °C**" / "**29.116 °C**" written below; a red **oval around "Weather Data"** input. — **Intent:** he stressed that **regression outputs a precise continuous number** (29.5 / 29.116 °C, not just "warm"), contrasting with classification's Hot/Cold bucket on the lower row.
- **Slide 59 — "Classification Vs Regression"** (a 3×3 under/just-right/overfitting grid, re-shown before validation).
  - ✍️ **Instructor ink (Slide 59):** green loops/circles around the **overfitting** column illustrations (the contorted decision boundary on the classification row and the spiky curve on the regression row). — **Intent:** he singled out the overfit cases — a too-wiggly regression curve and a too-twisty classification boundary both have very low training error but high variance — reinforcing that overfitting shows up the same way in both task types.
  - 🖼️ **Figure (Slide 59):** a matrix — rows = Regression vs Classification illustrations, columns = Underfitting / Just-right / Overfitting, with a Symptoms row (high bias → balanced → high variance). **Takeaway:** the underfit→good→overfit progression (bias-variance trade-off) is identical for regression and classification.

- 🎙️ **Spoken (Slide 36):** He used the **weather "feels like" temperature** to nail the distinction: from the *same* weather data (temperature, humidity, wind speed) you can output **"hot or cold" — discrete → classification**, OR a precise **"feels like 29.5 °C / 29.116 °C" — continuous → regression**. Crisp verbal definitions: *classification = output is a discrete set of classes; regression = output is a continuous value.*

## 8. Optimization (Slides 40–44)

### Closed-form (calculus) conditions — Slide 40

- **Slide 40 — "Optimizing ANN: Closed Form Expression":** treat loss as `y = f(x, ω)`. Min/max via calculus:

  | Condition | Maximum | Minimum |
  |---|---|---|
  | Necessary | `dy/dx = 0` | `dy/dx = 0` |
  | Sufficient | `dy/dx = 0` and `d²y/dx² < 0` | `dy/dx = 0` and `d²y/dx² > 0` |

  - On a convex (bowl) loss: slope `dy/dx` is negative on the left, zero at the bottom (the minimum), positive on the right.
  - Cautionary curve: points A (local max), B (local min), C (saddle/inflection) — closed-form alone can land on the wrong stationary point.
  - ✍️ **Instructor ink (Slide 40):** red "**y = f(x, ω)**" written to the left of the table, and over the pink bowl curve "**Loss (f(x, ω)) = y**" (with "ω" / "y" relabelled). — **Intent:** he explicitly mapped the abstract calculus (y, dy/dx) onto our case — **y IS the loss, x/ω are the weights** — so "set derivative = 0 for a minimum" is understood as "find the weights at the bottom of the loss bowl." The A/B/C curve warns that derivative=0 alone can land on a max or saddle, motivating the 2nd-derivative (sufficient) test and, next, gradient descent.

### Gradient Descent — Slides 41–42

- **Slide 41/42 — "Optimizing ANN: Gradient Descent":**
  - Derivative definition: `f'(a) = lim_{h→0} [ f(a+h) − f(a) ] / h`.
  - Notation: **Loss is f()**, **ANN weight is a**, **λ (lambda) is the learning rate, λ > 0.**
  - **Question:** what happens to the loss change `f(a+h) − f(a)` if the weight update is `h = −λ·f'(a)`?
  - **Answer:** `f(a+h) − f(a)` is **negative**, which means `f(a+h) ≤ f(a)` — the loss decreases.
  - **Gradient-descent update rule:**
    ```
    a ← a − λ · f'(a)          (λ = learning rate)
    ```
  - Generalizing: each ANN weight is updated by subtracting the learning rate times the gradient.
  - ✍️ **Instructor ink (Slide 41):** the full derivation worked by hand around the limit definition — "**f(a+h) ≈ f(a) + h·f'(a)**", the substitution "**h = −λ·f'(a)**", the sign conditions "**λ > 0**", "**h < 0**", and "**f(a+h) − f(a) = −λ·[f'(a)]² ≤ 0**", with "**x → i/p**" tying x to the weight. — **Intent:** he derived *why* the update lowers the loss: plugging `h = −λf'(a)` makes the loss change equal `−λ(f'(a))²`, which is always ≤ 0 — proving each gradient step cannot increase the loss.
  - ✍️ **Instructor ink (Slide 42):** light reinforcement of the boxed update rule (the red "Update each ANN weight a as a − λ·f'(a)" box is emphasized/underlined). — **Intent:** the takeaway formula is the gradient-descent step itself; he flagged it as the slide's punchline.

### Importance of the Learning Rate — Slide 43

- **Slide 43 — "Importance of Learning Rate":**
  - Two loss landscapes shown: an **ideal** smooth convex bowl vs a **practical** bumpy non-convex surface (many local minima).
  - **Very large learning rate:** can jump into a bad region; may overshoot and keep oscillating.
  - **Very small learning rate:** may not be able to "cross" a hill to reach the good (lower) side; may take too long to converge.
  - Takeaway: the learning rate must be tuned — not too big, not too small.
  - ✍️ **Instructor ink (Slide 43):** annotations linking the two landscapes — "**h = −λ·f'(a)**", a sample value "**λ = 0.001**", a "**Better λ**" label, and "**h < 0**" with X-marks/arrows tracing the descent path on the bumpy surface (some marks unclear). — **Intent:** he tied the learning-rate story back to the update rule — λ scales the step size; too big overshoots into bad regions, too small stalls before crossing a hill; a "better λ" (e.g. ~0.001) navigates the non-convex surface to a good minimum.
  - 🖼️ **Figure (Slide 43):** an **ideal smooth convex bowl** (single global min) vs a **practical bumpy multi-modal surface** (many local minima/ridges). **Takeaway:** real loss surfaces aren't simple bowls, so the learning rate must be tuned to escape bad local regions without overshooting.
- **Slide 44 — Workflow cycle** (re-shown, highlighting step 4, Optimize Weights).
  - ✍️ **Instructor ink (Slide 44):** green **✓ ticks on all four steps** (Collect / Design / Loss / Optimize). — **Intent:** closes the loop — the full 4-step ML workflow is now complete.

- 🎙️ **Spoken (Slides 40–44 — optimization):** He derived gradient descent **from scratch on the board**: starting from the derivative definition, "we want an update **h** so that **f(a+h) < f(a)**; substitute **h = −λ·f′(a)** and you get **f(a+h) − f(a) = −λ·[f′(a)]²**, which (since λ>0) is always ≤ 0 — so the loss can't increase." He explained **λ must be small because the derivative approximation only holds as h→0** ("h→0 means a small learning rate"). On the **learning-rate landscape** he stressed real losses are *not* nice convex bowls — they have **local minima vs a global minimum**; and gave the counter-intuitive point: **both too-large AND too-small λ can get you stuck in a local minimum** — too large "jumps" into a bad basin, too small "can't cross a hill," and it also depends on **where you start**. Hence **λ is a hyperparameter** ("hyper because it has a *very big* implication") that needs tuning, not solving. In **Q&A** he addressed why we don't just use the closed-form solution for big models: "for a CNN or Transformer, even **finding the derivative** is hard, and then **isolating W** (W to the left, everything else to the right) is another challenge — it *exists*, you can find it if you're eager, but the **utility** is unclear" (he tied this to current interpretability research on "where information is stored in transformer weights").

## 9. Parametric vs Non-parametric Methods (Slides 45–46)

- **Slide 45 — "Parametric vs Nonparametric Methods?":** the workflow shown with a **parametric** model — an ANN with a fixed number of learned weights (e.g. 784 input neurons → hidden → output); the model has a fixed parameter count regardless of data size.
  - ✍️ **Instructor ink (Slide 45):** green **✓ ticks beside the 4 workflow steps**, marking the ANN as the worked (parametric) example. — **Intent:** signals "this is the model we already built end-to-end" before contrasting it with the non-parametric case on the next slide.
- **Slide 46 — same question, non-parametric example:** a **decision tree** built on the digit data — a non-parametric model where structure/complexity grows with the data rather than being a fixed set of parameters.
  - ✍️ **Instructor ink (Slide 46):** green ticks on the workflow steps; a red "**y → o/p**" and a **circled "?"** with a loop over the decision-tree root. — **Intent:** highlights that for a tree there is **no fixed weight vector** — the structure itself (and thus the number of "parameters") grows with the data, the defining trait of non-parametric models.
  - 🖼️ **Figure (Slide 46):** a decision tree branching on pixel/feature tests down to digit-class leaves, replacing the fixed-size ANN. **Takeaway:** non-parametric models (trees, k-NN) let complexity scale with the data instead of fixing it in advance.
- **Distinction:** *Parametric* methods have a fixed number of parameters (e.g. neural nets, linear models); *non-parametric* methods (e.g. decision trees, k-NN) let model complexity scale with the data.

- 🎙️ **Spoken (Slides 45–46):** He summed up the whole pipeline as **Y = F(X, W)** and called the parametric model **"the linchpin — every AI technique you use today (Claude, ChatGPT) works this way: a model F, optimize W on huge data, freeze W, ship it."** Then he flagged that **F need not be parametric — there can be models with no weights at all** (decision trees, which you'll meet later), where the structure itself grows with the data.

- 🎙️ **Spoken (data Q&A bridge):** Before the data-challenges section, a participant asked **how much data is needed** and **how ChatGPT/Claude differ if trained on similar public data**. His answers: the dataset must **"capture most of the variability the model will see at deployment"** (he used the **school-kid analogy — teachers give "4 pages of A, 4 pages of B" because experience says that's enough repetition to learn each letter**); and models differ on **everything — data, model, AND loss** ("if you want high accuracy on math questions, that requirement must be *translated into the loss*"). On a CNN-vs-Transformer question he gave a sharp **inductive-bias rule**: **CNN for tasks needing only local connections (deblurring — "a pixel's blur depends only on nearby pixels," segmentation), Transformer for connecting far-apart pieces (image Q&A, summarization); autonomous driving is multimodal/agentic (LiDAR depth + images + sound), not CNN alone.**

## 10. Data Challenges (Slides 47–52)

- **Slide 47 — "In Practice"** (divider: real-world data is messy).

- **Slide 48 — Data Challenge 1: Missing Data.**
  - *"Missing data is a source of error in any data set requiring correction as they can lead to serious problems."*
  - **Imputation methods** can be used to fill those gaps and provide a complete data set.
  - ✍️ **Instructor ink (Slide 48):** red **underline of "methods"** in "Imputation methods"; a red list of imputation strategies in the left margin — "**Mean**", "**Median**", "**Network / ML model (→ ∞?)**" and "**first tuple**", plus "**Median im(putation)**" written above the text; **red boxes drawn around the `NaN` cells** in the table with arrows pointing to them. — **Intent:** he made "imputation" concrete by listing how you actually fill a NaN — mean, median, or a model-based prediction — and circled the literal missing (NaN) entries in the sample table so students see exactly what gets imputed.
  - 🖼️ **Figure (Slide 48):** a student-records table with several `NaN` cells (missing Address/Marks/etc.). **Takeaway:** real datasets have holes; imputation (mean/median/model) fills them so the model can train on a complete table.

- **Slide 49 — Data Challenge 2: Errors vs Artifacts.**
  - Aspects of the real world → Raw Data → Processed Data.
  - Distinguishes **Errors** vs **Artifacts** as two different corruptions in raw/processed data.

- **Slide 50 — Data Challenge 3: Outliers.**
  - **Definition (Outlier):** *A data object that deviates significantly from the normal objects, as if it were generated by a different mechanism.*
  - Example: an unusual credit-card purchase.
  - Key points: **Outliers are different from Errors.** **Outliers are interesting** — an outlier violates the mechanism that generates the normal data.
  - Diagram: a scatter trending upward with one point far off ("HERE I AM") — fitting a line `y = w0 + w1·x` is distorted when an outlier pulls the fit.
  - ✍️ **Instructor ink (Slide 50):** red **underline of "deviates significantly … generated by a different mechanism"**; right side a green sketch of the clean fit "**Real life (error): y = w0 + w1·x**" through the points, then a second blue sketch "**Real life + outlier**" where one X sits far off the line, with red "**which you want to retain — outlier**" and a blue "**required line**". — **Intent:** he contrasted two regimes by hand — a normal noisy fit vs the same data with a true outlier — to show that an outlier (not an error) is a *meaningful* point you may want to keep, even though it tilts a naive least-squares line.
  - 🖼️ **Figure (Slide 50):** the printed scatter with a lone far-off point captioned "HERE I AM". **Takeaway:** an outlier is generated by a different mechanism than the bulk of the data — interesting, not just noise, and it can distort a fitted line.

- **Slides 51–52 — Data Challenge 4: Curse of Dimensionality.**
  - **Slide 51 — "More Data Requirement":** example datasets — MNIST (e.g. 16×16 digits), CIFAR (e.g. 64,000 images, 10 classes); a Healthy vs MCI classification on features "Type-to-token ratio" and "Lexical density."
    - (a) In **1-D** a handful of samples leaves a "dataset blind spot" gap.
    - (b) In **2-D** the same number of points becomes sparse — large blind-spot region — so you need far more data to cover higher-dimensional space.
    - Takeaway: as the number of feature dimensions grows, the amount of data needed to cover the space grows explosively.
  - ✍️ **Instructor ink (Slide 51):** red dataset annotations across the top — "**16×16 MNIST data**", "**64,000**" (circled) "**10 class / 10 class**", "**CIFAR10**" (circled), and the key contrast "**10 data**" (over the 1-D line) vs a big "**20 data**" (over the 2-D scatter); plus red circling of the "**Dataset blind spot**" gaps and "**Type-to-token ratio**", and a red oval around "**More Data Requirement**". — **Intent:** he showed that the *same* number of points that densely covers a 1-D line becomes sparse in 2-D (big blind spots), so higher dimensions demand far more data — the curse of dimensionality.
  - 🖼️ **Figure (Slide 51):** (a) points on a 1-D axis with small "blind-spot" gaps vs (b) the same count of points scattered in a 2-D plane leaving a huge empty "Dataset blind spot" region. **Takeaway:** adding feature dimensions makes a fixed dataset sparse, exploding the data needed to cover the space.
  - **Slide 52 — "Requirement of Complex ANN Model":** higher-dimensional / more-varied data (ball-pit analogy: 20 balls vs 30 balls in a bigger box) also demands a **more complex model**.
  - ✍️ **Instructor ink (Slide 52):** red labels "**Case 1 = 20**" over the small ball-pit and "**Case 2 = 30**" over the bigger box (with "**29**"/"**30**" counts), and a red **circle around "Complex"** in "Requirement of Complex ANN Model". — **Intent:** more/varied data (more balls in a bigger box) can't be captured by a simple model — it forces a **more complex (higher-capacity) network**, the flip side of the curse of dimensionality.

- 🎙️ **Spoken (Slides 47–52 — data challenges):** **Missing data:** "**never drop missing rows — data is precious; impute instead.**" Concrete missing-value example: a poll field like **death date** is legitimately blank for living people, or a **sensor fails**. He named the imputation methods aloud — **mean, median, and nearest-neighbour** ("find the closest entry by name/location and copy its value"). **Errors vs artifacts:** he ran a **chat poll** and quoted the winning answer — *"errors destroy information while artifacts create false information."* His own framing: **errors are unavoidable acquisition noise you can't control** (night-time camera noise, a human walking through the pig-pen frame); **artifacts are false information YOU created and CAN remove** — his vivid example: a **fintech team merging finance data from US (dollars), Europe (euros), and India (rupees) without unifying currency** → "like a mother teaching the kid wrong things; **a model is only as good as its data.**" **Outliers:** the **credit-card** example (you normally buy groceries, then one **international trip** spikes flights/hotels). Key spoken insight on *why* outliers hurt: **the loss is an aggregate Σ over all points with no discrimination, so a single far-off point shouting "consider me too!" drags the fitted line away from the ideal — so usually remove outliers.** **Curse of dimensionality:** he ran the **ball-pit thought experiment live** — "classify balls by colour in a flat **2-D** tray vs a deep **3-D** box; which is easier?" The class answered **2-D is easier, 3-D is harder** — proving by themselves that *higher dimension needs both more data AND a more complex model.* Practical rule he gave: **keep dimensions low** — for loan approval (income, expense, savings) adding a redundant feature like "3×income" gives **zero new information**, so prefer dimensionality reduction. He also previewed CIFAR-10 (32×32) needing far more data than MNIST (16×16/28×28) precisely because of the bigger blind-spot.

## 11. Model Story: Fitting an Elephant (Slides 53–56)

A cautionary parable about over-parameterization / over-fitting.

- **Slide 53 — "Deriving Physics Equations":** the *right* way to model — Experiment Set-up → Data Collection and Fitting → Model `Acceleration = Const × 1/mass` → Interpretation of the quantity (Const = Force, F). A good model has few, physically-meaningful parameters.
  - ✍️ **Instructor ink (Slide 53):** red derivation under the apparatus — "**Accel ∝ m⁻¹**" / "**A ∝ 1/m**"; red arrows on the trolley (direction of motion) and the hanging "2 kg mass"; on the graph "**A**" (acceleration) up the y-axis and "**Mass**" along the x-axis with an arrow. — **Intent:** he re-derived Newton's law from the measured curve — acceleration is inversely proportional to mass (a = F/m) — to show a *good* physical model: just one meaningful constant (the force F), not many free parameters.
  - 🖼️ **Figure (Slide 53):** trolley–string–pulley–mass setup → a measured acceleration-vs-mass curve (a falling 1/m shape) → the boxed model `Acceleration = Const × 1/mass`. **Takeaway:** a principled model fits the data with few physically-interpretable parameters (Const = Force).
- **Slide 54 — "Von Neumann about Fermi's Results":** introduces John von Neumann (1903–1957, digital computer, quantum physics, game theory) and Enrico Fermi (1901–1954, radioactivity, Fermi–Dirac distribution).
- **Slide 55/56 — The quote:**
  - Neumann: "How many arbitrary parameters have you used for the calculations?"
  - Fermi: "Many (with physical interpretation)."
  - **Neumann: "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk."**
  - Reference: *Mayer, Khairy, Howard (2010), "Drawing an elephant with four complex parameters," American Journal of Physics.* Figure: outline of an elephant with 4 params; three snapshots of a wiggling trunk via a 5th param.
  - ✍️ **Instructor ink (Slide 56):** red "**y = f(x)**" written over the elephant outline with a circle/loop, and red marks on the wiggling-trunk snapshots. — **Intent:** he reframed the parable in ML terms — the elephant IS a fitted function `y = f(x)` with just 4–5 tunable parameters — to make Neumann's point literal: enough free parameters reproduce any shape, so "it fits" ≠ "it's the right model."
  - **Moral:** enough free parameters can fit *anything* — fitting the data is not the same as having a correct/meaningful model (leads into overfitting).

- 🎙️ **Spoken (Slides 53–56 — Fermi/Neumann):** He told the anecdote as a **story**: Fermi (then a research scholar under Neumann) excitedly reported "I fitted a model to a 5–6-attribute quantum experiment and got **zero error** — a breakthrough!" Neumann was **unimpressed** and asked, *"How many arbitrary parameters did you use?"* Fermi: "**20** (a 20th-degree polynomial over 5 attributes)." Neumann's deflating reply: **"With four parameters I can fit an elephant, and with five I can make him wiggle his trunk."** His ML translation: "if your **F** is super-super-complex (a crore-crore parameters) it'll fit *any* function — but **it need not work in practice**." A 2010 paper actually *did* draw the elephant with 4 complex parameters (and wiggle the trunk with a 5th). Takeaway he stressed: **"research can mislead you — fitting the training data ≠ a correct model."**

## 12. Model Challenge 1: Complexity (Slides 57–58)

- **Slide 57 — "Model Challenge 1: Complexity"** (divider).
  - ✍️ **Instructor ink (Slide 57):** a small red **circle around "Degree 0"** (constant function) and a red mark/underline on "**Degree 1**" (linear), plus a red underline under "Complexity" in the title. — **Intent:** he pointed at the polynomial-degree ladder (0,1,2,…,5) to set up "model complexity = polynomial order" — low degree = too simple, high degree = too flexible, the theme of the next slide.
  - 🖼️ **Figure (Slide 57):** six small plots of polynomials of increasing degree (constant → linear → quadratic → … → quintic), each wigglier than the last. **Takeaway:** higher polynomial degree = higher model capacity/complexity (more turning points it can chase).
- **Slide 58 — Under/Good/Over-fit, side by side:**
  - **Case 1 — first-order polynomial → Underfitted** (model too simple, misses the trend).
  - **Case 2 — 10th-order polynomial → Good Fit / Robust** (captures the trend without chasing noise).
  - **Case 3 — 40th-order polynomial → Overfitted** (wiggles through every point, chasing noise).
  - **Key line: "Fit on training data ≠ Fit on testing/unseen data."** Over-fitting fits training noise and generalizes poorly.
  - ✍️ **Instructor ink (Slide 58):** "**Case 1 / Case 2 / Case 3**" labels over the three panels; green "**Good**" on the middle (10th-order) fit; "**Neumann**" written above Case 3 (tying back to the elephant); heavy red scribbling/circling over the overfit curve with "**Bad o/p**"; and the hand-written takeaway across the bottom: "**Fit on train(ing) data ≠ Fit on test(ing) data**". — **Intent:** this is *the* punchline of the complexity section — the wildly wiggling 40th-order curve nails the training points (red mess) but is "Bad o/p" on unseen data; only the middle fit generalizes. Good training fit ≠ good test fit.
  - 🖼️ **Figure (Slide 58):** three scatter+fit panels — a straight underfit line, a smooth curve through the trend, and a spiky curve threading every point. **Takeaway:** model complexity must match the data — too little underfits, too much overfits the noise.

- 🎙️ **Spoken (Slides 57–58):** Another **live chat poll** — "which model fits this data best, case 1/2/3?" Many students picked **Case 3 "because it fits all the data points,"** which was exactly the trap he wanted: he showed Case 3 (the spiky overfit) gives **terrible outputs on new/unseen inputs** even though it nails every training point, while the middle fit generalizes. Repeated rule: **"Fit on training data does NOT imply fit on testing data — training data only *optimizes* the model; the real aim is to work on unseen examples,"** and he tied it straight back to Neumann ("100 parameters can fit the data but need not be real"). He noted the same over/under-fitting picture holds for **classification** (a contorted boundary that mislabels an intuitively-blue point as orange).

## 13. Training vs Validation & Cross-Validation (Slides 60–62)

- **Slides 60–61 — "Training vs Validation: For Overfitting":**
  - Split the **complete training set** into a part **used for Training** and a part **used for Validation** (a held-out slice).
  - ✍️ **Instructor ink (Slide 60):** green annotations on the split bars — a circle around "**Available Data**", "**80%**" over the Training portion and "**20%**" over the Testing portion, and a green **oval around the "Validation (holdout sample)"** block with the note "**unseen example → Not used for tr(aining)**". — **Intent:** he made the data-splitting concrete: ~80/20 train/test, and a *validation* slice carved out that the model never trains on — its whole purpose is to estimate performance on **unseen** data and catch overfitting.
  - Error-vs-model-complexity curve: as complexity increases, **training error keeps falling**, but **validation error falls then rises**. Three regions: **Underfitting** (left, both errors high), **Optimal solution** (middle, validation error minimized), **Overfitting** (right, training error low but validation error high). Pick the model complexity at the validation-error minimum.
  - ✍️ **Instructor ink (Slide 61):** green "**optimize weight**" by the training block; the "**Used for Validation**" slice circled; three hand-drawn fit sketches labelled "**0 / 1 / 2**" (an underfit line through scattered x's, a good arch, and a wildly oscillating overfit curve) tied to "**step 0 / step 1 / step 2**"; green check at the **Optimal-solution** dip; and "**Valid(ation) error**" / "**Train error**" labels on the two curves with an arrow up at the overfit end. — **Intent:** he linked the three complexity sketches to the U-shaped validation curve — pick the model at the validation minimum (step 1), where the validation error bottoms out before overfitting drives it back up.
- **Slide 62 — K-fold Cross Validation:**
  - **Definition:** *K-fold cross validation: train on (K−1) folds and test on 1 fold as the validation set.*
  - Diagram: the data is split into K folds; in each round a different fold is the validation set (the rest are training). Example (K = 10): Round 1 → 93%, Round 2 → 90%, Round 3 → 91%, …, Round 10 → 95%.
  - **Final accuracy = Average(Round 1, Round 2, …, Round K).**
  - Benefit: every sample is used for both training and validation across rounds → more reliable estimate than a single split.
  - ✍️ **Instructor ink (Slide 62):** green arrows looping the title; the word "**validation**" handwritten inside the **highlighted (yellow) fold of each round** — round 1's top band, round 2's second band, round 3's third band, …, round 10's bottom band — plus a green bracket/arrow down the left of round 1. — **Intent:** he traced by hand how the validation fold *slides* to a different position each round, the defining mechanic of K-fold — so every fold serves as validation exactly once and the final score is the average across rounds.

- 🎙️ **Spoken (Slides 60–62 — validation & cross-validation):** He explained the **early-stopping logic** verbally: during gradient descent **training error keeps falling toward 0**, but **validation error first falls then shoots up** — "we **don't wait until training error = 0**; we stop where validation error is still low (the optimal regime)." Then he voiced the student's natural objection as a mini-dialogue: *"You already made me give precious data for training, and now you want 10% more just for validation — is that fair?"* — and introduced **K-fold cross-validation as the fix**: "you can use **all** the data for training *and* still validate, because the validation fold **rotates each round**, so every sample is used for both." He framed validation/cross-validation as the tool to **tune hyperparameters** (like how many iterations to run).

## 14. Model Challenge 2: Inductive Bias (Slide 63)

- **Slide 63 — "Model Challenge 2: Inductive Bias":** images (e.g. a swimming squirrel / a flying duck-like creature that looks "wrong") used to illustrate that a model carries built-in assumptions (inductive bias) about what patterns are plausible; these assumptions shape what it can and cannot learn / generalize to.
  - ✍️ **Instructor ink (Slide 63):** green **✓ ticks placed on several of the animal photos** (the swimming squirrel, the duckling, the gliding/flying squirrel). — **Intent:** he ticked the images that *violate* our built-in expectations (a squirrel swimming, a squirrel "flying") to dramatize inductive bias — a model, like our intuition, assumes some patterns are "normal" and is surprised/wrong on the rest; those priors both help and limit generalization.

- 🎙️ **Spoken (Slide 63 — inductive bias):** He built it as a **squirrel parable**: "the squirrel (= a machine-learning model) eats a pomegranate from a tree brilliantly — it can climb, jump, grab. But ask the same squirrel to **fetch something from water** (it can't swim well) or **catch something flying** — it fails." Meanwhile a **duck** (webbed feet, water-resistant) or an **eagle** (huge wingspan) is built for those. The lesson: **every model has a built-in strength and weakness — that's its inductive bias.** "CNNs are good at vision, Transformers at sequential data, GANs at generation — so don't learn one model and stop; for *every* new problem, always ask: **am I using a model whose strength matches this problem?** Otherwise no amount of optimization or cross-validation will save you."

## 15. Model Challenge 3: Evaluation — Confusion Matrix & Error Types (Slides 64–65)

- **Slide 64 — "Model Challenge 3: Evaluation" (the Confusion Matrix):**
  - Axes: **Reality** (columns: True / False) vs **Measured or Perceived = ML output** (rows: True / False).
  - The four cells:

    |                | Reality = True | Reality = False |
    |----------------|----------------|------------------|
    | **ML says True**  | **Correct → True Positive (TP)** | **Type 1 error → False Positive (FP)** |
    | **ML says False** | **Type 2 error → False Negative (FN)** | **Correct → True Negative (TN)** |

  - **Type 1 error = False Positive (FP)** (predicted positive, actually negative).
  - **Type 2 error = False Negative (FN)** (predicted negative, actually positive).
  - ✍️ **Instructor ink (Slide 64):** "**ML output**" written by the row axis (clarifying that rows = the model's prediction); "**Reality**" circled over the columns; **green ovals around each cell's name** — "True Positive", "False Positive", "False Negative", "True Negative" — and margin notes "**Really / ML could predict / True positive / False (Type 1)**" working out the naming convention. — **Intent:** he hand-decoded the confusion matrix's naming rule live: the **second word** (Positive/Negative) is *what the model said*, the **first word** (True/False) is *whether it was right* — so FP = model said positive, reality negative (Type 1), FN = model said negative, reality positive (Type 2).
  - 🖼️ **Figure (Slide 64):** the 2×2 grid — green diagonal (Correct: TP, TN with smileys) vs the off-diagonal errors (Type 1 = FP, Type 2 = FN). **Takeaway:** every prediction lands in one of four cells; the two off-diagonal cells are the two distinct error types.

- 🎙️ **Spoken (Slide 64 — confusion matrix):** He motivated evaluation with the **sprint-vs-marathon analogy** (after a chat request for "less mathematics"): "you're the judge of a running race — but a **100 m sprint** (short, high-intensity) and a **marathon** (long, moderate) must be **evaluated differently**, even though both are 'running.' Likewise, two models both doing classification may need *different* metrics." He then gave the **naming mnemonic verbally**: read each cell as two words — **the second word = what the model predicted (positive/negative), the first word = whether that was right (true/false).** So **False Positive = model said yes, reality no; False Negative = model said no, reality yes.**

- **Slide 65 — "Error Types: Case Study":** which error hurts more depends on the application —
  - **Cancer Diagnostics:** a False Negative (missing a real cancer) is the costly error.
  - **Anti-missile System:** a False Negative (missing an incoming missile) is catastrophic.
  - **Weather Predictions:** the FP/FN trade-off is more forgiving.
  - Lesson: choose the metric (precision vs recall) according to which error type is more dangerous in context.
  - 🎙️ **Spoken (Slide 65 — which error costs more):** He ran it as a **live chat poll across all three cases** and reasoned each aloud. **Cancer:** "a **False Positive** (told you have cancer, you don't) just causes stress → a follow-up clears it; but a **False Negative** (told you're clear, you actually have cancer) is catastrophic — *'I'm fine, I'll smoke and drink,' then he's in a critical ward in two months.*" So **minimize FN here**. **Anti-missile:** **False Positive** = shoot down a **domestic/civilian aircraft** ("it has happened recently") → minimize FP; **False Negative** = miss a real enemy → also deadly, so both matter but FP is the highlighted danger he wrote "Previous" next to. **Weather** (pleasant → go play football; non-pleasant → stay home and watch Netflix): **both errors are low-stakes / equally tolerable.** Core line: **"the running race is the same, but how you evaluate depends on the application."** He corrected students who answered "make True Positive less" — "no, TP/TN are the *good* cells, keep them as high as possible; it's **FP and FN** that are the dangerous guys."
  - ✍️ **Instructor ink (Slide 65):** *(resolved from the PNG + transcript)* dense red/green "**TP / TN / FP / FN**" written over all three case-study photos, numbered **①②③**, with the costly error flagged in each — on **Cancer ①** the dangerous **FN** marked (told "no cancer" when there is); on **Anti-missile ②** "**FP**" with the word "**Previous**" + arrow (he said live "it has happened **recently** — a domestic aircraft shot down," i.e. a costly false positive, hence "Previous" = a real prior incident); on **Weather ③** "**pleasant or non-pleasant**" written with all four cells scattered (low stakes, both errors tolerable). — **Intent:** he hand-worked each scenario to show **the same error type carries wildly different costs by domain** — minimize **FN** (recall) for cancer, minimize **FP** (precision) for anti-missile, while weather is forgiving either way.

## 16. Performance Metrics (Slide 66)

- **Slide 66 — "Performance Metrics" table.** Key: **tp** = True Positive, **tn** = True Negative, **fp** = False Positive, **fn** = False Negative.

  ```
  Accuracy  = (tp + tn) / (tp + tn + fp + fn)
  Precision = tp / (tp + fp)
  Recall    = tp / (tp + fn)
  F1-score  = 2 · (precision · recall) / (precision + recall)
  Confusion matrix = NA (a table, not a single number)
  ```

  **When to use each (from the slide):**
  - **Accuracy** — default metric for classification problems; *not* the best for imbalanced classes.
  - **Precision** — higher precision ⇒ fewer false positives. (If FP = 0 then precision = 100%.)
  - **Recall** — higher recall ⇒ fewer false negatives. (If FN = 0 then recall = 100%.)
  - **F1-score** — combination of precision and recall; usually a good overall metric for a classification model.
  - **Confusion matrix** — compare predictions to truth labels to see where the model gets confused; can be hard to use with a large number of classes.
  - ✍️ **Instructor ink (Slide 66):** red ring around "**Accuracy**"; "**(FP)**" circled beside Precision with "**100% ⇒ 0 FP**" (i.e. `(fp)=0`) written in the margin; "**(FN)**" circled beside Recall with "**100% ⇒ 0 FN**" (`(fn)=0`); and red circling of the **fp** term in the Precision denominator and the **fn** term in the Recall denominator. — **Intent:** he tied each metric to the error it kills — drive **fp→0 and Precision→100%**, drive **fn→0 and Recall→100%** — making explicit which knob (precision vs recall) you push given which error type matters most (callback to slide 65).

- 🎙️ **Spoken (Slide 66 — metrics):** Spoken mapping: **Accuracy cares about FP and FN equally; Precision = 100% means FP = 0** (so use precision for the **anti-missile** case where you must not fire on civilian aircraft); **Recall = 100% means FN = 0** (use for **cancer**); **F1 is the harmonic mean of precision and recall**, and there's also a **weighted F1** ("if precision matters more, weight it 80/20"). The closing punchline tied metrics back to losses: **"your loss must be consistent with the performance metric you care about — if your loss is biased toward FN but you actually care about FP, you'll fail. Optimizing the loss must minimize *your* objective."**

## 17. Unsupervised Learning (Slides 67–70)

- **Slide 67 — "Introduction to Unsupervised Learning"** (divider).
- **Slide 68 — "vs":** supervised (labelled — kids told which flower is which) vs unsupervised (no labels — group similar flowers; e.g. hibiscus colors vs an iris).
- **Slide 69 — Clustering:** the classic **Iris** example — species Versicolor, Setosa, Virginica described by petal/sepal length & width; a 2-D scatter shows the points forming clusters (with centroids), grouped without using labels.
  - ✍️ **Instructor ink (Slide 69):** green labels drawn on the iris photo — "**petal**" (with width/length arrows) and "**sepal**" (with width/length arrows). — **Intent:** he hand-annotated the four measured features (petal length/width, sepal length/width) that become the coordinates in the scatter — emphasizing that clustering groups flowers purely by these feature values, with **no species labels used**.
  - 🖼️ **Figure (Slide 69):** photos of the 3 iris species → an annotated flower (petal/sepal dimensions) → a 2-D feature scatter where points self-organize into 3 colored clusters with centroids. **Takeaway:** clustering discovers the species-like groups from feature geometry alone, unsupervised.
- **Slide 70 — Association:** association-rule mining (finding items/events that co-occur, e.g. market-basket style relationships).

- 🎙️ **Spoken (Slides 67–70 — unsupervised):** **Clustering** told as the **Flower Show kids story**: he takes kids to a flower show and *says nothing* (no labels); the kids wander, and on their own start saying "this flower is similar to that one, and different from this one." He's "astonished — I taught nothing," yet they **grouped alike things and separated unlike things** — that's clustering, learning structure with **no labels**. **Association** told as a **Margin Free supermarket billing-agent story**: after a month at the till "nobody tells me anything, but I notice patterns — people who buy **bread also buy butter and jam**; **milk-buyers buy tea and sugar**; **biscuit-buyers buy Lays.**" Finding "if one item comes, the other comes too" — purely from data — is **association**.

## 18. Reinforcement Learning (Slides 71–76)

- **Slide 71 — "Introduction to Reinforcement Learning"** (divider).
- **Slides 72–73 — Reinforcement Learning:** an agent learns by interacting with an environment and receiving feedback (reward/penalty).
  - 🖼️ **Figure (Slide 73):** an **Actor** box (the policy network acting inside an "Environment") feeding experience to a **Learner** box (which updates the policy), with dashed loops between them and a tic-tac-toe board / robot as the task. **Takeaway:** RL is a closed loop — the actor takes actions in the environment, the learner uses the resulting reward to improve the policy, repeat.
- **Slides 74–75 — RL walking/locomotion example:**
  - **Objective: "Move forward while minimizing how often it fails and the energy it expends."**
  - Shows a **Learning Phase** where the agent improves its policy over trials.
- **Slide 76 — RL example continued** (image of the learned behavior).
  - 🖼️ **Figure (Slide 76):** a side-by-side comparison of the three paradigms as feedback loops — **Supervised** (Input = data *with* labels → Output = mapping, a "Critic" computes Error), **Unsupervised** (Input = data *without* labels → Output = classes/clusters, no error signal), **Reinforcement** (Input = states & actions → Output = state/action, a Critic returns a **reinforcement signal/reward**). **Takeaway:** the three learning types differ by *what feedback they get* — labelled error, no feedback, or a reward signal.

- 🎙️ **Spoken (Slides 71–76 — reinforcement learning):** He contrasted RL with the earlier paradigms: "supervised and unsupervised are **single input → single output**; RL is a **sequence of actions (a 'pulsing'/policy)** where success depends on the *whole sequence*, not one action." Told via a **kid-in-a-park** story: a child explores **multiple routes to the favourite slide** ("this path is crowded, that one I can manage"), tries different paths, and **eventually learns the best route** — "I don't care which way I went, only whether my steps reached the happy place efficiently." A second example: **chess** — "Pragg (Praggnanandhaa) sometimes makes a deliberately 'dumb' move that's actually strategic to confuse the opponent; **if he wins at the end, it was a good move**" — reward is judged at the *end*, not per-move. He also showed the **robot-locomotion** example (learning to balance/walk in unconstrained scenarios: "if my balance tips left, put the left leg out") and name-dropped **Boston Dynamics** and a **Chinese robotic police dog** as deployed RL. Closing synthesis: **supervised = a critic/mother/loss gives the signal; unsupervised = no signal, find features yourself; reinforcement = a sequence of actions rewarded only if it reaches the goal** ("if I succeed, tell my brain this path is good; if I fail, don't take it again").

## 19. Summary of "Intro to Machine Learning" (Slide 77)

- **Slide 77 — Taxonomy summary:**

  ```
  Machine Learning
  ├── Supervised Learning   (Parametric / Non-parametric)
  │     ├── Classification   (separate classes — scatter with a decision boundary, "?" point to classify)
  │     └── Regression       (fit a continuous line through points)
  ├── Unsupervised Learning
  │     ├── Clustering       (group similar points — colored blobs)
  │     └── Association      (find co-occurring items/relationships)
  └── Reinforcement Learning (learn by reward via interaction)
  ```

  This ties the whole deck together: the supervised branch (classification & regression) was the main focus — its workflow (data → model → loss → optimize), losses (cross-entropy, MSE), optimization (gradient descent), the parametric/non-parametric split, the data & model challenges, validation/cross-validation, and the evaluation metrics — with unsupervised and reinforcement learning introduced as the other two paradigms.

  - ✍️ **Instructor ink (Slide 77):** red **underline/loop around "Supervised Learning"** (and its "Parametric / Non-parametric" subtitle), a red line connecting the Supervised node down to **Regression**, "**99%**" written under the classification scatter, and a bottom scrawl now read as "**Data, model, loss**" *(resolved from the PNG)* under the regression scatter, with a long red sweep down the right side. — **Intent:** on the closing taxonomy he re-emphasized that **supervised learning (classification & regression) was the day's core** — the branch where he built the full **data → model → loss (→ optimize)** pipeline (exactly the words he closed the section with) and chases high accuracy (~99%); the unsupervised and reinforcement branches were only previewed. The "Data, model, loss" scrawl literally recaps the 4-step workflow.

---

## ✍️ Appendix A — Instructor Handwritten Annotations (live-class emphasis)

Pen/marker strokes the professor added on top of the printed slides during the live class. Where ink was partly illegible it is marked "(unclear)" and intent inferred from context.

| Slide | What he wrote/marked | Inferred teaching point |
|---|---|---|
| 1 | Short red cursive scribble in left margin, best read "Chit"/initials | **Stray pen-test / name-tag stroke** while renaming the session (transcript's setup minute); no concept. |
| 3 | Red "2" step-marker on arrow; margin sketch "pointing model by … windmill", "store data in memory", "x → ht of its windmill" | **The windmill height-vs-power example** — a 1-D signal across a *non-time* axis (height/distance). *(Resolved from transcript; earlier "polynomial/window" reading was a misread.)* |
| 4 | "Profit"; "E→Env, S→Soc, G→Govern"; "A*" over the forecast fan | Expanded ESG; tied forecasting to business risk; flagged the uncertainty cone. |
| 7 | "R, G, B"; tuples (128,0,0), (0,255,0), (0,0,0), (255,255,255) | A colour pixel is an (R,G,B) triple → image is H×W×3 numbers. |
| 8 | "Sharp"/"Blurred i/p", "Humans", "Bike", "Background", input→output arrows | Walked through semantic segmentation vs object detection on the examples. |
| 9 | "2D / single image", "10→time", "30", "3D", "sequence of video frames", "RGB-1/RGB-2" | Derived video dimensionality: image is 2-D; stacking frames over time → 3-D. |
| 10 | Red carets/arrows over blurred and deblurred frame stacks | Points to the per-frame blur→sharp change. |
| 11 | Dimension tags "5×8×30" and "6×4×30" (now legible) over the **pig-pen** colour video | Colour video = H×W×frames → 4-D data (the Illinois pig-activity clip, 15 fps over 4 months). |
| 13 | "stored disk"; "20k", "mobile phone" pointing at old mainframe | A modern ~20k phone beats a 1990s mainframe — bottleneck was hardware, not algorithms. |
| 14 | "1×16", "10,000×16", "1,00,000", "10,000" on CPU/GPU cores | Quantified GPU parallelism (thousands of cores) as the compute enabler. |
| 15 | "695…" on postcard; PIN "5 0 0 0 7 2" filled in; circle on digit "0", arrow+"2" | Read a real PIN code off an envelope to motivate digit classification. |
| 16 | Red shape sketches (curve+line, semicircle); boxed "Good" by swan rule | Sketched the strokes the verbal rules describe; sets up how brittle hand-rules are. |
| 19 | "Matrix / elements" note + arrow to grid; "0.5%?"; pixel boxed | The image IS a matrix of intensity numbers (0=black…255=white). |
| 31 | Green ✓ on step 1; "x→i/p", "y→o/p"; "ML model", "supply your o/p" | Step 1 done; overlaid input→model→output framing. |
| 32 | "Linear o/p"; "A", "x i/p", "Ax o/p"; "learnable parameter(s) / I need to learn"; "8" ringed | A layer = output = A·x; **A (weights) is what's learned**. |
| 33 | Green ✓ on steps 1&2; "f(x,ω)"; "optimize w.r.t. data → step 1"; "λ₁→7%…" | Steps 1–2 complete; previewed optimizing f(x,ω) over the data. |
| 34 | Green "network o/p" over S, "Target" over T; curved arrow joining them; class ticks | Loss compares predicted vector S to one-hot target T. |
| 35 | Boxed "Good"; brackets over t·log(p); "Case 1/2"; "NN o/p"; circles on 0.3677 and 0.095; down-arrow | Only the true class's −log(p) survives; lower CE (0.095<0.3677) = better. |
| 36 | "29°C" circled "Feb like"; "29.5°C", "29.116°C"; "Weather Data" ovalled | Regression outputs a *precise continuous number*, not a bucket. |
| 37 | "ANPR"; red boxes/arrows input→output; underline "Input and Output are similar" | Reconstruction task where target≈input → MSE is the right loss. |
| 39 | Green ✓ on steps 1, 2, 3 (not 4) | Three of four workflow steps done. |
| 40 | "y = f(x,ω)" by table; "Loss (f(x,ω)) = y" over the bowl | y IS the loss, ω the weights; minimum = bottom of the loss bowl. |
| 41 | Full GD derivation: "f(a+h)≈f(a)+h·f'(a)", "h=−λf'(a)", "λ>0", "f(a+h)−f(a)=−λ[f'(a)]²≤0" | Proves each gradient step cannot increase the loss. |
| 42 | Update-rule box "a − λ·f'(a)" emphasized | The gradient-descent step is the slide's punchline. |
| 43 | "h=−λf'(a)", "λ=0.001", "Better λ", "h<0", X-marks on the bumpy surface | λ scales step size; tune it to cross hills without overshooting. |
| 44 | Green ✓ on all 4 steps | Full ML workflow complete. |
| 45 | Green ✓ on the 4 steps (parametric ANN example) | "This is the model we built end-to-end." |
| 46 | Green ✓; "y→o/p"; circled "?" over the tree root | A tree has no fixed weight vector — structure grows with data (non-parametric). |
| 48 | Underline "methods"; list "Mean / Median / Network-ML model / first tuple"; red boxes round NaN cells | Imputation = filling NaNs by mean/median/model. |
| 50 | Underline of outlier definition; green "y=w0+w1·x" fit; blue "Real life + outlier / required line"; "which you want to retain — outlier" | An outlier (≠ error) is a meaningful point that can tilt a naive fit. |
| 51 | "16×16 MNIST", "64,000" ringed "10 class", "CIFAR10" ringed; "10 data" vs big "20 data"; blind-spot circles; "More Data Requirement" ovalled | Same points dense in 1-D become sparse in 2-D → curse of dimensionality. |
| 52 | "Case 1 = 20", "Case 2 = 30"; "Complex" circled | More/varied data forces a more complex (higher-capacity) model. |
| 53 | "Accel ∝ 1/m", "A"/"Mass" axis labels, arrows on trolley & mass | Re-derived a = F/m — a good model has one meaningful constant (Force). |
| 56 | "y = f(x)" looped over the elephant; marks on trunk snapshots | The elephant is a 4–5-param fitted function: "it fits" ≠ "it's right". |
| 57 | "Degree 0" circled, "Degree 1" marked; underline of "Complexity" | Model complexity = polynomial order. |
| 58 | "Case 1/2/3"; green "Good" on middle; "Neumann"; "Bad o/p"; red overfit scribble; "Fit on train data ≠ Fit on test data" | Overfit curve nails training points but fails on unseen data. |
| 59 | Green loops around the overfitting column (regression & classification) | Overfitting (high variance) looks the same in both task types. |
| 60 | "Available Data" circled; "80%"/"20%"; "Validation" ovalled; "unseen example → Not used for training" | Validation slice is held out, never trained on, to catch overfitting. |
| 61 | "optimize weight"; "Used for Validation" circled; "0/1/2" fit sketches + "step 0/1/2"; ✓ at optimal; "Valid error"/"Train error" | Pick the model at the validation-error minimum (before overfitting). |
| 62 | Green arrows on title; "validation" written in the moving (yellow) fold of each round | The validation fold slides each round → every fold validates once. |
| 63 | Green ✓ on the "surprising" animal photos (swimming/flying squirrel, duckling) | Inductive bias = built-in priors about what's "normal"; helps and limits generalization. |
| 64 | "ML output" on rows; "Reality" circled; green ovals on TP/FP/FN/TN; naming-rule notes | 2nd word = what model said, 1st word = whether it was right; FP=Type 1, FN=Type 2. |
| 65 | "TP/TN/FP/FN" over all 3 cases numbered ①②③; **FN** flagged on Cancer ①, **FP** + "Previous" arrow on Anti-missile ②, "pleasant or non-pleasant" on Weather ③ | Same error type costs differ wildly by domain → minimize **FN/recall** for cancer, **FP/precision** for anti-missile ("recently a domestic aircraft was shot down"), weather forgiving. |
| 66 | "Accuracy" ringed; "(FP)" + "100%⇒0 FP"; "(FN)" + "100%⇒0 FN"; fp/fn denominators circled | Push precision (fp→0) or recall (fn→0) depending on which error matters. |
| 69 | Green "petal"/"sepal" with width/length arrows on the iris | Clustering groups flowers by feature geometry — no labels used. |
| 77 | "Supervised Learning" underlined/looped; line to Regression; "99%"; "**Data, model, loss**" scrawl under the regression scatter (resolved) | Recap: supervised (classification & regression) was the day's core — the **data → model → loss → optimize** pipeline. |

## 🖼️ Appendix B — Key Figures & What They Teach

The concept-bearing visuals in the deck (the picture *is* the lesson).

| Slide | Figure | Concept it conveys |
|---|---|---|
| 4 | History line up to 2025 then a widening red→orange forecast band | Forecasting predicts the future with growing uncertainty the farther out you go. |
| 5 / 19 | Digit shown as a shaded pixel grid set equal to its 0–255 intensity matrix | To a computer, an image is literally a 2-D array of pixel intensities. |
| 7 | Bird image + stacked R/G/B matrix cube + colour→RGB table | A colour image is three stacked intensity planes (H×W×3). |
| 9 | 2-D frame → stack of frames along an X-Y-Time axis | Video stacks 2-D frames over time → a 3-D (H×W×T) volume. |
| 14 | CPU (few cores) vs GPU (thousands of cores) beside big-data logos | Abundant data + massive parallel compute = why ML took off. |
| 21 | LeNet-5 MNIST demo: layered net, 28×28 input, answer "0" | Learned digit recognition replaces brittle hand rules (60k train / 10k test, 0–9). |
| 24 / 77 | ML taxonomy tree with a sample plot under each leaf | Supervised (classify/regress) vs Unsupervised (cluster/associate) vs Reinforcement. |
| 27 | Presynaptic → synapses → postsynaptic neuron diagram | Biological neuron/synapse is the inspiration for the artificial neuron. |
| 32 | A·x matrix multiply expanded column-by-column beside the MNIST net | A network layer is a matrix multiply; learning = finding the weights A. |
| 34 | Image → NN → Logits → Softmax → probabilities → classes (dog/cat/horse/cheetah) | Softmax turns raw logits into a probability vector for classification. |
| 35 | log(x) curve, negative for x<1, →0 as x→1 | −log(p) punishes low confidence on the true class; →0 when p→1. |
| 38 | Scatter with a fitted line; vertical "Error" gaps marked | MSE averages the squared vertical residuals between points and the fit. |
| 40 | Convex bowl (slope −/0/+) + A/B/C curve (max/min/saddle) | Minimum where derivative=0 and 2nd-derivative>0; derivative=0 alone is ambiguous. |
| 43 | Smooth convex bowl vs bumpy multi-modal loss surface | Real loss surfaces have many local minima → learning rate must be tuned. |
| 51 | Points on a 1-D line vs same count scattered sparsely in 2-D | Adding dimensions makes a fixed dataset sparse → curse of dimensionality. |
| 55–56 | Elephant outline drawn from 4 params; trunk wiggles with a 5th | Enough free parameters fit anything — fitting ≠ a correct model. |
| 58 | Three scatter+fit panels: underfit line / good curve / spiky overfit | Complexity must match the data; good training fit ≠ good test fit. |
| 60–61 | Train/validation/test split bars + U-shaped validation-error curve | Held-out validation reveals overfitting; pick the validation-error minimum. |
| 62 | K folds with the validation fold sliding each round (93/90/91…95%) | K-fold uses every sample for both train and validation → robust estimate. |
| 64 | 2×2 confusion grid: green diagonal (TP/TN) vs FP (Type 1)/FN (Type 2) | Every prediction lands in one of four cells; off-diagonal = the two error types. |
| 69 | Iris species photos → petal/sepal features → 2-D scatter forming 3 clusters | Clustering discovers groups from feature geometry alone (unsupervised). |
| 73 / 76 | Actor↔Learner↔Environment loop; supervised/unsupervised/RL feedback comparison | The three paradigms differ by feedback: labelled error, none, or a reward signal. |

## 🎙️ Appendix C — Spoken Examples & Real-World Case Studies (per section)

The concrete stories the professor told *aloud* (not on the slides). Several are from his own group's work in **semiconductors / embedded / sensors / defence** — flagged ⚙️ where domain-relevant.

| Section / Slides | Spoken example or story | The concept it illustrates |
|---|---|---|
| 1 / Slide 3 | ⚙️ **Windmill height-vs-power** — same power at small height in the flat Sahara, but only at large height in tall-building Mumbai | 1-D data can vary across a *non-time* axis (height/distance), not just time |
| 1 / Slide 4 | **Kunal, the part-time PhD scholar** (company director, finance bg) whose ESG paper hit **ICML**; team flying to South Korea; **cigarette = profit but harms environment & society** | Time-series forecasting; ESG = Environment/Society/Governance balancing profit |
| 1 / Slide 6 | ⚙️ **KLA-Tencor SEM chip-defect inspection** — denoise grayscale scanning-electron-microscope images of fabricated chips (mobile/laptop/GPU) for QC | Grayscale image analysis; why SEM imaging is grayscale; microscopic defect detection |
| 1 / Slide 8 | ⚙️ **Autonomous driving** — motion-blurred camera frames deblurred *before* semantic segmentation (pink=human, green=bike) and object detection (boxes + confidences) | Colour image analysis; deblurring as a pre-step for downstream CV |
| 1 / Slide 10 | ⚙️ **DRDO submarine IR gimbal** — periscope IR camera does 360° gimbal rotation on surfacing; gimbal motion blurs footage → recover clean video | Grayscale-video analysis; motion deblurring for defence sensing |
| 1 / Slide 11 | ⚙️ **U. Illinois pig-pen monitoring** — 24/7 camera, classify each pig + track activity (15 fps, 4 months) to flag sick (inactive) pigs early | Colour-video analysis; temporal cue (activity over time) is essential |
| 2 / Slides 12–14 | **Punched-paper data storage** + "a 1990s room of vacuum tubes < a modern ₹20K phone"; **you create data** by browsing/uploading; **CPU 16 cores → 2-3 months vs GPU thousands → minutes** for 10 lakh images | Why ML booms now: data + GPU compute were the missing pieces, not algorithms |
| 2 / Slides 12 | **Live chat poll**: "why didn't AI boom before 1990?" → class answered "lack of data," "weak compute/hardware" | Crowd-sourced the two historical bottlenecks |
| 3 / Slides 15–18 | **IIT KGP post-office conveyor-belt sorter**; **live crowd-sourced rules for digit "2"** (the "swan-shape" rule), then broke every rule on real handwriting | Rules are brittle for perceptual tasks → use a data-centric (AI) method |
| 4 / Slides 26–27 | **Mother-and-kid "yellow block"** reinforcement; kid's neuron *chemistry* changes ↔ ANN *weights* are fixed | Supervised learning = input + label + a supervisor's feedback |
| 6 / Slide 37 | ⚙️ **Traffic e-challan "AI cameras"** — deblur the moving-car number plate (ANPR), MSE on pixel differences | MSE/regression for reconstruction where target ≈ cleaned input |
| 10 / Slide 49 | **Fintech merging US-$ / EU-€ / India-₹ data without unifying currency** → an *artifact* (false info you created and can remove) vs *error* (unavoidable acquisition noise) | Errors vs artifacts; "a model is only as good as its data" |
| 10 / Slide 50 | **Credit-card outlier** — one international trip spikes spending; the aggregate loss has no discrimination so it drags the fitted line | Outliers distort least-squares fits → usually remove them |
| 10 / Slides 51–52 | **Live ball-pit experiment** — classify ball colours in a flat 2-D tray vs a deep 3-D box; class agreed 3-D is harder. **Loan: "3×income" adds zero info** | Curse of dimensionality → more dims need more data *and* a more complex model |
| 11 / Slides 54–56 | **Fermi proudly fits a 20-parameter model with zero error; Neumann: "with four parameters I can fit an elephant, with five make him wiggle his trunk"** | Over-parameterization: fitting ≠ a correct model |
| 12 / Slide 58 | **Live poll** — class picked the spiky "fits all points" curve (Case 3); he showed it fails on unseen inputs | "Fit on training data ≠ fit on test data" |
| 13 / Slides 60–62 | Student-objection dialogue: "you want *more* of my precious data just for validation?" → **K-fold rotates the validation fold so all data trains** | Validation/early-stopping; cross-validation reclaims held-out data |
| 14 / Slide 63 | **Squirrel parable** — great at trees/pomegranates, useless in water or flying; a duck/eagle is built for those | Inductive bias = each model's built-in strength/weakness (CNN↔vision, Transformer↔sequence) |
| 15 / Slide 64 | **Sprint vs marathon judging** — both "running" but evaluated differently | Choose the evaluation metric to fit the task |
| 15 / Slide 65 | ⚙️ **Cancer (FN deadly: "I'm fine, I'll smoke"), Anti-missile (FP shoots down a civilian plane — "happened recently"), Weather (both errors fine)** | Same error type, wildly different costs → pick precision vs recall by domain |
| 17 / Slides 69–70 | **Flower-Show kids** grouping similar flowers unsupervised (clustering); **Margin Free billing agent** noticing bread→butter→jam, milk→tea→sugar (association) | Unsupervised learning: clustering & association from unlabelled patterns |
| 18 / Slides 71–76 | ⚙️ **Kid finding the best park route**, **chess strategic-sacrifice (Pragg)**, **robot learning to balance/walk**, **Boston Dynamics / Chinese police robot-dog** | Reinforcement learning: reward judged over a whole action *sequence*, not one step |
