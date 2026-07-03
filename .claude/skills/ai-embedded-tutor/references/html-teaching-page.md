# HTML teaching-page recipe (the "Sage-Mode presentation" standard)

Read this **whenever he asks for an HTML page / visual / interactive recap.** Every teaching page must
match the quality bar of the two references he pointed at as "this is what good looks like":
- `html/2026-06-30_covariance-eigen-capstone_F.html` (the covariance/eigen one)
- `html/2026-06-30_bell-curve-sigma-latency_F.html` + `html/normal_distribution.html` (the bell-curve/σ ones)

Open those and mirror their structure — don't reinvent. This file codifies *why* they work so new pages
land the same way. **Goal in his words: it should read like a presentation — interactive, visual, very
detailed — clear enough that he can turn around and teach someone else straight off the page.**

---

## 0. The three analogy channels (his 2026-07-01 upgrade — use ALL THREE)

He teaches himself through analogies. Until now we used two channels; he added a third:
1. **Verbal analogy** — the funny/SSD/generic wording (skill beat 3).
2. **Numerical plots** — hand-computable numbers + SVG number-lines/bars/matrices.
3. **⭐ PICTORIAL analogy (NEW)** — a *visual metaphor picture*, like the **"Normal Distribution (in the
   gym)"** weight-stack meme (a bell curve drawn over a gym weight stack: most people pull the middle
   plates, almost nobody the featherweight or the monster stack). Funny + visual + instantly correct.
   Every page should carry **at least one pictorial analogy** as a drawn scene, not just words.

**How to build a pictorial analogy** (self-contained, no external images):
- **Inline SVG scene** — draw the metaphor (a gym weight stack with a bell overlay, a swing arc for
  eigenvectors, a cigar-vs-blob scatter). This is the preferred, highest-quality route.
- **Emoji-composed picture** — arrange emoji (🏋️ 🍩 🎯 🐸) into a labeled visual when an SVG is overkill.
- Always **label it** and pair it with one caption line tying the picture back to the math.
- Same precision rule as verbal analogies: the picture's mechanism must actually match, or cut it.

---

## 0b. ⭐ The "3D animated movie" standard (his 2026-07-02 upgrade — the page's soul)

His words: *"Every concept should be visualizable... like a 3D animated movie of AI learning —
everything straight into the mind without any learning gap."* Concretely: if he thinks "matrix," he
should SEE space transforming; if the mean changes, he should SEE the dataset and bell curve move.

**Rule 1 — every equation has a VISUAL TWIN.** No number on the page may exist only as text. If a
value changes, something visible must move, stretch, tilt, or recolor. A formula without a picture is
a learning gap.

**Rule 2 — at least one WHAT-IF control per page (the movie he directs).** A slider or drag handle
that lets him change a cause and *watch* the effect, live:
- drag the **mean** → the whole dataset + bell curve slide along the axis
- drag **σ** → the bell widens/flattens, the data points spread
- edit **matrix entries** → the background grid warps, vectors rotate/stretch — and the eigenvector
  visibly stays on its own line while everything else swings
- drag the **learning rate** → the gradient-descent ball rolls down the loss bowl in bigger/smaller
  hops (overshoots when too big)
- drag one **data point** → covariance cloud re-tilts, the eigen-axes re-aim, the numbers update

**Rule 3 — the concept→visual vocabulary (reuse; consistency builds his mental furniture):**
| concept | its living visual |
|---|---|
| vector | an arrow from origin (length = magnitude, heading = direction) |
| matrix | a machine that WARPS the background grid (space transformation) |
| eigenvector / λ | the arrow that refuses to rotate under the warp; λ = its stretch |
| mean | a plumb-line / balance point the data hangs from |
| variance / σ | the width of the bell; the spread of the dots |
| covariance | the TILT of a point cloud (cigar vs blob) |
| PCA | finding the cigar's long axis and photographing along it |
| loss function | a terrain/bowl; height = how wrong |
| gradient descent | a ball rolling downhill on that bowl, step by step |
| probability | shaded AREA under a curve |
| dot/cosine | two arrows and the angle between them, with the shadow (projection) |

