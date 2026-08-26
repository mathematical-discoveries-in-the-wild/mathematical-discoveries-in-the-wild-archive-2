# Verification report

Verified: 2026-08-12 (Europe/Madrid)

## Mathematical checks

- Re-derived the leading moment expansion independently of the source's prose.
  A leading pairing of a word of length `2n` has `n` distinct entry pairs and
  `n+1` free index classes. The quotient graph is connected, hence a tree.
- Checked that a conjugate pair imposes only one oriented pattern indicator on
  its tree edge. Constant row and column section integrals therefore allow
  leaf deletion in either orientation.
- Checked the explicit two-block specialization: every tree has exactly two
  equal-edge block labelings and exactly two unequal-edge block labelings.
- Audited the source's vertical row-index reversal. `S_ne` activates every
  diagonal entry; `S_=` activates zero diagonal entries at even sizes and one
  at odd sizes. Hence the two trace polynomials differ for every size at least
  two.
- The non-similarity conclusion uses standard complex Gaussian entries, an
  allowed continuous iid law. Countably many zero-probability trace-equality
  events still have probability zero.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python verify_pairing_weights.py --max-length 10
```

Output:

```text
verified 350 balanced words and 1618 leading pairings
verified diagonal support counts for sizes 2 through 32
```

For each enumerated leading pairing, both block weights were exactly
`2^(-n)` up to machine-exact dyadic floating arithmetic.

## PDF checks

- `latexmk` completed with no unresolved references, warnings, overfull boxes,
  or underfull boxes in the final log.
- `solution_packet.pdf` has 3 A4 pages.
- Rendered all three pages at 140 dpi and inspected them. The source crop is
  legible; equations, theorem text, page breaks, and references are not
  clipped or overlapping.
- `source_paper.pdf` is the official 22-page arXiv PDF. The question appears on
  its printed page 20.

SHA-256:

```text
a5aaee0d76f56854834f105d3870a8bd3b8fdc97421f1d6f2bf783a753e78622  solution_packet.pdf
f9c178cc6047b387497851d7edfa4b63c1383ca7411b678c9d2935b38c804334  source_paper.pdf
```

