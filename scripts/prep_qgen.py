"""Write one compact, self-contained query-generation input file per cluster, so each Sonnet
workflow agent can Read just its own small file (notes + resolved link targets) instead of the
whole manifest. Output: corpus/qgen/<cluster>.json  +  corpus/qgen/clusters.json (key list)."""
import json
from pathlib import Path

import common

MANIFEST = common.path("corpus_dir").parent / "manifest.json"
OUT = common.path("corpus_dir").parent / "qgen"
MAX_LINKS = 3


def main():
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    notes = m["notes"]
    clusters = {k: v["slugs"] for k, v in m["clusters"].items()}
    OUT.mkdir(parents=True, exist_ok=True)

    for ck, slugs in clusters.items():
        items = []
        for s in slugs:
            if s not in notes:
                continue
            n = notes[s]
            links = []
            for t in n["links"][:MAX_LINKS]:
                if t in notes:
                    links.append({"slug": t, "title": notes[t]["title"],
                                  "summary": notes[t]["summary"]})
            items.append({"slug": s, "title": n["title"], "summary": n["summary"],
                          "body": n.get("body", "")[:240], "links": links})
        (OUT / f"{ck}.json").write_text(
            json.dumps({"cluster": ck, "notes": items}, ensure_ascii=False, indent=1),
            encoding="utf-8")

    (OUT / "clusters.json").write_text(json.dumps(sorted(clusters), ensure_ascii=False),
                                       encoding="utf-8")
    print(f"wrote {len(clusters)} cluster files -> {OUT}")
    print("clusters:", sorted(clusters))


if __name__ == "__main__":
    main()
