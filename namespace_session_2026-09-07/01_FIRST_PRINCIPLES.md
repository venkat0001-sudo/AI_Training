# NVMe Namespaces & Multi-Namespace — First Principles to Expert Clarity

**For:** internal Tech session, 7 Sep 2026 · audience = SSD-firmware engineers (assume NVMe/FTL fluency).
**Scope:** core NVM namespaces + multi-namespace lifecycle + the firmware-architecture bridge to code.
**Source safety:** everything here is PUBLIC NVMe spec knowledge. Proprietary FW details stay on the
office laptop; overlay them onto this scaffold live. **Verify every CNS/field code against the exact
spec revision our FW implements (2.0 / 2.1 / 2.2)** — CNS tables and fields grow across revisions.

---

## 0 · The one sentence the whole talk hangs on

> **A namespace is a quantity of non-volatile memory formatted into logical blocks; the controller is
> the thing that processes commands. NVMe deliberately decoupled the two, and the NSID is the handle
> that binds an I/O command to a namespace.**

If a colleague remembers only one thing, it's that decoupling. Everything below is consequences of it.

## 1 · Why namespaces exist (the founding decoupling)

- **SATA/ATA model:** one device = one linear LBA space. Storage and the command interface were fused.
- **NVMe move:** separate **controller** (command processing, queues, capabilities) from **namespace**
  (the formatted media presented as LBA ranges). One controller → many namespaces; one namespace →
  (optionally) many controllers.
- **Why it matters to firmware:** it turns "the drive" into an **NVM subsystem** — a media pool plus a
  set of controllers plus a set of namespaces you can create, format, attach, and isolate independently.
  Partitions live in the *host* filesystem; namespaces live in the *device* and are enforced by our FW.
- **First-principles contrast to have ready:** namespace vs partition vs LUN. Partition = host-side
  division of one LBA space. LUN = SCSI addressing unit. Namespace = device-enforced, independently
  formattable LBA space with its own block size, protection, and capacity accounting.

## 2 · The object model (subsystem → controller → namespace)

- **NVM Subsystem** = the whole thing: media pool + one-or-more controllers + zero-or-more namespaces +
  the ports.
- **Controller**: the command processor a host connects to (PCIe function, or a fabrics controller).
- **Namespace**: private (attached to exactly one controller) or shared (attachable to several
  controllers in the subsystem — out of talk scope, one-liner in Q&A).
- **NSID space** is *controller-relative*: NSID is how *this* controller refers to a namespace.
  - `0h` — not a valid namespace (means "no namespace" in some admin contexts).
  - `FFFFFFFFh` — **broadcast** (applies to all namespaces, where the command permits it).
- **Drawing to put on the whiteboard:** one subsystem box; inside it a media pool at the bottom, two
  namespaces (NS A 512B, NS B 4KB) carved from it, and a controller on top with arrows NSID→NS.

## 3 · Identity — two kinds, and why you need both

- **NSID** = the *handle* used in commands. Controller-relative, reassignable, not globally unique.
- **NGUID / EUI-64 / UUID** = *globally unique* namespace identifiers (the Namespace Identification
  Descriptor, Identify CNS 03h).
- **Why both:** the moment a namespace can be reached by more than one controller/path, the host must
  know two paths point at the *same* namespace — the NSID can't prove that, the global ID can. Even in a
  single-controller product, the global ID is what host multipath/inventory tooling keys on.
- **FW responsibility:** generate and persist a stable NGUID/EUI-64 per namespace for life; never
  recycle it across a delete/create of a *different* namespace.

## 4 · Anatomy of a namespace (Identify Namespace, CNS 00h)

The fields your code will read/populate — know these cold:

| Field | Meaning | Firmware note |
|---|---|---|
| **NSZE** | Namespace Size (logical blocks) — the reported size | what the host sees as "the disk" |
| **NCAP** | Namespace Capacity (blocks that may be allocated) | thin prov: NCAP ≤ NSZE |
| **NUSE** | Namespace Utilization (blocks currently allocated) | must survive power loss; grows with writes on thin NS |
| **NSFEAT** | features; bit0 = thin provisioning | drives NUSE semantics |
| **NLBAF / FLBAS** | number of LBA formats / which one is active | FLBAS also encodes extended-metadata bit |
| **LBAF[]** | each: LBA data size (2^LBADS), metadata size (MS), rel. perf (RP) | the 512 vs 4096 choice + metadata |
| **MC / DPC / DPS** | metadata caps / PI caps / PI settings | T10 DIF/PI: type, and PI in first vs last metadata bytes |
| **NMIC** | multipath/sharing caps; bit0 = shared | 0 = private (talk default) |
| **NGUID / EUI64** | global identifiers | §3 |

- **Metadata layout:** *extended LBA* (metadata interleaved at end of each logical block) vs *separate
  buffer* (metadata in its own transfer). This is a real FW/data-path decision — flag which our FW uses.
- **Protection Information (PI / T10 DIF):** Guard (CRC) + Application Tag + Reference Tag per block;
  Type 1/2/3; located in first or last bytes of metadata (DPS). End-to-end data protection story.

