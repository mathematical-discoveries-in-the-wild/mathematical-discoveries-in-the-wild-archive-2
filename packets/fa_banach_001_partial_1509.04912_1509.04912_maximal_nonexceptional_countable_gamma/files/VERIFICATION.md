# Verification report

## Verdict

Candidate full theorem likely valid. It is a sharp maximal spectral partial
answer to the source's broader Question 3, not a characterization of all
scalar sets.

## Analytic audit

1. `Gamma_*` is countable because it is a subset of the Gaussian rationals.
   Its closure misses the nonempty open half-annulus
   `{1 < |z| < 2, Re z < 0}`, so it is not dense.
2. For every `|mu| != 1` and fixed `c != 0`, `mu^{-n}c` eventually lies in
   the open unit disk (`|mu|>1`) or outside the closed disk of radius two
   (`|mu|<1`). Gaussian rationals can approximate it with error less than
   `|mu|^{-n}/n`, giving a rescaled error less than `1/n`. The case `c=0`
   is exact because `0 in Gamma_*`.
3. The projective-tail lemma removes finitely many projective lines. A finite
   union of proper closed linear subspaces has empty interior, so every tail
   of a supercyclic projective orbit is dense.
4. In the nonunit transfer step, applying an eigenfunctional forces
   `alpha_k mu^{n_k}` to a nonzero limit. Tail universality gives
   `gamma_k mu^{n_k}` with the same limit, hence `gamma_k/alpha_k -> 1`.
5. If a nontrivial unimodular scalar has finite order `q>=2`, its `q`
   rotations of a closed half-plane cover the plane; for infinite order, its
   cyclic group is dense on the unit circle. Since `Gamma_*` is dense in the
   open right half-plane, the source's condition
   `closure(Gamma_* G_theta)=C` follows.
6. In the empty-adjoint-point-spectrum case, Leon-Saavedra--Muller (as stated
   in Shkarin, Proposition LM) gives equality of the supercyclic and positive
   supercyclic vectors. Replacing a positive real coefficient by a nearby
   positive rational preserves membership in any chosen open target.
7. The supercyclic adjoint-spectrum dichotomy exhausts all cases on an
   infinite-dimensional complex Banach space. The reverse implication is
   automatic because `Gamma_*` is a subset of `C`.
8. Sharpness is exactly the necessity direction of source Theorem C(1) at
   `theta=0`: uniform equivalence in the class `sigma_p(T*)={1}` requires the
   scalar set itself to be dense.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1509.04912_maximal_nonexceptional_countable_gamma/code/verify_gamma_star.py
```

The script checks representative inward/outward rescalings and finite cyclic
half-plane covers. It is a sanity check, not part of the proof.

Result: passed for two complex nonunit multipliers and every finite cyclic
order from 2 through 40.

## Packet build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed with no LaTeX warnings, overfull boxes, underfull boxes, or
  unresolved references.
- The final packet has 5 A4 pages and was rendered at 150 dpi.
- All five rendered pages were inspected at original resolution. The source
  crops are readable; theorem/proof transitions, formulas, citations, page
  numbers, and margins show no clipping, overlap, or malformed glyphs.
- Final SHA-256:
  `964e6fbf9e9eb5c70319704abea4e1dc36bd9693fa3f58a29b01c110171c7ca7`.

## Novelty bounds

Search on 9 August 2026 covered the run indexes; arXiv:1509.04912,
arXiv:1209.1222, arXiv:1711.10932, and arXiv:2411.03179; and bounded arXiv
queries combining `Gamma-supercyclicity`, `countable non-dense scalar set`,
`point spectrum`, `annulus`, and `half-plane`. No statement using one
countable non-dense set for all spectral classes except the sharp eigenvalue
one obstruction was found. Novelty confidence is moderate.

## Human review focus

- Confirm that the source paper's dual convention only conjugates the
  eigenfunctional multiplier; the construction is invariant at the level
  needed here.
- Check the use and scope of Proposition LM and Theorem C(1).
- Check that the theorem is described as a full sharp spectral-coverage
  theorem but only a partial answer to the full characterization requested in
  Question 3.
