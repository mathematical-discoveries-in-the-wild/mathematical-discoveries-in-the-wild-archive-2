# Verification report

Verdict: `candidate_partial_solution_likely_valid`.

## Mathematical checks

- Differentiated the smooth phase path
  `exp(i(d theta + epsilon eta(theta)))` directly through second order.
- Recomputed the vector identities giving the kernel
  `|2 sin(dt/2)|^(p-2) (p cos^2(dt/2)-1)/(4 sin^2(t/2))`.
- Checked that the first variation vanishes by integrating the periodic phase
  difference in the base angle.
- Derived the cosecant root-sum identity by differentiating the standard
  cotangent root-sum identity; no numerical input enters the proof.
- Evaluated the degree-one integral using beta integrals and the ratios
  `A_1/A_0=1/p`, `A_2/A_0=3/(p(p+2))`, and
  `A_3/A_0=15/(p(p+2)(p+4))`.
- Verified that the perturbation remains smooth, has degree `d`, and converges
  to `z^d` in `W^{s,1/s}`.

No unresolved lemma or computational dependency remains in the proof.

## Independent numerical check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2006.07138_all_degree_power_map_instability/code/verify_multiplier.py
```

The script uses 50-digit quadrature for `p in {9,10,12}` and
`|d| in {1,2,3,5}`.  In every case it checks that the numerical quadratic form
equals `|d|` times the closed degree-one formula.  The observed errors were at
the `10^-47` to `10^-49` scale.  This is a regression check, not part of the
proof.

## Novelty check

The exact run indexes had no hit.  Official arXiv API searches performed on
2026-08-11 returned zero results for `"power maps" AND "fractional harmonic"`
and for `"second variation" AND "fractional harmonic maps"`; the exact
`"degree one" AND "W^s" AND "harmonic maps"` query returned only
arXiv:2606.15644v1.  That preprint labels the all-degree statement unverified.

## Packet and rendering checks

- Both source PDFs open and have 94 and 68 pages, respectively.
- The source crop contains the entire degree-one question on PDF page 6.
- The supporting crop contains Theorem 1.1 and the complete relevant footnote
  on PDF page 2.
- `main.tex` was compiled with build artifacts confined to `tmp/`.
- Every rendered page of `solution_packet.pdf` was inspected at full-page and
  readable-detail scale; no clipping, overlap, missing glyph, or blank-page
  defect was found.

