# Verification report

Status: `candidate_full_solution_likely_valid`

## Mathematical audit

- Confirmed the exact source definition: almost injectivity means global
  phase is the only ambiguity on an open dense signal set.  The packet proves
  the stronger negation that ambiguity holds on an open dense conull set.
- Checked the nonspanning case separately: adding a nonzero common-kernel
  vector preserves all intensities and is non-phase-equivalent off a proper
  subspace.
- Checked Parseval normalization algebraically.  With
  `S=sum(phi_j phi_j*)`, the change `x -> S^(1/2)x` and
  `phi_j -> S^(-1/2)phi_j` preserves every measurement and makes the analysis
  map an isometry.
- Checked that the normalized projective map lands in a simplex of dimension
  `N-1`, while `P(C^d)` has real dimension `2d-2`.  Below the critical count,
  its maximal-rank fibers are positive-dimensional.
- Checked the real-analytic rank argument: the rank-drop locus is the zero set
  of the nonzero analytic section `wedge^r(dq)`, hence is nowhere dense and
  null; the maximal-rank locus is therefore open dense and conull.
- Checked the tangent calculation at the critical count.  A kernel vector of
  the projective intensity differential has coordinates
  `delta_j=i h_j z_j`.  Removing the global infinitesimal phase sets `h_1=0`
  and gives exactly the derivative kernel of the phase-membership map
  `Psi_z:T^(2d-2)->C^(d-1)`.
- Checked the degree lemma independently: after one-point compactification,
  every map from the torus into Euclidean space misses infinity and has mod-2
  degree zero.  A unique nondegenerate zero would make zero a regular value
  with one preimage and degree one.
- Checked that the second torus zero is genuinely non-global: the fixed first
  phase and the nonzero-coordinate hypothesis force any global phase to be
  one and then force every coordinate phase to be one.
- Checked the dichotomy is exhaustive.  Deficient maximal rank gives local
  fibers; full maximal rank gives the degree obstruction on an open dense
  conull set.  A coordinate identically zero forces deficient rank.
- Checked that projective ambiguity lifts through radius/global phase and the
  invertible Parseval change to an open dense conull subset of `C^d`.
- Checked the source's already-known part (b) against Balan--Casazza--Edidin,
  arXiv:math/0412411, Theorem 3.4: for at least `2d` generic complex frame
  vectors, uniquely recoverable rays have dense interior.
- Checked the apparent generalized-measurement counterexample: the `2d-1`
  constructions in arXiv:1909.08874 use general Hermitian matrices, not the
  standard rank-one structure required by the plane--torus proof.

## Reproducible numerical stress test

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1403.1458_complex_almost_injectivity_phase_transition/code/verify_torus_obstruction.py
```

Observed output:

```text
d=2, N=3: ranks=2/2, phase zeros found=2, |det D(Psi)_identity|=1.270893e-02
d=3, N=5: ranks=4/4, phase zeros found=4, |det D(Psi)_identity|=2.328802e-06
d=4, N=7: ranks=6/6, phase zeros found=4, |det D(Psi)_identity|=7.383614e-07
all deterministic stress tests passed
```

The script checks the Parseval identity, equality of the two Jacobian ranks,
and the existence of a nonidentity numerical phase zero.  It does **not**
prove the degree lemma or the theorem.

## Literature and duplicate checks

- The cheap run indexes were searched for arXiv:1403.1458 and the core terms.
  The existing registry hit concerns the distinct `4M-4` everywhere-
  injectivity conjecture, not complex almost injectivity.
- The exact source paper was read at printed pp. 22--23.
- Huang--Rong--Wang--Xu, arXiv:1909.08874 (published 2021), Section 5,
  explicitly records the exceptional standard rank-one `2d-1` PR-ae case as
  still open and proves only generic critical failure.
- Exact-phrase web/arXiv searches through 2026-08-11 used `2d-1 PR-ae`,
  `standard phase retrieval`, `almost injective complex phase retrieval`, and
  variants.  The 11 OpenAlex citing records for DOI
  `10.1016/j.acha.2020.08.002` were also inspected; none resolved this
  exceptional rank-one question.
- This is a bounded novelty audit and does not establish publication priority.

## Build and visual QA

- Built with
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`.
- The final log has no warnings, undefined references, overfull boxes, or
  underfull boxes.
- The final PDF has 4 pages.  Every page was rendered at 1.8x resolution into
  `tmp/rendered/` and visually inspected.  The two-source-page crop is
  readable at normal zoom; theorem statements, equations, proof endings, and
  references are intact; no content is clipped or overlapped.
- Text extraction was checked on all four pages.
- `solution_packet.pdf` SHA-256:
  `6a00dbcc276109523552e8f364bf6183a57692adf1400e6c9271738ab92f2617`.
- `source_paper.pdf` SHA-256:
  `4b82c52a306c612a301803211eb83b4108475ec3107b70f48756dfb6a2b2e198`.
- Balan--Casazza--Edidin supporting PDF SHA-256:
  `74a0f5d1dfbbffa0996360600742ae6d8d95b57a9b3cc8eee1f119ea39dbcb8f`.
- Huang--Rong--Wang--Xu supporting PDF SHA-256:
  `c463123002d7bf7d6ef938493f515b48e7048aa4c8141d66211b8d12051de2e4`.

