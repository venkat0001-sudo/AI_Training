# Hard Q&A — the questions an all-firmware room will actually ask

Have a crisp, confident answer for each. Depth signals you own the topic; a clean one-liner on the
scoped-out topics keeps you on script. **Verify the exact codes/bits against our spec rev + FW.**

## Core / lifecycle
- **Q: Allocated vs attached vs active — restate it.** Allocated = created, exists in the subsystem, has
  an NSID, not yet usable (CNS 10h). Attached = bound to one/more controllers (Attach cmd). Active =
  attached to *this* controller, appears in its Active NS list (CNS 02h) and takes I/O.
- **Q: What happens on I/O to a valid-but-detached (or deleted) NSID?** Command fails — Invalid
  Namespace or Format (status). Our FW validates NSID against the per-controller active set before
  translation; broadcast (FFFFFFFFh) only where the spec permits.
- **Q: How does the host learn a namespace appeared/vanished?** AER "Namespace Attribute Changed"
  notice → host reads Changed Namespace List (log 04h) and re-reads Active NS list. We must post it and
  not lose it across coalescing.
- **Q: Thin provisioning — what exactly is NUSE and when does it move?** NUSE = logical blocks currently
  allocated; it grows as previously-unwritten blocks are written (and can shrink on deallocate/TRIM).
  NSFEAT bit0 advertises it. It must survive power loss — it's real accounting, not a hint.
- **Q: Format NVM scope and crypto-erase?** Reformat to a chosen LBAF, optional secure-erase via SES;
  FNA says whether format applies per-namespace or to all, and whether crypto-erase is supported.
- **Q: 512B vs 4KB namespace — what actually changes in the drive?** The LBA data size (LBADS in the
  active LBAF via FLBAS), metadata size, and PI layout. It changes host addressing granularity and our
  data-path/metadata handling — not the physical NAND page.

## Firmware architecture
- **Q: One FTL or per-namespace FTL?** [Answer for our FW.] Tradeoff: flat/global L2P shares the OP
  pool and is simpler, but GC/wear/accounting are subsystem-global; per-NS context isolates GC/OP/wear
  at the cost of more map + descriptor metadata.
- **Q: Is over-provisioning per-namespace or global?** [Answer for our FW.] Global pool = better
  utilization, cross-NS interference; per-NS reserve = predictable endurance/latency, less flexible.
- **Q: How is namespace config crash-consistent?** Namespace descriptor table persisted in NVM;
  Create/Delete/Attach/Format are atomic + replayable; recovered before namespaces are exposed at boot.
- **Q: Does deleting a namespace guarantee data is gone?** Only with secure/crypto erase; a plain delete
  returns capacity to the pool but blocks may persist until reused — state our FW's guarantee precisely.
- **Q: Two namespaces, one busy — do they interfere?** With a shared FTL/OP pool and shared channels,
  yes (GC, cache, bandwidth). True isolation needs physical partitioning (→ NVM Sets, next tier).

## Scoped-out topics — one-liners so you're never caught flat
- **NVM Sets / Endurance Groups?** "Namespaces are *logical* isolation; NVM Sets add *physical*
  isolation (die/channel partitioning) and Endurance Groups govern wear/QoS across sets. Out of scope
  today — happy to do a follow-up." [Say if our product supports it.]
- **ZNS / Zoned Namespaces?** "A 2.0 command set: the namespace is divided into sequential-write zones
  (Zone Append), cutting WA/OP/DRAM. Different command set (CSI), separate session." [Say if relevant.]
- **KV namespaces?** "Object/key-value command set instead of block LBAs — 2.0 addition; not our focus."
- **Shared namespaces / multipath?** "NMIC bit0 marks a namespace shareable across controllers; needs
  ANA multipath and reservations for fencing. We're covering private namespaces today." [Confirm.]
- **SR-IOV / virtualization?** "Primary + secondary controllers, VFs each seeing their own NS set — the
  virtualization layer on top of this model. Separate topic."
- **NVMe-oF difference?** "Same namespace model; the controller is reached over a fabric (TCP/RoCE/FC)
  instead of PCIe. The namespace semantics we covered are transport-agnostic."

## The one you want them to ask (your positioning)
- **Q: Where is this heading?** Storage is moving from 'stores' to 'participates in compute' — more
  namespace types (ZNS/KV), physical isolation for QoS, and eventually smarter in-controller management.
  Namespaces are the abstraction all of that hangs off. [Ties to your broader FMS/AI-in-SSD thread —
  keep it one sentence unless they pull.]
