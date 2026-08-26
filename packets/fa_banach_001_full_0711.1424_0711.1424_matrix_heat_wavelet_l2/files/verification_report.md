# Verification report

Agent: agent_lane_10  
Model: GPT5.6  
Date: 2026-08-13

## Claim and scope audit

- Exact target: Problem A, formulas (8.27)--(8.28), on source PDF page 21.
- Claimed scope: a full solution in the natural L2 setting, including an
  exact criterion in the nonnegative Laplace-profile class, actual L1
  wavelets, and explicit constants.
- Excluded scope: the separate Definition 8.7/Problem B classification and a
  characterization of all assumptions validating the source's particular
  pointwise Fubini exchange in Problem C.
- The packet therefore does not overstate an Lp result for p != 2 or
  pointwise convergence.

## Proof audit

1. For w in L1(P_m), heat contraction makes each fixed-scale composite
   transform a genuine L2 Bochner integral.
2. Fourier transformation gives the multiplier
   W(a^(1/2) q a^(1/2)), q=xi'xi.
3. Orthogonal invariance makes this equal to
   W(q^(1/2) a q^(1/2)); the two symmetric matrices have the same
   eigenvalues.
4. The congruence substitution r=q^(1/2) a q^(1/2) preserves d_*a
   and changes |a|^(-alpha/2) by the exact factor cancelling the Riesz
   multiplier.
5. Balanced truncations map to nested regions exhausting P_m for every
   full-rank q; the exceptional rank-deficient frequency set is null when
   n>=m.
6. For W>=0, the reconstruction multipliers increase to the weighted
   Mellin integral and are bounded by it. Plancherel and dominated convergence
   prove norm convergence.
7. The same monotone limit proves necessity: zero gives the zero operator,
   while infinity forces norm divergence on a compact full-rank Fourier
   support.
8. The determinant Riesz/Cayley safe range beta-N>d-1 makes
   D^N G_beta an ordinary L1 matrix-Laguerre function with no boundary
   distribution. Its Laplace transform is
   det(s)^N det(I+s)^(-beta).
9. The beta-prime cone integral gives exactly
   B_m(N-alpha/2,beta-N+alpha/2), and the stated parameter inequalities
   put both arguments above d-1.
10. The formula uses no unresolved interchange from Problem C.

The most important human check is item 8, although it is the standard
determinant Riesz-distribution range.

## Computational sanity checks

Command:

    conda run --no-capture-output -n sandbox python code/symbolic_checks.py

Observed output:

- scalar Laplace absolute error: 1.2528585e-52;
- scalar beta absolute error: 0.0;
- exact symbolic m=2, first-Cayley-derivative identity passed.

These checks are not used as proof.

## Literature and provenance

- Official source PDF downloaded from https://arxiv.org/pdf/0711.1424.
- Cheap indexes had no result for the arXiv id or the exact heat-composite
  problem.
- Exact-title, quoted-problem, matrix-cone-heat-wavelet, admissibility, and
  Cayley/matrix-gamma searches were performed.
- The full TeX of the closest cited predecessor, arXiv:math/0409100, was
  inspected. It treats a direct matrix-space convolution wavelet, not the
  source's cone heat-composite wavelet. Its Riesz inversion assumes a Fourier
  profile supported away from the rank-deficient boundary, which a nonzero
  cone Laplace transform cannot satisfy.
- No later direct solution or exact duplicate was located through
  2026-08-13. Novelty remains cautious because equivalent matrix-Laguerre
  language may exist.

## Build and visual QA

- latexmk with PDF, nonstop, halt-on-error, and tmp output completed
  successfully.
- The final log contains no warnings, undefined references, overfull boxes, or
  underfull boxes.
- pdfinfo reports a six-page US-letter PDF, unencrypted, with no JavaScript
  and no suspect objects.
- Ghostscript completed a nullpage rendering pass without error.
- All six pages were rasterized at 150 dpi and inspected individually.
  Text, formulas, theorem boxes, citations, and both source crops are readable;
  there is no clipping or overlap. A first render exposed a malformed
  left/right control sequence in formula (10); it was corrected and the
  affected page was re-rendered and re-inspected.

## Artifact hashes (SHA-256)

- solution_packet.pdf:
  6b2cff5480186eb1234878f1d6c20ddfc2cf6f73976c0890c4cc8cbffaedce9c
- source_paper.pdf:
  beaad1b23f913976ca2e7f20b3cedb10b83081174cc7d2ba2ac1b637cc35a028
- figures/open_problem_crop.png:
  c7f093123b1ef22fedf1e80dadc1ddaeb38d3102c93458cd8b180a74de978571
- figures/problem_c_crop.png:
  192684d438ccd62b498ab1eabcb131eeace90497687be75adf83cbed3c1698a9
- main.tex:
  a3515061363949bdafdd0f9742ba4181f03542a11f5ea9b52488aa05534bddb3

