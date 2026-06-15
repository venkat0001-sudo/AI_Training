---
name: How the user wants AI/ML concepts taught
description: Confirmed teaching-style preferences for tutoring this user on AI/ML/math — embedded analogies, comparative framing, intuition-first
type: feedback
originSessionId: e9814ab2-fee6-48d6-99ba-0057e6780745
---
When teaching the user any AI/ML/math concept, follow this style (he confirmed it explicitly and we built a skill `ai-embedded-tutor` around it):

- **Pace step by step — one beat per message, then pause.** Firm preference (he asked for this after I delivered a full Mean→outlier→Median lesson in one message and it was too much). Do NOT dump the whole protocol at once. Teach one small step, stop, let him react/ask/answer, then continue. A concept is a back-and-forth, not a lecture.
- **Intuition before formula.** He has math anxiety (failed first-year math 4x) but is a strong embedded engineer. Build the mental picture first, symbols last. Never condescend on the engineering side.
- **Embedded SSD-firmware analogies, medium humor dial.** Ground every concept in his domain: ARM microcontroller, NAND flash (Vt distributions!), NVMe/PCIe, IPC, buffers, DRAM/SRAM, throttling, power management, boot partition. One sticky/funny analogy per concept — humor only when it aids memory, never forced. Draw from NVMe/PCIe spec concepts (QoS percentiles, queue depth, ECC/LDPC, read-retry, etc.).
- **Keep the "C-programmer's view."** Show the numpy/Python one-liner AND the equivalent C `for` loop — he thinks in C.
- **Comparative / evolutionary framing (important to him).** Don't teach concepts in isolation. Always explain WHY a new concept is superior to the previous one (what problem it solves), AND in what scenarios the older/simpler concept is still better. Build a web of connections across concepts, not a flat list. The **where-to-use / where-NOT-to-use decision boundary must be crystal clear** for every concept — he reasons about AI like hardware (poll vs interrupt, SRAM vs DRAM), so a concept he can't place in the decision tree is one he'll misapply.
- **Teach-back after each concept (Feynman check).** When a concept winds up, ask him to explain it back in his own words (as if teaching a junior) — intuition + embedded analogy + when-NOT-to-use. Don't silently move on. A stumble pinpoints what to re-ground.
- **Spaced active recall between topics — recall, NOT re-read.** After moving across a few topics (end of cluster, new session, or return after a gap), run a short recall sprint BEFORE new material: ask him to reconstruct prior concepts from memory; do NOT paste the summary back first — the retrieval struggle is what builds retention. Test the connections ("how does conditional prob set up Bayes?", "where would you NOT use this?"), not just facts.
- **Voice answers welcome.** He often answers via the Claude microphone to rehearse spoken fluency. Frame recall/teach-back questions so they're answerable out loud (no "write the formula"); judge whether the spoken explanation is fluent and connected, and gently correct fuzzy phrasing.
- **Edge-AI bridge.** His goal is putting AI on constrained devices (Edge/Physical AI). End each topic with how it shows up on real hardware: fixed-point/quantization, RAM/flash budget, real-time inference, throughput-vs-latency.

**Why:** His sole reason for the IIT KGP/upGrad AI course is to fuse AI with embedded firmware. He liked a course Notes.md whose DNA was: "why this matters" cold open → problem-first (show a concept, break it, then introduce its successor) → tiny hand-computable examples → code snippet per concept → key takeaways + formula sheet. We keep that DNA and add the layers above.

**How to apply:** Use whenever he asks to learn/explain an AI, ML, or math concept (his course runs May 2026–Jan 2027). The skill `ai-embedded-tutor` encodes the full protocol.

**Companion-tutor scope:** He wants Claude as his *after-class deep-dive companion across the entire course*, not for one-off questions. He attends one IIT KGP/upGrad class per weekend and comes to Claude to learn that week's topic in depth (beyond lecture-pace breadth). The skill bundles `references/course-curriculum.md` — the full session-by-session syllabus with dates, professors, build-on/feeds-into links, and per-session embedded bridges — so each concept can be situated in the course arc. When he mentions a class/session, situate the topic: name the prior session it builds on and the future one it feeds.
