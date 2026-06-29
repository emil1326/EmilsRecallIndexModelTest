#!/usr/bin/env node
// build_corpus.mjs — (query -> slug) pair builder for the generative-retrieval experiment.
//
// The brief shipped this file's spec but not the file, so it's reimplemented here with
// its guarantees made explicit. It reads a vault of <slug>.md notes (flat frontmatter)
// and emits three pair kinds:
//   title   : note.title   -> slug            (anchors EVERY slug; always in train)
//   summary : note.summary -> slug            (different phrasing of the same note)
//   assoc   : A.summary     -> B   for A links [[B]]   (THE associative / two-hop signal)
//
// Held-out split — the validity-critical part:
//   * We hold out a deterministic ~15% of *source notes* (by stable hash of the slug).
//   * ALL summary/assoc pairs whose QUERY is that note's summary go to held-out together.
//     -> a held-out query string NEVER appears in train (no query-text leak), which is
//        stricter than a per-pair split and is what makes "novel phrasing" honest.
//   * title pairs are ALWAYS in train -> every slug (incl. every held-out target) is
//     anchored in train. No output-vocabulary leak.
//   * assoc targets are other notes' slugs, themselves anchored by their own title pair.
//
// Outputs (to --out, default data/): train.jsonl, heldout.jsonl, slugs.txt,
//   corpus_build_report.json (counts + verified guarantees).
//
// Usage: node scripts/build_corpus.mjs --vault corpus/vault [--out data] [--heldout 0.15] [--seed 42]

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

// ---- args ----
const args = process.argv.slice(2);
function arg(name, def) {
  const i = args.indexOf(`--${name}`);
  return i >= 0 && i + 1 < args.length ? args[i + 1] : def;
}
const VAULT = arg("vault", "corpus/vault");
const OUT = arg("out", "data");
const HELDOUT_FRAC = parseFloat(arg("heldout", "0.15"));
const SEED = arg("seed", "42");

// ---- deterministic hash in [0,1) (NOT Node's salted hashing) ----
function stableUnit(s) {
  const h = crypto.createHash("sha256").update(`${SEED}:${s}`).digest("hex");
  return parseInt(h.slice(0, 13), 16) / 2 ** 52;
}

// ---- minimal frontmatter parser for our known flat shape ----
function parseNote(text) {
  text = String(text).replace(/\r\n/g, "\n").replace(/\r/g, "\n");
  const m = text.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return null;
  const fm = m[1];
  const body = m[2].trim();
  const out = { title: "", summary: "", type: "", links: [], body };
  let inLinks = false;
  for (const raw of fm.split("\n")) {
    const line = raw.replace(/\s+$/, "");
    const kv = line.match(/^(\w+):\s*(.*)$/);
    if (kv && ["title", "summary", "type", "links"].includes(kv[1])) {
      inLinks = kv[1] === "links";
      if (kv[1] === "links") {
        // could be "links: []" or a block list following
        const inline = kv[2].trim();
        if (inline && inline !== "[]") {
          const one = inline.match(/\[\[([^\]]+)\]\]/);
          if (one) out.links.push(one[1].trim());
        }
      } else {
        out[kv[1]] = kv[2].trim();
      }
    } else if (inLinks) {
      const lm = line.match(/\[\[([^\]]+)\]\]/);
      if (lm) out.links.push(lm[1].trim());
    }
  }
  return out;
}

// ---- load vault ----
const files = fs.readdirSync(VAULT).filter((f) => f.endsWith(".md"));
const notes = {};
for (const f of files) {
  const slug = f.replace(/\.md$/, "");
  const n = parseNote(fs.readFileSync(path.join(VAULT, f), "utf8"));
  if (!n || !n.title || !n.summary) {
    console.error(`! skipping unparseable/empty note: ${f}`);
    continue;
  }
  notes[slug] = n;
}
const slugs = Object.keys(notes).sort();
const slugSet = new Set(slugs);
console.log(`loaded ${slugs.length} notes from ${VAULT}`);

// ---- resolve + sanity on links (assoc pairs require resolvable [[B]]) ----
let danglingLinks = 0;
for (const s of slugs) {
  notes[s].links = notes[s].links.filter((t) => {
    if (slugSet.has(t)) return true;
    danglingLinks++;
    return false;
  });
}
if (danglingLinks) console.error(`! dropped ${danglingLinks} dangling links (target missing)`);

// ---- build pairs ----
const train = [];
const heldout = [];
// held-out decision is per SOURCE NOTE (so a held-out query never appears in train)
const heldoutNote = {};
for (const s of slugs) heldoutNote[s] = stableUnit(s) < HELDOUT_FRAC;

function push(arr, query, slug, kind, source) {
  arr.push({ query, slug, kind, source });
}

for (const s of slugs) {
  const n = notes[s];
  // title -> slug : ALWAYS train (anchors the slug)
  push(train, n.title, s, "title", s);
  // summary -> slug : split by source note
  const dst = heldoutNote[s] ? heldout : train;
  push(dst, n.summary, s, "summary", s);
  // assoc : A.summary -> B, query is A's summary => same split bucket as A's summary
  for (const t of n.links) push(dst, n.summary, t, "assoc", s);
}

// ---- VALIDITY CHECKS ----
const trainQueries = new Set(train.map((p) => p.query));
let queryLeak = 0;
for (const p of heldout) if (trainQueries.has(p.query)) queryLeak++;

const trainSlugs = new Set(train.map((p) => p.slug));
let unanchored = 0;
for (const p of heldout) if (!trainSlugs.has(p.slug)) unanchored++;

// ---- write ----
fs.mkdirSync(OUT, { recursive: true });
const w = (file, rows) =>
  fs.writeFileSync(path.join(OUT, file), rows.map((r) => JSON.stringify(r)).join("\n") + "\n");
w("train.jsonl", train);
w("heldout.jsonl", heldout);
fs.writeFileSync(path.join(OUT, "slugs.txt"), slugs.join("\n") + "\n");

const byKind = (rows) =>
  rows.reduce((a, r) => ((a[r.kind] = (a[r.kind] || 0) + 1), a), {});
const report = {
  vault: VAULT,
  seed: SEED,
  heldout_fraction_target: HELDOUT_FRAC,
  notes: slugs.length,
  dangling_links_dropped: danglingLinks,
  train_pairs: train.length,
  heldout_pairs: heldout.length,
  heldout_notes: slugs.filter((s) => heldoutNote[s]).length,
  train_by_kind: byKind(train),
  heldout_by_kind: byKind(heldout),
  guarantees: {
    query_text_leak: queryLeak, // MUST be 0: no held-out query appears in train
    unanchored_heldout_slugs: unanchored, // MUST be 0: every held-out slug anchored in train
    slugs_anchored_in_train:
      slugs.every((s) => trainSlugs.has(s)), // every slug has a train pair
  },
};
fs.writeFileSync(path.join(OUT, "corpus_build_report.json"), JSON.stringify(report, null, 2));

console.log(JSON.stringify(report, null, 2));
if (queryLeak || unanchored || !report.guarantees.slugs_anchored_in_train) {
  console.error("!!! VALIDITY FAILURE — see guarantees above");
  process.exit(1);
}
console.log(`OK -> ${path.join(OUT, "train.jsonl")} (${train.length}), heldout.jsonl (${heldout.length}), slugs.txt (${slugs.length})`);
