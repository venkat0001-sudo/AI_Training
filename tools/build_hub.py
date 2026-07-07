#!/usr/bin/env python3
"""Build the Rasengan Path hub: scan artifact metadata + ledger + web.json,
inject as JSON into tools/hub_template.html, write /index.html.

Run from repo root or tools/:  python3 tools/build_hub.py
Stdlib only. Part of the end-of-session routine (after updating web.json + ledger).
"""
import json, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS, HTML, TOOLS = ROOT / "docs", ROOT / "html", ROOT / "tools"
GH = "https://github.com/venkat0001-sudo/AI_Training/blob/main/docs/"
warnings = []


# ---------------- session table (from course-curriculum.md, static) ----------------
# id, iso date, short title, module key, module label
SESSIONS = [
    ("F1", "2026-06-06", "Python tool proficiency",             "f",  "Foundation"),
    ("F2", "2026-06-07", "Probability & statistics",            "f",  "Foundation"),
    ("F3", "2026-06-13", "Linear algebra",                      "f",  "Foundation"),
    ("F4", "2026-06-14", "Calculus",                            "f",  "Foundation"),
    ("s1", "2026-06-20", "Data analysis · workflow · CV · metrics", "m1", "M1 · ML Fundamentals"),
    ("s2", "2026-06-27", "Linear & logistic regression",        "m1", "M1 · ML Fundamentals"),
    ("s3", "2026-07-04", "Decision trees & SVMs",               "m1", "M1 · ML Fundamentals"),
    ("s4", "2026-07-11", "Ensembles: bagging, forests, boosting","m1", "M1 · ML Fundamentals"),
    ("s5", "2026-07-18", "K-means & PCA",                       "m1", "M1 · ML Fundamentals"),
    ("s6", "2026-07-19", "Assignment & doubts",                 "m1", "M1 · ML Fundamentals"),
    ("s7", "2026-07-25", "Feedforward nets & backprop",         "m2", "M2 · Deep Learning"),
    ("s8", "2026-08-01", "Optimizers & regularization",         "m2", "M2 · Deep Learning"),
    ("s9", "2026-08-08", "CNNs",                                "m2", "M2 · Deep Learning"),
    ("s10","2026-08-16", "RNNs",                                "m2", "M2 · Deep Learning"),
    ("s11","2026-08-22", "Transfer learning & deployment",      "m2", "M2 · Deep Learning"),
    ("s12","2026-08-23", "Assignment & doubts",                 "m2", "M2 · Deep Learning"),
    ("s13","2026-08-29", "Text preprocessing & representation", "m3", "M3 · NLP & Transformers"),
    ("s14","2026-09-05", "Attention & the Transformer",         "m3", "M3 · NLP & Transformers"),
    ("s15","2026-09-12", "Transformer variants",                "m3", "M3 · NLP & Transformers"),
    ("s16","2026-09-19", "Speech: ASR · TTS",                   "m3", "M3 · NLP & Transformers"),
    ("s17","2026-09-20", "Exams",                               "m3", "M3 · NLP & Transformers"),
    ("s18","2026-09-26", "Foundations of GenAI",                "m4", "M4 · GenAI & LLMs"),
    ("s19","2026-10-03", "LLM architectures & pretraining",     "m4", "M4 · GenAI & LLMs"),
    ("s20","2026-10-10", "PEFT: LoRA · QLoRA",                  "m4", "M4 · GenAI & LLMs"),
    ("s21","2026-10-24", "Multimodal AI",                       "m4", "M4 · GenAI & LLMs"),
    ("s22","2026-10-31", "Alignment & Responsible AI",          "m4", "M4 · GenAI & LLMs"),
    ("s23","2026-11-01", "Assignment & doubts",                 "m4", "M4 · GenAI & LLMs"),
    ("s24","2026-11-21", "RAG & vector search",                 "m5", "M5 · RAG Systems"),
    ("s25","2026-11-28", "LangChain & orchestration",           "m5", "M5 · RAG Systems"),
    ("s26","2026-12-05", "Advanced RAG",                        "m5", "M5 · RAG Systems"),
    ("s27","2026-12-12", "Evaluation & debugging",              "m5", "M5 · RAG Systems"),
    ("s28","2026-12-13", "Assignment & doubts",                 "m5", "M5 · RAG Systems"),
    ("s29","2026-12-19", "Agentic AI foundations",              "m6", "M6 · Agents & MLOps"),
    ("s30","2026-12-26", "Building & deploying agents",         "m6", "M6 · Agents & MLOps"),
    ("s31","2027-01-02", "MLOps",                               "m6", "M6 · Agents & MLOps"),
    ("s32","2027-01-09", "Responsible agentic AI",              "m6", "M6 · Agents & MLOps"),
    ("FIN","2027-01-10", "Final exam",                          "m6", "M6 · Agents & MLOps"),
]

