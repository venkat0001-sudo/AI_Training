# Code-Trace Agent Prompt — paste into Claude Code on the OFFICE laptop

Run this from the root of our firmware repo. It turns `04_CODE_WALKTHROUGH_MAP.md` into an autonomous
trace the coding agent can execute, then hand you a report you distill into slides 11–13.

**Confidentiality:** the report this produces contains proprietary code detail — it STAYS on the office
laptop. Do not bring the raw report into the content-creation Claude session; only carry back
public-safe talking points you write yourself. Model-agnostic (works with whatever model Claude Code is
configured to use).

---

## PASTE FROM HERE

You are a senior SSD-firmware architect. I am preparing an expert internal session on NVMe namespaces
and must understand exactly how THIS codebase implements them. Trace the code and produce a factual
report. This is a **read-only** task.

**Hard rules:**
- Do NOT modify, refactor, build, or run anything. Read and report only.
- Cite evidence as `path/file:line` for every finding. If you can't find something, say
  "NOT FOUND / not implemented" — never guess or fill from general NVMe knowledge.
- Distinguish what the code actually does from what the NVMe spec says. Flag deviations, TODOs, and
  vendor-specific behavior explicitly.
- Note the NVMe spec revision the code targets if discoverable (macros, comments, version fields).
- Work incrementally: start from entry points and follow the call graph; use grep/search for opcodes,
  CNS values, and struct names rather than reading everything. Report as you go.

**Method:** find the admin-command dispatch and the I/O command dispatch first; from there follow
Identify, Namespace Management/Attachment, Format, and the NSID→FTL translation. Anchor searches on:
Identify/CNS, opcodes `0Dh` (NS Mgmt), `15h` (NS Attach), `80h` (Format), `FFFFFFFF` (broadcast NSID),
and the namespace struct/table names.

**Produce a report answering each item with `file:line` evidence:**

A. NAMESPACE OBJECT — the namespace descriptor/context struct + its fields (NSZE/NCAP/NUSE/FLBAS/DPS/
   NMIC/attach-state/global-ID); the table indexing namespaces; how NSID→context is resolved; where
   NGUID/EUI-64 is generated and persisted.

B. IDENTIFY — the Identify handler and CNS demux; which CNS values are implemented (00/01/02/03/10/11/
   12/13/…); how Identify Namespace (00h) is populated field-by-field; the Active-list (02h) vs
   Allocated-list (10h) code paths.

C. LIFECYCLE — Namespace Management Create (0Dh SEL0) and Delete (SEL1); Namespace Attachment (15h)
   attach/detach; Format NVM (80h) incl. SES secure-erase and FNA scope; AER posting on namespace
   change + Changed-NS-List log (04h).

D. I/O PATH — where NSID is validated (attached & active) before use; the (NSID,LBA)→FTL/L2P→physical
   translation and whether the map is flat/global or per-namespace; broadcast-NSID handling.

E. PERSISTENCE & POWER-LOSS — where the namespace descriptor table is persisted and its format/version;
   boot recovery before namespaces are exposed; atomicity mechanism for Create/Delete/Attach/Format
   (journal/shadow/replay); NUSE / thin-provisioning accounting persistence.

F. CAPACITY / OP / ISOLATION — over-provisioning per-NS or global; GC/wear-leveling scope per-NS or
   global; behavior when the pool can't satisfy NCAP.

G. EDGE CASES — I/O to a detached/deleted NSID (status + where returned); I/O during Format/Attach;
   AER coalescing / not losing a namespace-change event.

**Output format:** one Markdown report, sections A–G, each finding as a bullet with `file:line`. End
with: (1) a "Design decisions" summary — is the FTL flat or per-NS? OP global or per-NS? — in 5 bullets;
(2) an "Open questions / surprises / spec deviations" list; (3) a "Couldn't locate" list.

## PASTE TO HERE

---

## How to use the output well (for the presenter — you)

- **Let the agent do the *navigation*, not your *understanding*.** It finds where things live and how
  they connect; you read the logic yourself. You're presenting this and fielding expert Q&A — you can't
  narrate code you don't actually grasp. Use the report as a fast index into the real reading.
- **Optional "coach mode":** instead of the autonomous run, ask that agent to walk you one section at a
  time and push you to predict each next hop before revealing it — slower, but you'll own it cold (and
  it doubles as the fast-debugging practice).
- **Distill, don't copy.** From the report, write your own public-safe talking points for slides 11–13.
  The report stays local; only your distilled architecture story travels.
- Run this **2–3 days before** the talk so any surprise the code throws has time to be chased down.
