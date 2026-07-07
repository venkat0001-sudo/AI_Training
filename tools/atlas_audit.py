#!/usr/bin/env python3
"""Atlas vault auditor — run before committing any Obsidian Atlas note work.

Checks (stdlib only):
  1. every wikilink target resolves to a file, or is a KNOWN seed (listed in a MOC "Seeds pending")
  2. every [[file#heading]] anchor matches a real heading
  3. every ![[file#^block]] embed matches a real block ID
  4. no alias is claimed by two files
  5. no unfenced matrix-literal [[ hazards outside code
  6. atom front-matter (lane/edge/status) mirrors tools/web.json

Usage:  python3 tools/atlas_audit.py            # link/graph audit
        python3 tools/atlas_audit.py --twins    # additionally exec all ```python twins (needs numpy/matplotlib)
Exit code 0 = clean, 1 = problems found.
"""
import re, sys, json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
problems = []

files = list(DOCS.glob("*.md")) + list(DOCS.glob("concepts/*.md")) + list(DOCS.glob("maps/*.md"))
names = {p.stem: p for p in files}

# ---- harvest headings, block ids, aliases, seeds ----
headings, blocks = collections.defaultdict(set), collections.defaultdict(set)
aliases = {}
seeds = set()
for p in files:
    t = p.read_text(encoding="utf-8")
    for h in re.findall(r"^#{1,6}\s+(.+)$", t, re.M):
        headings[p.stem].add(h.strip())
    for b in re.findall(r"\^([a-zA-Z0-9-]+)\s*$", t, re.M):
        blocks[p.stem].add(b)
    m = re.search(r"^aliases:\s*\[([^\]]*)\]", t, re.M)
    if m:
        for a in (x.strip() for x in m.group(1).split(",")):
            if not a:
                continue
            if a in aliases and aliases[a] != p.stem:
                problems.append(f"ALIAS COLLISION: '{a}' claimed by {aliases[a]} and {p.stem}")
            aliases[a] = p.stem
    if p.parent.name == "maps":  # seeds are declared in MOC "Seeds pending" sections
        sp = re.search(r"## Seeds pending\n(.*?)(\n## |\Z)", t, re.S)
        if sp:
            seeds |= set(re.findall(r"\[\[([^\]|#^\\]+)", sp.group(1)))

def strip_code(t):
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    return re.sub(r"`[^`]*`", "", t)

# ---- audit links (handles table-escaped \| ) ----
LINK = re.compile(r"\[\[([^\]|#^\\]+)(#[^\]|\\]+)?(?:\\?\|[^\]]*)?\]\]")
for p in files:
    body = strip_code(p.read_text(encoding="utf-8"))
    for base, frag in LINK.findall(body):
        base = base.strip()
        if base not in names:
            if base not in seeds:
                problems.append(f"UNRESOLVED (not a declared seed): [[{base}]] in {p.name}")
            continue
        if frag.startswith("#^"):
            if frag[2:] not in blocks[base]:
                problems.append(f"BROKEN BLOCK REF: [[{base}{frag}]] in {p.name}")
        elif frag:
            if frag[1:].strip() not in headings[base]:
                problems.append(f"BROKEN HEADING LINK: [[{base}{frag[:50]}]] in {p.name}")
    # unfenced matrix-literal hazard: [[num, …  (comma after the first number —
    # distinguishes [[2,0],[0,3]] from legitimate dated-scroll links like [[2026-06-28_…]])
    for m in re.finditer(r"\[\[\s*[-+]?\d+(?:\.\d+)?\s*,", body):
        problems.append(f"MATRIX-LITERAL HAZARD (unfenced [[num,): {p.name} …{body[max(0,m.start()-30):m.start()+15]!r}")

# ---- atoms mirror web.json ----
web = json.loads((ROOT / "tools" / "web.json").read_text(encoding="utf-8"))
nodes = {n["slug"]: n for n in web["nodes"]}
for p in DOCS.glob("concepts/*.md"):
    t = p.read_text(encoding="utf-8")
    fm = dict(re.findall(r"^(lane|edge|status):\s*(\S+)", t, re.M))
    n = nodes.get(p.stem)
    if not n:
        problems.append(f"ATOM WITHOUT web.json NODE: {p.stem} (add the node or fix the slug)")
        continue
    for k in ("lane", "edge", "status"):
        if k in fm and str(n.get(k)) != fm[k]:
            problems.append(f"MIRROR DRIFT: {p.stem}.{k} vault={fm[k]} web.json={n.get(k)}")

# ---- optional: execute twins ----
if "--twins" in sys.argv:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import io, contextlib
        for p in sorted(DOCS.glob("concepts/*.md")):
            for i, code in enumerate(re.findall(r"```python\n(.*?)```", p.read_text(encoding="utf-8"), re.S)):
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        exec(code, {"__name__": f"{p.stem}_{i}"})
                except Exception as e:
                    problems.append(f"TWIN FAILED: {p.stem} block {i}: {e!r}")
    except ImportError:
        print("(--twins skipped: numpy/matplotlib not available in this python)")

if problems:
    print(f"✗ {len(problems)} problem(s):")
    for x in problems:
        print("  -", x)
    sys.exit(1)
print(f"✓ atlas audit clean — {len(files)} files, {len(aliases)} aliases, {len(seeds)} declared seeds")
