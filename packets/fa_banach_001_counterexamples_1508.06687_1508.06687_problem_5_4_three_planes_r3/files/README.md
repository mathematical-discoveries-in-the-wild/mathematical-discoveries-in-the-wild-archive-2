# Three-plane counterexample to Problem 5.4 of arXiv:1508.06687

Status: `candidate_counterexample_likely_valid`

Source: Jameson Cahill, Peter G. Casazza, John Jasper, and Lindsey M.
Woodland, *Phase Retrieval*, arXiv:1508.06687, Problem 5.4 on source-PDF
page 18.

## Result

Problem 5.4 has a negative answer, over both the real and complex fields.  In
`F^3`, where `F` is `R` or `C`, put

```text
W1 = e1^perp,
W2 = e2^perp,
W3 = (e1+e2+e3)^perp.
```

These are three distinct proper planes.  For every fourth subspace `W4`, the
four projection-norm measurements fail phase retrieval.  Nevertheless, for
no choices of orthonormal bases of `W1,W2,W3` can their union be partitioned
into `F1,F2` with

```text
dim span(F1) <= 1,   dim span(F2) <= 2.
```

Here `M=N=3`, so the counterexample is unaffected by the apparent `M` versus
`N` notational slip in Corollary 5.3 and Problem 5.4.

## Proof idea

Four projection measurements define four real linear functionals on the
six-dimensional space of real symmetric `3 x 3` matrices.  Their common
kernel contains a two-plane.  The determinant is an odd homogeneous cubic,
so it vanishes at a nonzero point of that two-plane.  The first two projection
constraints exclude every nonzero semidefinite kernel matrix.  The singular
matrix is therefore indefinite of rank two and is a difference `xx* - yy*`,
giving two non-phase-equivalent signals with identical measurements.

For the requested partition, let `L=span(F1)` and `H=span(F2)`.  Every plane
basis must either lie wholly in `H` or split orthogonally between `L` and `H`.
The three planes have zero common intersection, so one of them must equal
`H`; the other two force `L` to be their intersection line.  An explicit
three-case computation shows that this line is never orthogonal to the
required intersection with `H`, a contradiction.

## Scope and novelty check

This settles the exact converse question negatively; it does not classify
which families are completable by one subspace.  Cheap run indexes showed
many phase-retrieval results but no artifact for this source or Problem 5.4.
Bounded searches for the exact problem and Corollary 5.3 wording located the
source publication but no later resolution.  The proof is self-contained and
the novelty assessment remains subject to expert literature review.

## Files

- `source_paper.pdf`: arXiv:1508.06687.
- `figures/open_problem_crop.png`: Corollary 5.3 and Problem 5.4, PDF page 18.
- `main.tex` and `solution_packet.pdf`: full counterexample proof.
- `code/verify_counterexample.py`: exact incidence checks and 102 sampled
  fourth-subspace lifted-kernel checks.
- `verification_report.md`: independent proof and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/1508.06687_problem_5_4_three_planes_r3.json`.