## 5 · The lifecycle — allocated vs attached vs active (the #1 clarity win)

This trips people up; nail it and the room trusts you.

1. **Unallocated** — capacity in the pool, no namespace object.
2. **Allocated (Created)** — `Namespace Management: Create` (opcode 0Dh, SEL=0) with a create data
   structure (NSZE, NCAP, FLBAS, DPS, NMIC…). Namespace now *exists* in the subsystem and has an NSID —
   but **is not yet usable by any controller.**
3. **Attached** — `Namespace Attachment: Controller Attach` (opcode 15h, SEL=0) with a controller list.
   Now the namespace is visible to those controllers.
4. **Active (on this controller)** — attached to *this* controller → appears in its **Active Namespace
   ID list** and is usable for I/O.

- **Two lists, two questions:** **Allocated NS list (CNS 10h)** = "what exists in the subsystem?"
  **Active NS list (CNS 02h)** = "what can *this* controller do I/O to?" A namespace can be allocated
  but not attached (exists, invisible). Requires Namespace Management capability (**OACS bit 3**).
- **Format NVM (opcode 80h):** reformat a namespace to a chosen LBAF, optional secure-erase (SES);
  governed by **FNA** (Format NVM Attributes — e.g., does format apply to all namespaces, crypto-erase).
- **Delete** = Namespace Management SEL=1; detach first. Capacity returns to the pool.
- **Host notification — AER:** on any namespace attribute/inventory change, the controller posts an
  **Asynchronous Event (Namespace Attribute Changed, Notice)**; host reads the **Changed Namespace List
  log (04h)** and re-reads the Active NS list. Requires the notice enabled (Set Features: Async Event
  Config) and advertised (OAES in Identify Controller). *This is the async contract our FW must honor.*

## 6 · Why break one SSD into multiple namespaces (the use-case slide)

Have concrete reasons, not hand-waving:

- **Logical isolation / multi-tenancy** — separate LBA spaces per tenant/app.
- **Different formats side by side** — e.g., a 512B namespace for legacy/boot + a 4KB namespace for data;
  or PI enabled on one, off on another.
- **Security** — per-namespace encryption/key scoping; **write-protect a namespace** for recovery/golden
  images.
- **Endurance / performance** — per-namespace over-provisioning; separate hot and cold data so GC and
  wear don't cross-contaminate.
- **Boot vs data separation**, **capacity carving** for fixed provisioning.
- (Physical isolation — NVM Sets / Endurance Groups — is the *next tier* and is scoped out; one-liner in
  Q&A: namespaces = **logical** isolation, NVM Sets = **physical** isolation.)

## 7 · The firmware-architecture lens (the bridge to the code walkthrough)

This is where a firmware audience leans in. The design forks our code makes real:

- **How the FTL keys on (NSID, LBA):**
  - *Flat/global L2P* with NSID as a high-order key or per-NS base offset into one logical space —
    simplest, shares the OP pool, but GC/wear/accounting are subsystem-global.
  - *Per-namespace L2P context* — cleaner isolation (per-NS GC, OP, wear scope), more map metadata and
    more descriptor bookkeeping.
  - Name which our FW does and *why* — that's the architect payoff.
- **Namespace descriptor table (the source of truth):** the persisted record of which NSIDs exist and
  their NSZE/NCAP/FLBAS/DPS/NMIC/attach-state. Must be crash-consistent: Create/Delete/Attach/Format are
  **atomic + replayable** across power loss, and recovered *before* namespaces are exposed at boot.
- **Capacity & OP accounting:** per-NS vs global reserve; thin-provisioning NUSE bookkeeping that
  survives PLP; what happens when the pool can't satisfy NCAP.
- **Command routing:** admin path (Identify/CNS demux, NS Mgmt/Attach, Format) vs I/O path (NSID →
  validate attached/active → translate → media). Broadcast NSID handling (FFFFFFFFh).
- **Failure/edge semantics:** I/O to an unattached/deleted NSID, format-in-progress, attach during I/O,
  AER coalescing.

## 8 · The mental model to leave them with

> The subsystem is a **media pool**. Namespaces are **independently formatted windows** carved from it,
> each with its own block size, protection, capacity, and identity. The controller is the **doorway**;
> NSID is the **key** that says which window a command opens. Multi-namespace is just: many windows, one
> pool, one doorway — and our firmware is the part that keeps the windows honest across power loss.

---

### Precision checklist before presenting (verify against our spec rev + our FW)
- [ ] CNS values (00/01/02/03/10/11/12/13) match the rev we implement; note any CSI-qualified variants.
- [ ] Identify Namespace field offsets (NSZE/NCAP/NUSE/FLBAS/DPS/NMIC) confirmed.
- [ ] Namespace Management / Attachment opcodes + SEL values confirmed (0Dh / 15h).
- [ ] OACS bit for NS Management, OAES/AER notice bits confirmed.
- [ ] Which metadata layout (extended vs separate) and which PI types our drives support.
- [ ] Whether our product exposes shared NS / NVM Sets / ZNS (for the "out of scope but asked" answers).