# concept slugs that are allowed to have no node in web.json
SKIP_ORPHAN = {"meta"}


# ---------------- parsers ----------------
def parse_front_matter(text):
    """Minimal YAML front-matter: key: value, lists as [a, b]. Returns dict or None."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    meta = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            meta[k.strip()] = [x.strip() for x in inner.split(",") if x.strip()]
        else:
            meta[k.strip()] = v
    return meta


def scan_artifacts():
    arts = []
    # docs/ root + the Obsidian Atlas layers (concepts/ atoms, maps/ MOCs)
    md_paths = sorted(DOCS.glob("*.md")) + sorted(DOCS.glob("concepts/*.md")) + sorted(DOCS.glob("maps/*.md"))
    for p in md_paths:
        rel = p.relative_to(DOCS).as_posix()
        meta = parse_front_matter(p.read_text(encoding="utf-8"))
        if not meta:
            warnings.append(f"no front-matter: docs/{rel}")
            continue
        # concept atoms: the atom's own slug is its concept; front-matter has no concepts: list
        concepts = meta.get("concepts", [p.stem] if rel.startswith("concepts/") else [])
        arts.append({
            "file": rel, "href": GH + rel, "kind": meta.get("type", "notes"),
            "title": meta.get("title", p.name), "date": meta.get("date", ""),
            "sessions": meta.get("sessions", []), "concepts": concepts,
            "recap": meta.get("recap", ""), "loc": "gh",
        })
    for p in sorted(HTML.glob("*.html")):
        m = re.search(r"<!--HUB (\{.*?\}) -->", p.read_text(encoding="utf-8"), re.S)
        if not m:
            warnings.append(f"no HUB comment: html/{p.name}")
            continue
        try:
            meta = json.loads(m.group(1))
        except json.JSONDecodeError as e:
            warnings.append(f"bad HUB json in html/{p.name}: {e}")
            continue
        meta.update({"file": p.name, "href": "html/" + p.name,
                     "kind": meta.pop("type", "interactive"), "loc": "site"})
        arts.append(meta)
    return arts


def parse_ledger():
    """Rows of the recall-ledger table -> [{topic, next, due(bool)}]."""
    rows = []
    text = (DOCS / "recall-ledger.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|--") or "Anchor artifacts" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("Topic", "---"):
            continue
        rows.append({"topic": cells[0], "next": cells[5],
                     "due": "DUE" in cells[5].upper()})
    return rows


# ---------------- build ----------------
def main():
    today = datetime.date.today().isoformat()
    arts = scan_artifacts()
    web = json.loads((TOOLS / "web.json").read_text(encoding="utf-8"))
    ledger = parse_ledger()

    # validations
    slugs = {n["slug"] for n in web["nodes"]}
    for a in arts:
        for c in a.get("concepts", []):
            if c not in slugs and c not in SKIP_ORPHAN:
                warnings.append(f"artifact {a['file']}: concept '{c}' has no web.json node")
    for e in web["edges"]:
        for k in ("from", "to"):
            if e[k] not in slugs:
                warnings.append(f"edge {e['from']}->{e['to']}: unknown slug '{e[k]}'")
    for row in ledger:
        for name in re.findall(r"`([^`]+)`", row["topic"]):
            pass  # topic cell has no file refs; anchors live in col 2 (not validated here)

    # current session = first session whose date >= today
    cur = next((s[0] for s in SESSIONS if s[1] >= today), SESSIONS[-1][0])

    data = {
        "built": today,
        "current": cur,
        "sessions": [{"id": s[0], "date": s[1], "title": s[2], "lane": s[3], "module": s[4]}
                     for s in SESSIONS],
        "artifacts": arts,
        "web": web,
        "dueTopics": [r["topic"] for r in ledger if r["due"]],
    }

    tpl = (TOOLS / "hub_template.html").read_text(encoding="utf-8")
    token = "/*__DATA__*/"
    if token not in tpl:
        print("FATAL: template missing /*__DATA__*/ token"); sys.exit(1)
    out = tpl.replace(token, "const HUB=" + json.dumps(data, ensure_ascii=False) + ";")
    (ROOT / "index.html").write_text(out, encoding="utf-8")

    print(f"index.html built · {len(arts)} artifacts · {len(web['nodes'])} nodes · "
          f"{len(web['edges'])} edges · current={cur} · due={len(data['dueTopics'])}")
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print("  -", w)
    else:
        print("zero warnings ✓")


if __name__ == "__main__":
    main()
