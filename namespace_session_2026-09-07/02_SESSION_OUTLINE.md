# Session Outline — "NVMe Namespaces: From First Principles to Our Firmware"

**Audience:** SSD-firmware engineers (deep). **Length target:** ~50 min + 10 Q&A (tune to your slot).
**Design rule:** keep first-principles fast (they know NVMe) — earn the room by slide 3, then spend the
budget on the lifecycle clarity, the architecture forks, and the live code. Content maps to
`01_FIRST_PRINCIPLES.md` sections (§).

| # | Slide | Time | Content / speaker note |
|---|---|---|---|
| 1 | **Title + the one question** | 1m | "Namespaces: everyone uses NSID daily — but *why* did NVMe split controller from media, and what does our FW do to keep it honest?" |
| 2 | **The founding decoupling** (§1) | 3m | SATA: one device = one LBA space. NVMe: controller (commands) ≠ namespace (media); NSID binds them. The whole talk is consequences of this. |
| 3 | **Namespace vs partition vs LUN** (§1) | 2m | Kill the common conflation up front — device-enforced vs host-side. Establishes altitude. |
| 4 | **Object model: subsystem → controller → namespace** (§2) | 3m | Whiteboard/diagram: media pool → NS A (512B) + NS B (4KB) → controller. NSID space, 0h / FFFFFFFFh. |
| 5 | **Two identities: NSID vs NGUID/EUI-64** (§3) | 3m | Handle vs global ID; why both; our FW's stable-ID responsibility. |
| 6 | **Anatomy: Identify Namespace fields** (§4) | 5m | NSZE/NCAP/NUSE, FLBAS/LBAF, metadata (extended vs separate), DPS/PI. The fields the code fills. |
| 7 | **Lifecycle: allocated → attached → active** (§5) | 6m | ⭐ The clarity centerpiece. Two lists (CNS 10h vs 02h), Create/Attach/Format opcodes, "exists but invisible." |
| 8 | **The async contract: AER on NS change** (§5) | 3m | Namespace Attribute Changed → Changed NS List log 04h → host re-reads. Our FW's notification duty. |
| 9 | **Why multiple namespaces** (§6) | 4m | Isolation, mixed formats, per-NS security/OP, boot vs data. Concrete, not hand-wavy. |
| 10 | **Live demo: nvme-cli** | 6m | `id-ctrl` (NN, OACS), `id-ns`, `ns-list`, `create-ns`→`attach-ns`→`format`. Makes it tangible; ties structures to reality. (Have a recorded fallback.) |
| 11 | **Firmware architecture I — FTL keys on (NSID,LBA)** (§7) | 5m | The design fork: flat/global L2P vs per-NS context; GC/OP/wear scope tradeoffs. Name what we do + why. |
| 12 | **Firmware architecture II — descriptor persistence & PLP** (§7) | 5m | Namespace descriptor table = source of truth; atomic Create/Delete/Attach/Format; recover before exposing at boot; NUSE across power loss. |
| 13 | **Code walkthrough** | 6m | The real payoff — trace admin path (Identify/CNS demux → NS Mgmt/Attach → Format) + I/O path NSID validate→translate. Driven by `04_CODE_WALKTHROUGH_MAP.md`. |
| 14 | **The mental model + edges** (§8) | 2m | Pool / windows / doorway / key. Plus 2–3 edge cases (I/O to detached NSID, format-in-progress). |
| 15 | **Q&A** | 10m | Keep `03_HARD_QA.md` open; one-liners ready for NVM Sets / ZNS / shared-NS. |

## Delivery notes
- **The two "wow" beats** for this audience: slide 7 (allocated≠attached≠active — most people are fuzzy
  here) and slides 11–12 (our real FTL/persistence design). Budget accordingly.
- **First-principles fast, architecture slow.** They don't need NVMe 101; they need the *why* and the
  *our-FW* mapping. If short on time, compress 2–3, never 11–13.
- **The live nvme-cli demo** is the credibility multiplier — abstract fields become a terminal they
  recognize. Record it in advance as insurance.
- Leave every slide with one "for our firmware:" line — that's the thread that makes it *our* session,
  not a spec recap.