**Rule 4 — depth & motion techniques (still 100% self-contained, no CDN/libs):**
- **SVG + JS animation** — the default: animate `transform` on grid lines, arrows, curves.
- **CSS 3D transforms** — `perspective` + `rotateX/rotateY` on planes for true depth (loss bowls,
  tilted data planes). This is the "3D-level pictographic" layer.
- **`<canvas>`** — point clouds, particles, trajectories when SVG gets heavy (>~200 elements).
- **requestAnimationFrame easing** — nothing should teleport; values *travel* so cause→effect reads
  as a story. Keep animations 300–900 ms, interruptible, and re-runnable (a replay ⟳ button).

**Rule 5 — movie beats.** Each step should play like a scene: setup (what you're looking at) →
action (the change happens, animated) → punchline (the readout updates + one-line takeaway). The
reveal mechanic and the what-if control ARE the plot; text narrates it.

---

## 0c. ⛔ DEFINITION OF DONE — the pre-flight gate (added 2026-07-02 after a real violation)

A page was shipped with text-only panes and no plots, violating Rule 1 above. He caught it. This
gate exists so it can't recur. **Before saving any page, walk EVERY step and ask: "what does the
reader SEE here?" If the honest answer is "text and a formula block" — the step is NOT done.**

**Gate 1 — visuals are INFERRED, never requested.** He will not (and should not have to) say "plot
this vector." The content type dictates the visual, automatically:
| content on the page | mandatory visual (numpy-plot style: axes, grid, ticks) |
|---|---|
| any vector | arrow from origin on an axes+grid plot, labeled with its components |
| two+ vectors compared | side-by-side or overlaid arrow plots, same scale where honest |
| any `C·v = λv` claim | BEFORE/AFTER arrows — v (sage) and C·v (orange) on one plot; λ=1 → arrows overlap ("nothing moves") |
| any matrix | colored cell grid (diagonal highlighted where relevant) |
| a determinant / characteristic polynomial | the f(λ) CURVE with its roots dotted — a repeated root visibly *kisses* zero |
| 3-component vectors | isometric-projected 3D axes (tiny projection helper: X=(x−y)cos30°, Y=(x+y)sin30°−z) |
| any percentage / variance share | horizontal bars |
| any dataset | scatter plot, with the fitted/eigen direction drawn through it |

**Gate 2 — every pane stands ALONE.** In a side-by-side layout each pane is a complete lesson:
full narrative, full derivation, full visuals. NEVER truncate one pane because "the other side
already explains it" — the panes will be read independently, and re-explaining IS the revision.
If a case genuinely doesn't exist on one side (e.g. no repeated λ in a 2×2), fill that pane with
the honest equivalent story, fully told — not a "see other side" note.

**Gate 3 — the checklist, per page, before saving:**
- [ ] every step has ≥1 drawn visual (Gate 1 table)
- [ ] ≥1 interactive what-if control on the page (Rule 2)
- [ ] 1 pictorial analogy (§0)
- [ ] side-by-side panes independently complete (Gate 2)
- [ ] all numbers verified, all JS ids wired, zero external deps

---

## 1. Non-negotiables (what makes it "his" style)

- **Single self-contained `.html`** — inline `<style>` + `<script>`, zero external deps, opens offline.
- **Save to** `html/YYYY-MM-DD_<topic>_<F|sN>.html` (`_F` = Foundation extension, `_sN` = numbered session).
- **Sage-Mode dark theme** — olive/sage bg, cream text, orange accents. Reuse the exact
  palette in §3 so all pages look like one deck.
- **⛔ NO frog emoji/symbol (🐸) anywhere — his 2026-07-03 directive, permanent.** Header mark is the
  **🍥 Uzumaki spiral** (Naruto/Rasengan theme) instead. Older pages still carrying frogs get cleaned
  whenever they're next touched.
- **Step machinery** — ONE concept visible at a time; fixed bottom nav (`← Back` / `Next →`), a row of
  progress **dots**, and **arrow-key** navigation. Each step fades/rises in. This is what makes it feel like
  a presentation instead of a wall of text.
- **Predict-before-reveal** — hide punchlines/answers behind tap-to-reveal `.reveal` spans so he predicts
  first (mirrors the lesson protocol beat 10).
- **Precomputed data, VERIFIED vs numpy** — never hand-wave numbers in JS. Compute in Python first, paste
  the verified constants, add a `// verified vs numpy` comment. A wrong number on a "concrete memory" page
  is worse than no page.
- **Detailed, presentation-grade prose** — each step carries a full explanation, not a bullet stub. He may
  present from it, so it must stand alone without him narrating.
- **Mobile-responsive** — `.split` collapses to one column under 900px.

---

## 2. Per-step content skeleton (map the lesson beats onto each step)

Each step = one concept, built from these blocks (reuse the class names from the reference files):
```
.concept   → step number + title + the plain-words intuition
.joke      → 😄 the FUNNY example (gold, italic) — lead with it (skill beat 3)
[pictorial]→ 🖼️ inline-SVG or emoji visual metaphor (the §0 upgrade)
[what-if]  → 🎬 the live control (slider/drag) — change the cause, WATCH the effect (§0b Rule 2)
.ssd       → 🔧 the SSD-firmware grounding (teal)
numeric    → SVG number-line / bars / matrix-grid with the hand-computable numbers
.eq        → the formula, monospace, AFTER intuition — with its visual twin (§0b Rule 1)
.reveal    → predict-before-reveal spans for answers
.why       → the "why it matters / ML destination" box (orange left-border)
```
End the deck with a "🎯 the thread" note tying the concept forward to its ML use (PCA, embeddings, etc.).

---

## 3. The exact palette + machinery to copy (keeps every page one deck)

```css
:root{
  --bg:#0d1408; --bg2:#0f1d0a; --card:rgba(20,40,12,.72); --line:rgba(74,122,46,.5);
  --cream:#f5e6c8; --creamd:#cbbb95; --sage:#a8c87a; --sagem:#7a9e5a; --saged:#4a7a2e;
  --orange:#ff8c00; --orangeg:#ffb347; --red:#d9534f; --blue:#5a8fbf;
  --teal:#27c2a8; --gold:#ffce4a; --ink:#eaf0dd;
}
body{background:linear-gradient(135deg,#0c1607,#0e1f0a 55%,#171708);color:var(--cream);
  font-family:'Courier New',monospace;line-height:1.6}
/* step machine: .step{display:none} .step.on{display:block} + rise keyframe */
/* fixed .nav bottom bar with #prev #next, #dots, #slabel; wire ArrowLeft/ArrowRight */
```
Colour code: `.joke/.k`=gold, `.ssd/.t`=teal, `.o`=orange, `.g`=sage, `.r`=red. Frog header pulses
orange↔sage. Nav buttons flip to orange on hover. See the covariance-capstone `<head>` for the full sheet —
copy it wholesale, then swap the step content.

---

## 4. Build workflow

1. Nail the concept in chat first (the lesson happens in conversation; the HTML is the *artifact*).
2. Compute every number in Python, verify against `numpy`, keep the verified constants.
3. Copy the `<head>` + nav/step machinery from `2026-06-30_covariance-eigen-capstone_F.html`.
4. Fill one `.step` per concept using the §2 skeleton — humor-first, add the pictorial analogy, then SSD,
   then numbers, then formula, then the why-box.
5. Save to `html/YYYY-MM-DD_<topic>_<F|sN>.html`. These are his review artifacts — they get committed & pushed.
