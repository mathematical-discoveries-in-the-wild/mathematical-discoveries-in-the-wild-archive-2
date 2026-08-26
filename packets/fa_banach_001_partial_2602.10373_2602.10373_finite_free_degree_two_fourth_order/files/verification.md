# Verification record

## Mathematical checks

1. The degree-two MSS coefficient formula was expanded symbolically and gives
   `(x-m-n)^2-(alpha^2+beta^2)`.
2. For `g_t(v)=(sqrt(v)-t)_+^3`, the nonzero branch satisfies
   `g_t''(v)=3(v-t^2)/(4v^(3/2))>=0`; the value and first derivative glue to
   zero at `v=t^2`, so the full truncated function is convex.
3. The centered finite and free laws are symmetric and have equal second
   moment, hence equal moments through order three.
4. Taylor's formula with integral remainder was applied only on a compact
   interval containing both supports, so no growth assumptions on `f` are
   needed beyond the source's `C^4` hypothesis.

Run the symbolic verifier with:

```bash
conda run --no-capture-output -n sandbox python code/verify_degree_two.py
```

Expected output:

```text
finite coefficient identity: PASS
g''(v) = 3*(v - t**2)/(4*v**(3/2))
convex for v >= t^2: PASS
```

## Exploratory checks

The attempt contains two non-proof search scripts. Exact rational scans used
Newton identities and free cumulants; random-matrix scans tested the cubic
stop-loss characterization. They found no genuine counterexample. The packet
theorem does not rely on these computations.

## Source evidence

`figures/conjecture_5_2_crop.png` is cropped from page 16 of
`source_paper.pdf` at 180 dpi and contains the full statement of Conjecture
5.2 and its finite-free context.

## Packet QA

The final PDF is compiled into `tmp/`, copied to the packet root, checked for
LaTeX warnings, rendered page-by-page at 180 dpi, and visually inspected.

- Final length: 5 pages.
- Final LaTeX warning scan: no warnings, overfull boxes, underfull boxes, or
  undefined references.
- Ghostscript null-device validation: passed.
- All five RGB page renders at 180 dpi were visually inspected; no clipping,
  overlap, missing glyphs, or malformed equations were found.
- `solution_packet.pdf` SHA-256:
  `c16b91bb5f6440028f06427c9cdcecc7d62385685d3b248e2435bbe6a4ea8cc7`.
- `source_paper.pdf` SHA-256:
  `d6aaef88bba064fc17decd03b8980584e19e1c136d0ef8b8ebd0789af52a0389`.
- Supporting MSS PDF SHA-256:
  `4dee6f4a7866ff2c04e2d5e1e4ed300fc6d479d45992aef15e10ea7c3415dad4`.
