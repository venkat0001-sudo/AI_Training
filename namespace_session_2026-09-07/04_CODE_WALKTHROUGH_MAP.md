# Code Walkthrough Map — run this on your OFFICE laptop with Claude

**Boundary (important):** our in-house firmware source stays on the office machine. Do NOT paste it into
the content/creation Claude session — use the Claude on your office laptop for the actual code reading.
This file is the **map**: the structures and paths to trace, and the questions to ask the code, so the
walkthrough lines up with the talk (`01_FIRST_PRINCIPLES.md` §7 + `02_SESSION_OUTLINE.md` slides 11–13).

**How to drive it:** open our FW, and for each item below, find the code, then answer the question. Fill
the `→ ANSWER:` blanks — those become your slide 11–13 talking points. (You can run this in "coach mode"
— ask that Claude to push you one hypothesis at a time rather than hand you the answer; it doubles as
fast-debugging practice.)

## A · The namespace object in our FW
- [ ] The in-memory **namespace descriptor / context struct** — where is it defined?
  `→ ANSWER (fields it holds: NSZE/NCAP/NUSE/FLBAS/DPS/NMIC/attach-state/global-ID):`
- [ ] The **table/array** of namespaces (max count, indexing by NSID). How is NSID→context resolved?
  `→ ANSWER:`
- [ ] Where the **global identifier (NGUID/EUI-64)** is generated and persisted.
  `→ ANSWER:`

## B · Admin path — Identify
- [ ] The **Identify command handler** and its CNS demux. Which CNS values do we implement?
  `→ ANSWER (00h id-ns, 01h id-ctrl, 02h active list, 03h desc list, 10h/11h allocated, …):`
- [ ] How **Identify Namespace (00h)** is populated from the descriptor — field by field.
  `→ ANSWER:`
- [ ] **Active NS list (02h)** vs **Allocated NS list (10h)** — the two code paths / two source sets.
  `→ ANSWER:`

## C · Admin path — lifecycle commands
- [ ] **Namespace Management: Create (0Dh, SEL=0)** — parse create struct, allocate capacity, assign
  NSID, write descriptor. Where's the capacity-allocation call?
  `→ ANSWER:`
- [ ] **Delete (0Dh, SEL=1)** — detach check, capacity return, descriptor removal.
  `→ ANSWER:`
- [ ] **Namespace Attachment (15h)** Attach/Detach — controller-list handling, visibility change.
  `→ ANSWER:`
- [ ] **Format NVM (80h)** — LBAF change, SES secure-erase, FNA scope (per-NS vs all).
  `→ ANSWER:`
- [ ] **AER** posting on namespace attribute change + Changed NS List (log 04h) population.
  `→ ANSWER:`

## D · I/O path — the hot path
- [ ] Where an I/O command's **NSID is validated** (attached & active on this controller) before use.
  `→ ANSWER:`
- [ ] The **(NSID, LBA) → FTL/L2P → physical** translation. Flat/global map or per-NS context?
  `→ ANSWER (the design fork — this is the architect slide):`
- [ ] **Broadcast NSID (FFFFFFFFh)** handling in the I/O/admin paths.
  `→ ANSWER:`

## E · Persistence & power-loss (the crash-consistency story)
- [ ] Where the **namespace descriptor table is persisted** in NVM, and its format/versioning.
  `→ ANSWER:`
- [ ] **Boot recovery**: how descriptors are replayed/validated *before* namespaces are exposed.
  `→ ANSWER:`
- [ ] **Atomicity** of Create/Delete/Attach/Format across power loss (journal? shadow copy? replay?).
  `→ ANSWER:`
- [ ] **NUSE / thin-provisioning accounting** persistence and recovery.
  `→ ANSWER:`

## F · Capacity, OP, isolation (the tradeoff slide)
- [ ] **Over-provisioning**: per-namespace reserve or global pool?  `→ ANSWER:`
- [ ] **GC / wear-leveling scope**: per-NS or subsystem-global?  `→ ANSWER:`
- [ ] What happens when the **pool can't satisfy NCAP** (thin over-commit).  `→ ANSWER:`

## G · Edge cases to show you thought about them
- [ ] I/O to a **detached/deleted** NSID → what status, where returned.  `→ ANSWER:`
- [ ] I/O arriving **during Format** or during Attach/Detach.  `→ ANSWER:`
- [ ] AER **coalescing** — not losing a namespace-change event.  `→ ANSWER:`

---
**Output of this pass** = filled answers for A–G → directly become slides 11–13 and half your Q&A
confidence. Do this 2–3 days before the talk so you have time to chase anything the code surprises you
with.
